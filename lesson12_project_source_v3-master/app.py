from flask import Flask, request, render_template, send_from_directory
import json

# from functions import ...


POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)

app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024


@app.route("/")
def page_index():
    # with open("posts.json", encoding='utf8') as f:
    #     my_post = json.load(f)
    return render_template('index.html')


@app.route('/search')
def search_page():
    with open('posts.json', encoding='utf8') as f:
        my_post = json.load(f)
        s = request.args['s']
        result = '#' + s
        post_list = []
        for post in my_post:
            if result in post['content']:
                post_list.append(post)
        return render_template("post_list.html", posts=post_list)


@app.route("/list")
def page_tag():
    with open('posts.json', encoding='utf8') as f:
        my_post = json.load(f)
    return render_template('post_list.html', posts=my_post)


@app.route("/post", methods=["GET", "POST"])
def page_post_form():
    with open("posts.json", encoding='utf8') as f:
        return render_template('post_form.html')


@app.route("/post/upload", methods=["POST"])
def page_post_upload():
    picture = request.files.get("picture")
    if picture:
        filename = picture.filename
        picture.save(f"./uploads/images/{filename}")
        return f"Файл загружен и сохранен"
    else:
        return f"Файл не найден"


@app.route("/uploads/<path:path>")
def static_dir(path):
    return send_from_directory("uploads", path)


app.run()
