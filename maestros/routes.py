from . import maestros
<<<<<<< HEAD
from flask import render_template,request,redirect,url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask import g
import forms
from maestros.routes import maestros, maestros
from models import db
from models import Maestros

@maestros.route("/maestros", methods=['GET', 'POST'])
def index():
    create_form = forms.MaestrosForm(request.form)
    maestros_list = Maestros.query.all()
    return render_template("maestros/listadoMaes.html", form=create_form, maestros=maestros_list)

@maestros.route("/Maestro", methods=['GET', 'POST'])
def listadoMaestro():
    create_form = forms.MaestrosForm(request.form)
    
    if create_form.validate_on_submit():
        maes = Maestros(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            especialidad=create_form.especialidad.data,
            email=create_form.email.data
        )
        try:
            db.session.add(maes)
            db.session.commit()
            return redirect(url_for('maestros.index'))
        except Exception as e:
            db.session.rollback()
            flash("Error al guardar en la base de datos")
            
    return render_template("maestros/Maestro.html", form=create_form)

@maestros.route("/detallesMaestro", methods=['GET', 'POST'])
def detallesMaestro():
    create_form = forms.MaestrosForm(request.form)
    matricula = request.args.get('matricula')
    maes1 = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
    
    if not maes1:
        return "Maestro no encontrado", 404
        
    return render_template("maestros/detallesMaestro.html", 
                           form=create_form, 
                           matricula=matricula, 
                           nombre=maes1.nombre, 
                           apellidos=maes1.apellidos, 
                           especialidad=maes1.especialidad, 
                           email=maes1.email)

@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"

@maestros.route("/modificarMaestro", methods=['GET', 'POST'])
def modificarMaestro():
    create_form = forms.MaestrosForm(request.form)
    
    if request.method == 'GET':
        matricula = request.args.get('matricula') 
        maes1 = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
        
        if maes1:
            create_form.matricula.data = maes1.matricula
            create_form.nombre.data = maes1.nombre
            create_form.apellidos.data = maes1.apellidos
            create_form.email.data = maes1.email
            create_form.especialidad.data = maes1.especialidad
        else:
            return "Maestro no encontrado", 404
            
    if create_form.validate_on_submit():
        matricula = create_form.matricula.data
        maes1 = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
        
        if maes1:
            maes1.nombre = create_form.nombre.data
            maes1.apellidos = create_form.apellidos.data
            maes1.email = create_form.email.data
            maes1.especialidad = create_form.especialidad.data
            
            db.session.add(maes1)
            db.session.commit()
            return redirect(url_for('maestros.index'))
        else:
            return "Error al intentar actualizar: Maestro no existe", 404

    return render_template("maestros/modificarMaestro.html", form=create_form)

@maestros.route("/eliminarMaestro", methods=['GET', 'POST'])
def eliminarMaestro():
    create_form = forms.MaestrosForm(request.form)
    if request.method == 'GET':
        matricula = request.args.get('matricula')
        maes1 = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
        if maes1:
            create_form.matricula.data = maes1.matricula
            create_form.nombre.data = maes1.nombre
            create_form.apellidos.data = maes1.apellidos
            create_form.especialidad.data = maes1.especialidad
            create_form.email.data = maes1.email
        else:
            return "Maestro no encontrado", 404
            
    if create_form.validate_on_submit():
        matricula = create_form.matricula.data
        maes1 = db.session.query(Maestros).filter(Maestros.matricula == matricula).first()
        if maes1:
            if len(maes1.cursos) > 0:
                flash("No puedes eliminar el maestro porque aún hay cursos asignados. Primero debes darlos de baja.", "warning")
                return redirect(url_for('maestros.index'))
            db.session.delete(maes1)
            db.session.commit()
        return redirect(url_for('maestros.index'))
        
    return render_template("maestros/eliminarMaestro.html", form=create_form)
=======
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
>>>>>>> 5d0e5cb02d7b8789d994332094f5671803e63677
