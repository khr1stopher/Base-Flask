from app import db

class Prefijos(db.Model):
    __tablename__ = "catprefijos"
    keyx = db.Column(db.Integer, primary_key=True)
    fechaalta = db.Column(db.DateTime)
    prefijo = db.Column(db.String(40))

    def __repr__(self):
        return '<prefijo {}>'.format(self.prefijo)