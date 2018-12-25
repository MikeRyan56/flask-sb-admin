from flask import Blueprint, render_template

mod = Blueprint('site', __name__) #, template_folder='templates')

@mod.route('/')
@mod.route('/homepage')
def homepage():
    
	template = 'site/index.html'
	return render_template(template)

@mod.route("/about")
def about():
    
    template = 'site/about.html'
    return render_template(template)

@mod.route("/404")
def four_zero_four():
    
    template = '404.html'
    return render_template(template)