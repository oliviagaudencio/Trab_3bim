from flask import Blueprint, render_template, request, redirect, flash
from models import Clube, Aluno
from database import db

bp_clube = Blueprint('clube', __name__, template_folder="templates")

@bp_clube.route("/")
def index():
    c = Clube.query.all()
    return render_template("clubes.html", clubes=c)


@bp_clube.route("/add")
def add():
    a = Aluno.query.all()
    return render_template("clubes_add.html", alunos=a)


@bp_clube.route("/save", methods=['POST'])
def save():
    nome = request.form.get("nome")
    tipo = request.form.get("tipo")
    id_aluno = request.form.get("id_aluno")

    if nome and tipo and id_aluno:
        db_clube = Clube(nome, tipo, id_aluno)
        db.session.add(db_clube)
        db.session.commit()
        flash("Clube salvo!")
        return redirect("/clubes")
    else:
        flash("Preencha tudo!")
        return redirect("/clubes/add")


@bp_clube.route("/remove/<int:id>")
def remove(id):
    c = Clube.query.get(id)
    try:
        db.session.delete(c)
        db.session.commit()
        flash("Clube removido!")
    except:
        flash("Clube inválido!")
    return redirect("/clubes")


@bp_clube.route("/edit/<int:id>")
def edit(id):
    c = Clube.query.get(id)
    a = Aluno.query.all()
    return render_template("clubes_editar.html", clubes=c, alunos=a)


@bp_clube.route("/edit-save", methods=['POST'])
def edit_save():
    nome = request.form.get("nome")
    tipo = request.form.get("tipo")
    id_aluno = request.form.get("id_aluno")
    id_clube = request.form.get("id_clube")
    
    if nome and tipo and id_clube and id_aluno:
        c = Clube.query.get(id_clube)
        c.nome = nome
        c.tipo = tipo
        c.id_aluno = id_aluno
        db.session.commit()
        flash("Clube editado!")
    else:
        flash("Preencha tudo!")
    return redirect("/clubes")