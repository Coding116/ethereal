from django.shortcuts import render

# Create your views here.
def home(request):
    welcome = "Hello, Welcome to Horla's Fashion"
    return render(request, "index.html", {"welcome":welcome})