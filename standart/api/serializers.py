from rest_framework import serializers
from form_app.models import Application


class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = [
             'id',
             'summ',
             'requisites',
             'status',
         ]


class ApplicationStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = [
             'status',
         ]