from flask import Blueprint, request, render_template
from functions import *
import logging

logger_info = logging.getLogger('logger_info')
logger_errors = logging.getLogger('logger errors')

loader_blueprint = Blueprint('loader_blueprint', __name__)


@loader_blueprint.route("/post", methods=["GET"])
def page_post_form():
    """
    Возвращает страницу с формой для загрузки
    """
    return render_template('post_form.html')


@loader_blueprint.route("/post", methods=["POST"])
def page_post_upload():
    """
    Загружает картинку с описанием, возвращает пост при удачной загрузке
    """
    new_post = {}
    content = request.form['content']
    picture = request.files.get('pic')
    if picture and content:
        if is_filename_allowed(picture.filename):
            new_post['pic'] = picture.filename
            new_post['content'] = content
            append_post_to_data(new_post)
            picture.save(f'./uploads/images/{picture.filename}')
            return render_template('post_uploaded.html', post=new_post)
        else:
            logger_info.info(f'Была попытка загрузить файл с расширением {picture.filename.split(".")[-1]}')
            return 'Неверный формат изображения'
    logger_errors.error('Ошибка загрузки файла')
    return f'Ошибка загрузки'
