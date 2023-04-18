from flask import Flask, render_template, request, redirect, url_for
from werkzeug.urls import url_parse
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import create_database, database_exists
import uuid
import os
import json

app = Flask(__name__)
app.app_context().push()
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'
app.config['SQLALCHEMY_DATABASE_URI'] = ### Definir la URI de Conexión
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
    create_database(app.config['SQLALCHEMY_DATABASE_URI'])

db = SQLAlchemy(app)
db.init_app(app)

from models import Hospital, Patient, Doctor
db.create_all()

@app.route("/")
def index():
    return redirect("/hospitals")

@app.route("/home")
def show_home():
    return redirect("/hospitals")

# Buscar todos los hospitales 
@app.route("/hospitals")
def show_hospitals():
    ### Complete la función a partir de aquí ###


    return render_template("index_hospitals.html",hospitals=all_hospitals)

# Filtra los hospitales por ciudad
@app.route('/hospitals/filterByCity',methods=['GET','POST'])
def filterHospitalsByCity():
    ### Complete la función a partir de aquí ###


    return render_template("index_hospitals.html",hospitals=all_hospitals)
    
# Buscar pacientes de un hospital ordenadors por el nombre (de la A a la Z)
@app.route('/hospitals/<hospital_id>/patients',methods=['GET'])
def list_hospital_patients(hospital_id):
    ### Complete la función a partir de aquí ###


    return render_template("index_patients.html",hospital=hospital_id, patients= patients, patientDeleted='')

# Muestra la informacion de un paciente
@app.route('/hospitals/<hospital_id>/patients/<patient_id>',methods=['GET','POST'])
def read_patient(hospital_id,patient_id):
    ### Complete la función a partir de aquí ###


    return render_template("show.html",hospital=hospital_id, patient= patient)

@app.route("/hospitals/<hospital_id>/patients/new")
def show_create(hospital_id):
    return render_template('new.html',hospital=hospital_id)

# Crea un paciente en un hospital
@app.route('/hospitals/<hospital_id>/patients',methods=['POST'])
def create_patient(hospital_id):
    ### Complete la función a partir de aquí ###


    return redirect('/hospitals/'+hospital_id+'/patients')


@app.route('/hospitals/<hospital_id>/patients/<patient_id>/edit',methods=['GET'])
def create_edited_patient(hospital_id,patient_id):
    query = db.select(Patient).where(Patient.id==patient_id)
    patient = db.session.execute(query).first()[0]
    updated_patient = Patient(patient_id, patient.name,
        patient.surname,
        patient.dni,
        patient.hospital_id)
    return render_template("edit.html",hospital=hospital_id, patient= updated_patient)

# Borra un paciente
@app.route('/hospitals/<hospital_id>/patients/<patient_id>/delete',methods=['GET','POST'])
def delete_patient(hospital_id,patient_id):
    ### Complete la función a partir de aquí ###


    return redirect('/hospitals/'+hospital_id+'/patients?patientDeleted=true')

# Actualiza un paciente 
@app.route('/hospitals/<hospital_id>/patients/<patient_id>/updated', methods = ['POST','PUT'])
def update_patient(hospital_id,patient_id):
    ### Complete la función a partir de aquí ###


    return render_template("show.html",hospital=hospital_id, patient= patient)


# Asigna un doctor y devuelve los datos del paciente
@app.route('/hospitals/<hospital_id>/patients/<patient_id>/assign_doctor/assigned', methods = ['POST','PUT'])
def assign_doctor(hospital_id,patient_id):
    ### Complete la función a partir de aquí ###


    return render_template("show.html",hospital=hospital_id, patient= patient)


@app.route('/hospitals/<hospital_id>/patients/<patient_id>/assign_doctor',methods=['GET'])
def pass_doctor(hospital_id,patient_id):
    return render_template("assign_doctor.html",hospital=hospital_id, patient= patient_id)


# Muestras los medicos de un paciente
@app.route('/hospitals/<hospital_id>/patients/<patient_id>/show_doctors',methods=['GET','POST'])
def show_patient_doctors(hospital_id,patient_id):
    ### Complete la función a partir de aquí ###


    return render_template("show_doctors.html",doctors=doctors, patient= patient_id)


################### Espacio para seeders ############################

def seeder():

    print('#### Check Database seed ####')
    all_hospitals = db.session.execute(db.select(Hospital)).all()
    all_hospitals = [id for id, in all_hospitals]

    if (len(all_hospitals) <= 0):
        print('#### Tables are empty ####')
        print('#### Adding some entries... ####')
        with open('flaskr/seeders/seeders.json') as f:
            print('#### Adding some entries... ---####')
            data = json.load(f)

        for hospital in data['hospitals']:
            new_hospital = Hospital(hospital['id'], hospital['name'], hospital['city'])
            db.session.add(new_hospital)

        patients = {}
        for patient in data['patients']:
            new_patient = Patient(patient['id'], patient['name'], patient['surname'], patient['dni'], patient['hospital_id'])
            patients[patient['id']] = new_patient
            db.session.add(new_patient)

        for doctor in data['doctors']:
            new_doctor = Doctor(doctor['id'], doctor['name'], doctor['surname'], doctor['speciality'])
            if (new_doctor.id == '014bd297-0a3d-4a17-b207-cff187690045'):
                new_doctor.patients.append(patients['3a268172-6c5c-4d9b-8964-8b9a1e531af5'])
            if (new_doctor.id == 'a0f54d52-5ccb-4e50-adca-5ea0064262fd'):
                new_doctor.patients.append(patients['088d58e2-7691-47b6-a322-eeffcadc9054'])
            if (new_doctor.id == '1497d1be-577a-41ad-b129-45271e113cc0'):
                new_doctor.patients.append(patients['8ec8c43b-f7e1-43e4-b70f-6d5a9799a86a'])
            if (new_doctor.id == '9bb2e300-fa15-4063-a291-13f7199ddb52'):
                new_doctor.patients.append(patients['923ec756-87b7-4743-808b-795a04b6dd21'])
                new_doctor.patients.append(patients['3a268172-6c5c-4d9b-8964-8b9a1e531af5'])
            db.session.add(new_doctor)

        print(patients)
    
        db.session.commit()
        print('#### Finished! ####')
    else:
        print('#### Database already seed ####')

seeder()
