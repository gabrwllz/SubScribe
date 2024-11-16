from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
    
@api_view(['POST'])  # Cette vue accepte seulement les requêtes POST
@authentication_classes([])  # Pas d'authentification nécessaire pour cette vue
@permission_classes([AllowAny])  # Tout le monde peut accéder à cette vue
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save() # create is called to add to user to the db
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)