from rest_framework import serializers

from django.contrib.auth.models import User

from grocerymanagement.models import GroceryItem

class UserSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ['id', "username", 'email', 'password']

        read_only_fields = ['id']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
class GrocerySerializer(serializers.ModelSerializer):

    class Meta:

        model = GroceryItem

        fields = "__all__"

        read_only_fields = ["id", "created_at", "updated_at", "owner"]


    def validate_name(self, value):
        
        if not value or value.strip() == "":

            raise serializers.ValidationError("Item name cannot be empty")
        
        return value
        




