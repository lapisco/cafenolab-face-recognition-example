# CaféNoLab II - Face Recognition Example

## Requisitos:
  * Ambiente Virtual (sugestões: virtualenvwrapper, virtualenv ou venv)
  * Python 3 (sugestões: 3.8, 3.10)
  * OS: Ubuntu, Windows, MAC (sugestão: Ubuntu)
  * CMake (caso não esteja instalado)

## Configuração do ambiente

#### Criar um ambiente virtual com [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html) e ativá-lo:

```
mkvirtualenv cafe_no_lab -p python3.8

```

#### Instalar os requerimentos

``` 

pip install -r requirements.txt 

```

#### Criar o banco de dados local

```
sudo -u postgres createuser <username>
sudo -u postgres createdb <dbname>
sudo -u postgres psql

alter user <username> with encrypted password '<password>';
grant all privileges on database <dbname> to <username> ;

\q

```

## Para Rodar o código:
  * Abrir terminal
  * Ativar a env: `workon cafe_no_lab`
  * Rodar: `python main.py`

## Links úteis:
  * [SQL](https://www.tutorialspoint.com/sql/sql-expressions.htm)
  * [Dlib](http://dlib.net/)
  * [OpenCV](https://opencv.org/)
  * [PostgreSQL](https://www.digitalocean.com/community/tutorials/how-to-install-postgresql-on-ubuntu-22-04-quickstart)
  * [DBeaver](https://dbeaver.io/download/)
