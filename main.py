import os
from prometheus_client import make_wsgi_app
from prometheus_client.core import REGISTRY
from flask import Flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from sonar.sonar import SonarCollector

# Get credentials & environment
sonar_collector = SonarCollector(
    server=os.environ.get("SONAR_SERVER", "http://sonar_server"),
    user=os.environ.get("SONAR_USERNAME", "username"),
    passwd=os.environ.get("SONAR_PASSWORD", "password")
)
REGISTRY.register(sonar_collector)

# Create Flask app
app = Flask(__name__)
@app.route('/ready')
def ready():
    return 'To infinity and beyond!'

# Add prometheus wsgi middleware to route /metrics requests
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/metrics': make_wsgi_app()
})
