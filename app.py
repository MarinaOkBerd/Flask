from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/shoes')
def shoes():
    return render_template('shoes.html')


@app.route('/clothes')
def clothes():
    return render_template('clothes.html')


if __name__ == '__main__':
    app.run(debug=True)