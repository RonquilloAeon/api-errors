class StandardResponseMiddleware:
    def process_response(self, req, resp, resource, req_succeeded):
        if req_succeeded:
            context = resp.context

            result = context.get('result')
            results = context.get('results')

            if result and results:
                raise ValueError('Unexpected result and results in response')

            message = getattr(resp, 'message', None)
            status_message = getattr(resp, 'status_message', 'success')
            media = {
                'message': message,
                'status': status_message,
            }

            if result:
                media['result'] = result
            elif results:
                media['results'] = results

            resp.media = media
