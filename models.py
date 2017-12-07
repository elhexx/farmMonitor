from main import db
from datetime import datetime

class LOGS(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True)
    temp = db.Column(db.String(50))
    humd = db.Column(db.String(50))
    water_humd = db.Column(db.String(50))
    time = db.Column(db.DateTime)


    def __init__(self, temp, humd, water_humd):
        self.temp = temp
        self.humd = humd
        self.water_humd = water_humd
        self.time = datetime.utcnow()


    def __repr__(self):
        return '<User %r>' % self.id

def log(temp, humd, water_humd):
    print "log"
    db.create_all()
    log = LOGS(temp, humd, water_humd)
    db.session.add(log)
    db.session.commit()
    print 'done'
