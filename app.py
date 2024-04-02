from flask import Flask, request, render_template
import os
import img_paradox as ip

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = 'static/results'



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home.html')


@app.route('/encrypt',methods=['POST'])
def enc():
    a = float(request.form['a'])
    b = float(request.form['b'])
    file=request.files['file']
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    output_path = os.path.join(app.config['RESULT_FOLDER'], file.filename)
    file.save(file_path)
    ip.encrypt_image(file_path, a, b).save(output_path)
    return file.filename


@app.route('/decrypt',methods=['POST'])
def dec():
    a = float(request.form['a'])
    b = float(request.form['b'])
    file=request.files['file']
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    output_path = os.path.join(app.config['RESULT_FOLDER'], file.filename)
    file.save(file_path)
    ip.decrypt_image(file_path, a, b).save(output_path)
    return file.filename
if __name__ == '__main__':
    app.run(debug=True)
