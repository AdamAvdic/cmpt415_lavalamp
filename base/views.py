from django.shortcuts import render
from .models import HuggingFaceRefineWeb

# Example static rooms data for demonstration
rooms = [
    {'id': 1, 'name': 'ChatGPT-3'},
    {'id': 2, 'name': 'LLaMa'},
    {'id': 3, 'name': 'RoBERTA'},
]

def home(request):
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request, pk):
    room = next((r for r in rooms if r['id'] == int(pk)), None)
    contents = HuggingFaceRefineWeb.objects.all()
    context = {
        'room': room,
        'contents': contents
    }
    return render(request, 'base/room.html', context)