import sys

from flask import Flask, render_template, redirect
from flask_flatpages import FlatPages
from flaskext.markdown import Markdown
from flask.ext.assets import Environment as AssetManager
from flask_frozen import Freezer


# configuration
DEBUG = False
BASE_URL = 'https://nicolas.perriault.net'
ASSETS_DEBUG = DEBUG
FLATPAGES_AUTO_RELOAD = True
FLATPAGES_EXTENSION = '.md'
FLATPAGES_ROOT = 'pages'

# App configuration
SECTION_MAX_LINKS = 12

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)
markdown_manager = Markdown(app, extensions=['fenced_code'], output_format='html5',)
asset_manager = AssetManager(app)

@app.route('/')
def index():
    return render_template('index.html', pages=pages)

#@app.route('/sublocator/')
#def sublocator():
#    return redirect("https://docs.google.com/spreadsheets/d/1-TsLhg2NbzardgX6KckQM_p5O5VMesYYabcnwR09fZ0", code=302)

@app.route('/photos/')
def photos():
    return render_template("photos/photos.html")

#@app.route('/wiki/')
#def wiki():
#    return redirect("http://gleegue.wikidot.com/", code=302)

@app.route('/blog/')
def blog():
    return render_template("blog/blogs.html")

@app.route('/track/')
def track():
    return render_template("track/tracking-sheets.html")

@app.route('/<path:path>/')
def page(path):
    return pages.get_or_404(path).html

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(port=8000)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               