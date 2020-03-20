from django.shortcuts import render
from .forms import BlogPostModelForm
from .models import BlogPost
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth  import get_user_model
from django.http import HttpResponse

# Create your views here.
def blog_home(request):
    title = "Blog | Home"
    template  = "apps/blog/blog_home.html"
    obj = BlogPost.objects.filter(user=request.user).order_by('-published_date')
    context = {"title": title, "obj": obj}
    return render(request, template, context)


def blog_list(request):
    title = "Blog | List"
    template = "apps/blog/blog_list.html"
    blog = BlogPost.objects.all()
    context = {"title": title, "blog": blog}
    return render(request, template, context)


def blog_create(request):
    title = "Blog | Create"
    if not request.user.is_authenticated:
        return HttpResponse("""You are not logged in
        . Please <a href="/login"> login </a> or go 
        <a href="javascript:history.back()"> back </a>""")
    form = BlogPostModelForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = BlogPostModelForm()
    template  = "apps/blog/blog_create.html"
    context = {"title": title, "form": form}
    return render(request, template, context)


def blog_render(request, slug):
    title = "Read Blog"
    userobj = get_user_model()
    blog  = get_object_or_404(BlogPost, slug=slug)
    template  = "apps/blog/blog_render.html"
    context =  {"title": title, "blog": blog}
    return render(request, template, context)

def blog_update(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    form = BlogPostModelForm(request.POST or None, instance=obj)
    template_name = "apps/blog/blog_create.html"
    if not request.user == obj.user:
        return HttpResponse(f""" You are {request.user} so you can't edit {obj.user}'s post
                            Click here to go <a href="javascript:history.back()"> Back </a>""")
    if form.is_valid():
        form.save()
    context = {"object": obj, "form": form}
    return render(request, template_name, context)

def blog_delete(request, slug):
    obj = get_object_or_404(BlogPost, slug=slug)
    template_name = 'apps/blog/blog_delete.html'
    if request.method == "POST":
        if not request.user == obj.user:
            return HttpResponse(f"""You are {request.user} so you cannot delete {obj.user}'s Post
            <a href="/blog/list"> Click here to go Back </a>
            """)
        obj.delete()
        return redirect("/blog/list")
    context = {"object": obj}
    return render(request, template_name, context)