import os
from jogoteca import app
from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, PasswordField

class FormularioJogo(FlaskForm):
    nome = StringField('Nome do Jogo', [validators.DataRequired(), validators.Length(min=3, max=50)])
    categoria = StringField('Categoria', [validators.DataRequired(), validators.Length(min=3, max=40)])
    console = StringField('Console', [validators.DataRequired(), validators.Length(min=3, max=20)])
    salvar = SubmitField('Salvar',)

class FormularioUsuario(FlaskForm):
    usuario = StringField('Usuário', [validators.DataRequired(), validators.Length(min=3, max=8)])
    senha = PasswordField('Senha', [validators.DataRequired(), validators.Length(min=3, max=100)])
    login = SubmitField('Login')

def recupera_imagem(id):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa{id}' in nome_arquivo:
            return nome_arquivo
    return 'capapadrao.jpg'

def deleta_arquivo(id):
    arquivo = recupera_imagem(id)
    if arquivo != 'capapadrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))
    
