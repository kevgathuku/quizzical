from django.urls import path

from . import views

app_name = 'quizzes'
urlpatterns = [
  # ex: /quizzes/
    path('', views.index, name='index'),
    # ex: /quizzes/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /quizzes/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /quizzes/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
