from django.shortcuts import render


# Create your views here.
def index(request):
    """
    returns the home page of the blog.
    """
    template = 'blog/index.html'
    context = {}

    return render(request, template, context)
