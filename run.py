from RedTeamReport import app
import argparse
import os

parser = argparse.ArgumentParser(description='Red Team Reporting tool Server.')
parser.add_argument("--db-rebuild-delete", help='Rebuild the Database from Scratch (NOTE THIS WILL DELETE ALL DATA)', action="store_true")
parser.add_argument("--enviroment", help='Set the Enviroment to either development or production', choices=['development', 'production'])
args = parser.parse_args()
if args.db_rebuild_delete:
    print("Deleting DB and Rebuilding")

if args.enviroment:
        if args.enviroment == 'development':
            os.environ['FLASK_ENV'] = "development"
        elif args.enviroment == 'production':
            os.environ['FLASK_ENV'] = "production"


if __name__ == '__main__':

    if args.enviroment:
        if args.enviroment == 'development':
            app.config.from_object('RedTeamReport.config.DevConfig')
        elif args.enviroment == 'production':
            app.config.from_object('RedTeamReport.config.ProdConfig')
        else:
            app.config.from_object('RedTeamReport.config.Config')
    app.run(debug=True)
