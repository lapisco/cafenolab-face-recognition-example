import psycopg2

def insert(pessoa, nickname, cpf):
    '''
    Funcao para inserir dados individuais no banco
    '''
    connection = psycopg2.connect(host = 'localhost', 
                                dbname = 'cafe_db', 
                                user = 'cafe_user', 
                                password = 'cafeSenha',
                                port='5432')    
    
    cursor = connection.cursor()
    
    command = """CREATE TABLE IF NOT EXISTS
    registro_pessoas(id SERIAL PRIMARY KEY, name TEXT, nickname TEXT, cpf TEXT)
    """
    cursor.execute(command)

    command1= f"""INSERT INTO registro_pessoas(name, nickname, cpf) 
    VALUES('{str(pessoa)}', '{str(nickname)}', '{str(cpf)}');"""
    cursor.execute(command1)

    connection.commit()

    connection.close()

def get_id(cpf):
    '''
    Funcao para pegar o id correto relacionando os bancos
    '''
    connection = psycopg2.connect(host = 'localhost', 
                                dbname = 'cafe_db', 
                                user = 'cafe_user', 
                                password = 'cafeSenha',
                                port='5432')  
    
    get_id = f"""SELECT * FROM registro_pessoas"""

    cursor = connection.cursor()
    
    cursor.execute(get_id)
    dados = cursor.fetchall()
    connection.close()
    
    print(dados)

insert('Lucas Oliveira', 'Lucas_Oliveira', '155.365.152-66')
get_id('155.365.152-66')