from django.contrib.auth.models import User
from rest_framework import serializers

from apps.users.models import Staff, StaffRole



class user_serializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'
        extra_kwargs = {'password': {'write_only': True}}


class role_serializer(serializers.ModelSerializer):
    class Meta:
        model=StaffRole
        fields="__all__"

    def create(self, validated_data):
        role=StaffRole(**validated_data)
        role.save()
        print("Se aguardo")
        return role

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save(update_fields=validated_data.keys())
        return instance
    
class onget_role_serializer(serializers.ModelSerializer):
    class Meta:
        model=StaffRole
        fields=[
            "id",
            "name",
            "permissions",
            "deleted",
            "created_date",
            "created_by",
        ]


class staff_serializer(serializers.ModelSerializer):
    class Meta:
        model=Staff
        fields='__all__'

    def create(self, validated_data):

        validated_data['user']=self.context.get("user")
        validated_data['role']=StaffRole.objects.get(id=self.context.get("role"))

        staff=Staff(**validated_data)
        staff.save()

        return staff

    def update(self, instance, validated_data):
        for key,value in validated_data.items():
            setattr(instance,key,value)

        instance.save(update_fields=validated_data.keys())
        return instance

class  onget_staff_serializer(serializers.ModelSerializer):
    role=onget_role_serializer('role')


    class Meta:
        model = Staff
        fields = '__all__'

    def get_role(self, instance):
        return(
                onget_role_serializer(StaffRole.objects.filter(pk=instance.role).count())
        )
