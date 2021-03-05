from django.urls import path

from . import views

app_name = "alit"

urlpatterns = [
    path('', views.base, name='base'),
    
    path('questionlist/', views.Question_index, name='questionlist'),
    path('<int:question_id>/', views.Question_detail, name='questiondetail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),

    path('algolist/', views.Algoindex, name='algolist'),
    path('algo/<int:algo_id>/', views.Algodetail, name='algodetail'),
    path('algo/create/', views.algo_create, name='algo_create'),
    path('comment/create/algo/<int:algo_id>/', views.comment_create, name='comment_create'),

]
