from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    return 'Sopping'


@app.route('/Shoes/')
def shoes():
    return 'Shoes'


@app.route('/Clothes/')
def clothes():
    return 'Clothes'


if __name__ == '__main__':
    app.run(debug=True)