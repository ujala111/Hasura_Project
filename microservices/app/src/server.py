#First week task
from flask import Flask  #import flask module
from flask import render_template #import this module to render html templates
from flask import make_response
from flask import request
from flask import abort
import requests, sys
app = Flask("__name__") #object that is instance of the flask framework.

@app.route('/') #to give a url
def index(): #function to return a string
    return "Hello World - Ujjwal" #return to print Hello World.

	
@app.route('/authors', methods=['GET'])
def authors():
    data = requests.get('https://jsonplaceholder.typicode.com/users').json()
    posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()
    users = {d['id']:{'name':d['name'],'count':0} for d in data}
    for post in posts:
        users[post['userId']]['count']+=1
    return render_template('authors.html',users=users)
	
@app.route('/inputcookie')
def inputCookie():
    return render_template('inputcookie.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user_name = request.form['name']
        user_age = request.form['age']
        
    resp = make_response(render_template('readcookie.html'))
    resp.set_cookie('Name', user_name)
    resp.set_cookie('Age', user_age)
    return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('Name')
    age = request.cookies.get('Age')
    return '<h1>Welcome '+name+'. Your age is '+age+'.</h1>'
	
@app.route('/robots.txt')
def deny():
    return abort(401)
	
@app.route('/html')
def html():
    return(render_template('hello.html'))
	
@app.route('/input')
def input():
    return(render_template('input.html'))
	
@app.route('/display', methods = ['POST', 'GET'])
def display():
   if request.method == 'POST':
       user = request.form['post']
       print(user, file=sys.stdout)
   return 'Output is on terminal'
   
if __name__ == "__main__": #to run the app.
    app.run(debug=True)
	
