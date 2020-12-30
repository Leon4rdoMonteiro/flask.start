from uuid import uuid4

class UserService(object):

    def __init__(self):
        self.__users_data = []


    def create(self, body):

        found = list(
            filter(
                lambda user: user['email'] == body['email'], self.__users_data
            )
        )

        if found:
            return { 
                'error': True,
                'status_code': 400,
                'message': 'User already exists' 
            }

        body['id'] = str(uuid4())
        self.__users_data.append(body)

        response = {
            'error': False,
            'status_code': 201,
            'message': 'User created successfully'
        }

        return response


    def show(self, user_id):

        if not self.__users_data:
            return { 
                'error': True,
                'status_code': 404, 
                'message': 'No data found'
            }

        found = list(
            filter(
                lambda user: user['id'] == user_id, self.__users_data
            )
        )

        if not found:
            return { 
                'error': True,
                'status_code': 404,
                'message': 'User not found' 
            }

        [user] = found

        return {
            'error': False,
            'status_code': 200,
            'data': user
        }

    
    def index(self):
        # Get query strings
        # query = request.args
        if not self.__users_data:
            return { 
                'error': True,
                'status_code': 404, 
                'message': 'No data found'
            }

        users = {
            'error': False,
            'status_code': 200,
            'data': self.__users_data
        }

        return users
        
    def update(self, user_id, body):

        if not self.__users_data:
            return { 
                'error': True,
                'status_code': 404, 
                'message': 'No data found'
            }

        found = list(
            filter(
                lambda user: user['id'] == user_id, self.__users_data
            )
        )

        if not found:
            return { 
                'error': True,
                'status_code': 404,
                'message': 'User not found' 
            }


        [user] = found

        if user['email'] == body['email']:
            return { 
                'error': True,
                'status_code': 400,
                'message': 'User already exists' 
            }


        user.update(body)

        return {
            'error': False,
            'status_code': 200,
            'data': user,
            'message': 'User updated successfully'
        }


    def delete(self, user_id):

        if not self.__users_data:
            return { 
                'error': True,
                'status_code': 404,
                'message': 'No data was found' 
            }
        
        found = list(
            filter(
                lambda user: user['id'] == user_id, self.__users_data
            )
        )

        if not found:
            return { 
                'error': True,
                'status_code': 404,
                'message': 'User not found' 
            }
            
        [user] = found

        self.__users_data.remove(user)
        
        return {
            'error': False,
            'status_code': 200,
            'message': 'User removed successfully'
        }