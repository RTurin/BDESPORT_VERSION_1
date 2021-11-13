from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include

from .Views import accounts_view
from .Views import main_view
from .Views import tournament_view
urlpatterns = [

        # path('' ,accounts_view.home, name="home"),

        # ---Accounts | Login | Signup | Forget Password---

        # Accounts Related : Login, Register, Auth....Starts
        path('register/' , accounts_view.register_attempt , name="register_attempt"),
        path('accounts/login/' , accounts_view.login_attempt , name="login_attempt"),
        path('token' , accounts_view.token_send , name="token_send"),
        path('success' , accounts_view.success , name='success'),
        path('verify/<auth_token>' , accounts_view.verify , name="verify"),
        path('error' , accounts_view.error_page , name="error"),
        path('logout/' , accounts_view.logout_request , name="logout"),
        # Accounts Related : Login, Register, Auth....Ends

        # Password Reset Starts
        path('forgot-password/' , accounts_view.ForgotPassword , name="forgotpassword"),
        path('verifyforgotpassword/<auth_token>' , accounts_view.verifyforgotpassword , name="verifyforgotpassword"),
        # Password Reset Ends

        # ---Accounts | Login | Signup | Forget Password---

        # ---Main---
        path('',main_view.HomeView.as_view(),name ="main_home"),

        path('Join-Tournament/<slug:slug>/',main_view.TournamentInfo,name= "Tournament_Info"),
        
        path('<slug:slug>/Registration2/',main_view.RegisterTeam_Prev,name= "TeamRegistration2"),

        path('<slug:slug>/Registration/',main_view.RegisterTeam_Final,name= "TeamRegistration"),

        path('Registration-Status/',main_view.AfterRegistration,name = "AfterRegistration"),

        path('Payment-Instruction/<slug:slug>',main_view.Payment_View,name = "Payment"),

        path('Payment-Status/<slug:slug>/',main_view.PaymentStatus,name = "PaymentStatus"),

        path('Tournament/<slug:slug>/',main_view.Tournament_View,name= "Tournament_Page"),

        path('Team/<slug:slug>/',main_view.Team_View,name= "Team_View"),

        # ---Tournament View---
        # path('Tournament1/',tournament_view.test_view,name= "Tournament_Page"),
        # ---Tournament View---
]