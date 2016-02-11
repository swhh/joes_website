from db import Message, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from flask import Flask, render_template, request, url_for
import constants
import os

app = Flask(__name__)
uri = os.environ.get('DATABASE_URL', 'postgres://ikzsogicqzfoqk:zHHnNISnb4YH-2S8YiH5F9ES1U@ec2-107-20-136-89.compute-1.amazonaws.com:5432/d5c6j70ceof3k4')
engine = create_engine(uri)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    error, success = False, False
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        date = datetime.now().__str__()
        try:
            new_message = Message(name=name, email=email, message=message, date=date)
            session.add(new_message)
            session.commit()
            success = True
        except:
            error = True
    return render_template('contact.html', error=error, success=success)


@app.route('/music')
def music():
    return render_template('music.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/gallery/<int:img_id>')
def gallery(img_id):
    img_url = constants.URLs[img_id % len(constants.URLs)]
    return render_template('gallery.html', img_id=img_id, img_url=img_url)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)


