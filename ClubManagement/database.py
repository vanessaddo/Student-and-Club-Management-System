from app import db

class Club(db.Model):
	name = db.Column(db.String(50))
	id = db.Column(db.String(10), primary_key = True)
	member_constraint = db.relationship('Member', backref='member',lazy='dynamic')
	event_constraint = db.relationship('Event', backref='event',lazy='dynamic')
	def __init__(self,name,id):
		self.name = name
		self.id = id

class Member(db.Model):
	usn = db.Column(db.String(10), primary_key=True)
	clubId = db.Column(db.String(10), db.ForeignKey('club.id'))
	email = db.Column(db.String(25))
	eventVolenteer_constraint = db.relationship('Event_Volenteers', backref='eventVolenteers',lazy='dynamic')
	attendance_constraint = db.relationship('Attendance', backref='attendance',lazy='dynamic')
	def __init__(self,cId,name,usn,email):
		self.usn = usn
		self.name = name
		self.clubId = cId
		self.email = email

class Event(db.Model):
	eventId = db.Column(db.String(10), primary_key = True)
	name = db.Column(db.String(25))	
	clubId = db.Column(db.String(10), db.ForeignKey('club.id'))
	eventVolenteer_constraint = db.relationship('Event_Volenteers', backref='eventVolenteers',lazy='dynamic')	
	attendance_constraint = db.relationship('Attendance', backref='attendance',lazy='dynamic')	
	def __init__(self,eventId,name,cId):
		self.name = name
		self.clubId= cId
		self.eventId= eventId
	
class Event_Volenteers(db.Model):
	usn = db.Column(db.String(10),db.ForeignKey('member.usn'),primary_key=True)
	eventId= db.Column(db.String(10),db.ForeignKey('event.eventId'),primary_key=True)	
	def __init__(self,usn,eventId):
		self.usn = usn
		self.eventId = eventId				

class Attendance(db.Model):
	#id = db.Column(db.Integer,primary_key = True)
	eventId= db.Column(db.String(10),db.ForeignKey('event.eventId'),primary_key = True)	
	usn = db.Column(db.String(10),db.ForeignKey('member.usn'),primary_key = True)
	date= db.column(db.String(20))
	def __init__(self,event,name,date):
		self.name=name
		self.event= event
		self.date=date		
	
db.create_all()		
			