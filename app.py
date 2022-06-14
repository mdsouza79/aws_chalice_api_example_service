import os
from chalice import Chalice
from chalicelib.mainService import mainService

APP_NAME = os.getenv('APP_NAME')
ENV_NAME = os.getenv('ENV_NAME')

#the app_name value specified in config.json file is what gets displayed in aws lambda
#environment variable by the name APP_NAME has also been specified and set to same value as app_name in config.json file
#this is because the app_name parameter value specified for the "Chalice" function below is what gets used in aws api gatway
#so APP_NAME environment variable is imported in this name and used below
#when app_name is changed in config.json, the older function is still present in aws lambda and needs to be manually deleted
#when APP_NAME which is used here gets changed in config.json, the name gets automatically changed in aws api gateway as well

app = Chalice(app_name='{}-{}'.format(APP_NAME,ENV_NAME))
app.register_blueprint(mainService)