from django.shortcuts import HttpResponseRedirect, HttpResponse
from rest_framework import generics
from .serializers import LoginSerializer
from .serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from django.utils.encoding import smart_str, smart_bytes
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

User = get_user_model()

@csrf_exempt
def login_view(request):
    # Your login logic
    return JsonResponse({"message": "Login successful"})

class LoginView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = RefreshToken.for_user(user)
        response = {
            'email':user.email,
            'token': {"refresh": str(token),
            "access": str(token.access_token)}
        }
        return Response(response)

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

def activation_view(request, uuid64, token):
    id = smart_str(urlsafe_base64_decode(uuid64))
    user = User.objects.get(id=id)

    if not PasswordResetTokenGenerator().check_token(user, token):
        message = "Link Duzgun Deyil"
        return HttpResponse(f"<h1>{message}</h1>")

    user.is_active = True
    user.save()

    return HttpResponseRedirect("http://127.0.0.1:8000/access-activation") #login sehifesi