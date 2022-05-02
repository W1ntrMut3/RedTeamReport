from RedTeamReporter import app, db
import argparse
from werkzeug.debug import DebuggedApplication
import os

parser = argparse.ArgumentParser(description='Red Team Reporting tool Server.')
parser.add_argument("--db-rebuild-delete", help='Rebuild the Database from Scratch (NOTE THIS WILL DELETE ALL DATA)', action="store_true")
parser.add_argument("--environment", help='Set the Environment to either development or production', choices=['development', 'production'])
args = parser.parse_args()
    

if args.environment:
        if args.environment == 'development':
            os.environ['FLASK_ENV'] = "development"
        elif args.environment == 'production':
            os.environ['FLASK_ENV'] = "production"


if __name__ == '__main__':

    if args.environment:
        if args.environment == 'development':
            app.config.from_object('RedTeamReporter.config.flask_config.DevConfig')

        elif args.environment == 'production':
            app.config.from_object('RedTeamReporter.config.flask_config.ProdConfig')
        
        else:
            app.config.from_object('RedTeamReporter.config.flask_config.Config')
    
    if args.db_rebuild_delete:
        db.drop_all()
        print("Deleting DB and Rebuilding")
        db.create_all()
    
    if args.environment == 'production':
        app.run(debug=False, use_evalex=False)
        
    else:
        app.run(debug=True)
    
