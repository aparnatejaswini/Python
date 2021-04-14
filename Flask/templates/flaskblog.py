# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 23:34:38 2021

@author: Aparna
"""
from flask import Flask,render_template
app = Flask(__name__)

post = [
    {
         'author':'user1',
         'title': 'Blog Post 1',
         'content': 'first post content',
         'date_posted': 'April 14, 2021'
     },
    {
         'author':'user2',
         'title': 'Blog Post 2',
         'content': 'second post content',
         'date_posted': 'April 15, 2021'
     }
    ]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=post)

@app.route("/about")
def about():
    return render_template('about.html',   title ='About')

if __name__ == '__main__':
    app.run(debug=True)