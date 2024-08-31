from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)


conn = sqlite3.connect('items.db', check_same_thread=False)
cursor = conn.cursor()

jls_extract_var = '''
    CREATE TABLE IF NOT EXISTS items (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
'''
cursor.execute(jls_extract_var)
conn.commit()


@app.route('/')
def index():
    cursor.execute('SELECT * FROM items')
    items = cursor.fetchall()
    return render_template('index.html', items=items)


@app.route('/add', methods=['POST'])
def add_item():
    name = request.form['name']
    cursor.execute('INSERT INTO items (name) VALUES (?)', (name,))
    conn.commit()
    return redirect(url_for('index'))


@app.route('/delete/<int:item_id>')
def delete_item(item_id):
    cursor.execute('DELETE FROM items WHERE id = ?', (item_id,))
    conn.commit()
    return redirect(url_for('index'))


if __name__=="__main__":
    app.run(host="0.0.0.0",port=8000)