import falcon

import error_handlers
import middleware
import resources


def create():
    app = falcon.API(middleware=[middleware.StandardResponseMiddleware()])
    app.add_error_handler(Exception, error_handlers.generic_error_handler)
    app.add_error_handler(falcon.HTTPError, error_handlers.standard_response_error_handler)

    app.add_route('/bad_requests', resources.BadRequestResource())
    app.add_route('/details', resources.ListResource())
    app.add_route('/details/{id:int}', resources.DetailResource())
    app.add_route('/fails', resources.FailResource())
    app.add_route('/push_buttons', resources.PushButtonResource())
    app.add_route('/success', resources.SuccessResource())

    return app


application = create()
