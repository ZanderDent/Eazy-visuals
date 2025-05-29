from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for flash messages

@app.route('/')
def pricing():
    return render_template('pricing.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/samples')
def samples():
    return render_template('samples.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
