from flask import Flask, render_template, request,render_template_string

app = Flask(__name__)



@app.route('/')
def index():  # put application's code here
    return render_template('pages/frontpage/index.html')

@app.route('/archive')
def archive():  # put application's code here
    return render_template('archive.html')


if __name__ == '__main__':
    app.run()
