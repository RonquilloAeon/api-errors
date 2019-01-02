import falcon


def generic_error_handler(ex, req, resp, params):
    resp.media = {
        'title': '500 Internal Server Error',
        'message': 'An error occurred while processing your request',
        'status': 'error',
    }
    resp.status = falcon.HTTP_500


def standard_response_error_handler(ex, req, resp, params):
    status_code = int(ex.status[:3])

    media = {
        'title': ex.title,
        'message': ex.description,
        'status': 'fail' if status_code < 500 else 'error',
    }

    resp.media = media
    resp.status = ex.status
