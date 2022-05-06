from datetime import datetime, timezone
from flask_sqlalchemy import SQLAlchemy
##from flask_login import UserMixin

'''
@login_manager.user_loader
def load_user(user_id):
    return db_User.query.get(int(user_id))

'''

db = SQLAlchemy()

'''
Instantiating model for creating and interacting with the database.
'''

class db_User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer(), primary_key=True)
    userName = db.Column(db.String(80), nullable=False, unique=True)
    userPass = db.Column(db.Text(), nullable=False)
    userEmail = db.Column(db.String(150), nullable=False, unique=True)
    userPhone = db.Column(db.String(30))
    userFirstname = db.Column(db.String(50), nullable=False)
    userLastname = db.Column(db.String(50), nullable=False)
    userGroup = db.Column(db.Text())
    userPrivilege = db.Column((db.Text), nullable=False)
    userLastlogin = db.Column(db.DateTime())
    userCreated = db.Column(db.DateTime(), default=datetime.now(timezone.utc))
    userUpdated = db.Column(db.DateTime(), onupdate=datetime.now(timezone.utc))
    userImage = db.Column(db.Text())#generate a long random string for the filename, and then save it to the DB and the filesystem
    userDob = db.Column(db.Text())#probably not needed but will keep incase?
    userPasswordchange = db.Column(db.Boolean(), default=False)# is a password change pending?
    userLoginattemptscount = db.Column(db.Integer(), default=0)#increment on failed login
    userCanLogin = db.Column(db.Boolean, default=True) #check to see if this is true before giving access
    token = db.relationship('TokenBlocklist', backref='db_User', lazy=True)
    
    def __repr__(self):
        return f"User('{self.id}','{self.userName}', '{self.userEmail}', '{self.userCanLogin}')"


'''
Model for blacklisting sessions/JWT tokens, note: I need to write some sort of cleanup for sessions in here over x time.
Also note: this is such a garbage way of handling session tokens, I need to figure out a better way to do this.
'''
class TokenBlocklist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    jti = db.Column(db.String(36), nullable=False, index=True)
    created_at = db.Column(db.DateTime, nullable=False)
    type = db.Column(db.String(16), nullable=False)
    user_id = db.Column(db.ForeignKey('User.id'), nullable=False)


'''
Model for creating and interacting with the static VKD, this table should only store curated issues that have been QA'd.

'''

class db_restVKD(db.Model):
    __tablename__ = 'restVKD'

    id = db.Column(db.Integer, primary_key=True) #resting issue id
    issueTitle = db.Column(db.Text())
    issueBody = db.Column(db.Text())
    issueType = db.Column(db.Text())
    issueCategory = db.Column(db.Text())
    issueSummary = db.Column(db.Text())
    issueRemedy = db.Column(db.Text())
    issueCwe = db.Column(db.Text())
    issueCve = db.Column(db.Text())
    issueSeverity = db.Column(db.Text())
    issueReferences = db.Column(db.Text())
    issueCvssvector = db.Column(db.Text())
    issueFairvector = db.Column(db.Text())
    issueCreator = db.Column(db.Text())
    issueLastmodifieduser = db.Column(db.Text())
    issueDraftstatus = db.Column(db.Text())
    issueCreatedtime = db.Column(db.DateTime(), default=datetime.now(timezone.utc))
    issueLastmodifiedtime = db.Column(db.DateTime(), onupdate=datetime.now(timezone.utc))


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

'''
Model for creating and interacting with the LIVE issue table. This will hold all issues that are in use in reports, 
and import items in from the static database(db_restVKD). This will probably be the largest table.
'''
class db_liveVKD(db.Model):
    __tablename__ = 'liveVKD'

    id = db.Column(db.Integer, primary_key=True)
    issueTitle = db.Column(db.Text())
    issueBody = db.Column(db.Text())
    issueType = db.Column(db.Text())
    issueCategory = db.Column(db.Text())
    issueSummary = db.Column(db.Text())
    issueRemedy = db.Column(db.Text())
    issueCwe = db.Column(db.Text())
    issueCve = db.Column(db.Text())
    issueSeverity = db.Column(db.Text())
    issueReferences = db.Column(db.Text())
    issueCvssvector = db.Column(db.Text())
    issueFairvector = db.Column(db.Text())
    issueCreator = db.Column(db.Text()) #could this be a foreign key?
    issueLastmodifieduser = db.Column(db.Text())
    issueDraftstatus = db.Column(db.Text())
    issueCreatedtime = db.Column(db.DateTime(), default=datetime.now(timezone.utc))
    issueLastmodifiedtime = db.Column(db.DateTime(), onupdate=datetime.now(timezone.utc))
    issuePhaseid = db.Column(db.Integer(), db.ForeignKey('Phase.id')) #foreignkey phase
    engagementId = db.Column(db.Text(), db.ForeignKey('Engagement.id')) #foreignkey engagement
    issueAddtovkd = db.Column(db.Boolean())
    issueRestid = db.Column(db.Text())
    issueRetestflag = db.Column(db.Boolean())
    assets = db.relationship('db_Assets', backref='liveVKD', lazy=True)

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
        self.issueAddtovkd = issueAddtovkd
        self.issueRestid = issueRestid
        self.issueRetestflag = issueRetestflag
    
    def __repr__(self):
        return f"<Issue Title: {self.issueTitle} Issue Summary: {self.issueSummary} Issue Type:{self.issueType}  Issue Remedy:{self.issueRemedy}>"

