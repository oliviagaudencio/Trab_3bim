from flask import Blueprint, render_template, request, redirect, flash
from models import Aluno
from database import db

bp_aluno = Blueprint('aluno', __name__, template_folder="templates")

@bp_aluno.route("/")
def index():
    a = Aluno.query.all()
    return render_template("alunos.html", alunos=a)


@bp_aluno.route("/add")
def add():
    return render_template("alunos_add.html")


@bp_aluno.route("/save", methods=['POST'])
def save():
    nome = request.form.get("nome")
    matricula = request.form.get("matricula")

    if nome and matricula:
        db_aluno = Aluno(nome, matricula)
        db.session.add(db_aluno)
        db.session.commit()
        flash("Aluno salvo!")
        return redirect("/alunos")
    else:
        flash("Preencha tudo!")
        return redirect("/alunos/add")


@bp_aluno.route("/remove/<int:id>")
def remove(id):
    a = Aluno.query.get(id)
    try:
        db.session.delete(a)
        db.session.commit()
        flash("Aluno removido!")
    except:
        flash("Aluno inválido!")
    return redirect("/alunos")


@bp_aluno.route("/edit/<int:id>")
def edit(id):
    a = Aluno.query.get(id)
    return render_template("alunos_editar.html", alunos=a)


@bp_aluno.route("/edit-save", methods=['POST'])
def edit_save():
    nome = request.form.get("nome")
    matricula = request.form.get("matricula")
    id_aluno = request.form.get("id_aluno")
    
    if nome and matricula and id_aluno:
        a = Aluno.query.get(id_aluno)
        a.nome = nome
        a.matricula = matricula
        db.session.commit()
        flash("Aluno editado!")
    else:
        flash("Preencha tudo!")
    return redirect("/alunos")