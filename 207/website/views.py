from flask import Blueprint, render_template
from .models import event 

mainbp = Blueprint('index', __name__)
@mainbp.route('/', methods=['GET', 'POST'])
def run():
    events = event.query.all()
    return render_template('index.html', events=events)








