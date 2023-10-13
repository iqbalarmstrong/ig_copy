from application import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    tablename = "users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(128), nullable = False)
    password = db.Column(db.String(128), nullable = False)
    fullname = db.Column(db.String(128), nullable = False)
    email = db.Column(db.String(128), nullable = False)
    profile_pic = db.Column(db.String(128), default="default.jpg")
    bio = db.Column(db.String(128))
    join_data = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Boolean, default=True)
    following_users = db.relationship("Relation", foreign_keys="Relation.id_following", backref ="following", lazy=True)
    following_users = db.relationship("Relation", foreign_keys="Relation.id_follower", backref ="follower", lazy=True)
    posts = db.relationship("Post", backref="post_owner", lazy=True)
    comments = db.relationship("Comment", backref="comments_owner", lazy=True)
    likes = db.relationship("Like", backref="likes_owner", lazy=True)

class Relation(db.Model):
    tablename = "relationship"
    id = db.Column(db.Integer, primary_key = True)
    id_followers = db.Column(db.Integer, db.ForeignKey("users.id"),  nullable = False)
    id_following = db.Column(db.Integer, db.ForeignKey("users.id") , nullable = False)
    status = db.Column(db.Boolean, default=True)
    relation_date = db.Column(db.DateTime, default=datetime.utcnow)


class Post(db.Model):
    tablename = "posts"
    id = db.Column(db.Integer, primary_key = True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"),nullable = False)
    phote =db.Column(db.String(128), nullable = False)
    caption = db.Column(db.String(128), defaut="")
    post_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Boolean, default=True)
    comments = db.relationship("Comment", backref="commented", lazy = True)
    likes = db.relationship("Like", backref="liked", lazy = True)

class Comment(db.Model):
    tablename = "comments"
    id = db.Column(db.Integer, primary_key = True)
    text = db.Column(db.Text, nullable=False)
    cmmenter_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)
    hidden = db.Column(db.Boolean, default=False)
    comment_date = db.Column(db.DateTime, default=datetime.utcnow)


class Like(db.Model):
    tablename = "likes"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable = False)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable= False)
    status = db.Column(db.Boolean, default=True)
    like_date = db.Column(db.DateTime, default=datetime.utcnow)
    