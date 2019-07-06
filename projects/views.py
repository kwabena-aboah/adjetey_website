from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect

from . models import Project, Contact
from . forms import ContactForm

def index(request):
    projects = Project.objects.order_by('-title')[0:4]
    context = {'projects':projects}
    return render(request, 'projects/index.html', context)

def project_index(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'projects/project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    projects = Project.objects.order_by('-title')[0:4]
    context = {'project':project, 'projects':projects}
    return render(request, 'projects/project_detail.html', context)

def about(request):
    projects = Project.objects.order_by('-title')[0:4]
    context = {'projects':projects}
    return render(request, 'projects/about.html', context)

def contact(request):
    if request.method != 'POST':
        forms = ContactForm()
    else:
        forms = ContactForm(request.POST)
        if forms.is_valid():
            new_link = forms.save(commit=False)
            new_link.save()
            messages.info(request, "Message Sent")
            return HttpResponseRedirect(reverse('contact'))
    context = {'forms': forms}
    return render(request, 'projects/contact.html', context)
