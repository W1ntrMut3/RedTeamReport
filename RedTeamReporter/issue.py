from flask import Blueprint, jsonify, request
from datetime import datetime
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity
from RedTeamReporter.models import db, db_User, db_liveVKD, db_restVKD, db_Engagement, db_Phase, db_Assets
from RedTeamReporter.constants.http_status_codes import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_401_UNAUTHORIZED, HTTP_409_CONFLICT, HTTP_404_NOT_FOUND


issue = Blueprint("issue", __name__, url_prefix="/api/v1/issue")


'''
REST
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
    add_issue= db_restVKD(issueTitle=title, issueBody=body, issueType=_type, issueCategory=catergory, issueSummary=summary, issueRemedy=remedy, issueCwe=cwe, issueCve=cve, issueSeverity=severity, issueReferences=references, issueCvssvector=cvss, issueFairvector=fairvector, issueCreator=creator, issueCreatedtime=createdtime, issueLastmodifieduser=lastmodified, issueDraftstatus=draftstatus, issueLastmodifiedtime=lastmodifiedtime)
    
    db.session.add(add_issue)
    db.session.commit()
    return {"issueID":add_issue.id}#should probably be returning the issue id instead


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
def update_issue(rest_issue_id):
    issue = db_restVKD.query.filter_by(id=rest_issue_id).first()

    update_counter = []

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
    draftstatus = request.json['draftstatus']
    lastmodified = get_jwt_identity()
    lastmodifiedtime = datetime.now()

    if title != "":
        issue.issueTitle = title
        update_counter.append(title)
        db.session.flush()
    if body != "":
        issue.issueBody = body
        update_counter.append(body)
        db.session.flush()
    if _type != "":
        issue.issueType = _type
        update_counter.append(_type)
        db.session.flush()
    if catergory != "":
        issue.issueCategory = catergory
        update_counter.append(catergory)
        db.session.flush()
    if summary != "":
        issue.issueSummary = summary
        update_counter.append(summary)
        db.session.flush()
    if remedy != "":
        issue.issueRemedy = remedy
        update_counter.append(remedy)
        db.session.flush()
    if cwe != "":
        issue.issueCwe = cwe
        update_counter.append(cwe)
        db.session.flush()
    if cve != "":
        issue.issueCve = cve
        update_counter.append(cve)
        db.session.flush()
    if severity != "":
        issue.issueSeverity = severity
        update_counter.append(severity)
        db.session.flush()
    if references != "":
        issue.issueReferences = references
        update_counter.append(references)
        db.session.flush()
    if cvss != "":
        issue.issueCvssvector = cvss
        update_counter.append(cvss)
        db.session.flush()
    if fairvector != "":
        issue.issueFairvector = fairvector
        update_counter.append(fairvector)
        db.session.flush()
    if draftstatus != "":
        issue.issueDraftstatus = draftstatus
        update_counter.append(draftstatus)
        db.session.flush()
    issue.issueLastmodifieduser = lastmodified
    update_counter.append(lastmodified) 
    issue.issueLastmodifiedtime = lastmodifiedtime
    update_counter.append(lastmodifiedtime)
    
    db.session.commit()
    return {"RestIssueID": str(restVKD.id), "Updated Items": update_counter}

@issue.delete("/rest/<int:rest_issue_id>")  ##delete one issue
@jwt_required()
def delete_issue(rest_issue_id):
    issue = db_restVKD.query.filter_by(id=rest_issue_id).first()
    if issue is None:
        return {"ERROR":"Issue does not exist in rest Vulnerability Knowledge Database"}, HTTP_404_NOT_FOUND
    deleted_id = issue.id
    db.session.delete(issue)
    db.session.commit()
    return {"issue Deleted":deleted_id}



'''
LIVE
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
            return {"ERROR":"Phase not found"}, HTTP_404_NOT_FOUND
    else:
        return {"ERROR":"issue not added (probably no engagement under that ID)"}, HTTP_404_NOT_FOUND
    


@issue.get("/<int:engagement_id>/issue/<int:issue_id>")
@jwt_required()
def get_engagement_issue(engagement_id,issue_id):
    #get both the engagement and the issue
    engagement = db_Engagement.query.filter_by(id=engagement_id).first()
    item = db_liveVKD.query.filter_by(id=issue_id).first()
    #make sure the issue belongs to the engagement
    if int(item.engagementId) != int(engagement.id):
        return {"ERROR":"Issue does not exist in engagement"}, HTTP_404_NOT_FOUND
    
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

