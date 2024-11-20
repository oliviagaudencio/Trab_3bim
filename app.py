from flask import Flask, render_template, request, flash, redirect, Blueprint
app = Flask(__name__)
app.config['SECRET_KEY'] = 'senha'
conexao = "mysql+pymysql://alvaros@localhost:1406@127.0.0.1/trab"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
from flask_migrate import Migrate
from models import Aluno, Clube
db.init_app(app)
migrate = Migrate(app, db)

from modulos.alunos.alunos import bp_aluno
app.register_blueprint(bp_aluno, url_prefix='/alunos')
from modulos.clubes.clubes import bp_clube
app.register_blueprint(bp_clube, url_prefix='/clubes')

@app.route("/")
def index():
    return render_template("index.html")