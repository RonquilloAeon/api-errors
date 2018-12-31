class StandardResponseMiddleware:
    def process_response(self, req, resp, resource, req_succeeded):
        if req_succeeded:
            result = getattr(resp, 'result', None)
            results = getattr(resp, 'results', None)

            message = getattr(resp, 'message', None)
            status_message = getattr(resp, 'status_message', 'success')
            media = {
                'message': message,
                'status': status_message,
            }

            if result and results:
                raise ValueError('result and results cannot be both set')

            if result:
                media['result'] = result
            elif results:
                media['results'] = results

            resp.media = media
