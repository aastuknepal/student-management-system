from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer

from .permissions import CanAssignRolesPermission




class RegisterView(generics.CreateAPIView):
    queryset= User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer


class LogoutView(APIView):
    permission_classes  = [IsAuthenticated]

    def post(self, request):

        try:
            # Get the refresh token from the POST request 
            refresh_token = request.data["refresh"]

            # Instantiate the token and blacklist it
            token = RefreshToken(RefreshToken)
            token.blacklist()

            # Tell the user successfully logged out
            return Response(
                {"message": "Successfully Logge out."},
                status= status.HTTP_205_RESET_CONTENT
            )
        
        except Exception as e:

            # If the token is expred or already logged out or blocklisted
            return Response(
                {"error": "Invalid token or already logged out"},
                status= status.HTTP_400_BAD_REQUEST
            )
        