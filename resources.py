import falcon


class BadRequestResource:
    def on_post(self, req, resp):
        data = req.media

        raise falcon.HTTPBadRequest(description='Something bad')


class DetailResource:
    def on_get(self, req, resp, id):
        resp.context = {
            'result': {'hello': 'world'}
        }


class ListResource:
    def on_get(self, req, resp):
        resp.context = {
            'results': [{'say hello': c} for c in range(10)]
        }


class SuccessResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        data = req.media  # If no body, will throw 400

        resp.status = falcon.HTTP_201
