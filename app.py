import os
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from dotenv import load_dotenv
from werkzeug.utils import secure_filename  

load_dotenv()

app = Flask(__name__)

app.config['MYSQL_HOST'] = os.getenv('MYSQL_HOST')
app.config['MYSQL_USER'] = os.getenv('MYSQL_USER')
app.config['MYSQL_PASSWORD'] = os.getenv('MYSQL_PASSWORD')
app.config['MYSQL_DB'] = os.getenv('MYSQL_DB')
app.config['UPLOAD_FOLDER'] = os.getenv('UPLOAD_FOLDER')

mysql = MySQL(app)

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    for i in range(1, 6):
        file = request.files.get(f'file{i}')
        if file and file.filename != '':
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO files (filename) VALUES (%s)', (filename,))
            mysql.connection.commit()
            cursor.close()

    return redirect(url_for('index') + '?success=1')

if __name__ == '__main__':
    app.run(debug=True)
