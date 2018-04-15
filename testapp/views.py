from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class MainPageView(TemplateView):
	template_name = "testapp/main_page.html"


def error_404_view(request, exception):
    data = {"name": "ThePythonDjango.com"}
    return render(request,'testapp/error_404.html', data)
 