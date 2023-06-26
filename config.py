import os
SECRET_KEY = 'edmaker-com-flask-site-jogoteca'
UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads' # caminho absoluto para a pasta uploads do projeto (onde as imagens serão salvas)
#explicando upload_path: os.path.dirname(os.path.abspath(__file__)) retorna o caminho absoluto do arquivo config.py, que é o arquivo que está sendo executado.

# configurando sql alchemy
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{host}:{port}/{database}'.format(
        SGBD='mysql+mysqlconnector',
        usuario = 'root',
        senha = 'reset666',
        host = 'localhost',
        port = '3306',
        database = 'jogoteca'
    )
    #'mysql://root:reset666@localhost/jogoteca'
    #'SGBD://USUARIO:SENHA@HOST/BANCO_DE_DADOS'