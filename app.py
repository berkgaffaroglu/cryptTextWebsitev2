from flask import Flask,render_template,url_for,flash
from forms import decryptForm,encryptForm
from cryption import encryptMessage,generateKey,decryptMessage
app = Flask(__name__)
app.config['SECRET_KEY'] = '7908e7a467af3317a4e7f2b4324fdc03'

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('index.html',title='Start') # Choose Encrypt or Decrypt.

@app.route('/encrypt', methods=['GET', 'POST'])
def encrypt():
    form = encryptForm()
    if form.validate_on_submit():
        key = generateKey()
        encryptedMessage = encryptMessage(form.normalText.data,key)

        flash(f"{encryptedMessage}\n\n",'content')
        flash(f"{key}", 'key')
    return render_template('encrypt.html', form=form, title='Encrypt')
# Encrypt the given text.

@app.route('/decrypt', methods=['GET', 'POST'])
def decrypt():
    form = decryptForm()
    if form.validate_on_submit():
       try:
          formContent = form.normalText.raw_data[0].strip().encode()
          formKey = form.key.raw_data[0].strip().encode()
          decryptedMessage = decryptMessage(formContent,formKey)
          flash(f"{decryptedMessage.decode()}",'encryptedMessage')
       except Exception as e:
           print('olmadı')
    return render_template('decrypt.html', form=form, title='Decrypt')
# Decrypt the given text.

if __name__ == '__main__':
    app.run(debug=True)