from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from django.contrib.auth import authenticate
from .models import BlogPost
from .serializers import BlogPostSerializer, RegisterSerializer
# Create your views here.
class BlogPostListCreateView(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class BlogPostDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'message': 'Registration successful',
            'username': user.username,
            'token': token.key
        })

class LoginView(APIView):
        permission_classes = [AllowAny]

        def post(self, request):
            username = request.data.get('username')
            password = request.data.get('password')

            user = authenticate(
                username=username,
                password=password
            )

            if user is None:
                return Response(
                    {'error': 'Invalid username or password'},
                    status=401
                )

            token, created = Token.objects.get_or_create(
                user=user
            )

            return Response({
                'message': 'Login successful',
                'username': user.username,
                'token': token.key
            })
