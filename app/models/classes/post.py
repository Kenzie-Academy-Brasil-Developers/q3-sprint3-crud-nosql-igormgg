from app import db
from datetime import datetime

class Post:
    def __init__(self, title, author, tags, content):
        id_list = []
        for post in list(db.posts.find()):
            id_list.append(post['id'])
        self.id = 1 if len(id_list) == 0 else max(id_list) + 1
        self.created_at = datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")
        self.updated_at = datetime.utcnow().strftime("%d/%m/%Y %H:%M:%S")
        self.title = title
        self.author = author
        self.tags = tags
        self.content = content