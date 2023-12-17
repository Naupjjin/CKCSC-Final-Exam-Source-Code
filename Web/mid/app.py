from flask import Flask, request, render_template_string, redirect
import os
import urllib.parse

app = Flask(__name__)

base_directory = "message/"
default_file = "message.txt"

def ignore_it(file_param):
    yoooo = file_param.replace('.', '').replace('/', '')
    if yoooo != file_param:
        return "Illegal characters detected in file parameter!"
    return yoooo

def another_useless_function(file_param):
    return urllib.parse.unquote(file_param)

def url_encode_path(file_param):
    return urllib.parse.quote(file_param, safe='')

def useless (abcd):
    aa = ignore_it(abcd)
    bb = another_useless_function(aa)
    cc = ignore_it(bb)
    dd = another_useless_function(cc)
    ee = another_useless_function(dd)
    return ee


@app.route('/')
def index():
    return redirect('/read_secret_message?file=message')

@app.route('/read_secret_message')
def read_file(abcd=None):
    file_param = request.args.get('file')
    file_param = useless(file_param)
    print(file_param)
    file_path = os.path.join(base_directory, file_param)

    try:
        with open(file_path, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return 'File not found! or maybe illegal characters detected'
    except Exception as e:
        return f'Error: {e}'


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=50002)
