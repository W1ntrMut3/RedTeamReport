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
    - [ ] Create a database model using SQL Alchemy
    - [ ] Create a database model function to control, refresh or manually update the database
    - [ ] Create requests to the database for adding and removing issues
    - [ ] Create requests to the database for adding and removing users
    - [ ] Create requests to the database for adding and removing affected hosts to an engagement
    - [ ] Create requests to the database for adding and removing engagements
    - [ ] Create requests to the database for adding and removing customers? -- might not need this tbh
    - [ ] Create requests to the database for adding and removing phases of engagements


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
 - [ ] Create word/template documenting functionality
    - [ ] Create a word template by using python-docx-template
    - [ ] Create functionality to apply data from the database to the template
 - [ ] Create User Authentication & Access Control Matrix
    - [ ] Create a user authentication and access control matrix function, and apply privileges to user roles

 - [ ] Create CSV report generation functionality

