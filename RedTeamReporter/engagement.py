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
def update_engagement(engagement_id):
    engagement = db_Engagement.query.filter_by(id=engagement_id).first()
    update_counter = []
    engagementName = request.json['engagementName']
    rtCode = request.json['rtCode']
    customerName = request.json['customerName']
    customerEmail = request.json['customerEmail']
    customerOrg = request.json['customerOrg']
    scopeField = request.json['scopeField']
    consultantName = request.json['consultantName']
    if engagementName != "":
        engagement.engagementName = engagementName
        db.session.flush()
        update_counter.append("engagementName")
    if rtCode != "":
        engagement.rtCode = rtCode
        db.session.flush()
        update_counter.append("rtCode")
    if customerName != "":
        engagement.customerName = customerName
        db.session.flush()
        update_counter.append("customerName")
    if customerEmail != "":
        engagement.customerEmail = customerEmail
        db.session.flush()
        update_counter.append("customerEmail")
    if customerOrg != "":
        engagement.customerOrg = customerOrg
        db.session.flush()
        update_counter.append("customerOrg")
    if scopeField != "":
        engagement.scopeField = scopeField
        db.session.flush()
        update_counter.append("scopeField")
    if consultantName != "":
        engagement.consultantName = consultantName
        db.session.flush()
        update_counter.append("consultantName")
    db.session.commit()
    return {"engagementID": str(engagement.id), "Updated Items": update_counter}
    


@engagement.delete("/<int:engagement_id>")  ##delete one engagement
@jwt_required()
def delete_engagement(engagement_id):
    engagement = db_Engagement.query.filter_by(id=engagement_id).first()
    phase = db_Phase.query.filter_by(engagementId=engagement_id).all()
    issue = db_liveVKD.query.filter_by(issuePhaseid=engagement_id).all()
    for issues in issue:
        db.session.delete(issues)
    for phases in phase:
        db.session.delete(phases)
    db.session.delete(engagement)
    db.session.commit()
    return {"engagementID, all related phases, all related issues Deleted": str(engagement.id)}


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


@engagement.get("/<int:engagement_id>/get_phases/")
@jwt_required()
def get_all_phase(engagement_id):
    output = {}
    engagement = db_Phase.query.filter_by(engagementId=engagement_id).all()
    for item in engagement:
        output[item.id] = item.phaseName
    return jsonify(output)

@engagement.get("/<int:engagement_id>/get_single_phase/<int:phase_id>")
@jwt_required()
def get_one_phase():
    ##do sqlalchemy stuff to get one phase
    return {"user":"me"}




@engagement.put("/<int:engagement_id>/phase/<int:phase_id>")
@jwt_required()
def update_phase(engagement_id, phase_id):
    phase = db_Phase.query.filter_by(id=phase_id).first()
    engagement = db_Engagement.query.filter_by(id=engagement_id).first()
    if phase.engagementId != engagement.id:
        return {"ERROR":"Phase does not exist in engagement"}, HTTP_404_NOT_FOUND
    
    update_counter = []
    phase_name = request.json['phasename']
    phase_scope = request.json['phasescope']

    if phase_name != "":
        phase.phaseName = phase_name
        db.session.flush()
        update_counter.append("phaseName")
    if phase_scope != "":
        phase.phaseScope = phase_scope
        db.session.flush()
        update_counter.append("phaseScope")
    db.session.commit()
    return {"phaseID": str(phase.id), "Updated Items": update_counter}

'''
This needs some more thought, for example what do we do with the issues attached to a phase if it is deleted? do we just say that those issues are also deleteD?
They technically arent abandoned as we could find the issues due to the engagement. Perhaps a "Issues not in phase" area?
'''
@engagement.delete("/<int:engagement_id>/phase/<int:phase_id>")  ##delete one phase
@jwt_required()
def delete_phase(engagement_id, phase_id):
    engagement = db_Engagement.query.filter_by(id=engagement_id).first()
    phase = db_Phase.query.filter_by(id=phase_id).first()
    if phase.engagementId != engagement.id:
        return {"ERROR":"Phase does not exist in engagement"}, HTTP_404_NOT_FOUND
    if phase is not None:
        storage = phase.id
        db.session.delete(phase)
        db.session.commit()
        return {"phaseID Deleted": storage}, HTTP_200_OK

