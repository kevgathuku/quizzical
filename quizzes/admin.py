from django.contrib import admin

# Register your models here.
from .models import Answer, Quiz, Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ("question_text", "pub_date", "was_published_recently")
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("choice_text", "votes")
    list_filter = ["question"]
    search_fields = ["choice_text"]


class AnswerAdmin(admin.ModelAdmin):
    list_display = ("question", "correct_choice")


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
admin.site.register(Quiz)
admin.site.register(Answer, AnswerAdmin)
