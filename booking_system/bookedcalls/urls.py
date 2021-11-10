from django.urls import path 
from . import views
#simple jwt authentication
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenVerifyView)

urlpatterns = [
    #advisor add 
    path('admin/advisor' , views.add_advisor , name = 'add_advisor'),
    
    # user registration 
    path('user/register' , views.register , name = 'register'),
    
    # user login
    path('user/login' , views.login , name = 'login'),
   
    #get list of all advisors by user id
    path('user/user_id/advisors' , views.get_advisors , name = 'get_advisors'),
    
    #book a call by user id and advisor id
   path('user/userid/advisor/advisorid/book' , views.book_call , name = 'book_call'),
   
    #get all the booking of a user by user id
    path('user/userid/advisor/booking' , views.get_bookings , name = 'get_bookings'),
    
  

  path ('token/' , TokenObtainPairView.as_view() , name = 'token_obtain_pair'),
    path('user/token/verify', TokenVerifyView.as_view(), name='token_verify'),
    

   
   

 

]


