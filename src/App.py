from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQl Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345'
app.config['MYSQL_DB'] = 'flaskcontacts'
mysql = MySQL(app)

# Settings
app.secret_key = 'mysecretkey'

# Decorador de rutas
@app.route('/')
def index():
	cursor = mysql.connection.cursor()
	cursor.execute('SELECT * FROM contacts')
	data= cursor.fetchall()

	# Por defecto flask tiene configurado el nombre la carpeta como templates
	return render_template('index.html', contacts = data)

@app.route('/add', methods=['POST'])
def add_contact():
	if request.method == 'POST':
		fullname = request.form['fullname']
		phone = request.form['phone']
		email = request.form['email']
		
		# Usamos la conexion a mysql
		cursor = mysql.connection.cursor()
		cursor.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)', (fullname, phone, email))
		mysql.connection.commit()
		flash('Contacto Agregado')

		return redirect(url_for('index'))

@app.route('/edit/<id>')
def getContact(id):
	cursor = mysql.connection.cursor()
	cursor.execute('SELECT * FROM contacts WHERE id = %s',(id))
	data = cursor.fetchone()
	return render_template('edit_contact.html', contact = data)

@app.route('/update/<id>', methods=['POST'])
def update_contact(id):

	if request.method == 'POST':
		# Coloco los valores en una tupla
		data = (
			request.form['fullname'],
			request.form['phone'],
			request.form['email'],
			id
			)
		cursor = mysql.connection.cursor()
		cursor.execute("""
				UPDATE contacts
				SET fullname = %s,
				phone = %s,
				email = %s 
				WHERE id = %s
			""", data)
		mysql.connection.commit()
		
		flash('Contacto Actualizado Satisfactoriamente')
		return redirect(url_for('index'))

@app.route('/delete/<string:id>')
def deleteContact(id):
	cursor = mysql.connection.cursor()
	cursor.execute('DELETE FROM contacts WHERE id = {0}'.format(id))
	mysql.connection.commit()
	flash('Contacto {0} eliminado'.format(id))
	return redirect(url_for('index'))

if __name__ == '__main__':
	app.run(port = 3000, debug = True)

