from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def blog(request):
    return render(request, 'blog.html')
def courses(request):
    return render(request, 'courses.html')
def instructors(request):
    return render(request, 'instructors.html')
def pricing(request):
    return render(request, 'pricing.html')


