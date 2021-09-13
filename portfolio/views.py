from django.shortcuts import render

from .models import Project


def index(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/index.html', {"projects": projects, "title": "Projects"})

def project_details(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, 'portfolio/project_details.html', {"project": project})
