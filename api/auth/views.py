from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import GenericAPIView
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

from api.auth.serializers import LoginSerializer, UserSerializer


class LoginGenericAPIView(GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = request.data['username']
        password = request.data['password']

        user = authenticate(username=username, password=password)
        if user:
            token = Token.objects.get_or_create(user=user)[0].key
            user_as_dict = UserSerializer(user, many=False)

            return Response({**user_as_dict.data, 'token': token})

        return Response({'message': 'The user is not found or incorrect password'}, status.HTTP_401_UNAUTHORIZED)