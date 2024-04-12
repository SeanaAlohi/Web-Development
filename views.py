#standard routes for the website that users can go to (i.e. login page)
from flask import Blueprint, flash, render_template, request, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__) #set up a blueprint for flask app


#define view:
@views.route('/', methods=['GET', 'POST']) #allowing 'POST' method for this route
#this decorator makes it so that you cannot access the home page unless you are logged in. 
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short', category='error')
        else:
            #adding the note:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added', category='success')
    #actually rendering the template made in templates:
    return render_template("home.html", user=current_user) #current user allows us to check and authenticate the current user

@views.route('/delete-note', methods=['POST'])
def delete_note():
    #look for note id that was sent
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            
    return jsonify({})