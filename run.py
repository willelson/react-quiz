#!flask/bin/python
from app import app
app.run(debug=app.config["DEBUG"], port=app.config["PORT"])