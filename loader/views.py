from flask import request, render_template, Blueprint, send_from_directory
import functions
import logging

logging.basicConfig(filename='basic.log', level=logging.INFO)

post_loader_blueprint = Blueprint('post_loader', __name__, template_folder='templates')


@post_loader_blueprint.route('/uploads/<path:path>')
def statis_dir(path):
    return send_from_directory('uploads', path)


@post_loader_blueprint.route('/')
def load_post_page():
    return render_template('post_form.html')


@post_loader_blueprint.route('/new-post', methods=['POST'])
def upload_post():
    picture = request.files.get('picture')
    filename = picture.filename.replace(' ', '_')
    file_is_allowed = functions.is_filename_allowed(filename)
    if file_is_allowed:
        pic_path = f'./uploads/images/{filename}'
        picture.save(pic_path)
        text = request.form.get('content')
        functions.add_new_post_into_database(pic_path, text, functions.POST_PATH)
    else:
        pic_path = './uploads/images/sad_cat.jpg'
        text = 'Попробуйте загрузить другую картинку'
        logging.info('Загруженный файл - не картинка')
    return render_template('post_uploaded.html',
                           path=pic_path, text=text,
                           file_is_allowed=file_is_allowed,
                           filename=filename)
