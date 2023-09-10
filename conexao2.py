import sqlite3
conexao= sqlite3.connect('bdd2')
cursor = conexao.cursor()

#cursor.execute('CREATE TABLE alunos (id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(1, "LUISA", 37, "engenharia")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(2, "PEDRO", 35, "engenharia")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(3, "LAURA", 35, "QUIMICA")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(4, "JORGE", 35, "engenharia")')
#cursor.execute('INSERT INTO alunos(id,nome,idade,curso) VALUES(5, "DIEGO", 35, "cssociales")')

#dados = cursor.execute('select * from alunos')
#for aluno in dados:
#    print (aluno)

#dados = cursor.execute('select nome, idade from alunos WHERE idade>20')
#for aluno in dados:
#   print (aluno)

#dados = cursor.execute('select * FROM alunos WHERE curso="engenharia" ORDER BY nome')
#for aluno in dados:
#   print (aluno)

#dados = cursor.execute('select * FROM alunos WHERE curso="engenharia" ORDER BY nome')
#for aluno in dados:
#   print (aluno)

#essa consulta nao sabia fazer,
#dados = cursor.execute('SELECT COUNT(*) FROM alunos')
#resultado = dados.fetchone()[0]  # Obter o valor da contagem
#print("Número total de alunos:", resultado)

cursor.execute('UPDATE alunos SET idade = 25 WHERE nome = "Luisa"')
dados = cursor.execute('select * from alunos')
for aluno in dados:
    print (aluno)

conexao.commit()
conexao.close 