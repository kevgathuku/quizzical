from rest_framework import serializers

from .models import Quiz


class QuizSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Quiz
        fields = ('url', 'description', 'pub_date', 'was_published_recently',)

