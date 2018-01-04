from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/jm4590')
def about_me():
    return render_template('jm4590.html')

if __name__ == '__main__':
    app.run()
