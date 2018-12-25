from flask import Blueprint, render_template

mod = Blueprint('example', __name__, template_folder="template")

@mod.route('/')
@mod.route('/charts')
def charts():
    
	template = 'example/charts.html'
	return render_template(template)

@mod.route("/tables")
def tables():
    
    template = 'example/tables.html'
    return render_template(template)

@mod.route("/blank")
def blank():
    
    template = 'example/blank.html'
    return render_template(template)
