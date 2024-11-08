from flask import Flask, render_template, request, flash, redirect, Blueprint
app = Flask(__name__)
app.config['SECRET_KEY'] = 'senha'
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/trab"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
from flask_migrate import Migrate
from models import Aluno, Clube
db.init_app(app)
migrate = Migrate(app, db)
#from modulos.usuarios.usuarios import bp_usuario
#app.register_blueprint(bp_usuario, url_prefix='/usuarios')
#from modulos.pizzas.pizzas import bp_pizza
#app.register_blueprint(bp_pizza, url_prefix='/pizzas')