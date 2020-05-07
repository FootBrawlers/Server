from flask import Flask, render_template
from Server.forms import CommandForm
from Server.pygame_inst import generate,show_text

app=Flask(__name__)

app.config['SECRET_KEY']='Shh!ItsSecret'


@app.route('/', methods=['POST', 'GET'])
def index():
    form = CommandForm()
    if form.validate_on_submit():
        if form.command.data==0:
            show_text("start")
        elif form.command.data==1:
            show_text("Stop")
        elif form.command.data==2:
            show_text("Throw in")
    return render_template('home.html',form=form)

