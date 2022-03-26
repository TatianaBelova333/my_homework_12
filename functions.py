import json
from json.decoder import JSONDecodeError


ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
POSTS = []
POST_PATH = "posts.json"


def is_filename_allowed(filename):
    extension = filename.split(".")[-1]
    if extension in ALLOWED_EXTENSIONS:
        return True
    return False


def load_json_data(filename=POST_PATH):
    global POSTS
    try:
        with open(filename, 'r', encoding='utf') as file:
            data = json.load(file)
            POSTS = data
        return POSTS
    except (FileNotFoundError, JSONDecodeError):
        return None



def add_new_post_into_database(pic_path, post_text, filename=POST_PATH):
    global POSTS
    new_post = {'pic': pic_path, 'content': post_text}
    POSTS.append(new_post)
    with open(filename, 'w') as file:
        json.dump(POSTS, file, ensure_ascii=False, indent=4)


def search_for_user_input(user_input, posts=POSTS):
    matched_posts = []
    user_input = user_input.strip().lower()
    try:
        for post in posts:
            if len(user_input) > 1 and user_input in post.get('content').lower():
                matched_posts.append(post)
        return matched_posts
    except:
        return None








