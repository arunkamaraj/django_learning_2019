from django.conf import settings
import requests

class StackOverflowMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)

    def process_exception(self, request, exception):
        if settings.DEBUG:
            error = '{}: {}'.format(exception.__class__.__name__, exception)
            print(error)

            url = 'https://api.stackexchange.com/2.2/search'
            headers = { 'User-Agent': 'github.com/vitorfs/seot' }
            params = {
                'order': 'desc',
                'sort': 'votes',
                'site': 'stackoverflow',
                'pagesize': 3,
                'tagged': 'python;django',
                'intitle': error
            }

            r = requests.get(url=url, params=params, headers=headers)
            questions = r.json()

            print('')

            for question in questions['items']:
                print(question['title'])
                print(question['link'])
                print('')

        return None