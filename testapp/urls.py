from django.urls import path
from .import views
app_name = "testapp"
urlpatterns = [
	path('', views.MainPageView.as_view(), name='main_page')
]