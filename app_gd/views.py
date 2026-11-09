from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.http.request import HttpRequest, HttpHeaders
import json


# Create your views here.
def index(request: HttpRequest):
    context = {"text": "This Is Main Page", "link": "first_page"}
    response = render(request, 'index.html', context=context)
    response.headers["World"] = "hello"
    response.status_code = 200
    return response

def first_page(request: HttpRequest):
    context = {
               "text": "Это первая страница",
               "link": "second_page",
               "link_home": "/"
    }
    return render(request, 'index.html', context)

def second_page(request: HttpRequest):
    context = {
                "text": "Это вторая страница",
                "link": "first_page",
                "link_home": "/"
    }
    return render(request, 'index.html', context)

# curl -X POST --data '{"request":"name"}'  http://127.0.0.1:8000/json_example
# {"req": "name", "name": "Adam"}
def json_example(request: HttpRequest):
    data = {}
    if request.method == "GET":
        data["result"] = "Hello World"
    elif request.method == "POST":
        req_body = dict(json.loads(request.body))
        if req_body["request"]:
            data["req"] = req_body["request"]
            data["name"] = "Adam"
    response = JsonResponse(data)
    response.status_code = 418
    return response


