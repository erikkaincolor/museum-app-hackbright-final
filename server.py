"This is the server my web app runs on"

from flask import Flask

app = Flask(__name__)


# This is where you'd write your view functions and routes, but there's
# no need to run server.py during the SQLAlchemy 1 lecture, so
# we didn't create any routes or view functions here.


if __name__ == "__main__":
    from model import connect_to_db

    connect_to_db(app, "cats") ############### ADD DB NAME

    app.run(debug=True, host="0.0.0.0")