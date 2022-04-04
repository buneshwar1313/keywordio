from django.shortcuts import render
from rest_framework import mixins, generics

from rest_framework.response import Response
from django.contrib.auth import login as django_login,authenticate,logout as django_logout
from .serializers import *
from rest_framework.views import APIView

from rest_framework.settings import api_settings

from rest_framework.permissions import IsAuthenticated

from rest_framework.authentication import TokenAuthentication
# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer




class UserRegistration(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    serializer_class = UserProfileSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            serialized_data = serializer.data
            return Response(serialized_data, status=201)
        return Response(serializer.errors, status=400)


class LoginView(APIView):


    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']
        print(user)
        django_login(request,user)
        token,created = Token.objects.get_or_create(user=user)
        return Response({'token':token.key,'message':'login successful'}, status =200)



class LogoutView(APIView):

    authentication_classes=(TokenAuthentication,)
    queryset = UserProfile.objects.all()

    def get(self, request):

        django_logout(request)
        return Response(status=200)




class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    # permission_classes = (IsAuthenticated,)
    # authentication_classes = [TokenAuthentication, ]
    def perform_create(self, serializer):
        serializer.save()

class BookUpdateDelete(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    serializer_class = BookSerializers
    queryset = Book.objects.all()

    def get(self,request,*args,**kwargs):
       return self.retrieve(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return self.delete(request,*args,**kwargs)



class Book(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = BookSerializers
    queryset = Book.objects.all()
    # pagination_class = MyPageNumberPagination
    lookup_field = 'id'

    def post(self, request):
        return self.create(request)

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def delete(self, request, id=None):
        return self.destroy(request, id)

    def put(self, request, id=None):
        return self.update(request, id)
