from django.shortcuts import render
from rest_framework import status

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegistrationSerializer
from .utils import send_verification_email
from django.utils import timezone
from datetime import timedelta
from .models import CustomUser

# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.generate_verification_token()
            send_verification_email(user)
            return Response({
                'message': 'Verification email sent. Please check your inbox.'
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class VerifyEmailView(APIView):
    def get(self, request, token):
        try:
            user = CustomUser.objects.get(verification_token=token)
            # Check if token is expired (e.g., 24 hours)
            if user.token_created_at and (timezone.now() - user.token_created_at) < timedelta(hours=24):
                user.email_verified = True
                user.is_active = True
                user.verification_token = None
                user.token_created_at = None
                user.save()
                return Response({'message': 'Email verified successfully!'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Verification link expired.'}, status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            return Response({'error': 'Invalid verification token.'}, status=status.HTTP_404_NOT_FOUND)