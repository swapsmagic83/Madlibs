from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "this is secret key"
debug = DebugToolbarExtension(app)

@app.route('/')
def show_form():
    return render_template('home.html')

@app.route('/story')
def add_story():
    place= request.args.get('place')
    noun= request.args.get('noun')
    verb= request.args.get('verb')
    adjective= request.args.get('adjective')
    plural_noun= request.args.get('plural_noun')
    answers={'place':place,'noun':noun,'verb':verb,'adjective':adjective,'plural_noun':plural_noun}
    story1= story.generate(answers)

    return render_template('story.html',story1=story1)
