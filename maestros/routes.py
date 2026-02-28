from . import maestros
from flask import render_template, request, redirect, url_for, flash
from models import db
from models import  Maestros
from forms import MaestroForm
import forms

@maestros.route("/maestros", methods=['GET', 'POST'])
def maestro():
    create_form = MaestroForm(request.form)
    lista_maestros = Maestros.query.all()

    return render_template("maestros/listadoMaes.html",form=create_form, maestros=lista_maestros)

@maestros.route("/Maestro",methods=['GET','POST'])
def Maestro():
    create_form = forms.MaestroForm(request.form)
    if request.method == 'POST':
        maes = Maestros(
            nombre = create_form.nombre.data,
            apellidos = create_form.apellidos.data,
            especialidad = create_form.especialidad.data,
            email = create_form.email.data
        )
        db.session.add(maes)
        db.session.commit()
        return redirect(url_for('maestros.index'))
    return render_template("maestros/Maestro.html",forms = create_form)

@maestros.route("/detalles", methods=['GET', 'POST'])
def detalles():
	create_form = forms.MaestroForm(request.form)
	if request.method=='GET':
		matricula=request.args.get('matricula')
		# select * from alumnos where id == id
		maes1=db.session.query(Maestros).filter(Maestros.matricula==matricula).first()
		matricula=request.args.get('matricula')
		nombre=maes1.nombre
		apellidos=maes1.apellidos
		especialidad = maes1.especialidad
		email=maes1.email
	return render_template ('detalles.html', matricula=matricula, nombre=nombre, especialidad=especialidad, apellidos=apellidos, email=email)

@maestros.route("/modificar", methods=['GET', 'POST'])
def modificar():
    create_form = forms.MaestroForm(request.form)
    matricula = request.args.get('matricula')

    maes1 = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()

    if request.method == 'GET':
        create_form.matricula.data = maes1.matricula
        create_form.nombre.data = maes1.nombre
        create_form.apellidos.data = maes1.apellidos
        create_form.especialidad.data = maes1.especialidad
        create_form.email.data = maes1.email

    if request.method == 'POST':
        maes1.nombre = create_form.nombre.data
        maes1.apellidos = create_form.apellidos.data
        maes1.especialidad = create_form.especialidad.data
        maes1.email = create_form.email.data

        db.session.commit()
        return redirect(url_for('maestros.maestro'))

    return render_template("maestros/modificar.html", form=create_form)

@maestros.route("/eliminar", methods=['GET', 'POST'])
def eliminar():
    create_form = forms.MaestroForm(request.form)

    matricula = request.args.get('matricula')

    maes1 = db.session.query(Maestros).filter(
        Maestros.matricula == matricula
    ).first()

    if not maes1:
        return redirect(url_for('maestros.maestro'))

    if request.method == 'GET':
        create_form.matricula.data = maes1.matricula
        create_form.nombre.data = maes1.nombre
        create_form.apellidos.data = maes1.apellidos
        create_form.especialidad.data = maes1.especialidad
        create_form.email.data = maes1.email

    if request.method == 'POST':
        db.session.delete(maes1)
        db.session.commit()
        return redirect(url_for('maestros.maestro'))

    return render_template("maestros/eliminar.html", form=create_form)