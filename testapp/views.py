from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
class IndexView(View):
    def get(self, request):
        return HttpResponse(f"<h1>Yo.</h1>")

class DudeView(View):
    def get(self, request, dude):
        return HttpResponse(f"<h1>Dude.</h1>")
