from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.views.generic import UpdateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from urllib.parse import quote_plus


# CRUD

def is_staff_superuser(request):
    return request.user.is_superuser and request.user.is_staff


# Create your views here.
def post_create(request):
    
    if not is_staff_superuser(request):
        raise Http404
    if request.POST:
        form_data = PostForm(request.POST, request.FILES)
        if form_data.is_valid():
            # this is the way to save and add the name info 
            instance = form_data.save(commit=False)
            instance.author = request.user
            form_data.save()
            return redirect('post:list')
        else:
            messages.error(request, "Failed to save the data")
            return render(request, template_name="posts/create.html", context={'form': form_data})

    else:
        form = PostForm()
        return render(request, template_name="posts/create.html", context={'form': form})


# retrieve
def post_list(request):
    queryset_list = Post.objects.all().order_by('-timestamp')
    paginator = Paginator(queryset_list,5)

    # For pagination :
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)


    context_data = {
        'title': "List",
        'object_list': queryset
    }
    return render(request, template_name='posts/index.html', context=context_data)


def post_detail(request, slug):
    if not is_staff_superuser(request):
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    context_data = {
        'title': "Detail",
        'instance': instance,
        # it is handled by templatetags
        # 'url_encoded_content': quote_plus(instance.content)
    }
    return render(request, template_name='posts/detail.html', context=context_data)


def post_update(request, slug):
    if not is_staff_superuser(request):
        raise Http404
    # here the instance is very imporant
    instance = get_object_or_404(Post, slug=slug)
    if request.POST:
        form_data = PostForm(request.POST, request.FILES, instance=instance)
        if form_data.is_valid():
            form_data.save()
            messages.success(request, "Successfully saved")
            return redirect('post:detail', slug=slug)
        else:
            messages.error(request, "Failed to save the data")
            return render(request, template_name="posts/update.html", context={'form': form_data})

    else:
        form = PostForm(instance=instance)
        return render(request, template_name="posts/update.html", context={'form': form})

def post_delete(request, slug):
    if not is_staff_superuser(request):
        raise Http404
    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "Successfully deleted !!!")
    return redirect('post:list')

# class PostUpdate()


# class PostUpdate(UpdateView):
#     model = Post
#     template_name = "update.html"

