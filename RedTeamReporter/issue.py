from flask import Blueprint, jsonify
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from RedTeamReporter.models import db, db_User, db_liveVKD, db_restVKD, db_Engagement

issue = Blueprint("issue", __name__, url_prefix="/api/v1/issue")


'''
Issue control for rest VKD, need to be able to read update etc. These are for the database and saved issues.
'''


@issue.post('/<int:id>')
@jwt_required()
def add_issue():
    return "issue Added"


@issue.get("/rest")
@jwt_required()
def get_all_rest_issue():
    issue = db_restVKD.query.filter_by().all()
    ##for items in issue (after sqlalchemy):
    ## return list as python dict that should get jsonify'd, this is also maybe 
    json = []
    for item in issue:
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
            "draftstatus": item.issueDraftstatus,
            "createdtime": item.issueCreatedtime,
            "lastmodifiedtime": item.issueLastmodifiedtime,
        })
        
    return jsonify(json)

@issue.get("/rest/<int:rest_issue_id>")
@jwt_required()
def get_one_rest_issue():
    ##do sqlalchemy stuff to get one issue -- maye like this def search():
    #query = request.args.get("query") # here query will be the search inputs name
    #allVideos = Videos.query.filter(Videos.title.like("%"+query+"%")).all()
    issue = db_live
    return {"user":"me"}


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



@issue.post('/<int:engagement_id>/issue/')
@jwt_required()
def add_engagement_issue():
    #return the issue ID and the engagement id after creating it, needs to take in a whole lot here
    return "issue Added"


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