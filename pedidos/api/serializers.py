from rest_framework import serializers
from rest_framework.authtoken.models import Token
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('id',
                  'username',
                  'isTechnician')

class RequisitionSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')
    author = serializers.SlugRelatedField(many=False, read_only=True, slug_field='username')
    assignedTechnician = serializers.SlugRelatedField(many=False, read_only=True, slug_field='username')
    priority = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')
    affectedSystem = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')
    module = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')
    constancy = serializers.SlugRelatedField(many=False, read_only=True, slug_field='description')
    status = serializers.SlugRelatedField(many=False, read_only=True, slug_field='current')

    class Meta:
        model = models.Requisition
        fields = ('id',
                  'type',
                  'author',
                  'assignedTechnician',
                  'subject',
                  'details',
                  'priority',
                  'affectedSystem',
                  'module',
                  'date',
                  'attachedFile',
                  'constancy',
                  'status')

class RequisitionCommonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Requisition
        fields = ('id',
                  'type',
                  'author',
                  'assignedTechnician',
                  'subject',
                  'details',
                  'priority',
                  'affectedSystem',
                  'module',
                  'date',
                  'attachedFile',
                  'constancy',
                  'status')

class RequisitionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Requisition
        fields = ('id',
                  'type',
                  'author',
                  'assignedTechnician',
                  'subject',
                  'details',
                  'priority',
                  'affectedSystem',
                  'module',
                  'date',
                  'attachedFile',
                  'constancy',
                  'status')

class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Token
        fields = ('key',
                  'user')

class SystemSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    class Meta:
        model = models.System
        fields = ('id',
                  'name')

class ModuleSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    class Meta:
        model = models.Module
        fields = ('id',
                  'name',
                  'system')

class NestedSystemModulesSerializer(serializers.ModelSerializer):
    system = ModuleSerializer(many=True)

    class Meta:
        model = models.System
        fields = ('id',
                  'name',
                  'system')

class ConstancySerializer(serializers.ModelSerializer):
    description = serializers.CharField(required=True)
    finishDate = serializers.DateField(required=True)
    class Meta:
        model = models.Constancy
        fields = ('id',
                  'description',
                  'attachedFile',
                  'finishDate')

class RequerimentConstancySerializer(serializers.ModelSerializer):
    affectedSystem = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')
    type = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')
    module = serializers.SlugRelatedField(many=False, read_only=True, slug_field='name')
    constancy = serializers.SlugRelatedField(many=False, read_only=True, slug_field='description')
    class Meta:
        model = models.Requisition
        fields = ('id',
                  'affectedSystem',
                  'type',
                  'module',
                  'constancy')

class StatusSerializer(serializers.ModelSerializer):
    current = serializers.CharField(required=True)
    class Meta:
        model = models.Status
        fields = ('id',
                  'current')

class PrioritySerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    class Meta:
        model = models.Priority
        fields = ('id',
                  'name')

class TypeSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    class Meta:
        model = models.Type
        fields = ('id',
                  'name')

class AffectedSystemsSerializer(serializers.ModelSerializer):
    affectedSystem = serializers.SlugRelatedField(many=False, read_only=True, slug_field= 'name')
    class Meta:
        model = models.Requisition
        fields = ('affectedSystem',)

class AffectedModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Requisition
        fields = ('module',)

class AffectedConstancySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Requisition
        fields = ('constancy',)
