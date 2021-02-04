from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
   
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/novedades')
def novedades():
    return render_template('novedades.html')




