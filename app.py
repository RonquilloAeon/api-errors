import falcon

import error_handlers
import middleware
import resources


def create():
    app = falcon.API(middleware=[middleware.StandardResponseMiddleware()])
    app.add_error_handler(falcon.HTTPError, error_handlers.standard_response_error_handler)

    app.add_route('/success', resources.SuccessResource())

    return app


application = create()
