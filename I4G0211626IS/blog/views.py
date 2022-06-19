from http.client import HTTPResponse
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HTTPResponse("Hello world")