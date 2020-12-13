from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def main_view(request):
    user = 'test'

    context = {
        'user': user
    }

    return render(request, 'mainApp/main.html')
