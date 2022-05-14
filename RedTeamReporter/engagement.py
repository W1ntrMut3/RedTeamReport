from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from RedTeamReporter.models import db, db_User, db_liveVKD, db_restVKD, db_Engagement, db_Phase, db_Assets
from RedTeamReporter.constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_404_NOT_FOUND, HTTP_409_CONFLICT


engagement = Blueprint("engagement", __name__, url_prefix="/api/v1/engagement")

@engagement.post('/add_engagement')
@jwt_required()
def add_engagement():
    engagementName = request.json['engagementName']
    rtCode = request.json['rtCode']
    customerName = request.json['customerName']
    customerEmail = request.json['customerEmail']
    customerOrg = request.json['customerOrg']
    scopeField = request.json['scopeField']
    consultantName = request.json['consultantName']
    newEng = db_Engagement(engagementName=engagementName, rtCode=rtCode, customerName=customerName, customerEmail=customerEmail, customerOrg=customerOrg, scopeField=scopeField, consultantName=consultantName)
    db.session.add(newEng)
    db.session.commit()
    
    
    return {"engagementID": str(newEng.id)}


@engagement.get("/")
@jwt_required()
def get_all_engagement():

    ##for items in engagement (after sqlalchemy):
    ## return list as python dict that should get jsonify'd
    eng_iter = db_Engagement.query.filter_by().all()
    ##for items in issue (after sqlalchemy):
    ## return list as python dict that should get jsonify'd, this is also maybe 
    json = []
    for item in eng_iter:
        json.append({
            "id": item.id,
            "engagementName": item.engagementName,
            "rtCode": item.rtCode,
            "customerName": item.customerName,
            "customerEmail": item.customerEmail,
            "scopeField": item.scopeField,
            "consultantName": item.consultantName,
            "createdTime": item.createdTime
        })
        
    return jsonify(json)

@engagement.get("/get_single_engagement/<int:engagement_id>")
@jwt_required()
def get_one_engagement(engagement_id):
    ##do sqlalchemy stuff to get one engagement, should return a list of issues, their associated phases and the associated assets
    item = db_Engagement.query.filter_by(id=engagement_id).first()
    json = []
    json.append({
            "id": item.id,
            "engagementName": item.engagementName,
            "rtCode": item.rtCode,
            "customerName": item.customerName,
            "customerEmail": item.customerEmail,
            "scopeField": item.scopeField,
            "consultantName": item.consultantName,
            "createdTime": item.createdTime
        })
        
    return jsonify(json)

@engagement.get("/<int:engagement_id>")
@jwt_required()
def get_engagement_issues(engagement_id):
    engagement = db_Phase.query.filter_by(engagementId=engagement_id).all()
    output = []
    issue = []


    for phases in engagement:
        phase = {}
        phase['id'] = phases.id
        issues = db_liveVKD.query.filter_by(issuePhaseid=phases.id).all()
        for item in issues:
            issue.append({
                "issueid": item.id,
                "title": item.issueTitle,
                "body": item.issueBody,
                "type": item.issueType,
                "category": item.issueCategory,
                "summary": item.issueSummary,
                "remedy": item.issueRemedy,
                "cwe": item.issueCwe,
                "cve": item.issueCve,
                "severity": item.issueSeverity,
                "references": item.issueReferences,
                "cvss": item.issueCvssvector,
                "fairvector": item.issueFairvector,
                "creator": item.issueCreator,
                "lastmodified": item.issueLastmodifieduser,
                "draftstatus": str(item.issueDraftstatus),
                "createdtime": str(item.issueCreatedtime),
                "lastmodifiedtime": str(item.issueLastmodifiedtime)
            })
        phase["issues"] = issue     
        output.append(phase)
        issue = [] # lol this stupid loop took me an hour to figure out why it was not working, wasnt clearing the caches doh
    return jsonify(output)


@engagement.put("/<int:engagement_id>")
@jwt_required()
def update_engagement():
    ##do sqlalchemy stuff to update one engagement
    return "Engagement Updated"


@engagement.delete("/<int:engagement_id>")  ##delete one engagement
@jwt_required()
def delete_engagement():
    #do sqlalchemy stuff to delete one engagement
    return "Engagement Deleted"


'''
PHASES

'''

#phase = Blueprint("phase", __name__, url_prefix="/api/v1/phase")

@engagement.post('/<int:engagement_id>/add_phase')
@jwt_required()
def add_phase(engagement_id):
    phase_name = request.json['phasename']
    phase_scope = request.json['phasescope']
    engagementid = engagement_id
    if db_Engagement.query.filter_by(id=engagementid).first() is not None:
        newPhase = db_Phase(phaseName=phase_name, engagementId = engagementid, phaseScope=phase_scope)
        db.session.add(newPhase)
        db.session.commit()
    
    
        return {"phaseID": str(newPhase.id)}, HTTP_200_OK
    else:
        return {"ERROR":"EngagementID not found"}, HTTP_404_NOT_FOUND


@engagement.get("/<int:engagement_id>/phase/")
@jwt_required()
def get_all_phase():

    ##for items in engagement for items in phase (after sqlalchemy):
    ## return list as python dict that should get jsonify'd
    return {"user":"me"}

@engagement.get("/<int:engagement_id>/phase/<int:phase_id>")
@jwt_required()
def get_one_phase():
    ##do sqlalchemy stuff to get one phase
    return {"user":"me"}


@engagement.put("/<int:engagement_id>/phase/<int:phase_id>")
@jwt_required()
def update_phase():
    ##do sqlalchemy stuff to update one phase
    return "phase Updated"


@engagement.delete("/<int:engagement_id>/phase/<int:phase_id>")  ##delete one phase
@jwt_required()
def delete_phase():
    #do sqlalchemy stuff to delete one phase
    return "phase Deleted"


'''
ASSETS

'''

#asset = Blueprint("asset", __name__, url_prefix="/api/v1/asset")

@engagement.post('/<int:engagement_id>/asset/<int:asset_id>')
@jwt_required()
def add_asset():
    return "asset Added"


@engagement.get("/<int:engagement_id>/asset/")
@jwt_required()
def get_all_asset():

    ##for items in engagement for items in asset (after sqlalchemy):
    ## return list as python dict that should get jsonify'd
    return {"user":"me"}

@engagement.get("/<int:engagement_id>/asset/<int:asset_id>")
@jwt_required()
def get_one_asset():
    ##do sqlalchemy stuff to get one asset
    return {"user":"me"}


@engagement.put("/<int:engagement_id>/asset/<int:asset_id>")
@jwt_required()
def update_asset():
    ##do sqlalchemy stuff to update one asset
    return "asset Updated"


@engagement.delete("/<int:engagement_id>/asset/<int:asset_id>")  ##delete one asset
@jwt_required()
def delete_asset():
    #do sqlalchemy stuff to delete one asset
    return "asset Deleted"
