from rest_framework import generics, status
from .serializer import TheUserSerializer, TaskSerializer, LoginUserSerializer
from .models import Task
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

class TheTaskList(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer   
    
class TheTask(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
class UserList(generics.CreateAPIView):
        queryset = User.objects.all()
        serializer_class = TheUserSerializer
        
class LoginUser(APIView):
    def post(self, request, format=None):
        serializer = LoginUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['username']
            passwd = serializer.validated_data['password']
            loguser = authenticate(request, username=user, password=passwd)
            if loguser is not None:
                login(request, loguser)
                return Response({"message":"Your logged in"}, status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid username or password"}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            # Step 5: Return validation errors
            return Response(
                serializer.errors, 
                status=status.HTTP_400_BAD_REQUEST
            )
        
    
