from flask import render_template, url_for, flash, redirect, request, jsonify, Blueprint
#from RedTeamReporter import app, db, bcrypt
from RedTeamReporter.models import db_Assets, db_liveVKD, db_restVKD, db_Engagement
from RedTeamReporter.issue import add_issue, get_all_issue, get_one_issue, update_issue, delete_issue, copy_issue, add_engagement_issue, get_engagement_issue, get_engagement_issues, update_engagement_issue, delete_engagement_issue
from RedTeamReporter.engagement import add_engagement, get_all_engagement, get_one_engagement, update_engagement, delete_engagement, add_phase, get_all_phase, get_one_phase, update_phase, delete_phase, add_asset, get_all_asset, get_one_asset, update_asset, delete_asset
#from flask_login import login_user, current_user, logout_user, login_required
from urllib.parse import urlparse, urljoin



def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc




#@app.route('/', methods=['GET','POST'])
def main_page():
    return("Hello World")

#@app.get("/hello")
def say_hello():
    return jsonify({"message": "hello world"})


'''
Login Page routes, deals with logging in, creating a session using flask_login and redirecting to the home page
'''
'''@app.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db_User.query.filter_by(userName=form.username.data).first()
        if user and bcrypt.check_password_hash(user.userPass, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            if not is_safe_url(next_page):
                return flask.abort(400)

            return redirect(next_page) if next_page else redirect(url_for('dashboard'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')

    return render_template('login.html', form=form)

'''

'''
Main dashboard that should appear on first login. Should include buttons to add new engagements, and retrieve current projects
that are specific to the user. 
'''
#@app.route('/dashboard')
#def dashboard():
    
'''
    Future Authentication work to be done here, flask_login wont work with API properly maybe.
    
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    return render_template('dashboard.html', user=current_user)
'''

'''
This should be rolled into the dashboard, but for now it is just a test page.
'''
#@app.route('/home')
#def home():
#	return render_template('home.html', posts=posts)




'''
This page will act as the home for the currently selected engagement. It will include a list of phases and issues in phases. The
 user will be able to select a phase and then view the issues in that phase.
'''
#@app.route('/engagement')
#def project():

'''
    Future Authentication work to be done here, flask_login wont work with API properly maybe.
    
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    return render_template('engagement.html', user=current_user)
'''


'''

'''
#@app.route('/passwordreset')
#def customer():

'''
    Future Authentication work to be done here, flask_login wont work with API properly maybe.
    
    if not current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('passwordreset.html')
'''


'''
This will be the main add a new engagement and phases page. A user can add a new engagement, and then add phases to that engagement.
After that has been configured, other engagement data is able to be added such as custmer etc.
'''
#@app.route('/newengagement')
#def newengagement():


'''
    Future Authentication work to be done here, flask_login wont work with API properly maybe.
    
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    return render_template('newengagement.html', user=current_user)
'''



'''
This page will show all of the Vulnerability Knowledge Database (VKB) issues that have been created and are stored. It 
will need some serach functionality or sort functionality to go through them, and probably only list up to 50 so
pagination will be required as well.
'''
#@app.route('/vkd')
#def vkd():

'''
    Future Authentication work to be done here, flask_login wont work with API properly maybe.
    
	if not current_user.is_authenticated:
        return redirect(url_for('login'))
    return render_template('vkd.html', user=current_user)
'''


'''
Admin page to add new users, and delete users, pause user login, and resume user login, add directly to the database.
Other functionality TBD, maybe configuration options?
'''

#@app.route('/admin')
#def admin():



'''
    Future Authentication work to be done here, flask_login wont work with API properly maybe.
    
	if not current_user.is_authenticated:
        return redirect(url_for('login'))
    return render_template('dashboard.html', user=current_user)
'''


'''
Logout requests come here to null the session and redirect for url. Not yet in use as the authentication method has changed.

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('login'))
'''