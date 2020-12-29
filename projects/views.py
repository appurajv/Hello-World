from django.shortcuts import render
from projects.models import Project
from django.views.generic import TemplateView

# Create your views here.
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'projects/all_projects.html', {'projects': projects})


class About(TemplateView):
    template_name = 'about.html'
