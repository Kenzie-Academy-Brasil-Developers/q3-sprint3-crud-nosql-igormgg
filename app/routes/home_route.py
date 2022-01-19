from app.controllers.user_controllers import del_post, get_all_posts, patch_post, register
from app.models.decorators.decorators import verify_id, verify_keys, verify_one_key
from flask import Flask, request

def all_routes(app: Flask):

    @app.get('/')
    def rota_teste():
        print(request.get_json())
        return 'Essa é a rota teste'
    
    @app.get('/posts')
    def get_posts():
        return get_all_posts()
    
    @app.get('/posts/<int:id>')
    @verify_id
    def get_post(id):
        return get_all_posts(id)

    @app.post('/posts')
    @verify_keys(['title', 'author', 'tags', 'content'])
    def register_user():
        return register()

    @app.patch('/posts/<int:id>')
    @verify_id
    @verify_one_key(['title', 'author', 'tags', 'content'])
    def update_post(id):
        return patch_post(id)

    @app.delete('/posts/<int:id>')
    @verify_id
    def delete_post(id):
        return del_post(id)