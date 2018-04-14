from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class MainPageView(TemplateView):
	template_name = "testapp/main_page.html"


def error_404(request):
        data = {}
        return render(request,'myapp/error_404.html', data)
 
def error_500(request):
        data = {}
        return render(request,'myapp/error_500.html', data)