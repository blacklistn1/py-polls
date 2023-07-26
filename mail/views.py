from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from mail.serializers import SendMailSerializer


class SendMailView(APIView):
    """Handle sending emails"""

    @staticmethod
    def get(request):
        return Response({'message': 'Send mail apis'})

    @staticmethod
    def post(request):
        serializer = SendMailSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={
                    'message': 'request is not valid',
                    'errors': serializer.errors,
                }
            )

        # print(serializer.validated_data)
        # return Response({'validated': serializer.data}, status=status.HTTP_201_CREATED)
        delivered = send_mail(
            subject='Subject of the email',
            message=serializer.data.get('body'),
            from_email='from@example.com',
            recipient_list=serializer.data.get('recipients')
        )
        return Response(status=status.HTTP_200_OK, data={'delivered_emails': delivered})
