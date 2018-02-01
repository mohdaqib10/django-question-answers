from django.db import models
from django.utils.translation import ugettext_lazy as _


class Question(models.Model):
    """
    Create Question model
    """
    publish_date = models.DateTimeField(_('Published Date'), auto_now_add=True)
    question_text = models.CharField(_('Question'), max_length=256)
    updated_date = models.DateTimeField(_('Updated Date'), null=True, blank=True)

    def __str__(self):
        return '{0}'.format(self.question_text)

    class Meta:
        verbose_name_plural = 'Questions'
        ordering = ['-publish_date']


class Answer(models.Model):
    """
    Answer model for the question
    """
    question = models.ForeignKey(Question, related_name='questions', on_delete=models.CASCADE)
    answer_text = models.CharField(_('Answer'), max_length=1024)
    ans_date = models.DateTimeField(_('Answer Date'), auto_now_add=True)
    updated_date = models.DateTimeField(_('Updated Date'), null=True, blank=True)

    def __str__(self):
        return '{0}'.format(self.answer_text)

    class Meta:
        verbose_name_plural = 'Answers'
        ordering = ['-ans_date']


class LikeDislike(models.Model):
    """
    Like and Dislike model
    """
    created = models.DateTimeField(_('Created Date'), auto_now_add=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
    like = models.PositiveIntegerField(null=True, blank=True)
    dislike = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return 'Likes: {0} & Dislikes: {1}'.format(self.like, self.dislike)

    class Meta:
        verbose_name_plural = 'Likes & Dislikes'
        ordering = ['-like']
