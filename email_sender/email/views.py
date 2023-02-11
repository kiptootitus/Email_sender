from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class EmailSenderView(APIView):
    def post(self, request):
        subject = request.data.get('subject')
        message = request.data.get('message')
        from_email = request.data.get('from_email')
        recipient_list = request.data.get('recipient_list')

        if subject and message and from_email and recipient_list:
            try:
                send_mail(subject, message, from_email, recipient_list)
                return Response({"message": "Email sent successfully"}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({"message": "Failed to send email. Error: {}".format(str(e))}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "All fields are required to send email"}, status=status.HTTP_400_BAD_REQUEST)
