from django.shortcuts import render

from django.http import HttpResponse
from .models import Question, Answer, Algoset, Comment
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import QuestionForm, AnswerForm, CommentForm, AlgoForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def base(request):
    """홈 화면 출력"""
    return render(request, 'index.html')

def Question_index(request):
    """
    질문 목록 출력
    """
    page = request.GET.get('page', '1')

    question_list = Question.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj}
    return render(request, 'alit/question_list.html', context)

def Question_detail(request, question_id):
    """
    질문 내용 출력
    """
    question = get_object_or_404(Question, id=question_id)
    context = {"question": question}
    return render(request, 'alit/question_detail.html', context)

# '애너테이션' 이라고 함
# @login_required 애너테이션을 통해 로그인이 되었는지를 우선 검사함
@login_required(login_url='common:login')
def answer_create(request, question_id):
    """ alit 답변등록"""
    question = get_object_or_404(Question, id=question_id)
    
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('alit:questiondetail', question_id = question.id)
    else:
        form = AnswerForm()
    context = {'question' : question, 'form' : form}
    return render(request, 'alit/question_detail.html', context)

@login_required(login_url='common:login')
def question_create(request):
    """ alit 질문등록"""
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.create_date = timezone.now()
            question.save()
            return redirect('alit:questionlist')
    else:
        form = QuestionForm()

    context = {'form' : form}
    return render(request, 'alit/question_form.html', context)

def Algoindex(request):
    page = request.GET.get('page', '1')

    algo_list = Algoset.objects.order_by('-create_date')

    # 페이징처리
    paginator = Paginator(algo_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'algo_list': page_obj}
    return render(request, 'alit/algo_list.html', context)

@login_required(login_url='common:login')
def algo_create(request):
    """ alit 질문등록"""
    if request.method == 'POST':
        form = AlgoForm(request.POST)
        if form.is_valid():
            algoset = form.save(commit=False)
            algoset.author = request.user
            algoset.create_date = timezone.now()
            algoset.save()
            return redirect('alit:algolist')
    else:
        form = AlgoForm()

    context = {'form' : form}
    return render(request, 'alit/algo_form.html', context)

def Algodetail(request, algo_id):
    """
    algo 내용 출력
    """
    algo = get_object_or_404(Algoset, id=algo_id)
    context = {"algo": algo}
    return render(request, 'alit/algo_detail.html', context)

@login_required(login_url='common:login')
def comment_create(request, algo_id):
    """ alit 답변등록"""
    algo = get_object_or_404(Algoset, id=algo_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.algoset = algo
            comment.save()
            return redirect('alit:algodetail', algo_id=algo.id)
    else:
        form = CommentForm()
    context = {'algo' : algo, 'form' : form}
    return render(request, 'alit/algo_detail.html', context)