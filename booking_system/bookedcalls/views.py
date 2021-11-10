from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
# import simple jwt authentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.response import Response

from bookedcalls.models import User , Advisor , Booking
from bookedcalls.serializers import UserSerializer , AdvisorSerializer , BookingSerializer
from rest_framework.decorators import api_view

# Create your views here.

#register user with response user_id
@api_view(['POST'])
def register(request):
     if request.method == 'POST':
      data = JSONParser().parse(request)
     try:   #check if user already exists
            user = User.objects.get(email=data['email'])
            return JsonResponse({'error':'Email already exists'}, status=status.HTTP_400_BAD_REQUEST)
     except User.DoesNotExist:
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'user_id':serializer.data['userid'] } , status=status.HTTP_201_CREATED)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
#login  user with email and password
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            user = User.objects.get(email=data['email'])
            if user.password == data['password']:
                return JsonResponse({'user_id' : user.userid, 'message':'Login successful'}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({'error':'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return JsonResponse({'error':'Invalid email'}, status=status.HTTP_400_BAD_REQUEST)

#add advisor 
@api_view(['POST'])
def add_advisor(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            advisor = Advisor.objects.get(advisor_name=data['advisor_name'])
            return JsonResponse({'error':'Advisor already exists'}, status=status.HTTP_400_BAD_REQUEST)
        except Advisor.DoesNotExist:
            serializer = AdvisorSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({'advisor_id':serializer.data['advisorid'] } , status=status.HTTP_201_CREATED)
            return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#book call with advisor id and user id
@api_view(['POST'])
def book_call(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        try:
            advisor = Advisor.objects.get(advisorid=data['advisorid'])
            #advisor name and image filter by advisor id
            advisorname = Advisor.objects.get(advisorid=data['advisorid']).advisor_name
            advisorimg = Advisor.objects.get(advisorid=data['advisorid']).advisor_img
            user = User.objects.get(userid=data['userid'])
            booking = Booking(advisorid=advisor.advisorid, userid=user.userid , booking_date=data['booking_date'], booking_time=data['booking_time'] , advisor_img = advisorimg , advisor_name = advisorname)
            booking.save()
            return JsonResponse({'message':'Booking successful'}, status=status.HTTP_201_CREATED)
        except Advisor.DoesNotExist:
            return JsonResponse({'error':'Advisor does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return JsonResponse({'error':'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        
        
#get all the advisors by userid 
@api_view(['GET'])
def get_advisors(request):
    if request.method == 'GET':
        data = JSONParser().parse(request)
        try:
            user = User.objects.get(userid=data['userid'])
            advisors = Advisor.objects.all()
            serializer = AdvisorSerializer(advisors, many=True)
            if user.userid == data['userid']:
                return JsonResponse(serializer.data, safe = False,status=status.HTTP_200_OK)
            else:
                return JsonResponse({'error':'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            return JsonResponse({'error':'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
 
           
#get all the booking of a user by userid
@api_view(['GET'])
def get_bookings(request):
    if request.method == 'GET':
        data = JSONParser().parse(request)
        try:
            booking = Booking.objects.get(userid=data['userid'])
            serializer =  BookingSerializer(booking)
            return JsonResponse(serializer.data,  status = status.HTTP_200_OK)
        except Booking.DoesNotExist:
            return JsonResponse({'error':'Booking does not exist'}, status=status.HTTP_400_BAD_REQUEST)
            
            
            
            
            