'''
ASSETS

'''

#asset = Blueprint("asset", __name__, url_prefix="/api/v1/asset")

@engagement.post('/<int:engagement_id>/asset/<int:asset_issue_id>')
@jwt_required()
def add_asset(engagement_id, asset_issue_id):
    name = request.json['assetname']
    fqdn = request.json['assetfqdn']
    criticality = request.json['assetcriticality']
    location = request.json['assetlocation']
    engagement = db_Engagement.query.filter_by(id=engagement_id).first()
    issue = db_liveVKD.query.filter_by(id=asset_issue_id).first()
    print(engagement.id)
    print(issue.engagementId)
    if engagement is not None:
        if issue is not None:
            if int(issue.engagementId) == int(engagement.id):
                newAsset = db_Assets(assetIssueid=asset_issue_id, assetEngagementid=engagement_id, assetName = name, assetFqdn = fqdn, assetCriticality=criticality, assetLocation = location)
                db.session.add(newAsset)
                db.session.commit()
                return {"assetID": str(newAsset.id)}, HTTP_200_OK
            else:
                return {"ERROR":"Issue not in engagement"}, HTTP_404_NOT_FOUND
    return {"ERROR":"EngagementID or IssueID not found"}, HTTP_404_NOT_FOUND


@engagement.get("/<int:engagement_id>/assets/")
@jwt_required()
def get_all_asset_for_engagement(engagement_id):
    query = db_Assets.query.filter_by(assetEngagementid=engagement_id).all()
    assets = []
    for item in query:
        assets.append({
                "assetID": item.id,
                "assetName": item.assetName,
                "assetFQDN": item.assetFqdn,
                "assetCriticality": item.assetCriticality,
                "assetLocation": item.assetLocation
            })
    ##for items in engagement for items in asset (after sqlalchemy):
    ## return list as python dict that should get jsonify'd
    return jsonify(assets)




@engagement.put("/<int:engagement_id>/asset/<int:asset_id>")
@jwt_required()
def update_asset(engagement_id, asset_id):
    asset = db_Assets.query.filter_by(id=asset_id).first()
    engagement = db_Engagement.query.filter_by(id=engagement_id).first()
    if int(asset.assetEngagementid) != int(engagement.id):
        return {"ERROR":"Asset does not exist in engagement", "asset":asset.assetEngagementid,"engagement":engagement.id}, HTTP_404_NOT_FOUND
    
    update_counter = []
    asset_name = request.json['assetname']
    asset_fqdn = request.json['assetfqdn']
    criticality = request.json['assetcriticality']
    location = request.json['assetlocation']

    if asset_name != "":
        asset.assetName = asset_name
        db.session.flush()
        update_counter.append("assetName")
    if asset_fqdn != "":
        asset.assetFqdn = asset_fqdn
        db.session.flush()
        update_counter.append("assetFqdn")
    if criticality != "":
        asset.assetCriticality = criticality
        db.session.flush()
        update_counter.append("assetCriticality")
    if location != "":
        asset.assetLocation = location
        db.session.flush()
        update_counter.append("assetLocation")
    db.session.commit()
    return {"assetID": str(asset.id), "Updated Items": update_counter}


@engagement.delete("/<int:engagement_id>/asset/<int:asset_id>")  ##delete one asset
@jwt_required()
def delete_asset(engagement_id, asset_id):
    #do sqlalchemy stuff to delete one asset
    asset = db_Assets.query.filter_by(id=asset_id).first()
    engagement = db_Engagement.query.filter_by(id=engagement_id).first()
    if int(asset.assetEngagementid) != int(engagement.id):
        return {"ERROR":"Asset does not exist in engagement"}, HTTP_404_NOT_FOUND
    if db_Assets.query.filter_by(id=asset_id).first() is not None:
        storage = asset.id
        db_Assets.query.filter_by(id=asset_id).delete()
        db.session.commit()
        return {"Asset Successfully Deleted ID:":storage}

    
