from flask import render_template,flash,redirect
from app import app
from app.forms import LoginForm

# @app.route('/sai')
# def sai():
#     return '''
#     <button>sai</button>
#     '''

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Tony Stark'}
    posts =[
        {
            'author':{'username':'tony stark'},
            'body':'great american ass'
        },
        {
            'author':{'username':'steve rogers'},
            'body':'Avengers Assemble'
        }
    ]
    return render_template('index.html',title='home',user=user,posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash('login requested for user {},remember_me={}'.format(form.username.data,form.remember_me.data))
        return redirect('/index')
    return render_template('login.html',title='Sign In',form=form)    