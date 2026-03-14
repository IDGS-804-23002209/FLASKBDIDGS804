from flask import Flask, render_template, request,redirect,url_for
from flask import flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from flask_migrate import Migrate
from flask import g
import forms
from models import db
from models import Curso, Alumno
from maestros.routes import maestros
from cursos.routes import cursos
from inscripciones.routes import inscripciones

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(maestros)
app.register_blueprint(cursos)
app.register_blueprint(inscripciones)
db.init_app(app)
migrate = Migrate(app,db)
app.secret_key='clave_secreta'
csrf = CSRFProtect()

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/alumnosA", methods=['GET', 'POST'])
def alum(): # <-- Este es el nombre que usaremos
    create_form = forms.UserForm(request.form)
    alumno = Alumno.query.all()
    return render_template("indexA.html", form=create_form, alumno=alumno)

@app.route("/Alumnos", methods=['GET', 'POST'])
def Alumnos():
    create_form = forms.UserForm(request.form)
    alumnos_list = Alumno.query.all() 
    
    if create_form.validate_on_submit():
        alum = Alumno(nombre=create_form.nombre.data,
                      apellidos=create_form.apellidos.data,
                      email=create_form.email.data,
                      telefono=create_form.telefono.data)
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('Alumnos')) 
    
    return render_template("Alumnos.html", form=create_form, alumno=alumnos_list)

@app.route("/detalles",methods=['GET','POST'])
def detalles():
	create_form = forms.UserForm(request.form)
	if request.method == 'GET':
		id=request.args.get('id')
		alum1 = db.session.query(Alumno).filter(Alumno.id==id).first()
		nombre = alum1.nombre
		apellidos = alum1.apellidos
		email = alum1.email
		telefono = alum1.telefono
	return render_template("detalles.html",form=create_form,id=id,nombre=nombre,apellidos=apellidos,email=email,telefono=telefono)

@app.route("/modificar",methods=['GET','POST'])
def modificar():
	create_form = forms.UserForm(request.form)
	if request.method == 'GET':
		id=request.args.get('id')
		alum1 = db.session.query(Alumno).filter(Alumno.id==id).first()
		create_form.id.data = request.args.get('id')
		create_form.nombre.data = alum1.nombre
		create_form.apellidos.data = alum1.apellidos
		create_form.email.data = alum1.email
		create_form.telefono.data = alum1.telefono
	if create_form.validate_on_submit():
		id=request.args.get('id')
		alum1 = db.session.query(Alumno).filter(Alumno.id==id).first()
		alum1.id = id
		alum1.nombre = create_form.nombre.data
		alum1.apellidos = create_form.apellidos.data
		alum1.email = create_form.email.data
		alum1.telefono = create_form.telefono.data
		db.session.add(alum1)
		db.session.commit()
		return redirect(url_for('alum'))
	return render_template("modificar.html",form=create_form)

@app.route("/eliminar", methods=['GET', 'POST'])
def eliminar():
    create_form = forms.UserForm(request.form)
    id = request.args.get('id')
    alum1 = Alumno.query.get_or_404(id)
    
    if request.method == 'GET':
        create_form.id.data = alum1.id
        create_form.nombre.data = alum1.nombre
        create_form.apellidos.data = alum1.apellidos
        create_form.email.data = alum1.email
        create_form.telefono.data = alum1.telefono

    if create_form.validate_on_submit():
        if len(alum1.cursos) > 0:
            flash(f"No se puede eliminar a {alum1.nombre}. Tiene {len(alum1.cursos)} curso(s) inscrito(s).", "warning")
            return redirect(url_for('alum'))
        
        db.session.delete(alum1)
        db.session.commit()
        flash("Alumno eliminado con éxito", "success")
        return redirect(url_for('alum'))

    return render_template("eliminar.html", form=create_form)

@app.route("/explorar-cursos")
def lista_cursos_general():
    cursos_db = Curso.query.all()
    return render_template("vista_cursos.html", cursos=cursos_db)

@app.route("/curso-detalle/<int:id>")
def ver_alumnos_por_curso(id):
    curso = Curso.query.get_or_404(id)
    return render_template("detalle_curso_alumnos.html", curso=curso)

@app.route("/alumno-cursos/<int:id>")
def ver_cursos_por_alumno(id):
    alumno = Alumno.query.get_or_404(id)
    return render_template("detalle_alumno_cursos.html", alumno=alumno)

@app.route("/consulta-cursos", methods=['GET', 'POST'])
def consulta_cursos():
    todos_los_cursos = Curso.query.all()
    curso_seleccionado = None

    if request.method == 'POST':
        curso_id = request.form.get('curso_id')
        if curso_id:
            curso_seleccionado = Curso.query.get(curso_id)

    return render_template("consulta_cursos.html", 
                           todos_los_cursos=todos_los_cursos, 
                           curso_seleccionado=curso_seleccionado)

@app.route("/consulta-alumnos", methods=['GET', 'POST'])
def consulta_alumnos():
    todos_los_alumnos = Alumno.query.all()
    alumno_seleccionado = None

    if request.method == 'POST':
        alumno_id = request.form.get('alumno_id')
        if alumno_id:
            alumno_seleccionado = Alumno.query.get(alumno_id)

    return render_template("consulta_alumnos.html", 
                           todos_los_alumnos=todos_los_alumnos, 
                           alumno_seleccionado=alumno_seleccionado)

if __name__ == '__main__':
	csrf.init_app(app)
	
	with app.app_context():
		db.create_all()
	app.run(debug=True)
