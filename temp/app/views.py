from django.shortcuts import render

# Create your views here.
def home(request):
    content = {'t':'I\'m the winner','n':1}
    return render(request,"app/home.html",content)

def extension(request):
    return render(request,"app/extension.html")

def relate(request):
    return render(request,"app/relate.html")