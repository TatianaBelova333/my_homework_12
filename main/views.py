from flask import request, render_template, Blueprint, send_from_directory
import functions
import logging


main_blueprint = Blueprint('main', __name__, template_folder='templates')

logging.basicConfig(filename='basic.log', level=logging.INFO)


@main_blueprint.route('/uploads/<path:path>')
def statis_dir(path):
    return send_from_directory('uploads', path)


@main_blueprint.route('/')
def page_index():
    return render_template('main.html')


@main_blueprint.route('/search')
def search_post():
    posts = functions.load_json_data(functions.POST_PATH)
    if not posts:
        logging.error('Ошибка загрузки файла')
    s = request.args.get('s')
    if not s or set(s) == {' '}:  # if search bar left blank or contains whitespaces only
        return page_index()
    posts_found = functions.search_for_user_input(s, posts)
    logging.info(f'Поиск по запросу {s}')
    return render_template('posts_list.html', user_input=s, posts=posts_found)
