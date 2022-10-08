from . import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), index = True, unique = True, nullable = False)
    emailid = db.Column(db.String(100), index = True, nullable = False)
    password_hash = db.Column(db.String(255), nullable = False)

    comments = db.relationship('Comment', backref = 'user')

class Destination(db.Model):
    __tablename__ = 'destination'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))
    description = db.Column(db.String(512))
    image = db.Column(db.String(400))
    currency = db.Column(db.String(3))

    comments = db.relationship('Comment',backref='destination')

class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default = datetime.now())

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    destination_id = db.Column(db.Integer, db.ForeignKey('destination.id'))







# class Destination:
    
#     def __init__(self, name, description, image_fp, currency):
#         self.name=name
#         self.description=description
#         self.image=image_fp
#         self.currency=currency
#         self.comments=list()
    
#     def set_comments(self,comment):
#         self.comments.append(comment)

#     def __repr__(self):
#         str = 'Name {0}, Currency {1}'
#         str.format(self.name, self.currency)
#         return str

# class Comment:
#     def __init__(self,user,text,created_at):
#         self.user=user
#         self.text=user
#         self.created_at = created_at