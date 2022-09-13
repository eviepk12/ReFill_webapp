from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@views.route('/main', methods=['GET'])
def main_page():
    return render_template("main_page.html")