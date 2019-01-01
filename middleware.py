class StandardResponseMiddleware:
    def process_response(self, req, resp, resource, req_succeeded):
        if req_succeeded:
            context = resp.context

            result = context.get('result')
            results = context.get('results')

            if result and results:
                raise ValueError('Unexpected result and results in response')

            message = context.get('message')
            status = context.get('status', 'success')
            media = {
                'message': message,
                'status': status,
            }

            if result:
                media['result'] = result
            elif results:
                media['results'] = results

            resp.media = media
