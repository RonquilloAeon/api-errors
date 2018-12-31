import falcon

import resources


def create():
    app = falcon.API()

    app.add_route('/success', resources.SuccessResource())

    return app


application = create()
