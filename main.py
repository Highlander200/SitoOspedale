from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/analisi/')
def analisi():
    return render_template("analisi.html")

@app.route('/visite/')
def visite():
    return render_template("visite.html")

@app.route('/prenotaVisite/')
def prenotaVisite():
    return render_template("prenotaVisite.html")

@app.route('/prenotaAnalisi/')
def prenotaAnalisi():
    return render_template("prenotaAnalisi.html")

@app.route('/login/')
def login():
    return render_template("login.html")
  
@app.route('/register/')
def register():
    return render_template("register.html")

@app.route('/medici/')
def medici():
    return render_template("medici.html")


app.run(host='0.0.0.0', port=81)
