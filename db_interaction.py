'''
Created on Apr 4, 2019
Copyright (c) 2018-2019 Alberto Monge Roffarello

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License
@author: alberto-mr
'''

import sqlite3


def db_insert_task(text):
    '''
    :param text: text that we want to insert as task in the db
    This method insert a task in the database
    '''

    # prepare the query text
    sql = """INSERT INTO task(todo) VALUES (?)"""

    #connect to the db
    conn = sqlite3.connect("task_list.db")
    cursor = conn.cursor()
    result = -1
    try:
        #execute the query passing the needed parameters
        cursor.execute(sql, (text, ) )
        #commit all pending queries
        conn.commit()
        result = 1
    except Exception as e:
        print(str(e))
        # if something goes wrong: rollback
        conn.rollback()

    #close the connection
    conn.close()

    return result


def get_sorted_tasks_list():
    '''
    :param tasks_list: list of existing tasks
    Get existing tasks from the database
    '''

    tasks_list = []
    sql = "SELECT id, todo FROM task order by todo ASC" #here we order data using "order by"
    conn = sqlite3.connect("task_list.db")

    # to remove u from sqlite3 cursor.fetchall() results
    conn.text_factory = sqlite3.OptimizedUnicode


    cursor = conn.cursor()
    cursor.execute(sql)

    results = cursor.fetchall()

    # print results

    for row in results:
        tasks_list.append( {'id': row[0], 'todo': row[1]})

    conn.close()

    return tasks_list


def db_contains(task):
    '''
    :param task: the task we want to check
    This method returns true if a given task is in the db, false otherwise
    '''

    # prepare the query text
    sql = "select todo from task where todo = ?"

    # connect to the db
    conn = sqlite3.connect("task_list.db")
    cursor = conn.cursor()
    cursor.execute(sql, (task,))

    results = cursor.fetchall()
    conn.close()

    if(len(results) == 0):
        return False
    else:
        return True


def db_remove_task(task):
    '''
    :param task: the task we want to remove from the db
    This method remove from the db a specific task
    '''

    # prepare the query text
    sql = "delete from task where todo = ?"

    # connect to the db
    conn = sqlite3.connect("task_list.db")
    cursor = conn.cursor()
    result = -1
    try:
        # execute the query passing the needed parameters
        cursor.execute(sql, (task,))
        # commit all pending executed queries in the connection
        conn.commit()
        result = 1
    except Exception as e:
        print(str(e))
        # if something goes wrong: rollback
        conn.rollback()

    # close the connection
    conn.close()

    return result

def db_remove_multiple_tasks(text):
    '''
    :param text: text (or part of it) of the task we want to remove from the db
    This method remove from the db all the tasks that contain the specified string
    '''

    # prepare the query text
    sql = "delete from task where todo LIKE ?"

    # add percent sign (%) wildcard to select all the strings that contain specified text
    # <<the multiple character percent sign (%) wildcardcan be used to represent any number of characters in a value match>>
    text = "%" + text + "%"

    #connect to the db
    conn = sqlite3.connect("task_list.db")
    cursor = conn.cursor()

    result = -1
    try:
        #execute the query passing the needed parameters
        cursor.execute(sql, (text, ) )
        #commit all pending executed queries in the connection
        conn.commit()
        result = 1
    except Exception as e:
        print(str(e))
        # if something goes wrong: rollback
        conn.rollback()

    #close the connection
    conn.close()

    return result
