#Importacion de Librerias
from ensurepip import bootstrap
from flask import Flask
from flask import render_template, request
from flaskext.mysql import MySQL
from flask_bootstrap5 import Bootstrap
import cryptography
#from flask_bootstrap5 import Bootstrap

app = Flask(__name__)
#bootstrap = Bootstrap(app)

# Configuracion de Gestor de Base de Datos
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'LuisA5841@&'
app.config['MYSQL_DATABASE_DB'] = 'Oddo'
mysql.init_app(app)

@app.route('/')
def index():
    sql = "SELECT * FROM getAllCards"
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute(sql)
    best = cursor.fetchall()
    conn.commit()
    return render_template("views/index.html", response = True)

@app.route('/login', methods=['POST'])
def login():
    myUser = request.form['user']
    myPass = request.form['pass']
    if(myUser == "AngelDev" and myPass == "Code"):
        return render_template("views/inicio.html");
    
    return render_template("views/index.html", response = False);

if __name__ == '__main__':
    app.run(debug=True)