from uuid import uuid4
from json import loads

from config import db

from models.User import User

class UserService(object):

    def __init__(self):
        self.__users_data = []


    def create(self, body):

        found = User.query.filter_by(email=body['email']).first()

        if found:
            return { 
                'error': True,
                'status_code': 400,
                'message': 'User already exists' 
            }

        name, email, password = body.values()

        created = User(name, email, password)
        db.session.add(created)
        db.session.commit()

        user = loads(str(created))

        response = {
            'error': False,
            'status_code': 201,
            'data': user,
            'message': 'User created successfully'
        }

        return response


    def show(self, user_id):

        found = User.query.filter_by(id=user_id).first()

        if not found:
            return { 
                'error': True,
                'status_code': 404,
                'message': 'User not found' 
            }

        user = loads(str(found))

        return {
            'error': False,
            'status_code': 200,
            'data': user
        }

    
    def index(self):
        found = User.query.all()

        users = []

        for user in found:
            users.append(loads(str(user)))

        return { 
            'error': False,
            'status_code': 200,
            'data': users
        }
        
    def update(self, user_id, body):

        found = User.query.filter_by(id=user_id).first()

        if not found:
            return { 
                'error': True,
                'status_code': 404,
                'message': 'User not found' 
            }

        try:
            if found.email == body['email']:
                return { 
                    'error': True,
                    'status_code': 400,
                    'message': 'User already exists' 
                }
        except:
            pass

        user = loads(str(found))

        user.update(body)

        found.name = user['name']
        found.email = user['email']
        found.password = user['password']

        db.session.add(found)
        db.session.commit()
        
        return {
            'error': False,
            'status_code': 200,
            'data': user,
            'message': 'User updated successfully'
        }


    def delete(self, user_id):

        found = User.query.filter_by(id=user_id).first()

        if not found:
            return { 
                'error': True,
                'status_code': 404,
                'message': 'User not found' 
            }
            
        db.session.delete(found)
        db.session.commit()

        return {
            'error': False,
            'status_code': 200,
            'message': 'User removed successfully'
        }