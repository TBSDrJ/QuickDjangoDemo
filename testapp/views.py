from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, 'testapp/index.html', {})

class DudeView(View):
    def get(self, request, dude):
        return HttpResponse(f"<h1>Dude: {dude} Method: Get.</h1>")
    def post(self, request, dude):
        return HttpResponse(f"<h1>Dude: {dude} Method: Post.</h1>")
