def not_found(error):
    return { 
        'error': True,
        'status_code': 404,
        'message': 'Route not found',
    }, 404
