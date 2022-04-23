from datetime import datetime
from RedTeamReporter import db
##from flask_login import UserMixin

'''
@login_manager.user_loader
def load_user(user_id):
    return db_User.query.get(int(user_id))


class db_User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    userId = db.Column(db.String(30), nullable=False)
    userName = db.Column(db.String(), nullable=False, unique=True)
    userPass = db.Column(db.String(), nullable=False)
    userEmail = db.Column(db.String(), nullable=False, unique=True)
    userPhone = db.Column(db.String())
    userGroup = db.Column(db.String())
    userPrivilege = db.Column(db.String(), nullable=False)
    userLastlogin = db.Column(db.String())
    userCreated = db.Column(db.String())
    userOrg = db.Column(db.String())
    userImage = db.Column(db.String())#might need to be binary
    userDob = db.Column(db.String())
    userPasswordchange = db.Column(db.String())
    userLoginattemptscount = db.Column(db.String())
    userCanLogin = db.column(db.Boolean, default=True)



    def __init__(self, userId, userName, userPass, userEmail, userPhone, userGroup, userPrivilege, userLastlogin, userCreated, userOrg, userImage, userDob, userPasswordchange, userLoginattemptscount):
        self.userId = userId
        self.userName = userName
        self.userPass = userPass
        self.userEmail = userEmail
        self.userPhone = userPhone
        self.userGroup = userGroup
        self.userPrivilege = userPrivilege
        self.userLastlogin = userLastlogin
        self.userCreated = userCreated
        self.userOrg = userOrg
        self.userImage = userImage
        self.userDob = userDob
        self.userPasswordchange = userPasswordchange
        self.userLoginattemptscount = userLoginattemptscount
        self.userCanLogin = userCanLogin
    
    def __repr__(self):
        return f"User('{self.userName}', '{self.userEmail}', '{self.userCanLogin}')"
'''

class db_restVKD(db.Model):
    __tablename__ = 'restVKD'

    id = db.Column(db.Integer, primary_key=True)
    issueTitle = db.Column(db.String())
    issueBody = db.Column(db.String())
    issueType = db.Column(db.String())
    issueCategory = db.Column(db.String())
    issueSummary = db.Column(db.String())
    issueRemedy = db.Column(db.String())
    issueCwe = db.Column(db.String())
    issueCve = db.Column(db.String())
    issueSeverity = db.Column(db.String())
    issueReferences = db.Column(db.String())
    issueCvssvector = db.Column(db.String())
    issueFairvector = db.Column(db.String())
    issueCreator = db.Column(db.String())
    issueLastmodifieduser = db.Column(db.String())
    issueDraftstatus = db.Column(db.String())
    issueCreatedtime = db.Column(db.DateTime())
    issueLastmodifiedtime = db.Column(db.DateTime())


    def __init__(self, id, issueTitle, issueBody, issueType, issueCategory, issueSummary, issueRemedy, issueCwe, issueCve, issueSeverity, issueReferences, issueCvssvector, issueFairvector, issueCreator, issueLastmodifieduser, issueDraftstatus, issueCreatedtime, issueLastmodifiedtime):
        self.id = id
        self.issueTitle = issueTitle
        self.issueBody = issueBody
        self.issueType = issueType 
        self.issueCategory = issueCategory 
        self.issueSummary = issueSummary
        self.issueRemedy = issueRemedy  
        self.issueCwe = issueCwe 
        self.issueCve = issueCve
        self.issueSeverity = issueSeverity
        self.issueReferences = issueReferences
        self.issueCvssvector = issueCvssvector
        self.issueFairvector = issueFairvector
        self.issueCreator = issueCreator
        self.issueLastmodifieduser = issueLastmodifieduser  
        self.issueDraftstatus = issueDraftstatus 
        self.issueCreatedtime = issueCreatedtime
        self.issueLastmodifiedtime = issueLastmodifiedtime 
    
    def __repr__(self):
        return f"<Issue Title: {self.issueTitle} Issue Summary: {self.issueSummary} Issue Type:{self.issueType}  Issue Remedy:{self.issueRemedy}>"