@issue.put("/<int:engagement_id>/issue/<int:issue_id>")
@jwt_required()
def update_engagement_issue(engagement_id, issue_id):
    #get both the engagement and the issue
    engagement = db_Engagement.query.filter_by(id=engagement_id).first()
    issue = db_liveVKD.query.filter_by(id=issue_id).first()
    #make sure the issue belongs to the engagement
    if int(issue.engagementId) != int(engagement.id):
        return {"ERROR":"Issue does not exist in engagement"}, HTTP_404_NOT_FOUND
    
    update_counter = []
    #Get all of the data from the request
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
    draftstatus = request.json['draftstatus']
    lastmodified = get_jwt_identity()
    lastmodifiedtime = datetime.now()
    issueAddtovkd = request.json['addtovkd']
    retestflag = request.json['retestflag']
    #if the issue has new data, update the database object and then semi commit.
    if issueAddtovkd != "":
        print(int(issueAddtovkd))
        if int(issueAddtovkd) != 0 and int(issueAddtovkd) != 1:
            return {"ERROR":"Addtovkd must be 0 or 1"}
        issue.issueAddtovkd = int(issueAddtovkd)
        update_counter.append("issueAddtovkd")
        db.session.flush()
    if retestflag != "":
        if int(retestflag) != 0 and int(restestflag) != 1:
            return {"ERROR":"Retestflag must be 0 or 1"}
        issue.issueRetestflag = int(retestflag)
        update_counter.append("retestflag")
        db.session.flush()

    if title != "":
        issue.issueTitle = title
        update_counter.append("title")
        db.session.flush()
    if body != "":
        issue.issueBody = body
        update_counter.append("body")
        db.session.flush()
    if _type != "":
        issue.issueType = _type
        update_counter.append("type")
        db.session.flush()
    if catergory != "":
        issue.issueCategory = catergory
        update_counter.append("catergory")
        db.session.flush()
    if summary != "":
        issue.issueSummary = summary
        update_counter.append("summary")
        db.session.flush()
    if remedy != "":
        issue.issueRemedy = remedy
        update_counter.append("remedy")
        db.session.flush()
    if cwe != "":
        issue.issueCwe = cwe
        update_counter.append("cwe")
        db.session.flush()
    if cve != "":
        issue.issueCve = cve
        update_counter.append("cve")
        db.session.flush()
    if severity != "":
        issue.issueSeverity = severity
        update_counter.append("severity")
        db.session.flush()
    if references != "":
        issue.issueReferences = references
        update_counter.append("references")
        db.session.flush()
    if cvss != "":
        issue.issueCvssvector = cvss
        update_counter.append("cvss")
        db.session.flush()
    if fairvector != "":
        issue.issueFairvector = fairvector
        update_counter.append("fairvector")
        db.session.flush()
    if draftstatus != "":
        issue.issueDraftstatus = draftstatus
        update_counter.append("draftstatus")
        db.session.flush()

    
    #add the last modified user and time
    issue.issueLastmodifieduser = lastmodified
    issue.issueLastmodifiedtime = lastmodifiedtime

    
    #Update the database
    db.session.commit()
    return {"LiveIssueID": str(issue.id), "Updated Items": update_counter}


@issue.delete("/<int:engagement_id>/issue/<int:issue_id>")  ##delete one issue
@jwt_required()
def delete_engagement_issue(engagement_id, issue_id):
    #do sqlalchemy stuff to delete one issue
    engagement = db_Engagement.query.filter_by(id=engagement_id).first()
    issue = db_liveVKD.query.filter_by(id=issue_id).first()
    if engagement is None:
        return {"ERROR":"Engagement does not exist"}, HTTP_404_NOT_FOUND
    if issue is None:
        return {"ERROR":"Issue does not exist in engagement"}, HTTP_404_NOT_FOUND
    if int(issue.engagementId) != int(engagement.id):
        return {"ERROR":"Issue does not exist in engagement"}, HTTP_404_NOT_FOUND
    deleted_id = issue.id
    db.session.delete(issue)
    db.session.commit()
    return {"issue Deleted":deleted_id}