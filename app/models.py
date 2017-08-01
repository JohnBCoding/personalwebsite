from app import db


class Admin(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(64))
    posts = db.relationship("Post", backref="author", lazy="dynamic")

    @property
    def is_authenticated(self):

        return True

    @property
    def is_active(self):

        return True

    @property
    def is_anonymous(self):

        return False

    def get_id(self):

        return str(self.id)

    def __repr__(self):

        return "<User %r>" % (self.username)


class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey("admin.id"))

    def convert_datetime(self):

        # Converts post timestamp to MONTH DAY, YEAR format.
        # Ex. July 21, 2018
        return self.timestamp.strftime("%B %d, %Y")

    def __repr__(self):

        return "<Post %r>" % (self.body)