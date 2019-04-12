import requests

base_uri = 'http://localhost:5000/api/v1'

if __name__=='__main__':
    requests.post(base_uri+'/tasks', json={'todo': "Go home"})

    tasks = requests.get(base_uri+'/tasks')
    tasklist = tasks.json()

    for t in tasklist:
        print(f"{t['id']}: {t['todo']}")
