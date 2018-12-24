from flask import Flask

app = Flask(__name__)

from project.api.routes import mod
from project.site.routes import mod
from project.admin.routes import mod


app.register_blueprint(site.routes.mod)
app.register_blueprint(api.routes.mod, url_prefix='/api')
app.register_blueprint(admin.routes.mod, url_prefix='/admin')