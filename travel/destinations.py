#from crypt import methods
from flask import Blueprint, render_template, request, url_for, redirect

from travel.auth import login
from .models import Destination, Comment
from datetime import datetime
from .forms import DestinationForm, CommentForm
from . import db
import os
from werkzeug.utils import secure_filename
from flask_login import login_required, current_user

# name - first argument is the blue print name 
# import name - second argument - helps identify the root url for it 
bp = Blueprint('destination', __name__, url_prefix='/destinations')

@bp.route('/<id>')
def show(id):
    commentForm = CommentForm()
    destination = Destination.query.filter_by(id=id).first()
    return render_template('destinations/show.html', destination=destination, form=commentForm)

@bp.route('/<id>/comment', methods = ['GET', 'POST'])
@login_required
def comment(id):
    #here the form is created  form = CommentForm()
    form = CommentForm()
    destination = Destination.query.filter_by(id=id).first()
    if form.validate_on_submit():	#this is true only in case of POST method
        comment = Comment(text=form.comment.data, destination=destination, user=current_user)
        # notice the signature of url_for
        db.session.add(comment)
        db.session.commit()
    return redirect(url_for('destination.show', id=1))

@bp.route('/create', methods = ['GET', 'POST'])
@login_required
def create():
    print('Method type: ', request.method)
    form = DestinationForm()
    if form.validate_on_submit():
        destination = Destination(name=form.name.data,
        description= form.description.data,
        image=form.image.data,
        currency=form.currency.data)
        # add the object to the db session
        db.session.add(destination)
        # commit to the database
        db.session.commit()
        print('Successfully created new travel destination', 'success')
        #Always end with redirect when form is valid
        return redirect(url_for('destination.create'))
    return render_template('destinations/create.html', form=form)

# @dest_bp.route('/<destination>/comment', methods = ['GET', 'POST'])  
# def comment(destination):  
#     form = CommentForm()  
#     #get the destination object associated to the page and the comment
#     destination_obj = Destination.query.filter_by(id=destination).first()  
#     if form.validate_on_submit():  
#         #read the comment from the form
#         comment = Comment(text=form.text.data, destination=destination_obj) 
#         #here the back-referencing works - comment.destination is set
#         # and the link is created
#         db.session.add(comment) 
#         db.session.commit() 

#         #flashing a message which needs to be handled by the html
#         #flash('Your comment has been added', 'success')  
#         print('Your comment has been added', 'success') 
#     # using redirect sends a GET request to destination.show
#     return redirect(url_for('destination.show', id=destination))

def check_upload_file(form):
    #get file data from form  
    fp=form.image.data
    filename=fp.filename
    #get the current path of the module file… store image file relative to this path  
    BASE_PATH=os.path.dirname(__file__)
    #upload file location – directory of this file/static/image
    upload_path=os.path.join(BASE_PATH,'static/image',secure_filename(filename))
    #store relative path in DB as image location in HTML is relative
    db_upload_path='/static/image/' + secure_filename(filename)
    #save the file and return the db upload path  
    fp.save(upload_path)
    return db_upload_path