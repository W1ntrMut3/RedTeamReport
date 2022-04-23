from flask import Blueprint

issue = Blueprint("issue", __name__, url_prefix="/api/v1/issue")


'''
Issue control for rest VKD, need to be able to read update etc. These are for the database and saved issues.
'''


@issue.post('/<int:id>')
def add_issue():
    return "issue Added"


@issue.get("/")
def get_all_issue():

    ##for items in issue (after sqlalchemy):
    ## return list as python dict that should get jsonify'd, this is also maybe 
    return {"user":"me"}

@issue.get("/<int:rest_issue_id>")
def get_one_issue():
    ##do sqlalchemy stuff to get one issue -- maye like this def search():
    #query = request.args.get("query") # here query will be the search inputs name
    #allVideos = Videos.query.filter(Videos.title.like("%"+query+"%")).all()
    return {"user":"me"}


@issue.put("/<int:rest_issue_id>")
def update_issue():
    ##do sqlalchemy stuff to update one issue
    return "issue Updated"


@issue.delete("/<int:rest_issue_id>")  ##delete one issue
def delete_issue():
    #do sqlalchemy stuff to delete one issue
    return "issue Deleted"


@issue.post('/<int:engagement_id>/issue_copy/<int:rest_issue_id>')
def copy_issue():
    return "Issue copied"


'''
Issue control for engagements. These are issues that are applied to an issue or an engagement.

'''



@engagement_issue.post('/<int:engagement_id>/issue/')
def add_engagement_issue():
    #return the issue ID and the engagement id after creating it, needs to take in a whole lot here
    return "issue Added"


@engagement_issue.get("/<int:engagement_id>/issue/")
def get_engagement_issues():

    ##list all issues attached to an engagement
    ## return list as python dict that should get jsonify'd
    return {"user":"me"}

@engagement_issue.get("/<int:engagement_id>/issue/<int:issue_id>")
def get_engagement_issue():
    ##list one issue and all data for it including remediation etc
    return {"user":"me"}


@engagement_issue.put("/<int:engagement_id>/issue/<int:issue_id>")
def update_engagement_issue():
    ##do sqlalchemy stuff to update one issue uipdates the entirety of it
    return "issue Updated"


@engagement_issue.delete("/<int:engagement_id>/issue/<int:issue_id>")  ##delete one issue
def delete_engagement_issue():
    #do sqlalchemy stuff to delete one issue
    return "issue Deleted"