from app import db
from flask import request
from functools import wraps

def verify_keys(trusted_keys: list[str]):
    def middleFunction(func):
        @wraps(func)
        def innerFunction():
            requirement = request.get_json()
            title = trusted_keys[0]
            author = trusted_keys[1]
            tags = trusted_keys[2]
            content = trusted_keys[3]
            
            try:
                requirement[title]
                requirement[author]
                requirement[tags]
                requirement[content]
                return func()
            
            except KeyError:
                return {
                    "error": "Wrong key(s)",
                    "expected": [
                        "title",
                        "author",
                        "tags",
                        "content"
                    ],
                    "received": list(requirement.keys())
                }, 400

        return innerFunction

    return middleFunction

def verify_one_key(trusted_keys: list[str]):
    def middleFunc(func):
        @wraps(func)
        def innerFunc(id):
            requirement = request.get_json()
            
            try:
                for key in requirement.keys():
                    if key not in trusted_keys:
                        raise KeyError()
                return func(id)
            
            except KeyError:
                return {
                    "error": "Wrong key(s)",
                    "expected": [
                        "title",
                        "author",
                        "tags",
                        "content"
                    ],
                    "received": list(requirement.keys())
                }, 400

        return innerFunc

    return middleFunc

def verify_id(func):
    @wraps(func)
    def inFunction(id = 0):
        try:
            post_to_find = db.posts.find_one({'id': int(id)})
            if post_to_find:
                return func(id)
            raise TypeError()
        except (TypeError):
            return {
                    "error": "Post ID not found"
                    }, 404

    return inFunction