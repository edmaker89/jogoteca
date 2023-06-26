from jogoteca import app
from flask import render_template, request, redirect, session, flash, url_for
from models import Usuarios
from helpers import FormularioUsuario
from flask_bcrypt import check_password_hash

@app.route('/login')
def login():
    proxima = request.args.get('proxima')
    form = FormularioUsuario()
    if proxima == None:
        proxima = url_for('index')
    return render_template('login.html', titulo='Login', proxima=proxima, form=form)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    form = FormularioUsuario(request.form)
    usuario = Usuarios.query.filter_by(usuario=form.usuario.data).first()
    senha = check_password_hash(usuario.senha, form.senha.data) #check_password_hash(hash do banco, senha do formulario)
    if usuario and senha:
        session['usuario_logado'] = usuario.usuario
        flash(usuario.nome + ' logou com sucesso!')
        proxima_pagina = request.form['proxima']
        return redirect(proxima_pagina)
    else:
        flash('Não logado, tente novamente!')
        return redirect(url_for('login'))
    
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado!')
    return redirect(url_for('login'))