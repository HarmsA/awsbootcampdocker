from django.shortcuts import render
# from .models import Topic, Question
from .forms import QNAForm, TagSearch
from django.contrib.auth.decorators import login_required

def index(request):
    print('In search_tag')
    tag_form = TagSearch()
    return render(request, 'guides/base.html', locals())

def search_tag(request):
    
    if request.method == 'POST':
        print('In search_tag')
        tag_form = TagSearch(request.POST)
        if tag_form.is_valid():
            tag = tag_form.cleaned_data["tag"]
            print(tag)
            # questions = Question.objects.filter(search_terms__contains=tag)
            print("questions: ", questions)
            tag_form = TagSearch()
            return render(request, 'guides/topic.html', locals())
    return render(request, 'guides/topic.html', locals())

def topic(request, topic):
    if request.method == 'POST':
        tag_form = TagSearch(request.POST)
        if tag_form.is_valid():
            tag = tag_form.cleaned_data["tag"]
            # questions = Question.objects.filter(question__contains=tag)
            tag_form = TagSearch()
            return render(request, 'guides/topic.html', locals())
        
    tag_form = TagSearch()
    # questions = Question.objects.filter(topic__name=topic)
    return render(request, 'guides/topic.html', locals())

def create_question(request):
    if request.user.is_authenticated:
        new_question = Question.objects.create(user=request.user, text='Your question text here')
    pass

# @login_required
def qna(request):
    error = None
    if request.method == 'POST':
        form = QNAForm(request.POST)
        if form.is_valid():
            form_topics=form.cleaned_data['topic']
            # new_question = Question(user=request.user,
            #                         question=form.cleaned_data['question'],
            #                         answer=form.cleaned_data['answer'],
            #                         search_terms=form.cleaned_data['search_terms']
            #                         )
            # new_question.save()
            # new_question.user = request.user
            # new_question.topic.set(form_topics)
            error = "Question Saved"
    form = QNAForm()
    print(form)
    return render(request, 'guides/add_question.html', locals())
