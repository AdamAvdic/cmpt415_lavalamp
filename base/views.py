from django.shortcuts import render

rooms = [
    {'id':1, 'name':'prompt 1'},
    {'id':2, 'name':'prompt 2'},
    {'id':3, 'name':'prompt 3'},
]

# Create your views here.
def home(request):
    return render(request, 'base/home.html', {'rooms':rooms})
def room(request,pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room' : room}
    return render(request, 'base/room.html',context)