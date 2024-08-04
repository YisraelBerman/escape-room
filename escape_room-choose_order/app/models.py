from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    stage = db.Column(db.Integer, nullable=False, default=1)
    points = db.Column(db.Integer, nullable=False, default=0)  # Add this line
    completed_stage1 = db.Column(db.Boolean, default=False)
    completed_stage2 = db.Column(db.Boolean, default=False)
    completed_stage3 = db.Column(db.Boolean, default=False)
    completed_stage4 = db.Column(db.Boolean, default=False)
    completed_stage5 = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}', 'Stage {self.stage}', 'Points {self.points}')"
