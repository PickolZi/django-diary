from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html", {})

def aboutMe(request):
    template_name = "about_me.html"
    return render(request, template_name, {})