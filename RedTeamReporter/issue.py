from flask import Blueprint, jsonify, request
from datetime import datetime
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from RedTeamReporter.models import db, db_User, db_liveVKD, db_restVKD, db_Engagement, db_Phase, db_Assets
from RedTeamReporter.constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT


issue = Blueprint("issue", __name__, url_prefix="/api/v1/issue")


'''
Issue control for rest VKD, need to be able to read update etc. These are for the database and saved issues.
'''


@issue.post('/rest/add_issue')
@jwt_required()
def add_issue():
    title = request.json['title']
    body = request.json['body']
    _type = request.json['type']
    catergory = request.json['category']
    summary = request.json['summary']
    remedy = request.json['remedy']
    cwe = request.json['cwe']
    cve = request.json['cve']
    severity = request.json['severity']
    references = request.json['references']
    cvss = request.json['cvss']
    fairvector = request.json['fairvector']
    creator = get_jwt_identity()
    createdtime = datetime.now()
    lastmodified = get_jwt_identity()
    draftstatus = request.json['draftstatus']
    lastmodifiedtime = datetime.now()
    db.session.add(db_restVKD(issueTitle=title, issueBody=body, issueType=_type, issueCategory=catergory, issueSummary=summary, issueRemedy=remedy, issueCwe=cwe, issueCve=cve, issueSeverity=severity, issueReferences=references, issueCvssvector=cvss, issueFairvector=fairvector, issueCreator=creator, issueCreatedtime=createdtime, issueLastmodifieduser=lastmodified, issueDraftstatus=draftstatus, issueLastmodifiedtime=lastmodifiedtime))
    db.session.commit()
    return "issue Added"


@issue.get("/rest")
@jwt_required()
def get_all_rest_issue():
    issue_iter = db_restVKD.query.filter_by().all()
    ##for items in issue (after sqlalchemy):
    ## return list as python dict that should get jsonify'd, this is also maybe 
    json = []
    for item in issue_iter:
        json.append({
            "id": item.id,
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
            "lastmodifiedtime": str(item.issueLastmodifiedtime),
        })
        
    return jsonify(json)

@issue.get("/rest/<int:rest_issue_id>")
@jwt_required()
def get_one_rest_issue(rest_issue_id):
    ##do sqlalchemy stuff to get one issue -- maye like this def search():
    #query = request.args.get("query") # here query will be the search inputs name
    #allVideos = Videos.query.filter(Videos.title.like("%"+query+"%")).all()
    item = db_restVKD.query.filter_by(id=rest_issue_id).first()
    json = []
    
    json.append({
        "id": item.id,
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
        "lastmodifiedtime": str(item.issueLastmodifiedtime),
        })
    return jsonify(json)


@issue.put("/rest/<int:rest_issue_id>")
@jwt_required()
def update_issue():
    ##do sqlalchemy stuff to update one issue
    return "issue Updated"


@issue.delete("/rest/<int:rest_issue_id>")  ##delete one issue
@jwt_required()
def delete_issue():
    #do sqlalchemy stuff to delete one issue
    return "issue Deleted"


@issue.post('/<int:engagement_id>/issue_copy/<int:rest_issue_id>')
@jwt_required()
def copy_issue():
    return "Issue copied"


'''
Issue control for engagements. These are issues that are applied to an issue or an engagement.

'''



@issue.post('/<int:engagement_id>/<int:phase_id>/add_live_issue/')
@jwt_required()
def add_issue_live(engagement_id, phase_id):
    title = request.json['title']
    body = request.json['body']
    _type = request.json['type']
    catergory = request.json['category']
    summary = request.json['summary']
    remedy = request.json['remedy']
    cwe = request.json['cwe']
    cve = request.json['cve']
    severity = request.json['severity']
    references = request.json['references']
    cvss = request.json['cvss']
    fairvector = request.json['fairvector']
    creator = get_jwt_identity()
    createdtime = datetime.now()
    lastmodified = get_jwt_identity()
    draftstatus = request.json['draftstatus']
    lastmodifiedtime = datetime.now()
    engagementid = engagement_id
    phaseid = phase_id
    retestflag = int(request.json['retestflag'])
    addtovkd = int(request.json['addtovkd'])
    
    
    if db_Engagement.query.filter_by(id=engagementid).first() is not None:
        if db_Phase.query.filter_by(id=phaseid).first() is not None:
            liveIssueAdd = db_liveVKD(issueTitle=title, issueBody=body, issueType=_type, issueCategory=catergory, issueSummary=summary, issueRemedy=remedy, issueCwe=cwe, issueCve=cve, issueSeverity=severity, issueReferences=references, issueCvssvector=cvss, issueFairvector=fairvector, issueCreator=creator, issueCreatedtime=createdtime, issueLastmodifieduser=lastmodified, issueDraftstatus=draftstatus, issueLastmodifiedtime=lastmodifiedtime, engagementId = engagementid, issuePhaseid = phaseid, issueRetestflag = retestflag, issueAddtovkd = addtovkd)
            db.session.add(liveIssueAdd)
            db.session.commit()
            return {"IssueID": str(liveIssueAdd.id)}
        else:
            return "Phase not found"
    else:
        return "issue not added (probably no engagement under that ID)"
    


@issue.get("/<int:engagement_id>/issue/")
@jwt_required()
def get_engagement_issues():

    ##list all issues attached to an engagement
    ## return list as python dict that should get jsonify'd
    return {"user":"me"}

@issue.get("/<int:engagement_id>/issue/<int:issue_id>")
@jwt_required()
def get_engagement_issue():
    ##list one issue and all data for it including remediation etc
    return {"user":"me"}


@issue.put("/<int:engagement_id>/issue/<int:issue_id>")
@jwt_required()
def update_engagement_issue():
    ##do sqlalchemy stuff to update one issue uipdates the entirety of it
    return "issue Updated"


@issue.delete("/<int:engagement_id>/issue/<int:issue_id>")  ##delete one issue
@jwt_required()
def delete_engagement_issue():
    #do sqlalchemy stuff to delete one issue
    return "issue Deleted"