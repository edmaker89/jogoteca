from jogoteca import db

class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    console = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'Jogo: {self.nome}, Categoria: {self.categoria}, Console: {self.console}'
    
class Usuarios(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    usuario = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f'Nome: {self.nome}, Usuário: {self.usuario}'
