from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework.decorators import APIView
from django.contrib.auth.models import User
from .models import Action
from .serializers import ActionSerializer


class ActionList(APIView):
    # def get(self, request):
    #     if request.user.is_authenticated:
    #         actions = Action.objects.filter(user=request.user)
    #         serializer = ActionSerializer(actions, many=True)
    #         return Response(serializer.data)
    #     else:
    #         return Response('You must be logged in to do that')
    def get(self, request):
        actions = Action.objects.all()
        serializer = ActionSerializer(actions, many=True)
        return Response(serializer.data)

