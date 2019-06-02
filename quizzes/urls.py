from django.urls import path

from . import views

app_name = 'quizzes'
urlpatterns = [
  # ex: /quizzes/
    path('', views.IndexView.as_view(), name='index'),
    # ex: /quizzes/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /quizzes/5/results/
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /quizzes/5/vote/
    path('<int:quiz_id>/submit/', views.process_answers, name='process_answers'),
]
