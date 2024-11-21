import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from replit import db
import json

app = Flask(__name__)

import os  #from GPT

if os.environ.get("FLASK_ENV") == "development":  #from GPT
  app.debug = True  #from GPT

tasks = []


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    task_content = request.form['content']
    tasks = db.get("tasks") or []
    tasks.append(task_content)
    db["tasks"] = tasks

  tasks = db.get("tasks") or []

  return render_template('index.html', tasks=tasks)


@app.route('/database')
def database():
  tasks = db["tasks"]
  return json.dumps([task for task in tasks], default=lambda o: o.__dict__)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))
