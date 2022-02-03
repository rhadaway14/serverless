from flask import Flask
from flask_restful import Api


from resource import CL_Resource, CL_DBBuild



app = Flask(__name__)
api = Api(app)



# resources
api.add_resource(CL_Resource, '/')
api.add_resource(CL_DBBuild, '/build')



if __name__ == '__main__':
    app.run()