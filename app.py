from flask import Flask, render_template, request,render_template_string, redirect, url_for
from queries import *
from forms import *


app = Flask(__name__)
app.config['WTF_CSRF_SECRET_KEY'] = "secretkey"
app.config['SECRET_KEY'] = "secretkey"


@app.route('/')
def index():  # put application's code here
    meta = fetchFiletableData()
    catalogs = fetchAllCatalogs()
    tagCategories = fetchAllTagCatergories()
    return render_template('pages/frontpage/index.html', meta=meta, catalogs=catalogs, tagCategories=tagCategories)

@app.route('/archive')
def archive():  # put application's code here
    catalogs = fetchAllCatalogs()
    tagCategories = fetchAllTagCatergories()

    return render_template('archive.html',catalogs=catalogs, tagCategories=tagCategories)


if __name__ == '__main__':
    app.run()
