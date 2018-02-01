from django.contrib import admin
from .models import Question, Answer, LikeDislike


class QuestionAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'question_text', 'publish_date', 'updated_date'
    )


class AnswerAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'answer_text', 'question', 'ans_date', 'updated_date'
    )


class LikeDislikeAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'like', 'dislike', 'question', 'answer', 'created'
    )

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(LikeDislike, LikeDislikeAdmin)
