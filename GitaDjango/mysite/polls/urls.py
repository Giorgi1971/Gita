from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views.QuestionListView.as_view(), name='question_list'),

    # ex: /polls/5/
    path('<int:pk>/', views.QuestionDetailView.as_view(), name='detail'),
    # ex: /polls/5/results/
    path('<int:pk>/results/', views.QuestionResultView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:pk>/vote/', views.vote, name='vote'),
]