from flask import Blueprint
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

engagement = Blueprint("engagement", __name__, url_prefix="/api/v1/engagement")

@engagement.post('/<int:engagement_id>')
@jwt_required()
def add_engagement():
    return "Engagement Added"


@engagement.get("/")
@jwt_required()
def get_all_engagement():

    ##for items in engagement (after sqlalchemy):
    ## return list as python dict that should get jsonify'd
    return {"user":"me"}

@engagement.get("/<int:engagement_id>")
@jwt_required()
def get_one_engagement():
    ##do sqlalchemy stuff to get one engagement, should return a list of issues, their associated phases and the associated assets
    return {"user":"me"}


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

phase = Blueprint("phase", __name__, url_prefix="/api/v1/phase")

@phase.post('/<int:engagement_id>/phase/<int:phase_id>')
@jwt_required()
def add_phase():
    return "phase Added"


@phase.get("/<int:engagement_id>/phase/")
@jwt_required()
def get_all_phase():

    ##for items in engagement for items in phase (after sqlalchemy):
    ## return list as python dict that should get jsonify'd
    return {"user":"me"}

@phase.get("/<int:engagement_id>/phase/<int:phase_id>")
@jwt_required()
def get_one_phase():
    ##do sqlalchemy stuff to get one phase
    return {"user":"me"}


@phase.put("/<int:engagement_id>/phase/<int:phase_id>")
@jwt_required()
def update_phase():
    ##do sqlalchemy stuff to update one phase
    return "phase Updated"


@phase.delete("/<int:engagement_id>/phase/<int:phase_id>")  ##delete one phase
@jwt_required()
def delete_phase():
    #do sqlalchemy stuff to delete one phase
    return "phase Deleted"


'''
ASSETS

'''

asset = Blueprint("asset", __name__, url_prefix="/api/v1/asset")

@asset.post('/<int:engagement_id>/asset/<int:asset_id>')
@jwt_required()
def add_asset():
    return "asset Added"


@asset.get("/<int:engagement_id>/asset/")
@jwt_required()
def get_all_asset():

    ##for items in engagement for items in asset (after sqlalchemy):
    ## return list as python dict that should get jsonify'd
    return {"user":"me"}

@asset.get("/<int:engagement_id>/asset/<int:asset_id>")
@jwt_required()
def get_one_asset():
    ##do sqlalchemy stuff to get one asset
    return {"user":"me"}


@asset.put("/<int:engagement_id>/asset/<int:asset_id>")
@jwt_required()
def update_asset():
    ##do sqlalchemy stuff to update one asset
    return "asset Updated"


@asset.delete("/<int:engagement_id>/asset/<int:asset_id>")  ##delete one asset
@jwt_required()
def delete_asset():
    #do sqlalchemy stuff to delete one asset
    return "asset Deleted"
