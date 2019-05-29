from app import db

class Animals(db.Model):
  __tablename__ = 'animalOrbs'
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



class Actor(db.Model):
  __tablename__ = 'Actor'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(400))
  dob = db.Column(db.String(10))
  description = db.Column(db.String(2000))
  movies = db.relationship('Movie', secondary = 'name', backref = 'actors')
  def __repr__(self):
    return 'Name: {}'.format(self.name)


class Role(db.Model):
  __tablename__ = 'Role'
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(400))
  superName = db.Column(db.String(400))
  mid = db.Column(db.Integer, db.ForeignKey('movies.id'))
  aid = db.Column(db.Integer, db.ForeignKey('Actor.id'))


  def __repr__(self):
    return 'Role: {}'.format(self.role)
