import datetime

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from .models import Question


def create_question(question_text, days):
    """
    days can be negative, indicate the pub date will be in the past
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() return False for questions
        whose pub_date is in the future
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() return False for questions
        whose pub_date is far in the past
        """
        far_past = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_question = Question(pub_date=far_past)
        self.assertIs(old_question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() return True for questions
        whose pub_date is recent
        """
        recent_date = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=recent_date)
        self.assertIs(recent_question.was_published_recently(), True)


class QuestionIndexViewTest(TestCase):
    def test_no_questions(self):
        """
        If no questions exist, an appropriate message will be displayed.
        """
        response = self.client.get(reverse('polls:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No polls are available')
        self.assertQuerySetEqual(response.context['latest_questions'], [])

    def test_past_questions(self):
        """
        Question with a pub_date in the past is displayed on the index page
        """
        past_question = create_question(question_text='Past question', days=-30)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerySetEqual(
            response.context['latest_questions'],
            [past_question]
        )

    def test_future_question(self):
        """
        Future question are not displayed on the page
        """
        create_question('Future question', days=1)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerySetEqual(
            response.context['latest_questions'],
            []
        )

    def test_past_and_future_question(self):
        """
        Only past questions are displayed on the page, even though future questions are created
        """
        question = create_question('past question', days=-30)
        create_question('Future question', days=3)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerySetEqual(
            response.context['latest_questions'],
            [question]
        )

    def test_two_past_questions(self):
        """
        Past questions are displayed in the correct order of
        most recent publish date
        """
        q1 = create_question('Past 1', days=-20)
        q2 = create_question('Past 2', days=-5)
        response = self.client.get(reverse('polls:index'))
        self.assertQuerySetEqual(
            response.context['latest_questions'],
            [q2, q1]
        )


class QuestionDetailTest(TestCase):
    def test_future_question(self):
        """
        Accessing a future question should return a 404
        """
        future_question = create_question('Future', days=1)
        url = reverse('polls:detail', args=(future_question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_past_question(self):
        """
        Accessing a question with a pub date in the past should display the question text
        """
        question = create_question('Past', days=-4)
        url = reverse('polls:detail', args=(question.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, question.question_text)
