from flask_app import db
import datetime



class Gympost(db.Model):
    __tablename__ = 'gymposts'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    date = db.Column(db.DateTime)
    machine = db.Column(db.String)
    weight = db.Column(db.Integer)
    num_1set = db.Column(db.Integer)
    total_set = db.Column(db.Integer)
    comments = db.relationship('Comment',backref='post')


class Comment(db.Model):
    __tablename__ =  'comments'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('gymposts.id'))
    creator = db.Column(db.String)
    
    
 


def get_table():
    return Gympost.query.all()

def delete_post(id):
    post = db.session.query(Gympost).filter_by(id = id).first()
    if post is None:
        return None
    db.session.delete(post)
    db.session.commit()
    return True