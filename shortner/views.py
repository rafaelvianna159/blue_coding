from django.http import HttpResponse
from django.shortcuts import redirect
import random
import string
from .models import ShortUrl
import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def short_main_api(request, short_url, length=1):  # TODO make avoid duplicates in db
    if request.method == 'POST':
        request_to_parse = requests.get(f"https://{request.POST['full_url']}")  # may need header
        soup = BeautifulSoup(request_to_parse.content, 'html.parser')
        id = get_random_string(length)
        if ShortUrl.objects.filter(url_id=id):
            short_main_api(request, length + 1)
        else:
            entity = ShortUrl(url_id=id, full_url=request.POST['full_url'], title=soup.find('title').text)
            entity.save()
            return HttpResponse(f'localhost:8000/short/{entity.url_id}')
    if request.method == 'GET':
        object = ShortUrl.objects.get(url_id=short_url)
        return redirect(f"https://{object.full_url}")


def get_random_string(length):
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str
