import mysql.connector
from mysql.connector import errorcode

print("Conectando...")
try:
    con = mysql.connector.connect(
        user='root', 
        password='reset666', 
        host='127.0.0.1',
        port=3306
        )
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Usuário ou senha inválidos!")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Banco de dados não existe!")
    else:
        print(err)

cursor = con.cursor()
cursor.execute("DROP DATABASE IF EXISTS `jogoteca`;")
cursor.execute("CREATE DATABASE IF NOT EXISTS `jogoteca`;")
cursor.execute("USE `jogoteca`;")

# criando tabelas
TABLES = {}
TABLES['Jogos'] = ("""
    CREATE TABLE `jogos` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `nome` varchar(50) NOT NULL,
        `categoria` varchar(40) NOT NULL,
        `console` varchar(20) NOT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
""")
TABLES['usuarios'] = ("""
    CREATE TABLE `usuarios` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `nome` varchar(50) NOT NULL,
        `usuario` varchar(40) NOT NULL,
        `senha` varchar(20) NOT NULL,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
""")
for table_name in TABLES:
    tabela_sql = TABLES[table_name]
    try:
        print(f"Criando tabela {table_name}...")
        cursor.execute(tabela_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
            print(f"Tabela {table_name} já existe.")
        else:
            print(err.msg)
    else:
        print(f"Tabela {table_name} criada com sucesso.")

con.commit()

# inserindo usuarios
usuario_sql = "INSERT INTO `usuarios` (`nome`, `usuario`, `senha`) VALUES (%s, %s, %s);"
usuarios = [
    ('Douglas', 'edmaker', 'reset666'),
    ('Vanessa', 'lost12', 'morango62'),
    ('Euclides', 'cride', 'montandor123')
]

cursor.executemany(usuario_sql, usuarios)

cursor.execute("SELECT * FROM usuarios")
print(" ------------- Usuários: ------------- ")
for user in cursor.fetchall():
    print(user[1])

# inserindo jogos
jogo_sql = "INSERT INTO `jogos` (`nome`, `categoria`, `console`) VALUES (%s, %s, %s);"
jogos = [
    ('God of War', 'Ação', 'PS4'),
    ('Super Mario', 'Ação', 'SNES'),
    ('Mortal Kombat', 'Luta', 'SNES'),
    ('FIFA 18', 'Esporte', 'PS4'),
    ('Resident Evil 7', 'Terror', 'PS4'),
    ('Need for Speed', 'Corrida', 'PS4'),
    ('Super Mario Kart', 'Corrida', 'SNES')

]

cursor.executemany(jogo_sql, jogos)

cursor.execute("SELECT * FROM `jogoteca`.`jogos`;")
print(" ------------- Jogos: ------------- ")
for jogo in cursor.fetchall():
    print(jogo[1])

# commitando alterações
con.commit()
cursor.close()
con.close()

print("Pronto!")




                   