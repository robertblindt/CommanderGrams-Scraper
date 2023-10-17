from app import app
from flask import render_template, redirect, url_for
from app.forms import CommanderSearch
from app.processing import Processing

processor = Processing()

@app.route('/', methods = ["GET","POST","PUT"])
def index():
    form = CommanderSearch()
    if form.validate_on_submit():
        # print(form.commander.data)
        card_retrieval_list = processor.parseEDHrec_for_card_names(form.commander.data)
        if card_retrieval_list:
            print(card_retrieval_list)

            print("OOO you searched for a commander! Nicely done!")
            return redirect(url_for('index'))
    
    # return 'Hello!' 
    return render_template('index.html', form = form)

