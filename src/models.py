from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Person(db.Model):
    __tablename__= 'person'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250),nullable=False)
    last_name = db.Column(db.String(250),nullable=False)
    relationship = db.Column(db.String(250),nullable=False)
    age = db.Column(db.Integer,nullable=False)
    father_id = db.Column(db.Integer, db.ForeignKey('person.id'))
    mother_id = db.Column(db.Integer, db.ForeignKey('person.id'))


    def __repr__(self):
        return '<Person %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            'relationship':self.relationship
            # do not serialize the password, its a security breach
        }
    
    def getAll():
        members=Person.query.order_by(Person.age.desc())
        members= list(map(lambda Person: Person.serialize(),members))
        return members

    def getPerson(id):
        member= Person.query.get(id)
        if member is None: 
           return {'msg':'This member does not exist'}
        member= Person.serialize(member)

        return member