# RedTeamReport
A reporting tool for red teams written in python with rich functionality and report generation.

## Problem Statement:
The Red Team needs a reporting tool which can perform the following:

Web application that can be scaled
Authenticate a user to the application
Identify and find engagement reports
Create new issues in a HTML Rich way
Provide an easy issue risk marking 
Store issues/ add to issue library
Access issue library
Visualise the issues in a report and organise them based on severity
Generate a report based on a template
Generate a CSV Report of the issues


## Indepth Requirements and Features:
### Database:
 - [ ] Create backend database connectors
    - [x] Create a database model using SQL Alchemy
    - [x] Create classes for the following tables:
        - Rest VKD
        - Live VKD
        - Engagement
        - Assets
        - Authentication
        - Audit
    - [x] Create a database model function to control, refresh or manually update the database
    - [ ] Create requests to the database for adding and removing issues
    - [x] Create requests to the database for adding and removing users
    - [ ] Create requests to the database for adding and removing affected hosts to an engagement
    - [ ] Create requests to the database for adding and removing engagements
    - [ ] Create requests to the database for adding and removing phases of engagements
    - [x] Add Foreign Keys to the database/create relations between data

### Frontend:
 - [ ] Create frontend web application
    - [ ] Create issue risk marking functionality
    - [ ] Create issue library page
    - [ ] Create visualisation and main engagement page
    - [ ] Create engagement creation page
    - [ ] Create profile page
    - [ ] Create admin page
    - [ ] Create user addition and removal page, and user management page
    - [ ] Create report generation functionality
    - [ ] Create issue addition page
    - [ ] Create user authentication/login landing page
    - [ ] Create issue removal or move functionality
    - [ ] Create phase addition removal or movement functionality in engagement page


### Backend:
 - [ ] Create API for frontend to hook into

 - [ ] Create word/template documenting functionality
    - [ ] Create a word template processing function by using python-docx-template
    - [ ] Create a word document template with jinja2
    - [ ] Create functionality to apply data from the database to the template
 - [ ] Create User Authentication & Access Control Matrix
    - [ ] Create a user authentication and access control matrix function, and apply privileges to user roles
    - [ ] Define individual roles that build from the bottom up (Viewer > Contributor > Manager > Admin)
    - [ ] Tag and update functionality at API level? with user roles
 - [ ] Create CSV report generation functionality
    - [ ] Create a csv file output and structure it using lists and using csv library

 - [ ] Create Docker/K8 container for Web Server and App Server components/ Maybe microservice?
    - [ ] Research differences between web and app servers and find appropriate setups




