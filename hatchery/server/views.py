from flask import Blueprint
from flask import render_template


main_bp = Blueprint('main_bp', __name__,
                    template_folder='./templates',
                    static_folder='./static_files',
                    static_url_path='/static')


@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/visual')
def visual():
    return render_template('visualization.html')


@main_bp.route('/upload')
def upload_files():
    return render_template('index.html')
