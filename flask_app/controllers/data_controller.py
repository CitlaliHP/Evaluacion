
from flask import Blueprint, render_template, request, redirect
from models.data_model import DataModel

data_blueprint = Blueprint('data', __name__)
data_handler = DataModel()

@data_blueprint.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and file.filename.endswith('.csv'):
            data_handler.load_csv(file)
            return redirect('/head')
    return render_template('index.html')

@data_blueprint.route('/head', methods=['GET', 'POST'])
def head():
    if request.method == 'POST':
        n = int(request.form['n'])
        result = data_handler.get_head(n)
        return render_template('head.html', result=result)
    return render_template('head.html')

@data_blueprint.route('/tail', methods=['GET', 'POST'])
def tail():
    if request.method == 'POST':
        n = int(request.form['n'])
        result = data_handler.get_tail(n)
        return render_template('tail.html', result=result)
    return render_template('tail.html')

@data_blueprint.route('/info')
def info():
    result = data_handler.get_info()
    return render_template('info.html', result=result)

@data_blueprint.route('/columns')
def columns():
    result = data_handler.get_columns()
    return render_template('columns.html', result=result)

@data_blueprint.route('/shape')
def shape():
    result = data_handler.get_shape()
    return render_template('shape.html', result=result)

@data_blueprint.route('/describe')
def describe():
    result = data_handler.get_describe()
    return render_template('describe.html', result=result)

@data_blueprint.route('/select_one', methods=['GET', 'POST'])
def select_one():
    result = None
    if request.method == 'POST':
        col = request.form['column']
        result = data_handler.select_column(col)
    return render_template('select_one.html', result=result)

@data_blueprint.route('/select_many', methods=['GET', 'POST'])
def select_many():
    result = None
    if request.method == 'POST':
        cols = request.form['columns'].split(',')
        result = data_handler.select_columns(cols)
    return render_template('select_many.html', result=result)

@data_blueprint.route('/filter', methods=['GET', 'POST'])
def filter_data():
    result = None
    if request.method == 'POST':
        col = request.form['column']
        op = request.form['operator']
        val = request.form['value']
        result = data_handler.filter_rows(col, op, val)
    return render_template('filter.html', result=result)
