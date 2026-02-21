from flask import Flask, render_template, request, redirect, url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask_migrate import Migrate
from flask import g
import forms

from models import db
from models import Alumno

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
db.init_app(app)
migrate = Migrate(app, db)
csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html"),404

@app.route("/", methods=["GET", "POST"])
@app.route("/index")
def index():
	create_form = forms.UserForm(request.form)
	alumno = Alumno.query.all()
	return render_template("index.html", form=create_form, alumno=alumno)

@app.route("/Alumnos", methods=['GET', 'POST'])
def alumnos():
	create_form = forms.UserForm(request.form)
	if request.method == 'POST':
		alum = Alumno(nombre=create_form.nombre.data,
					  apellidos=create_form.apellidos.data,
					  telefono=create_form.telefono.data,
					  email=create_form.email.data)
		db.session.add(alum)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template("Alumnos.html", form=create_form)

@app.route("/modificar", methods=['GET', 'POST'])
def modificar():
	create_form = forms.UserForm(request.form)
	if request.method == 'GET':
		id=request.args.get('id')
		alm1 = db.session.query(Alumno).filter(Alumno.id==id).first()
		id=request.args.get('id')
		create_form.id.data=alm1.id
		create_form.nombre.data=alm1.nombre
		create_form.apellidos.data=alm1.apellidos
		create_form.telefono.data=alm1.telefono
		create_form.email.data=alm1.email
		
	if request.method == 'POST':
		id=request.args.get('id')
		alm1 = db.session.query(Alumno).filter(Alumno.id==id).first()
		alm1.id=id
		alm1.nombre=create_form.nombre.data
		alm1.apellidos=create_form.apellidos.data
		alm1.telefono=create_form.telefono.data
		alm1.email=create_form.email.data
		db.session.add(alm1)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template("modificar.html", form=create_form)

@app.route("/eliminar", methods=['GET', 'POST'])
def eliminar():
	create_form = forms.UserForm(request.form)
	if request.method == 'GET':
		id=request.args.get('id')
		alm1 = db.session.query(Alumno).filter(Alumno.id==id).first()
		id=request.args.get('id')
		create_form.id.data=alm1.id
		create_form.nombre.data=alm1.nombre
		create_form.apellidos.data=alm1.apellidos
		create_form.telefono.data=alm1.telefono
		create_form.email.data=alm1.email
		
	if request.method == 'POST':
		id=create_form.id.data
		alm=Alumno.query.get(id)
		db.session.delete(alm)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template("eliminar.html", form=create_form)

@app.route("/detalles", methods=['GET', 'POST'])
def detalles():
	create_form = forms.UserForm(request.form)
	if request.method == 'GET':
		id=request.args.get('id')
		alm1 = db.session.query(Alumno).filter(Alumno.id==id).first()
		id=request.args.get('id')
		nombre=alm1.nombre
		apaterno=alm1.apellidos
		email=alm1.email

	return render_template('detalles.html', nombre=nombre, apaterno=apaterno, email=email)

if __name__ == '__main__':
	csrf.init_app(app)

	with app.app_context():
		db.create_all()

	app.run(debug=True)