class db_liveVKD(db.Model):
    __tablename__ = 'liveVKD'

    id = db.Column(db.Integer, primary_key=True)
    issueTitle = db.Column(db.String())
    issueBody = db.Column(db.String())
    issueType = db.Column(db.String())
    issueCategory = db.Column(db.String())
    issueSummary = db.Column(db.String())
    issueRemedy = db.Column(db.String())
    issueCwe = db.Column(db.String())
    issueCve = db.Column(db.String())
    issueSeverity = db.Column(db.String())
    issueReferences = db.Column(db.String())
    issueCvssvector = db.Column(db.String())
    issueFairvector = db.Column(db.String())
    issueCreator = db.Column(db.String()) #could this be a foreign key?
    issueLastmodifieduser = db.Column(db.String())
    issueDraftstatus = db.Column(db.String())
    issueCreatedtime = db.Column(db.DateTime())
    issueLastmodifiedtime = db.Column(db.DateTime())
    issuePhaseid = db.Column(db.String()) #foreignkey phase
    engagementId = db.Column(db.String()) #foreignkey engagement
    issueAddtovkd = db.Column(db.Boolean())
    issueRestid = db.Column(db.String())
    issueRetestflag = db.Column(db.Boolean())

    def __init__(self, id, issueTitle, issueBody, issueType, issueCategory, issueSummary, issueRemedy, issueCwe, issueCve, issueSeverity, issueReferences, issueCvssvector, issueFairvector, issueCreator, issueLastmodifieduser, issueDraftstatus, issueCreatedtime, issueLastmodifiedtime, issuePhaseid, engagementId, issueAddtovkd, issueRestid, issueRetestflag):
        self.id = id
        self.issueTitle = issueTitle
        self.issueBody = issueBody
        self.issueType = issueType 
        self.issueCategory = issueCategory 
        self.issueSummary = issueSummary
        self.issueRemedy = issueRemedy  
        self.issueCwe = issueCwe 
        self.issueCve = issueCve
        self.issueSeverity = issueSeverity
        self.issueReferences = issueReferences
        self.issueCvssvector = issueCvssvector
        self.issueFairvector = issueFairvector
        self.issueCreator = issueCreator
        self.issueLastmodifieduser = issueLastmodifieduser  
        self.issueDraftstatus = issueDraftstatus 
        self.issueCreatedtime = issueCreatedtime
        self.issueLastmodifiedtime = issueLastmodifiedtime 
        self.issuePhaseid = issuePhaseid
        self.engagementId = engagementId
        self.assetId = assetId
        self.issueAddtovkd = issueAddtovkd
        self.issueRestid = issueRestid
        self.issueRetestflag = issueRetestflag
    
    def __repr__(self):
        return f"<Issue Title: {self.issueTitle} Issue Summary: {self.issueSummary} Issue Type:{self.issueType}  Issue Remedy:{self.issueRemedy}>"

class db_Engagement(db.Model):
    __tablename__ = 'Engagement'

    id = db.Column(db.Integer, primary_key=True)
    engagementId = db.Column(db.String()) 
    engagementName = db.Column(db.String())
    rtCode = db.Column(db.String())
    customerName = db.Column(db.String())
    customerEmail = db.Column(db.String())
    customerOrg = db.Column(db.String())
    scopeField = db.Column(db.String())
    phaseId = db.Column(db.String()) 


    def __init__(self, id, engagementId, engagementName, rtCode, customerId, scopeId, phaseId):
        self.id = id
        self.engagementId = engagementId
        self.engagementName = engagementName
        self.rtCode = rtCode 
        self.customerName = customerName
        self.customerEmail = customerEmail
        self.customerOrg = customerOrg
        self.scopeField = scopeId
        self.phaseId = phaseId
    
    def __repr__(self):
        return f"<Engagement ID: {self.engagementID} Name: {self.engagementName} RedTeam Code: {self.rtCode} Customer Name: {self.customerName}  Customer Email: {self.customerEmail} Customer Organization: {self.customerOrg} Scope: {self.scopeField} Phase: {self.scopeField}>"



class db_Assets(db.Model):
    __tablename__ = 'Assets'

    id = db.Column(db.Integer, primary_key=True)
    assetEngagementid = db.Column(db.String())
    assetIssueid = db.Column(db.String())
    assetName = db.Column(db.String())
    assetFqdn = db.Column(db.String())
    assetCriticality = db.Column(db.String())
    assetLocation = db.Column(db.String())


    def __init__(self, id, assetEngagementid, assetName, assetFqdn, assetCriticality, assetLocation):
        self.id = id
        self.assetEngagementid = assetEngagementid
        self.assetName = assetName
        self.assetFqdn = assetFqdn
        self.assetCriticality = assetCriticality
        self.assetLocation = assetLocation
    
    def __repr__(self):
        return f"<Asset name: {self.assetName}, Asset Engagement ID: {self.assetEngagementid}>"

