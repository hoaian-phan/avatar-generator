""" Models for avatar generator app """

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Image class
class Image(db.Model):
    """ Image information """

    __tablename__ = "images"

    url = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    likes = db.Column(db.Integer)
    downloads = db.Column(db.Integer)

    def __repr__(self):
        """ Display image object on the screen """

        return f"<Image url={self.url} name={self.name} likes={self.likes} downloads={self.downloads}>"



# Connect to database
def connect_to_db(flask_app, db_uri="postgresql:///avatars", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")



if __name__ == "__main__":
    from server import app

    connect_to_db(app)