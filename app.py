from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story1, story2

app = Flask(__name__)
app.config['SECRET_KEY'] = "this is secret key"
# app.config['SEND_FILE_MAX_AGE_DEFAULT'] = -1
debug = DebugToolbarExtension(app)

@app.route('/')
def show_form():
    return render_template('base.html')

@app.route('/form1')
def goto_story1():
    return render_template('form1.html')
@app.route('/form2')
def goto_story2():
    return render_template('form2.html')

@app.route('/story1')
def get_story1():
    place= request.args.get('place')
    noun= request.args.get('noun')
    verb= request.args.get('verb')
    adjective= request.args.get('adjective')
    plural_noun= request.args.get('plural_noun')
    answers={'place':place,'noun':noun,'verb':verb,'adjective':adjective,'plural_noun':plural_noun}
    
    newstory= story1.generate(answers)
    return render_template('new-story.html',newstory=newstory)

@app.route('/story2')
def get_story2():
    noun= request.args.get('noun')
    verb= request.args.get('verb')
    answers={'noun':noun,'verb':verb}
    newstory= story2.generate(answers)
    return render_template('new-story.html',newstory=newstory)
    