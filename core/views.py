from django.shortcuts import render, get_object_or_404
from .models import Project, Blog


def home(request):
    projects = Project.objects.all()[:3]
    blogs = Blog.objects.all()[:3]

    return render(request, 'core/home.html', {
        'projects': projects,
        'blogs': blogs
    })


def about(request):
    return render(request, 'core/about.html')


def projects(request):
    return render(request, 'core/projects.html', {
        'projects': Project.objects.all()
    })


def blogs(request):
    return render(request, 'core/blogs.html', {
        'blogs': Blog.objects.all().order_by('-created_at')
    })


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    return render(request, 'core/blog_detail.html', {
        'blog': blog
    })



from django.http import HttpResponse

def robots_txt(request):
    lines = [
        "User-agent: *",
        "Allow: /",
        "Sitemap: https://whoistordi.pythonanywhere.com/sitemap.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")


def profile(request):
    return render(request, 'core/profile.html')