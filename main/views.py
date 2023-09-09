from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'app_name': "EURORA'S CLOSET",
        'name': 'Lidwina Eurora Firsta Nobella',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)