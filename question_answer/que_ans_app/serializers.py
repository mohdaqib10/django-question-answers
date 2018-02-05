from rest_framework.serializers import ModelSerializer, ValidationError
from . import models
from . import messages


class QuestionSerializer(ModelSerializer):
    """
    Serialize `Question` model
    """
    class Meta:
        model = models.Question
        exclude = ()

    def validate(self, data):
        que_len = len(data['question_text'])
        if que_len < 20:
            raise ValidationError({'error': messages.SHORT_QUE})
        if que_len > 256:
            raise ValidationError({'error': messages.Long_QUE})
        return data
