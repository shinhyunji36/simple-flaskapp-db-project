from flask_app import db
import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique = True, nullable = False)
    email = db.Column(db.String(120), unique = True, nullable = False)
    password = db.Column(db.String(32), nullable = False)
    


class Gympost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable = False)
    date = db.Column(db.DateTime, nullable=True)
    machine = db.Column(db.String)
    weight = db.Column(db.String)
    num_1set = db.Column(db.String)
    total_set = db.Column(db.String)



def get_table():
    return Gympost.query.all()

def delete_post(post_id):
    post = db.session.query(Gympost).filter_by(id = post_id).first()
    if post is None:
        return None
    db.session.delete(post)
    db.session.commit()
    return True