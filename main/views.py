from flask import Blueprint, request, render_template
from functions import *
import logging

logging.basicConfig(filename="basic.log", level=logging.INFO)

main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.route('/')
def page_index():
    """
    Возвращает главную страницу
    """
    return render_template('index.html')


@main_blueprint.route('/search')
def search_page():
    """
    Возвращает списко постов по введенному слову пользователя
    """
    s = request.args['s']
    posts = search_post_by_user_words(s)
    logging.info(f'Был произведен поиск по слову {s}')
    return render_template('post_list.html', list_of_posts=posts, user_search=s)
