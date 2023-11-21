from django.shortcuts import render
from .models import Praise

def praise_list(request):
    praises = Praise.objects.all()
    return render(request, 'index.html', {'praises': praises})