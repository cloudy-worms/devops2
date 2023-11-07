from flask import Flask, request, redirect
from jinja2 import Template
from os.path import join as path_to

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        with open(path_to('static', 'index.html'), 'rt', encoding='utf-8') as ht:
            with open('count.txt', 'rt', encoding='utf-8') as count:
                return Template(ht.read()).render({'count': count.read()})

    elif request.method == "POST":
        with open('count.txt', 'rt', encoding='utf-8') as countfile:
            count = int(countfile.read())
        with open('count.txt', 'wt', encoding='utf-8') as countfile:
            print(count + 1, file=countfile)
        return redirect('/')


if __name__ == '__main__':
    app.run()
