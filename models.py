from database import db

class Aluno(db.Model):
    __tablename__ = 'alunos'
    id_aluno = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    matricula = db.Column(db.String(50))
   
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula
    
    def __repr__(self):
        return "<Aluno {self.nome}>".f
    

class Clube(db.Model):
    __tablename__ = 'clube'
    id_clube = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    tipo = db.Column(db.String(50))
    id_aluno = db.Column(db.Integer, db.ForeignKey('alunos.id')

    aluno = db.relationship('Aluno', foreign_keys=alunos_id)

    def __init__(self, nome, tipo, alunos_id):
        self.nome = nome
        self.tipo = tipo
        self.alunos_id = alunos_id
    
    def __repr__(self):
        return "<Cadastro: {self.nome} - {self.tipo} - {self.alunos_id}> ".f