import email
from tkinter.messagebox import RETRY
from flask import Blueprint, render_template, request, session, redirect, url_for
from travel import destinations

from travel.models import Destination

mainbp = Blueprint('main', __name__) #handles log in and log out

@mainbp.route('/')
def index():
    destinations = Destination.query.all()
    return render_template('index.html', destinations=destinations)

@mainbp.route('/search')
def search():
    if request.args['search']:
        print(request.args['search'])
        dest = '%' + request.args['search'] + '%'
        destinations = Destination.query.filter(Destination.description.like(dest)).all()
        return render_template('index.html', destinations=destinations)
    else:
        return redirect(url_for('main.index'))


#@main_bp.route('/login', methods = ['GET','POST']) #pass in get and post so we can get the website to view and pass post so we can submit data back to server
#def login():
 #   email = request.values.get('email')
  #  passwd = request.values.get('pwd')
   # session['email'] = request.values.get('email') #session object stores values of the post request
    #print('Users email: {}\nUsers Password: {}'.format(email,passwd))
    #return render_template('login.html')

#@main_bp.route('/logout') #doesnt render a page so doesnt need get or post assigned to it
#def logout():
 #   if 'email' in session:  #if email key is in session object we want to get rid of it
  #      session.pop('email') #uses pop function to clear email key
   # return "logged out" 


#if 'email' in session:    
#        str='<h1>hello ' + session['email'] + '</h1>' #if email exists create new string called str which holds a bit of html and users interperlation to add a value fo the email that holds the key for the session object
#    else:
#        str='<h1>hello world</h1>' #if there is no key in the session object it just prints hello world
#    return str