from flask import Flask, request, jsonify, render_template
from utils import connection1
import re
import psycopg2
import json
import random

app = Flask(__name__)


@app.route('/')
def method_name():
    return render_template('postgresql_data.html')

dict_1 = {}
list_1 = []

def check(func):
    def change(e):
        match = re.fullmatch('[a-zA-Z0-9._]+@[a-z.]+',e)
        if match != None:
            return func(e)
        else:
            return func('INVALID EMAIL')
    return change

@check
def email_op(e):
    return e

@app.route('/receiving', methods = ['POST', 'GET'])
def data_receving():
    conn, cur = connection1()
    if request.method == 'POST':
        list_2 = ['ids', 'first_name', 'last_name', 'email', 'passwords']
        list_3 = []
        dict_2 = {}

        for i in list_2:
            data = request.form.get(i)
            list_3.append(data)
            print(list_3)
        
        for i in range(len(list_3)):
            dict_2.setdefault(list_2[i], list_3[i])

        list_1.append(dict_2)
        print(list_1)

        with open("json_file.json","w+") as f:
            json.dump(list_1, f, indent=5)
            f.seek(0)
            data = json.load(f)
            print('successfully data fetched')
            print(data)

        for var in data:
            if var['passwords'] == None:
                var['passwords']=''.join((random.choice('abcdxyzpqrstuvwxyz12354@') for i in range(8)))
        for i in data:
            ids = i['ids']
            first_name = i['first_name']
            last_name = i['last_name']
            email = email_op(i['email'])
            passwords = i['passwords']
            cur = conn.cursor()

            insert_stmt = "INSERT INTO details (ids,first_name, last_name, email, passwords)\
                VALUES (%s,%s,%s,%s,%s)"
            data1 = (ids,first_name, last_name, email, passwords)

            cur.execute(insert_stmt, data1)
            
            conn.commit()
            return "data inserted"
        return 'done'
print ("Records created successfully")

           
if __name__ == '__main__':
    app.run(debug=True)
    
            