import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question, Quiz


def create_quiz(description, days):
    """
    Create a quiz with the given `description` and published the
    given number of `days` offset to now (negative for quizzes published
    in the past, positive for quizzes that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Quiz.objects.create(description=description, pub_date=time)


class QuizModelTests(TestCase):
    def test_was_published_recently_with_future_quiz(self):
        """
        was_published_recently() returns False for quizzes whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_quiz = Quiz(pub_date=time)
        self.assertIs(future_quiz.was_published_recently(), False)

    def test_was_published_recently_with_old_quiz(self):
        """
        was_published_recently() returns False for quizzes whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_quiz = Quiz(pub_date=time)
        self.assertIs(old_quiz.was_published_recently(), False)

    def test_was_published_recently_with_recent_quiz(self):
        """
        was_published_recently() returns True for quizzes whose pub_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_quiz = Quiz(pub_date=time)
        self.assertIs(recent_quiz.was_published_recently(), True)


class QuizIndexViewTests(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse("quizzes:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No quizzes are available.")
        self.assertQuerysetEqual(response.context["latest_quiz_list"], [])

    def test_past_quiz(self):
        """
        Questions with a pub_date in the past are displayed on the
        index page.
        """
        create_quiz(description="Past question.", days=-30)
        response = self.client.get(reverse("quizzes:index"))
        self.assertQuerysetEqual(
            response.context["latest_quiz_list"], ["<Quiz: Past question.>"]
        )

    def test_future_question(self):
        """
        Questions with a pub_date in the future aren't displayed on
        the index page.
        """
        create_quiz(description="Future question.", days=30)
        response = self.client.get(reverse("quizzes:index"))
        self.assertContains(response, "No quizzes are available.")
        self.assertQuerysetEqual(response.context["latest_quiz_list"], [])

    def test_future_question_and_past_quiz(self):
        """
        Even if both past and future quizzes exist, only past questions
        are displayed.
        """
        create_quiz(description="Past question.", days=-30)
        create_quiz(description="Future question.", days=30)
        response = self.client.get(reverse("quizzes:index"))
        self.assertQuerysetEqual(
            response.context["latest_quiz_list"], ["<Quiz: Past question.>"]
        )

    def test_two_past_questions(self):
        """
        The questions index page may display multiple questions.
        """
        create_quiz(description="Past question 1.", days=-30)
        create_quiz(description="Past question 2.", days=-5)
        response = self.client.get(reverse("quizzes:index"))
        self.assertQuerysetEqual(
            response.context["latest_quiz_list"],
            ["<Quiz: Past question 2.>", "<Quiz: Past question 1.>"],
        )


class QuestionDetailViewTests(TestCase):
    def test_future_question(self):
        """
        The detail view of a question with a pub_date in the future
        returns a 404 not found.
        """
        future_question = create_quiz(description="Future question.", days=5)
        url = reverse("quizzes:detail", args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        The detail view of a question with a pub_date in the past
        displays the question's text.
        """
        past_question = create_quiz(description="Past Question.", days=-5)
        url = reverse("quizzes:detail", args=(past_question.id,))
        response = self.client.get(url)
        self.assertContains(response, past_question.description)
