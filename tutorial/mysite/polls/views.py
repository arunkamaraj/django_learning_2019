from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView, DetailView, TemplateView
from django.core.files.storage import FileSystemStorage
from . import models
from .forms import bookform


def index(request):
    latest_five = models.Question.objects.order_by('publication_date')[:5]
    return render(request, 'polls/index.html', context={'latest_five': latest_five})


def detail(request, quest_id):
    detail_result = get_object_or_404(models.Question, pk=quest_id)
    return render(request, 'polls/detail.html', context={'result': detail_result})


def result(request, quest_id):
    result_obj = models.Question.objects.get(pk=quest_id)
    return render(request, 'polls/result.html', context={'result': result_obj})


def vote(request, quest_id):
    question_obj = models.Question.objects.get(pk=quest_id)

    try:
        choice_obj = question_obj.choice_set.get(pk=request.POST['choice'])
    except KeyError:
        return render(request, 'polls/detail.html',
                      context={'result': question_obj, 'error_message': 'None of the choice is selected'})

    choice_obj.votes += 1
    choice_obj.save()

    return HttpResponseRedirect(reverse('polls:result', args=(quest_id,)))


def upload_file(request):
    context = {}
    if request.method == "POST":
        file = request.FILES['document']

        fs = FileSystemStorage()
        name = fs.save(file.name, file)# if the user uploade the same file name then it will be useful
        context['url'] = fs.url(name)

    return render(request, 'polls/upload.html', context)

def book_list(request):
    request.session['name'] = 'arun'
    result = models.book.objects.all()
    # result = models.book.arun.all()
    return render(request, 'polls/book_list.html', {'result': result})

def book_upload(request):
    if request.method == 'POST':
        my_form = bookform(request.POST, request.FILES)
        if my_form.is_valid():
            my_form.save()
            return redirect(reverse('polls:booklist', args=()))
    else:
        my_form = bookform()
    return render(request, 'polls/book_upload.html', {'form': my_form})

def book_delete(request, pk):
    # return HttpResponse(status=200)
    book_obj = models.book.objects.get(pk=pk)
    book_obj.delete()

    # return redirect(reverse('polls:booklist', args=()))
    # return redirect('polls:booklist')
    return  redirect(book_obj)

class IndexView(ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_five'

    def get_queryset(self):
        return models.Question.objects.order_by('publication_date')[:5]


class DetailPageView(DetailView):
    model = models.Question
    template_name = 'polls/detail.html'
    context_object_name = 'result'


class ResultView(DetailView):
    model = models.Question
    template_name = 'polls/result.html'
    context_object_name = 'result'


class AboutView(TemplateView):
    template_name = 'summa'
