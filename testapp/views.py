from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
class IndexView(View):
    def get(self, request):
        response = HttpResponse(f"<h1>Yo. Method: Get.</h1>\n")
        response.write(f"<form action='/Jonas'>\n")
        response.write(f"<input type='text' name='dude' value='Jonas' />\n")
        response.write(f"<input type='submit' name='submit' value='Submit' />\n")
        response.write(f"</form>\n")
        return response

class DudeView(View):
    def get(self, request, dude):
        return HttpResponse(f"<h1>Dude: {dude} Method: Get.</h1>")
    def get(self, request, dude):
        return HttpResponse(f"<h1>Dude: {dude} Method: Post.</h1>")
