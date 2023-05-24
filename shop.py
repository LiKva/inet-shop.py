from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Izveidojam savienojumu ar datu bāzi
conn = sqlite3.connect('veikals.db')
c = conn.cursor()

# Izveidojam produktu tabulu datu bāzē
c.execute('''CREATE TABLE IF NOT EXISTS produkts
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              nosaukums TEXT,
              cena REAL)''')

# Ceļš uz galveno lapu
@app.route('/')
def index():
    # Atgriežam visas preces no datu bāzes
    c.execute("SELECT * FROM produkts")
    preces = c.fetchall()
    return render_template('index.html', preces=preces)

# Ceļš uz preces pievienošanas lapu
@app.route('/pievienot', methods=['GET', 'POST'])
def pievienot():
    if request.method == 'POST':
        nosaukums = request.form['nosaukums']
        cena = request.form['cena']
        # Ievietojam jaunu produktu datu bāzē
        c.execute("INSERT INTO produkts (nosaukums, cena) VALUES (?, ?)", (nosaukums, cena))
        conn.commit()
        return redirect(url_for('index'))
    return render_template('pievienot.html')

if __name__ == '__main__':
    app.run(debug=True)
