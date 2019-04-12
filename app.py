from flask import Flask, jsonify, request
import db_interaction

api_endpoint = '/api/v1'

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route(api_endpoint+'/tasks', methods=['GET'])
def get_task_list():
    tasks = db_interaction.get_sorted_tasks_list() ;
    return jsonify(tasks)


@app.route(api_endpoint+'/tasks/<int:id>', methods=['GET'])
def get_one_task(id):
    tasks = db_interaction.get_sorted_tasks_list();
    one_task = [task for task in tasks if task['id']==id]
    return jsonify(one_task[0])


@app.route(api_endpoint+'/tasks', methods=['POST'])
def add_one_task():
    one_task = request.json
    #print(one_task)
    db_interaction.db_insert_task(one_task['todo'])
    return ""

if __name__ == '__main__':
    app.run()
