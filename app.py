import falcon

import middleware
import resources


def create():
    app = falcon.API(middleware=[middleware.StandardResponseMiddleware()])

    app.add_route('/success', resources.SuccessResource())

    return app


application = create()
