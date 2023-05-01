<img  align="left" width="150" style="float: left;" src="https://www.upm.es/sfs/Rectorado/Gabinete%20del%20Rector/Logos/UPM/CEI/LOGOTIPO%20leyenda%20color%20JPG%20p.png">
<img  align="right" width="60" style="float: right;" src="http://www.dit.upm.es/figures/logos/ditupm-big.gif">


<br/><br/>


# Practica BDRD - SQLAlchemy ORM

## 1. Objetivo

- Desarrollar las 4 operaciones CRUD (Create, Read, Update and Delete), así como otra serie de queries, a través de un ORM
- Practicar con un ORM para realizar queries
- Afianzar las ventajas de usar ORMs en el desarrollo de aplicaciones

## 2. Dependencias

Para realizar la práctica el alumno deberá tener instalado en su ordenador:
- Entorno de ejecución de Python 3 [Python](https://www.python.org/downloads/)
- Base de datos PostgreSQL [PostgreSQL](https://www.postgresql.org/download/)

## 3. Descripción de la práctica

La práctica simula una aplicación de gestión de pacientes basada en el patron MVC (Modelo-Vista-Controlador) utlizando la librería Flask de python. La práctica tambien usa SQLAlchemy como ORM para poder almacenar los datos de la aplicación en PostgreSQL.

La **vista** es una interfaz web basada en HTML y CSS que permite realizar diversas acciones sobre los pacientes como crear, editar, buscar, filtrar, listar o eliminar. La vista esta incluida ya en el codigo descargado.

El **modelo** es la representación de la información de los pacientes. En esta apliación se van a usar tres modelos: doctor, hospital y patient. Un ejemplo de como están definidos los modelos en esta práctica es el siguiente (la definición de todos los modelos se encuentra en models.py):

```
class Patient(db.Model):

    __tablename__ = 'patient'

    id = db.Column(db.String(80), primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=True)
    dni = db.Column(db.String(80), nullable=False)
    hospital_id = db.Column(db.String, db.ForeignKey('hospital.id'))
    doctors = db.relationship("Doctor", secondary=patient_doctor, backref="patients")

    def __init__(self,id,name,surname,dni,hospital_id):
        self.id=id
        self.name=name
        self.surname=surname
        self.dni=dni
        self.hospital_id=hospital_id
```

El **controlador** ejecuta acciones sobre los modelos. El alumno deberá desarrollar varias funciones del controlador para que las acciones que se realicen a través de la página web funcionen correctamente. Para ello, desarrollara las operaciones correspondientes con SQLAlchemy implementando las operaciones CRUD sobre los objetos patiente, hospital y doctor, así como otra serie de queries.

En el siguiente video puede observar cual sería el funcionamiento normal de la aplicación [link](https://youtu.be/8xXaFCRxMXE)

## 4. Descargar e instalar el código del proyecto

Abra un terminal en su ordenador y siga los siguientes pasos.

Descarguese y descomprima el código pinchando más arriba en el botón code y eligiendo opción "Download ZIP".

Navegue a través de un terminal a la carpeta P5_ORM_FLASK.
```
$ cd P5_ORM_FLASK
```

Una vez dentro de la carpeta, se instalan las dependencias. Para ello debe crear un virtual environment de la siguiente manera:

```
[LINUX/MAC] $ python3 -m venv venv
[WINDOWS] > py -m venv env
```

Si no tiene instalado venv, Lo puede instalar de la siguiente manera:

```
[LINUX/MAC] $ python3 -m pip install --user virtualenv
[WINDOWS] > py -m pip install --user virtualenv
```

Una vez creado el virtual environment lo activamos para poder instalar las dependencias:

```
[LINUX/MAC] $ source venv/bin/activate
[WINDOWS] > .\env\Scripts\activate
```

Instalamos las dependencias con pip:

```
$ pip3 install -r flaskr/requirements.txt 
```

Teniendo arrancado PostgreSQL, indicamos a Flask el fichero con el que arrancar el servidor

```
[LINUX/MAC] $ export FLASK_APP=flaskr/run.py
[WINDOWS/cmd] > set FLASK_APP=flaskr/run.py
[WINDOWS/powershell] > $env:FLASK_APP = "flaskr/run.py"
```

Podemos arrancar el servidor con el siguiente comando. Hasta que no realize el primer ejercicio sobre la configuración de la URI, el servidor no arrancara.

```
$ flask run
```


Abra un navegador y vaya a la url "http://localhost:5000" para ver la aplicación de gestión de pacientes.


## 5. Consejos para antes de empezar

**Cada vez que se quiera realizar una prueba del código desarrollado, debemos parar y arrancar de nuevo la practica. Para ello, desde el terminal pulse ctrl+c para parar y arranque de nuevo con flask run**

**Si ha modificado alguna tabla de manera indeseada y se quiere volver a restablecer los valores por defecto, borre la base de datos orm_bddd y vuelva a arrancar el servidor con flask.**


## 6. Tareas a realizar


El alumno deberá editar el siguiente fichero:

- flaskr/run.py. Se le provee un esqueleto con todos los funciones que deberá rellenar. En cada uno de estas funciones se deberá hacer uso del ORM SQL Alchemy para realizar operaciones con la base de datos y devolver un resultado de la operación.

Definir la URI de Conexión a la base de datos con nombre **orm_bbdd** :

```app.config['SQLALCHEMY_DATABASE_URI'] = ### Definir la URI de Conexión.```

En cuanto a las funciones que debe editar en run.py debe hacer lo siguiente:

### show_hospitals()

**Descipcion:**
- Busca en la base de datos todos los hospitales existentes en la coleccion "Hospital"

**Parámetros:**

- Ninguno

**Returns:**

- Un array de objetos de hospitales

### filterHospitalsByCity()

**Descipcion:**
- Busca en la colección "Hospital" filtrando por ciudad
- Para acceder al parametro ciudad que se pasa desde la vista puede usar:
```
city = request.form['city']
```
**Parámetros:**

- Ninguno

**Returns:**

- Un array de objetos de hospitales

### list_hospital_patients(hospital_id)

**Descripción:**
- Busca todos los pacientes correspondientes a un hospital ordenados por el nombre (de la A a la Z)

**Parámetros:**

- hospital_id - Id del hospital

**Returns:**

- Un array de objetos de pacientes

### read_patient(hospital_id, patient_id)

**Descripción:**
- Busca los datos de un paciente

**Parámetros:**

- hospital_id - Id del hospital
- patient_id - Id del paciente a actualizar

**Returns:**

- Un objeto paciente

### create_patient(hospital_id)

**Descripción:**
- Crea un paciente dentro de un hospital

**Parámetros:**


- id - id del Paciente, debe generarse con:
```
id = uuid.uuid4()
```
- name - Nombre del paciente. Puede acceder al parametro "name" al igual que en la función "filterHospitalsByCity" a city
- surname - Apellido del paciente. Puede acceder al parametro "surname" al igual que en la función "filterHospitalsByCity" a city
- dni - DNI del paciente. Puede acceder al parametro "dni" al igual que en la función "filterHospitalsByCity" a city
- hospital_id - Id del hospital

**Returns:**

- El objeto paciente creado

### update_patient(hospital_id, patient_id)

**Descripción:**
- Actualiza los datos del paciente identificado por patient_id

**Parámetros:**

- hospital_id - Id del hospital
- patient_id - Id del paciente
- name - Nombre del paciente. Puede acceder al parametro "name" al igual que en la función "filterHospitalsByCity" a city
- surname - Apellido del paciente. Puede acceder al parametro "surname" al igual que en la función "filterHospitalsByCity" a city
- dni - DNI del paciente. Puede acceder al parametro "dni" al igual que en la función "filterHospitalsByCity" a city

**Returns:**

- El objeto paciente actualizado

### delete_patient(patient_id)

**Descripción:**
- Borra un paciente de la base de datos

**Parámetros:**

- patient_id - Id del paciente

**Returns:**

- El resultado de la operación de borrado

### assignDoctor(hospital_id, patient_id)

**Descripción:**
- Asigna un medico a un paciente en la base de datos.
- Para acceder al id del doctor puede usar:
```
doctor_id = request.form['doctor']
```
**Parámetros:**

- patient_id - Id del paciente
- hospital_id - Id del hospital

**Returns:**

- Devuelve los datos del paciente al que se le ha asignado el medico

### show_patient_doctors(hospital_id, patient_id)

**Descripción:**
- Devuelve los doctores que estan asignados a un paciente.

**Parámetros:**

- patient_id - Id del paciente
- hospital_id - Id del hospital

**Returns:**

- Un array de objetos de doctores 


## 7. Instrucciones para la Entrega y Evaluación.

El alumno deberá subir a Moodle únicamente el fichero *run.py* con las modificaciones realizadas. 

**RÚBRICA**: Cada método que se pide resolver de la practica se puntuara de la siguiente manera:
-  **1 punto por cada uno de las siguientes funciones realizadas:**  list_hospitals, filterHospitalsByCity, list_hospital_patients, read_patient, create_patient, update_patient y delete_patient.
-  **1,5 puntos por cada uno de las siguientes funciones realizadas:**  assignDoctor y showPatientDoctors 
