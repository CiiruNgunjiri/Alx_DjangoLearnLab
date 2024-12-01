from django.shortcuts import render
from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()  # Queryset for retrieving all books
    serializer_class = BookSerializer  # Use the BookSerializer for serialization

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Queryset for retrieving all books
    serializer_class = BookSerializer  # Use the BookSerializer for serialization
    permission_classes =[IsAuthenticated] #Only authenticated users can access this view set

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

class CustomAuthToken(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
