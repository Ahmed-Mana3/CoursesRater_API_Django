from django.shortcuts import render
from .models import Rate, Course, Channel
from .serializers import RateSerializer, ChannelSerializer, CourseSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import permissions
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAdminUser]


class RateViewSet(viewsets.ModelViewSet):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]

    def update(self, request, *args, **kwargs):
         json = {
              'message':'This is not how you should update the rate',
         }
         return Response(json, status=status.HTTP_400_BAD_REQUEST)
    
    def create(self, request, *args, **kwargs):
         json = {
              'message':'This is not how you should create the rate',
         }
         return Response(json, status=status.HTTP_400_BAD_REQUEST)


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    """
    Extra actions in viewset views
    """
    # detail=True --> you will work on an exact course, so --> domain/courses/(pk)/action_func_name
    @action(detail=True, methods=['POST'])
    def rate_course(self, request, pk=None):
        user = request.user
        course = Course.objects.get(pk=pk)
        stars = request.data['stars']
        comment = request.data['comment']
        if not request.user or not request.user.is_authenticated:
            return Response({'detail': 'Authentication credentials were not provided.'}, status=status.HTTP_401_UNAUTHORIZED)
        if 'stars' in request.data:
            # update
            try:
                rate = Rate.objects.get(user=user, course=course)
                rate.stars = stars
                rate.comment = comment
                rate.save()
                serializer = RateSerializer(rate)
                json = {
                    'message':'The Rate Was Updated',
                    'result': serializer.data
                }
                return Response(json, status=status.HTTP_202_ACCEPTED) 
            except Rate.DoesNotExist:
                rate = Rate.objects.create(user=user, course=course, stars=stars, comment=comment)
                serializer = RateSerializer(rate)
                json = {
                    'message':'New Rate Was Created',
                    'result': serializer.data
                }
                return Response(json, status=status.HTTP_201_CREATED)
        else:
                return Response(status=status.HTTP_400_BAD_REQUEST)


class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all()
    serializer_class = ChannelSerializer


