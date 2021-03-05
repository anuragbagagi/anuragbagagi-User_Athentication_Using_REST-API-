from accounts.serializers import UserAccountSerializer
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# you have to pass string as parameter
password = "123"
make_password(password)

class UserCreate(APIView):
    """
    Crate the User
    """

    def post(self, request,format='json'):
        serializer = UserAccountSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                jsn = serializer.data
                jsn['token'] = token.key
                return Response(jsn, status=status.HTTP_201_CREATED)
            # end if
        # end if
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)