from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from model import connect_to_db, User, Team, Point, db

app=Flask(__name__)

connect_to_db(app, 'teampoints')

@app.route('/')
def show_points():
    teams = Team.query.all()
    return render_template('showpoints.html', teams=teams)


if __name__ == '__main__':

    app.debug = False

    app.run(host="0.0.0.0")
