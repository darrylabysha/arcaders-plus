from django.shortcuts import render

# Create your views here.

def show_main(request):
    context = {
        'name': 'Darryl Abysha',
        'class': 'PBP E',
        'NPM': '2206082846'
    }

    return render(request, "main.html", context)