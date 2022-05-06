import re, string
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, decode_token, jwt_required, get_jwt_identity, get_jwt, JWTManager, verify_jwt_in_request
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timezone

from RedTeamReporter.models import db, db_User, TokenBlocklist
from RedTeamReporter.constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT


auth = Blueprint("auth", __name__, url_prefix="/api/v1/auth")


jwt = JWTManager()

@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    jti = jwt_payload["jti"]
    token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()
    return token is not None

@auth.post('/register')
def register():
    username = request.json['username']
    email = request.json['email']
    password = request.json['password']
    phone = request.json['phone']
    firstname = request.json['firstname']
    lastname = request.json['lastname']
    password_validated = validate_password(password)
    user_validated = validate_username(username)
    email_validated = validate_email(email)
    phone_validated = validate_phone(phone)
    firstname_validated = validate_name(firstname)
    lastname_validated = validate_name(lastname)

    if password_validated is not True:
        return password_validated
    if user_validated is not True:
        return user_validated
    if email_validated is not True:
        return email_validated
    if phone_validated is not True:
        return phone_validated
    if firstname_validated is not True:
        return firstname_validated
    if lastname_validated is not True:
        return lastname_validated

    if password_validated and user_validated and email_validated and phone_validated and firstname_validated and lastname_validated is True:
        hashed_password = generate_password_hash(password, method='sha256')
        user = db_User(userName=username, userEmail=email, userFirstname=firstname, userLastname=lastname, userPass=hashed_password, userPhone=phone, userGroup="viewer", userPrivilege="viewer")
        db.session.add(user)
        db.session.commit()
        return {"message": "Please check your email for validation"}, HTTP_201_CREATED
    else:
        return {"message": "Please check your email for validation"}, HTTP_201_CREATED


@auth.post('/login')
@jwt_required(optional=True, verify_type=False)
def login():
    email = request.json['email']
    password = request.json['password']
    user = db_User.query.filter_by(userEmail=email).first()
    if user:
        
        check_password = check_password_hash(user.userPass, password)
        if check_password:
            now = datetime.now(timezone.utc)
            db.session.add(TokenBlocklist(jti=user.userAccesstoken, type="access", created_at=now, user_id=user.id))
            db.session.add(TokenBlocklist(jti=user.userRefreshtoken, type="refresh", created_at=now, user_id=user.id))
            refresh_token=create_refresh_token(identity=user.id)
            access_token=create_access_token(identity=user.id)
            user.userAccesstoken = decode_token(access_token)["jti"]
            user.userRefreshtoken = decode_token(refresh_token)["jti"]
            db.session.commit()

            return {
                    'refresh_token': refresh_token,
                    'access_token': access_token
            }, HTTP_200_OK
            
    return {'message': 'Incorrect Credentials'}, HTTP_401_UNAUTHORIZED

'''
When calling the below logout, make sure to pass both the access and refresh token
otherwise the user can use them both still
'''
@auth.delete('/logout')
@jwt_required(verify_type=False)
def logout():
    token = get_jwt()
    jti = token["jti"]
    ttype = token["type"]
    now = datetime.now(timezone.utc)
    #THIS user_id below should correlate to the user id i think... may be dragons ahead.
    db.session.add(TokenBlocklist(jti=jti, type=ttype, created_at=now, user_id=get_jwt_identity()))
    db.session.commit()
    return jsonify(messsage=f"{ttype.capitalize()} token successfully revoked"), HTTP_200_OK



@auth.get("/me")
@jwt_required()
def me():
    ident = get_jwt_identity()
    user = db_User.query.filter_by(id=ident).first()
    return {"username": user.userName, 
    "email": user.userEmail, 
    "firstname": user.userFirstname, 
    "lastname": user.userLastname, 
    "phone": user.userPhone, 
    "group": user.userGroup, 
    "privilege": user.userPrivilege}, HTTP_200_OK


@auth.get('/token/refresh')
@jwt_required(refresh=True)
def refresh_users_token():
    identity = get_jwt_identity()
    user = db_User.query.filter_by(id=identity).first()
    new_token = create_access_token(identity=identity)
    now = datetime.now(timezone.utc)
    db.session.add(TokenBlocklist(jti=user.userAccesstoken, type="access", created_at=now, user_id=user.id))
    user.userAccesstoken = decode_token(new_token)["jti"]
    db.session.commit()

    return {'access_token': new_token}, HTTP_200_OK


def validate_username(username):
    if len(username) >79:
        return {"message": "Username must be below 79 characters long"}, HTTP_400_BAD_REQUEST       
    if len(username) < 3:
        return {"message": "Username must be at least 3 characters long"}, HTTP_400_BAD_REQUEST
    if not any(char.isalnum() for char in username) or " " in username:
        return {"message": "Username must contain at least one letter or number, and cannot contain spaces"}, HTTP_400_BAD_REQUEST
    if db_User.query.filter_by(userName=username).first() is not None:
        return {"message": "Please check your email for validation"}, HTTP_201_CREATED
        
    else:
        return True


def validate_email(email):
    regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
    if db_User.query.filter_by(userEmail=email).first() is not None:
        return {"message": "Please check your email for validation"}, HTTP_201_CREATED
        
    if re.fullmatch(regex, email):
        return True
    else:
        return {"message": "Email is not valid"}, HTTP_400_BAD_REQUEST


def validate_password(password):
    special_char = r"[!@#$%^&*(),.?:{}|<>]"

    if len(password) < 12:
        return {"message": "Password must be at least 12 characters long"}, HTTP_400_BAD_REQUEST
    if not any(char.isdigit() for char in password):
        return {"message": "Password must contain at least one number"}, HTTP_400_BAD_REQUEST
    if not any(char.isupper() for char in password):
        return {"message": "Password must contain at least one uppercase letter"}, HTTP_400_BAD_REQUEST
    if not any(char.islower() for char in password):
        return {"message": "Password must contain at least one lowercase letter"}, HTTP_400_BAD_REQUEST
    if not any(char.isalnum() for char in password):
        return {"message": "Password must contain at least one letter or number"}, HTTP_400_BAD_REQUEST
    if re.search(special_char, password) is None:
        return {"message": "Password must contain at least one Symbol or Special Character (!@#$%^&*(),.?:{|}<>)"}, HTTP_400_BAD_REQUEST
    else:
        return True
    

def validate_phone(phone):
    if len(phone) >29:
        return{"message": "Phone number is invalid."}, HTTP_400_BAD_REQUEST
    if len(phone) <8:
        return{"message": "Phone number is invalid."}, HTTP_400_BAD_REQUEST
    if any (char.isalpha() for char in phone):
        return{"message": "Phone number is invalid."}, HTTP_400_BAD_REQUEST
    else:
        return True


def validate_name(name):
    if len(name) >49:
        return {"message": "Names must be smaller than 50 characters"}, HTTP_400_BAD_REQUEST
    if len(name) <3:
        return {"message": "Names must be larger than two characters"}, HTTP_400_BAD_REQUEST
    if not any(char.isalpha() for char in name) or " " in name:
        return {"message": "Names cannot contain spaces or numbers"}, HTTP_400_BAD_REQUEST
    else:
        return True
    