from django.contrib import admin

# Register your models here.
from .models import Answer, Quiz, Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ("question_text",)
    search_fields = ["question_text"]


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("choice_text", "votes")
    list_filter = ["question"]
    search_fields = ["choice_text"]


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("question", "correct_choice")

class QuizAdmin(admin.ModelAdmin):
    list_display = ("description", "pub_date", "was_published_recently")
    inlines = [QuestionInline]
    list_filter = ["pub_date"]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Answer, AnswerAdmin)
