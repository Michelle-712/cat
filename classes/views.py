from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def blog(request):
    return render(request, 'blog.html')
def blog_details(request):
    return render(request, 'blog_details.html')
def courses(request):
    return render(request, 'courses.html')
def course_details(request):
    return render(request, 'course_details.html')
def events(request):
    return render(request, 'events.html')
def enroll(request):
    return render(request, 'enroll.html')
def instructors(request):
    return render(request, 'instructors.html')
def instructor_profile(request):
    return render(request, 'instructor_profile.html')
def pricing(request):
    return render(request, 'pricing.html')
def privacy(request):
    return render(request, 'privacy.html')
def terms(request):
    return render(request, 'terms.html')
def starter_page(request):
    return render(request, 'starter_page.html')


