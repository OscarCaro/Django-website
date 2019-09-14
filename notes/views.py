from django.shortcuts import render

from notes.models import Note

def index(request):
    template = 'index.html'
    context = {
        'note_list': Note.objects.all()      
    }
    response = render(request, template, context)
    return response
