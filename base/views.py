from django.shortcuts import render
from .models import ChatGPTResponse

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
    # Fetch the first 10 responses from the chatgpt_response table
    responses = ChatGPTResponse.objects.all()[:10]
    context = {
        'room': room,
        'responses': responses
    }
    return render(request, 'base/room.html', context)