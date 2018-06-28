from django.shortcuts import render
from .models import Note, PersonalNote

# Create your views here.

def index(request):
    context = {
        'notes': Note.objects.all(),
    }
    if request.user.is_anonymous:
        context['personal_notes'] = PersonalNote.objects.none()
    else:
        context['personal_notes'] = PersonalNote.objects.filter(user=request.user)

        

    return render(request, 'notes/index.html', context)