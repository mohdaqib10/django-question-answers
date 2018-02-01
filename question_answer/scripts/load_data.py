import random
from faker import Faker
from que_ans_app.models import Question, Answer, LikeDislike
from faker.providers import BaseProvider
fake = Faker()


class MyFakeProvider(BaseProvider):
    """
    Custom provider to generate data
    """
    que_choices = [
        'What is Information Technology?', 'What is Django?',
        'What is the importance of data structure to create an application?'
    ]

    def que_text(self):
        return random.choice(self.que_choices)

fake.add_provider(MyFakeProvider)


def load_questions(num):
    """
    Dump some fake question in the database
    :param num:
    :return:
    """
    for i in range(num):
        data = dict()
        data['question_text'] = fake.que_text()
        data['updated_date'] = fake.date()
        que_obj = Question.objects.create(**data)
        print('Question Created: ', que_obj)


def load_answers(num):
    """
    Dump some fake answers in the database
    :param num:
    :return:
    """
    que = Question.objects.all()

    for i in range(num):
        data = dict()
        data['answer_text'] = fake.text()
        data['question'] = random.choice(que)
        data['updated_date'] = fake.date()
        ans_obj = Answer.objects.create(**data)
        print('Answers Created: ', ans_obj)


def load_like_n_dislikes(num):
    """

    :param num:
    :return:
    """
    que = Question.objects.all()
    ans = Answer.objects.all()

    for i in range(num):
        data = dict()
        data['question'] = random.choice(que)
        data['answer'] = random.choice(ans)
        data['like'] = random.randint(10, 100)
        data['dislike'] = random.randint(10, 100)
        like_obj = LikeDislike.objects.create(**data)
        print('Like & Dislike Created: ', like_obj)


def run():
    """
    run methods
    :return:
    """
    load_questions(10)
    load_answers(10)
    load_like_n_dislikes(10)
