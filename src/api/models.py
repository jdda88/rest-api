from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    favorite_planets = db.Column(db.String(200))
    favorite_people = db.Column(db.String(200))


    # email = db.Column(db.String(120), unique=True, nullable=False)
    # password = db.Column(db.String(80), unique=False, nullable=False)
    # is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            # "email": self.email,
            "favorite_planets": json.loads(self.favorite_planets),
            "favorite_people": json.loads(self.favorite_people)
            # do not serialize the password, its a security breach
        }