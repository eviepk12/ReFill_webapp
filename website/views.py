from flask import Blueprint, render_template
from .models import User
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home.html")

@views.route('/main', methods=['GET', 'POST'])
def main_page():
    return render_template("main_page.html")

@views.route("/detail", methods=['GET'])
def detail():
    return render_template("detail.html")