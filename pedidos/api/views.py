from django.shortcuts import render
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated

# Create your views here.

from . import models
from . import serializers

ORDERMINORMAYOR = 0
ORDERMAYORMINOR = 1
WAITING = 1
INPROGRESS = 2
CANCELLED = 3
DONE = 4

class UserListView(generics.ListAPIView):
    lookup_field = 'id'
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

class UniqueUserListView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = models.CustomUser.objects
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return models.CustomUser.objects.filter(id=id)

class CommonUsersListView(generics.ListAPIView):
    queryset = models.CustomUser.objects.all().filter(isTechnician = False)
    serializer_class = serializers.UserSerializer

class TechniciansListView(generics.ListAPIView):
    queryset = models.CustomUser.objects.all().filter(isTechnician = True)
    serializer_class = serializers.UserSerializer


class TechnicianRequisitionView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = serializers.RequisitionSerializer

    def get_queryset(self):
        techId = self.kwargs['id']
        return models.Requisition.objects.filter(assignedTechnician = techId)


class RequisitionListView(generics.ListCreateAPIView):
    lookup_field = 'id'
    serializer_class = serializers.RequisitionCommonSerializer
    queryset = models.Requisition.objects.all()

class DeleteRequisitionView(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = models.Requisition.objects.all()
    serializer_class = serializers.RequisitionSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return models.Requisition.objects.filter(id=id)

class UpdateRequisitionView(generics.UpdateAPIView):
    lookup_field = 'id'
    queryset = models.Requisition.objects.all()
    serializer_class = serializers.RequisitionUpdateSerializer

class MyRequisitionsListView(generics.ListAPIView):
    lookup_field = 'id'
    queryset = models.Requisition.objects
    serializer_class = serializers.RequisitionSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return models.Requisition.objects.filter(author=id)

class SystemsView(generics.ListCreateAPIView):
    lookup_filed = 'id'
    queryset = models.System.objects.all()
    serializer_class = serializers.SystemSerializer

class ModulesView(generics.ListCreateAPIView):
    lookup_filed = 'id'
    queryset = models.Module.objects.all()
    serializer_class = serializers.ModuleSerializer

class ConstancysView(generics.ListCreateAPIView):
    lookup_field = 'id'
    queryset = models.Constancy.objects.all()
    serializer_class = serializers.ConstancySerializer

class UniqueSystemView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = serializers.SystemSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return models.System.objects.filter(id=id)

class DeleteSystemView(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = serializers.SystemSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return models.System.objects.filter(id=id)

class UniqueModuleView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = serializers.ModuleSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return models.Module.objects.filter(id=id)

class DeleteModuleView(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = serializers.ModuleSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return models.Module.objects.filter(id=id)

class UniqueConstancyView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = serializers.ConstancySerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return models.Constancy.objects.filter(id=id)

class DeleteConstancyView(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = serializers.ConstancySerializer

    def get_queryset(self):
        id = self.kwargs['id']

        return models.Constancy.objects.filter(id=id)

class SystemModulesView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = serializers.ModuleSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return models.Module.objects.all().filter(system=id)

class StatusView(generics.ListCreateAPIView):
    lookup_field = 'id'
    queryset = models.Status.objects.all()
    serializer_class = serializers.StatusSerializer

class PriorityView(generics.ListCreateAPIView):
    lookup_field = 'id'
    queryset = models.Priority.objects.all()
    serializer_class = serializers.PrioritySerializer

class RequisitionByStatusView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = serializers.RequisitionSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return models.Requisition.objects.all().filter(status = id)

class RequisitionByStatusAndDateView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = serializers.RequisitionSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        queryset = models.Requisition.objects.all().filter(status=id).order_by('date')
        order = self.kwargs['order']
        if order == ORDERMAYORMINOR :
            queryset = models.Requisition.objects.all().filter(status=id).order_by('date')

        elif order == ORDERMINORMAYOR :
            queryset = models.Requisition.objects.all().filter(status=id).order_by('-date')

        return queryset

class RequisitionByStatusAndPriorityView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = serializers.RequisitionSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        queryset = models.Requisition.objects.all().filter(status=id).order_by('priority')
        order = self.kwargs['order']
        if order == ORDERMAYORMINOR :
            queryset = models.Requisition.objects.all().filter(status=id).order_by('priority')

        elif order == ORDERMINORMAYOR :
            queryset = models.Requisition.objects.all().filter(status=id).order_by('-priority')

        return queryset

class OrderRequisitionByPriority(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = serializers.RequisitionSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        queryset = models.Requisition.objects.all().order_by('priority')
        order = self.kwargs['order']

        if order == ORDERMAYORMINOR :
            queryset = models.Requisition.objects.all().filter(status=id).order_by('priority')

        elif order == ORDERMINORMAYOR :
            queryset = models.Requisition.objects.all().filter(status=id).order_by('-priority')

        return queryset

class OrderRequisitionByDate(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = serializers.RequisitionSerializer

    def get_queryset(self):
        queryset = models.Requisition.objects.all().order_by('date')
        order = self.kwargs['order']

        if order ==  ORDERMAYORMINOR:
            queryset = models.Requisition.objects.all().order_by('date')

        elif order == ORDERMINORMAYOR:
            queryset = models.Requisition.objects.all().order_by('-date')

        return queryset

class PriorityAdvancedSearchSystem(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = serializers.RequisitionSerializer

    def get_queryset(self):
        queryset = models.Requisition.objects.all().order_by('priority')
        system = self.kwargs['system']
        status = self.kwargs['status']
        order = self.kwargs['order']

        if order == ORDERMAYORMINOR :
            queryset = models.Requisition.objects.all().filter(affectedSystem=system, status=status).order_by('priority')

        elif order == ORDERMINORMAYOR :
            queryset = models.Requisition.objects.all().filter(affectedSystem=system, status=status).order_by('-priority')

        return queryset

class DateAdvancedSearchSystem(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = serializers.RequisitionSerializer

    def get_queryset(self):

        queryset = models.Requisition.objects.all().order_by('date')
        system = self.kwargs['system']
        status = self.kwargs['status']
        order = self.kwargs['order']

        if order == ORDERMAYORMINOR :
            queryset = models.Requisition.objects.all().filter(affectedSystem=system, status=status).order_by('date')

        elif order == ORDERMINORMAYOR :
            queryset = models.Requisition.objects.all().filter(affectedSystem=system, status=status).order_by('-date')

        return queryset

class PriorityAdvancedSearchModule(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = serializers.RequisitionSerializer

    def get_queryset(self):
        queryset = models.Requisition.objects.all().order_by('priority')
        order = self.kwargs['order']
        module = self.kwargs['module']
        status = self.kwargs['status']


        if order == ORDERMAYORMINOR :
            queryset = models.Requisition.objects.all().filter(module=module, status=status).order_by('priority')

        elif order == ORDERMINORMAYOR :
            queryset = models.Requisition.objects.all().filter(module=module, status=status).order_by('-priority')

        return queryset

class DateAdvancedSearchModule(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = serializers.RequisitionSerializer

    def get_queryset(self):

        queryset = models.Requisition.objects.all().order_by('date')
        order = self.kwargs['order']
        module = self.kwargs['module']
        status = self.kwargs['status']

        if order == ORDERMAYORMINOR :
            queryset = models.Requisition.objects.all().filter(module=module, status=status).order_by('date')

        elif order == ORDERMINORMAYOR :
            queryset = models.Requisition.objects.all().filter(module=module, status=status).order_by('-date')

        return queryset

class PriorityAdvancedSearchTechnician(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = serializers.RequisitionSerializer

    def get_queryset(self):
        queryset = models.Requisition.objects.all().order_by('priority')
        order = self.kwargs['order']
        technician = self.kwargs['technician']
        status = self.kwargs['status']


        if order == ORDERMAYORMINOR :
            queryset = models.Requisition.objects.all().filter(assignedTechnician=technician, status=status).order_by('priority')

        elif order == ORDERMINORMAYOR :
            queryset = models.Requisition.objects.all().filter(assignedTechnician=technician, status=status).order_by('-priority')

        return queryset

class DateAdvancedSearchTechnician(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = serializers.RequisitionSerializer

    def get_queryset(self):

        queryset = models.Requisition.objects.all().order_by('date')
        order = self.kwargs['order']
        technician = self.kwargs['technician']
        status = self.kwargs['status']

        if order == ORDERMAYORMINOR :
            queryset = models.Requisition.objects.all().filter(assignedTechnician=technician, status=status).order_by('priority')

        elif order == ORDERMINORMAYOR :
            queryset = models.Requisition.objects.all().filter(assignedTechnician=technician, status=status).order_by('-priority')

        return queryset

class OrderRequisitionByAuthor(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = serializers.RequisitionSerializer

    def get_queryset(self):
        queryset = models.Requisition.objects.all().order_by('author')
        order = self.kwargs['order']

        if order == ORDERMAYORMINOR :
            queryset = models.Requisition.objects.all().order_by('author')

        elif order == ORDERMINORMAYOR :
            queryset = models.Requisition.objects.all().order_by('-author')

        return queryset

class Priority(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = models.Requisition.objects.all()
    serializer_class = serializers.PrioritySerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return models.Priority.objects.all().filter(id=id)

class UnderwayByTechnicianView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = serializers.RequisitionSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return models.Requisition.objects.all().filter(assignedTechnician = id, status = INPROGRESS)

class ImplementedByTechnicianView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = serializers.RequisitionSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return models.Requisition.objects.all().filter(assignedTechnician = id, status = DONE)

class TypesView(generics.ListCreateAPIView):
    lookup_filed = 'id'
    queryset = models.Type.objects.all()
    serializer_class = serializers.TypeSerializer

# class AffectedSystems(generics.ListAPIView):
#     lookup_filed = 'id'
#     queryset = models.Requisition.objects.all()
#     serializer_class = serializers.AffectedSystemsSerializer

class SystemAffectedModules(generics.ListAPIView):
    lookup_filed = 'id'
    serializer_class = serializers.AffectedModulesSerializer

    def get_queryset(self):
        systemId = self.kwargs['system']
        return models.Requisition.objects.all().filter(affectedSystem = systemId, status = DONE)

class ModulesConstancy(generics.ListAPIView):
    lookup_filed = 'id'
    serializer_class = serializers.AffectedConstancySerializer

    def get_queryset(self):
        moduleId = self.kwargs['module']
        return models.Requisition.objects.all().filter(module = moduleId, status = DONE)

class TypeObjectView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = serializers.TypeSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return models.Type.objects.all().filter(id=id)

class StatusObjectView(generics.RetrieveAPIView):
    lookup_field = 'id'
    serializer_class = serializers.StatusSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return models.Status.objects.all().filter(id=id)

class PriorityObjectView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = models.Priority.objects.all()
    serializer_class = serializers.PrioritySerializer

    def get_queryset(self):
        id = self.kwargs['id']
        return models.Priority.objects.all().filter(id=id)

class NestedSystemsModules(generics.ListAPIView):
    lookup_field = 'id'
    queryset = models.System.objects.all()
    serializer_class = serializers.NestedSystemModulesSerializer

# class SearchRequisitionByModule(generics.ListAPIView):
#     lookup_field = 'id'
#     serializer_class = serializers.RequisitionSerializer
#
#     def get_queryset(self):
#         moduleId = self.kwargs['moduleId']
#         return models.Requisition.objects.all().filter(module = moduleId)


class WaitingRequistionsView(generics.ListAPIView):
    lookup_filed = 'id'
    queryset = models.Requisition.objects.all().filter(status = WAITING)
    serializer_class = serializers.RequisitionSerializer

class InProgressRequistionsView(generics.ListAPIView):
    lookup_filed = 'id'
    queryset = models.Requisition.objects.all().filter(status = INPROGRESS)
    serializer_class = serializers.RequisitionSerializer

class CancelledRequistionsView(generics.ListAPIView):
    lookup_filed = 'id'
    queryset = models.Requisition.objects.all().filter(status = CANCELLED)
    serializer_class = serializers.RequisitionSerializer

class DoneRequistionsView(generics.ListAPIView):
    lookup_filed = 'id'
    queryset = models.Requisition.objects.all().filter(status = DONE)
    serializer_class = serializers.RequisitionSerializer