'''
Model for creating and interacting with engagement data. This will hold the framework of report creation and be the main
pivot table for putting the report together. Everything will refer back to the engagement ID (issues assets and phases), to correlate
where they need to be.
'''

class db_Engagement(db.Model):
    __tablename__ = 'Engagement'

    id = db.Column(db.Integer, primary_key=True)
    engagementName = db.Column(db.Text())
    rtCode = db.Column(db.Text())
    customerName = db.Column(db.Text())
    customerEmail = db.Column(db.Text())
    customerOrg = db.Column(db.Text())
    scopeField = db.Column(db.Text())
    consultantName = db.Column(db.Text())
    issue = db.relationship('db_liveVKD', backref='Engagement', lazy=True)
    assets = db.relationship('db_Assets', backref='Engagement', lazy=True)
    phase = db.relationship('db_Phase', backref='Engagement', lazy=True)


    def __init__(self, id, engagementId, engagementName, rtCode, customerId, scopeId, consultantName):
        self.id = id
        self.engagementName = engagementName
        self.rtCode = rtCode 
        self.customerName = customerName
        self.customerEmail = customerEmail
        self.customerOrg = customerOrg
        self.scopeField = scopeId
        self.consultantName = consultantName
    
    def __repr__(self):
        return f"<Engagement ID: {self.id} Name: {self.engagementName} RedTeam Code: {self.rtCode} Customer Name: {self.customerName}  Customer Email: {self.customerEmail} Scope: {self.scopeField} Consultant Name: {self.consultantName}>"

'''
Model for determining what phase issues are assigned to as well as the phase id and any scoping differences.
'''
class db_Phase(db.Model):
    __tablename__ = 'Phase'

    id = db.Column(db.Integer, primary_key=True)
    engagementId = db.Column(db.Integer(), db.ForeignKey('Engagement.id'))
    phaseName = db.Column(db.Text())
    phaseScope = db.Column(db.Text())
    issue = db.relationship('db_liveVKD', backref='Phase', lazy=True)


    def __init__(self, id, engagementId, engagementName, rtCode, customerId, scopeId, phaseId):
        self.id = id
        self.engagementId = engagementId
        self.phaseScope = phaseScope
        self.phaseName = phaseName
    
    def __repr__(self):
        return f"<Phase ID: {self.id} Name: {self.phaseName} Phase Scope: {self.phaseScope} Related Engagement ID: {self.engagementId}>"

'''
Model for determining what assets are assigned to what issue, and most likely engagement. Return points should be
something along the lines of "assets where assetEngagementid = engagementId" or something similar.
'''

class db_Assets(db.Model):
    __tablename__ = 'Assets'

    id = db.Column(db.Integer, primary_key=True)
    assetEngagementid = db.Column(db.Text(), db.ForeignKey('Engagement.id')) # probably needs to be a FK to the Engagement table
    assetIssueid = db.Column(db.Text(), db.ForeignKey('liveVKD.id')) # probably needs to be a FK to the Issue table
    assetName = db.Column(db.Text())
    assetFqdn = db.Column(db.Text())
    assetCriticality = db.Column(db.Text())
    assetLocation = db.Column(db.Text())


    def __init__(self, id, assetEngagementid, assetName, assetFqdn, assetCriticality, assetLocation):
        self.id = id
        self.assetEngagementid = assetEngagementid
        self.assetIssueid = assetIssueid
        self.assetName = assetName
        self.assetFqdn = assetFqdn
        self.assetCriticality = assetCriticality
        self.assetLocation = assetLocation
    
    def __repr__(self):
        return f"<Asset name: {self.assetName}, Asset Engagement ID: {self.assetEngagementid}, Asset Issue ID: {self.assetIssueid}>"

