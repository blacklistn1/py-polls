from django.urls import path

from mail.views import SendMailView

urlpatterns = [
    path('send-mail/', SendMailView.as_view(), name='send_mail')
]
