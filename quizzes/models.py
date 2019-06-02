import datetime
from django.db import models
from django.utils import timezone


class Quiz(models.Model):
    description = models.CharField(max_length=500)
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
        now = timezone.now()
        # The pub_date should be between now and 1 day ago
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.description


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    quiz = models.ForeignKey(Quiz, models.SET_NULL, blank=True, null=True)

    def was_published_recently(self):
        now = timezone.now()
        # The pub_date should be between now and 1 day ago
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct_choice = models.ForeignKey(Choice, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(
            self.question.question_text, self.correct_choice.choice_text
        )
