from app import db
from app.models.classes.post import Post
from datetime import datetime
from flask import request, jsonify

def get_all_posts(id = None):
    if id == None:
        data_result = list(db.posts.find())
        for one_post in data_result:
            del one_post['_id']
    else:
        data_result = db.posts.find_one({'id': int(id)})
        del data_result['_id']

    return jsonify(data_result), 200

def register():
    data = request.get_json()
    
    data_class = Post(data.get('title'), data.get('author'), data.get('tags'), data.get('content'))
    post_data = data_class.__dict__


    db.posts.insert_one(post_data)

    del post_data["_id"]

    return post_data, 201

def patch_post(id):
    data = request.get_json()
    db.posts.update_one({"id": int(id)}, {"$set": {**data, "updated_at": datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")}} )

    patched_post = db.posts.find_one({'id': int(id)})
    del patched_post['_id']

    return patched_post, 200

def del_post(id):
    post_to_delete = db.posts.find_one({'id': int(id)})
    del post_to_delete['_id']

    db.posts.delete_one({"id": int(id)})

    return post_to_delete, 200
