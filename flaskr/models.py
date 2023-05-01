from flask import url_for
from sqlalchemy.exc import IntegrityError
from run import db
import uuid


class Hospital(db.Model):

    __tablename__ = 'hospital'

    id = db.Column(db.String(80), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(256), nullable=False)
    patient = db.relationship('Patient', backref='patient')
    # patient = db.relationship('Patient', backref='patient', uselist=False)


    def __init__(self,id,name,city):
        self.id=id #uuid.uuid4()
        self.name=name
        self.city=city

patient_doctor = db.Table('patient_doctor',
    db.Column('patient_id', db.String, db.ForeignKey('patient.id'), primary_key=True),
    db.Column('doctor_id', db.String, db.ForeignKey('doctor.id'), primary_key=True)
)

class Patient(db.Model):

    __tablename__ = 'patient'

    id = db.Column(db.String(80), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=True)
    dni = db.Column(db.String(80), nullable=False)
    hospital_id = db.Column(db.String, db.ForeignKey('hospital.id'))
    doctors = db.relationship("Doctor", secondary=patient_doctor, backref="patients")


    def __init__(self,id,name,surname,dni,hospital_id):
        self.id=id #uuid.uuid4()
        self.name=name
        self.surname=surname
        self.dni=dni
        self.hospital_id=hospital_id

class Doctor(db.Model):

    __tablename__ = 'doctor'

    id = db.Column(db.String(80), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=True)
    speciality = db.Column(db.String(80), nullable=False)
    # patient_doctor = db.relationship("patient_doctor",secondary=patient_doctor)

    def __init__(self,id,name,surname,speciality):
        self.id=id #uuid.uuid4()
        self.name=name
        self.surname=surname
        self.speciality=speciality

