from django.shortcuts import render
from .models import *
from .serializer import StudentSerializer
from django.contrib.auth.hashers import check_password,make_password
from rest_framework import generics
from rest_framework_simplejwt.token import RefreshToken
from rest_framework.response import Response
class RegistrationApiView(generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def post(self,request):
        data = request.POST.copy()
        password = data.get('password')
        data['password'] = make_password(password)

        serializer = self.get_serializer(data = data)
        serializer.is_valid(raise_exception = True)
        student = serializer.save()

        refresh = RefreshToken.for_user(student)
        token = {'refresh':str(refresh),
                 'access':str(refresh.access_token)}
        
        return Response(token)
