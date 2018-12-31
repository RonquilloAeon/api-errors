import falcon


class SuccessResource:
    def on_get(self, req, resp):
        resp.media = {'test:': 123}
        resp.status = falcon.HTTP_200
