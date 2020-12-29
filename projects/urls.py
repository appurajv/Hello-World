from django.urls import path
from projects import views
from projects.views import About
app_name = 'about'

urlpatterns = [
    path('', views.project_list),
    path('about', About.as_view(), name='about'),
]
