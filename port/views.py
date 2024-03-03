from django.shortcuts import render

# Create your views here.


def Index(request):
    #data = HomeFields.objects.all()
    return render(request, 'index.html')
