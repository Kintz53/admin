from django.shortcuts import render
from .models import Game
def admin2(request):
    jeux = Game.objects.all()
    context={}
    context['jeux']=Game.objects.all()
    return render(request,'admin.html',context)
# Create your views here.
