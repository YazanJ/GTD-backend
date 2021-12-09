from rest_framework import serializers
from .models import Action, Project, Tag

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = "__all__"

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
