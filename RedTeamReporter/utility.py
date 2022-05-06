from flask import Blueprint
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

index = Blueprint("index", __name__, url_prefix="/api/v1/index")

@dashboard.post('/dashboard')
@jwt_required()
def dashboard():
    return "dashboard"

@vkd.post('/vkd')
@jwt_required()
def vkd():
    return "vkd"


@admin.post('/admin/adduser')
@jwt_required()
def admin_adduser():
    return "admin"


@admin.post('/admin/deluser')
@jwt_required()
def admin_deluser():
    return "admin"

@admin.post('/admin/modifyuser')
@jwt_required()
def admin_modifyuser():
    return "admin"
