from app import db

class Orb(db.Model):
    __tablename__ = 'Orb'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    locationid = db.Column(db.Integer, db.ForeignKey('Location.id'), nullable=False)
    description = db.Column(db.String(2000))
    cost = db.Column(db.Integer)
    req = db.Column(db.String(1000))
    magicBonus = db.Column(db.Integer)
    strengthBonus = db.Column(db.Integer)
    defenseBonus = db.Column(db.Integer)
    agilityBonus = db.Column(db.Integer)
    xpBonus = db.Column(db.Integer)

class Location(db.Model):
    __tablename__ = 'Location'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(2000))
    chapter = db.Column(db.Integer, nullable=False)
    localeType = db.Column(db.String(10))
    orbLoc = db.relationship('Orb')
    weaponLoc = db.relationship('Weapon')

class Weapon(db.Model):
    __tablename__ = 'Weapon'
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    locationid = db.Column(db.Integer, db.ForeignKey('Location.id'), nullable=False)
    reqItem = db.Column(db.String(2000))
    reqLevel = db.Column(db.Integer, nullable=False)
    mode = db.Column(db.String(10), nullable=False)
    strength = db.Column(db.Integer)
    magic = db.Column(db.Integer)
    defense = db.Column(db.Integer)
    agility = db.Column(db.Integer)
    iceSpecial = db.Column(db.Integer)
    critSpecial = db.Column(db.Integer)
    fireSpecial = db.Column(db.Integer)
    elecSpecial = db.Column(db.Integer)
    poiSpecial = db.Column(db.Integer)
    cost = db.Column(db.Integer)
