from rest_framework import generics, status
from form_app.models import Requisites, Application
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ApplicationSerializer, ApplicationStatusSerializer


class CreateInvoice(APIView):

    def post(self, request):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'id': serializer.data['id'], 'requisites': serializer.data['requisites']}, status=status.HTTP_201_CREATED)
        return Response({'400': 'Не верно введены данные'}, status=status.HTTP_400_BAD_REQUEST)


class GetInvoiceStatus(generics.ListAPIView):
    model = Application
    serializer_class = ApplicationStatusSerializer

    def get_queryset(self):
        application_id = self.kwargs['pk']
        queryset = self.model.objects.filter(id=application_id)
        return queryset


