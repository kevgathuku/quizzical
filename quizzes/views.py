from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views import generic

from .models import Answer, Choice, Question, Quiz


class IndexView(generic.ListView):
    template_name = "quizzes/index.html"
    context_object_name = "latest_quiz_list"

    def get_queryset(self):
        """
        Return the last five published quizzes (not including those set to be
        published in the future).
        """
        return Quiz.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[
            :5
        ]


class DetailView(generic.DetailView):
    model = Quiz
    template_name = "quizzes/detail.html"

    def get_queryset(self):
        """
        Excludes any quizzes that aren't published yet.
        """
        return Quiz.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Quiz
    template_name = "quizzes/results.html"


def process_answers(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = quiz.question_set.all()
    answers = {}

    try:
        for question in questions:
            selected_answer = request.POST["choice_{}".format(question.id)]
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the quiz form.
        return render(
            request,
            "quizzes/detail.html",
            {"quiz": quiz, "error_message": "You didn't answer all the questions"},
        )
    else:
        for question in questions:
            correct_answer = (
                "Correct"
                if Answer.objects.get(question=question).correct_choice.pk
                == int(request.POST["choice_{}".format(question.id)])
                else "Wrong"
            )
            answers[question] = correct_answer
        return render(
            request, "quizzes/results.html", {"quiz": quiz, "answers": answers}
        )
