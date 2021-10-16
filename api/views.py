from django.db.models import query
from .models import User, Event, School, Keyword
from .serializers import UpdateUserSerializer, UserSerializer, CreateUserSerializer, EventSerializer, SchoolSerializer, KeywordSerializer

from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.conf import settings


class UserView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CreateUserView(APIView):
    serializer_class = CreateUserSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            first_name = serializer.data.get('first_name')
            last_name = serializer.data.get('last_name')
            phone = serializer.data.get('phone')
            school = serializer.data.get('school')
            city_of_origin = serializer.data.get('city_of_origin')
            current_city = serializer.data.get('current_city')
            email = serializer.data.get('email')

            user = User(first_name=first_name, last_name=last_name, phone=phone, school=school,
                        city_of_origin=city_of_origin, current_city=current_city, email=email)
            user.save()

            send_email_from_app(serializer.data.get(
            'email'), serializer.data.get('first_name'))

            return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

        print(serializer.errors)
        return Response({'Bad Request': 'Invalid data...'}, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserView(APIView):
        serializer_class = UpdateUserSerializer

        def patch(self, request, format=None):
            serializer = self.serializer_class(data = request.data)
            if serializer.is_valid():
                first_name = serializer.data.get('first_name')
                last_name = serializer.data.get('last_name')
                phone = serializer.data.get('phone')
                school = serializer.data.get('school')
                city_of_origin = serializer.data.get('city_of_origin')
                current_city = serializer.data.get('current_city')
                email = serializer.data.get('email')

                queryset = User.objects.filter(email=email)
                if not queryset.exists():
                    return Response({'msg': 'Email not found.'}, status=status.HTTP_404_NOT_FOUND)

                user = queryset[0]

                user.first_name = first_name
                user.last_name = last_name
                user.phone = phone
                user.school = school
                user.city_of_origin = city_of_origin
                user.current_city = current_city
                user.email = email

                user.save(update_fields=['first_name', 'last_name', 'phone', 'school',
                      'city_of_origin', 'current_city', 'email'])
                send_email_from_app(serializer.data.get(
            'email'), serializer.data.get('first_name'))

                return Response(UserSerializer(user).data, status=status.HTTP_200_OK)
            
            print(serializer.errors)
            return Response({'Bad request': "Invalid data..."}, status=status.HTTP_400_BAD_REQUEST)

class EventsView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    
# for the test only


def send_email_from_app(recEmail, recName):
    html_tpl_path = 'email_templates/index.html'
    context_data = {'name': recName}
    email_html_template = get_template(html_tpl_path).render(context_data)
    receiver_email = recEmail
    email_msg = EmailMessage('Obtain Your Badge',
                             email_html_template,
                             settings. APPLICATION_EMAIL,
                             [receiver_email],
                             reply_to=[settings.APPLICATION_EMAIL]
                             )
    # this is the crucial part that sends email as html content but not as a plain text
    email_msg.content_subtype = 'html'
    email_msg.send(fail_silently=False)