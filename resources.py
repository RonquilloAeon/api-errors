import falcon


class SuccessResource:
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        data = req.media  # If no body, will throw 400

        resp.status = falcon.HTTP_201
