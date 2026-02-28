from . import maestros
from flask import render_template, request, redirect, url_for, flash
from models import db
from models import Alumnos, Maestros
from maestros.forms import UserForm

@maestros.route("/maestros", methods=['GET', 'POST'])
@maestros.route("/index")
def index():
    create_form = UserForm(request.form)
    lista_maestros = Maestros.query.all()

    return render_template(
        "maestros/listadoMaes.html",
        form=create_form,
        maestros=lista_maestros
    )