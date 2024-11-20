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
        return f"<Aluno {self.nome}>"
    

class Clube(db.Model):
    __tablename__ = 'clube'
    id_clube = db.Column(db.Integer, primary_key = True)
    nome = db.Column(db.String(100))
    tipo = db.Column(db.String(50))
    id_aluno = db.Column(db.Integer, db.ForeignKey('alunos.id_aluno'))

    aluno = db.relationship('Aluno', foreign_keys=id_aluno)

    def __init__(self, nome, tipo, id_aluno):
        self.nome = nome
        self.tipo = tipo
        self.id_aluno = id_aluno
    
    def __repr__(self):
        return f"<Cadastro: {self.nome} - {self.tipo} - {self.id_aluno}> "