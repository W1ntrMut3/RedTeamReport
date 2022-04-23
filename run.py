from RedTeamReporter import app
import argparse
import os

parser = argparse.ArgumentParser(description='Red Team Reporting tool Server.')
parser.add_argument("--db-rebuild-delete", help='Rebuild the Database from Scratch (NOTE THIS WILL DELETE ALL DATA)', action="store_true")
parser.add_argument("--environment", help='Set the Environment to either development or production', choices=['development', 'production'])
args = parser.parse_args()
if args.db_rebuild_delete:
    print("Deleting DB and Rebuilding")

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
    app.run(debug=True)
