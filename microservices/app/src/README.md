<h1>Fellowship Week-1 Task</h1>

<p>These are the simple tasks of python and Flask framework, given in the HPDF week-1 project.</p>

<h1>Getting Started</h1>

<p>To know the project tasks just <a href="https://docs.google.com/document/d/1cnCbFkgn-A7pSONDTX9AlIzaqyWlZFZAT4xncfAYXcc/edit?ts=5a1e8781#">Click Here</a> The list of these tasks are given to us just to improve our fundamental knowledge of Python & Flask and communication with other interns. I started to go through youtube tutorials and some written tutorials, then done all tasks with the help of other intern and internet.</p>

<h1>Prerequisites</h1>

<p>Need to install Python 3.7 and Flask 0.12.2</p>

<h1>Installation</h1> 

<p>First, download python on https://www.python.org/downloads/ and install it. Then go to your command prompt and type pip install flask then click enter to install flask on your computer. This command to install flask is for Windows only. Now install virtual environment into the Scripts folder of Python package. First open Scripts folder in the command prompt and type the command "pip install virtualenv" and then click enter. You also need to install flask and virtual environment directly into your project folder. Now you all set to go.</p>

<h1>Description</h2>

<p><strong>Task-1</strong></p>

<p>The first task is quite an easy task. First import flask module as Importing flask module in the project is mandatory, create an object of flask module as an object of Flask class is our WSGI application, add route(URL) to a particular function, and return a string using a function. You have to declare current module(__name__) as main to run the code. Now call run() method to run the application on a local development server. Interpret your code on command prompt by giving the following command into your app folder.- "python app.py" and press enter. Now you can check your route URL as http://localhost:5000/ So Task-1 is completed.</p>
<p>To return a string- http://localhost:8080/</p> 

<p><strong>Task-2</strong></p>

<p>The second task is quite difficult for me. First added a route and start a function. In this task, we need to fetch data using JSON API. So first to talk to APIs, we have to import requests module of python package. Now get all the required information to fetch result through different APIs using requests.get() method. Now we use a list comprehension to get required result on an HTML page with the help of userID and count variable. Now to show this HTML page on our given route, we need to import a render_template module from the flask and return the HTML file using a render_template method. To view this HTML page on given route, be ensure you put this HTML file in templates folder where your app.py file is placed. Just run the app.py. Task-2 is also completed. I provided a hyperlink on this HTML page for my next task which is explained in next paragraph. </p>
<p>To fetch specific data from API - http://localhost:5000/authors/ </p>

<p><strong>Task-3</strong></p>

<p>This task was so interesting as I took much time to implement this. As the task was to set two simple value(First name and age) as cookie But I implemented through user input. First created a form to input first name and age on http://localhost:5000/inputcookie Link to this page is already given on Task-2 URL. Now form action is set to http://localhost:5000/setcookie . Now on this route, setcookie function is associated. Now to request GET/POST methods and values, import request module from Flask. now request both form fields in two different variables. Now to make responses, import make_response from the flask. I made response on readcookie.html by rendering HTML(resp = make_response(render_template('readcookie.html'))) Now set cookie on the response object using resp.set_cookie() method and return response.- Task-3 is completed successfully. Now click on click here to read cookie, you'll move to http://localhost:5000/getcookie  </p>
<p>To input cookie manually - http://localhost:5000/inputcookie </p>
<p>To Set cookie using input values - http://localhost:5000/setcookie </p>

<p><strong>Task-4</strong></p>

<p>This is just a part of previous task. In this task we have to get cookie using cookie name. I used request.cookies.get() method to get cookie in two variables and return a string with contaning these variables as '+name+ and '+age+'. Task-4 is completed. Now just check http://localhost:5000/getcookie </p>
<p>To get cookie - http://localhost:5000/getcookie </p>

<p><strong>Task-5</strong></p>

<p>This task was also simple. Just need to render an HTML to show "Unauthorised Access" or use abort() method with 401 error. I used abort() method. Hence first I added abort module from the flask. and just passed the error code(401) in the parameter and return this abort method with 401 error and completed this task. </p>
<p>To deny requests at Robots.txt- http://localhost:8080/robots.txt </p>

<p><strong>Task-6</strong></p>

<p>This is an easy task as I have already used render_template() method to render an HTML file. To use this method we need to import render_template from the flask. I created a simple HTML file named hello.html and return with render_template function on given URL. Completed this task.</p>
<p>To render a HTML page - http://localhost:8080/html </p>

<p><strong>Task-7</strong></p>

<p>This task is new and different from another one. We need to take input and POST to any endpoint and show the input in the console. First I render an HTML file input.html on the given route. In input.html, we did action the post method to http://localhost:8080/display . In display function, I requested to POST and request form data in a user variable.(user = request.form['post']) and print this variable value to the console using sys.stdout(print(user, file=sys.stdout)). To use this method we need to import sys module from python package. I imported sys module and completed this task successfully.</p>
<p>To input data to a text box - http://localhost:8080/input </p>
<p>End point of POST method - http://localhost:8080/display </p>

<h1>Author</h1>

<p>Ujjwal Mishra - Web Analyst - Pune</p>

<h1>References</h1>

<p>https://codeshare.io <br> https://www.tutorialspoint.com/flask <br> http://flask.pocoo.org/docs/0.12/tutorial/ <br> https://www.youtube.com/watch?v=kvux1SiRIJQ <br> HPDF Intern Help</p>
