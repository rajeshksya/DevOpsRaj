from flask import Flask, request,jsonify

app = Flask(__name__)

tasks=[{"id": 1,

"title": "Buy groceries",

"description": "Milk, Cheese, Pizza, Fruit",

"done": False},

 {

"id": 2,

"title": "Learn Python",

"description": "Need to find a good Python tutorial on the web",

"done": False

 }]

@app.route('/tasks',methods=['GET'])

def get_tasks():

return task

@app.route('/tasks/<id>',methods=['GET'])

def get_task_id(id):

 task=tasks[int(id)-1]

return task

if name== '__main__':

 app.run(debug=True)