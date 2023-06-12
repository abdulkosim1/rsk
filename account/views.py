from rest_framework.views import APIView
from account.serializers import RegisterSerializer, ForgotPasswordSerializer,ForgotPasswordCompleteSerializer, ProfileSerializer, ChangePasswordSerializer
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import status

User = get_user_model()

class RegisterAPIView(APIView): # Пост запрос на регистрацию
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Вы успешно зарегистрировались. Вам отправлено письмо с активацией на вашу почту.', status=201)

class ActivationView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response('Активация аккаунта прошла успешно.', status=200)
        except User.DoesNotExist:
            return Response('Ссылка уже была использована.', status=400)

