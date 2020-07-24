from django.shortcuts import render

from datetime import datetime

def index(request):
    now = datetime.today()
    return render(request, 'monday/index.html', {
        "monday": now.weekday() == 0
    })
