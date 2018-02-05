from django.http import Http404
from django.utils import timezone
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status, exceptions
from . import models
from . import serializers


class QuestionList(views.APIView):
    """
    `get` and `create` Question
    """
    model = models.Question

    # List all questions.
    def get(self, request):
        queryset = self.model.objects.all()
        serializer = serializers.QuestionSerializer(queryset, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = serializers.QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetail(views.APIView):
    """
    Detail Views
    """
    model = models.Question

    @staticmethod
    def get_object(pk):
        try:
            return models.Question.objects.get(pk=pk)
        except:
            raise Http404
            # raise exceptions.ParseError({'error': 'Detail not found.'})

    def get(self, request, pk):
        queryset = self.get_object(pk)
        serializer = serializers.QuestionSerializer(queryset)
        return Response(serializer.data)

    def put(self, request, pk):
        quesryset = self.get_object(pk)
        serializer = serializers.QuestionSerializer(quesryset, data=request.data)
        if serializer.is_valid():
            serializer.validated_data['updated_date'] = timezone.now()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        queryset = self.get_object(pk)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
