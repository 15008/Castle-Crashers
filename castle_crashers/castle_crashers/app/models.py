from app import db

class Animal(db.Model):
  __tablename__ = 'Animal'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  location = db.Column(db.String(10))
  cost = db.Column(db.Integer)
  description = db.Column(db.String(2000))
  requirement = db.Column(db.String(1000))
  magicBonus = db.Column(db.Integer)
  strengthBonus = db.Column(db.Integer)
  defenseBonus = db.Column(db.Integer)
  agilityBonus = db.Column(db.Integer)
  xpMultiplier = db.Column(db.Integer)
  #roles = db.relationship('Role', backref = 'movies')
  #def __repr__(self):
    #return 'Movie: {}'.format(self.title)

class Level(db.Model):
  __tablename__ = 'Level'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50))
  dob = db.Column(db.String(2000))
  chapter = db.Column(db.Integer)
  bossLevel = db.Column(db.String(10))
  arena = db.Column(db.String(10))
  store = db.Column(db.String(10))
  #movies = db.relationship('Movie', secondary = 'name', backref = 'actors')
  #def __repr__(self):
    #return 'Name: {}'.format(self.name)

class Weapon(db.Model):
  __tablename__ = 'Weapon'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100))
  strength = db.Column(db.Integer)
  magic = db.Column(db.Integer)
  defense = db.Column(db.Integer)
  agility = db.Column(db.Integer)
  iceSpecial = db.Column(db.Integer)
  critSpecial = db.Column(db.Integer)
  fireSpecial = db.Column(db.Integer)
  elecSpecial = db.Column(db.Integer)
  poiSpecial = db.Column(db.Integer)
  location = db.Column(db.String(100))
  requirement = db.Column(db.String(100))
  gold = db.Column(db.Integer)
  mode = db.Column(db.String(50))
  reqlvl = db.Column(db.Integer)
  #mid = db.Column(db.Integer, db.ForeignKey('movies.id'))
  #aid = db.Column(db.Integer, db.ForeignKey('Actor.id'))
  #def __repr__(self):
    #return 'Role: {}'.format(self.role)
