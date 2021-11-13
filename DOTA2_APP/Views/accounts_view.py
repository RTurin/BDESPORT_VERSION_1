from django.shortcuts import render,redirect,reverse

from DOTA2_APP.models import *  # Displayed red underline below App.models...IntelliJ IDEA Software Read Issue....
from django.contrib.auth.models import User

from django.contrib import messages

import uuid
from django.conf import settings
from django.core.mail import send_mail

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# --------------------------------------------------------------------

# Accounts Views
# @login_required
# def home(request):
#     return render(request,"Accounts/home.html")

def login_attempt(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username = username).first()
        if user_obj is None:
            messages.success(request, 'User not found.')
            return redirect('/accounts/login')

        profile_obj = Profile.objects.filter(user = user_obj ).first()

        if not profile_obj.is_verified:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('/accounts/login')

        user = authenticate(username = username , password = password)
        if user is None:
            messages.success(request, 'Wrong password.')
            return redirect('/accounts/login')

        login(request , user)
        return redirect('/')


    return render(request , 'Accounts/login.html')

def register_attempt(request):

    if request.user.is_authenticated:
        return redirect('/')

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        phoneNo = request.POST.get('phoneNo')

        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        try:
            if User.objects.filter(username = username).first():
                messages.success(request, 'Username is taken.')
                return redirect('/register')

            if User.objects.filter(email = email).first():
                messages.success(request, 'Email is taken.')
                return redirect('/register')

            if password != confirm_password:
                messages.success(request, 'Password Mismatch.')
                return redirect('/register')

            user_obj = User(username = username , email = email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user = user_obj ,email=email,phoneNo=phoneNo, auth_token = auth_token)
            profile_obj.save()
            send_mail_after_registration(email , auth_token)
            return redirect('/token')

        except Exception as e:
            print(e)

    return render(request , 'Accounts/register.html')


def logout_request(request):

    logout(request)
    return redirect('/')

def success(request):
    return render(request , 'Accounts/success.html')

def token_send(request):
    return render(request , 'Accounts/token_send.html')

def verify(request , auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token = auth_token).first()

        if profile_obj:
            if profile_obj.is_verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('/accounts/login')
            profile_obj.is_verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('/accounts/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)
        return redirect('/')

def error_page(request):
    return  render(request , 'Accounts/error.html')

def send_mail_after_registration(email , token):
    subject = 'Your accounts need to be verified'
    message = f'Hi paste the link to verify your account http://127.0.0.1:8000/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message , email_from ,recipient_list )

# Password Reset -------------------------------

def ForgotPassword(request):

    try:
        if request.method == 'POST':
            email = request.POST.get('email')

            if not  User.objects.filter(email = email).first():
                messages.success(request, 'No Account Found with this email')
            else:
                user_obj = User.objects.filter(email = email).first()
                # print("Username",user_obj.username)
                username = user_obj.username
                profile_obj = Profile.objects.get(email = email)

                # print("Auth Token:",profile_obj.auth_token)
                auth_token = profile_obj.auth_token
                send_mail_after_forgot_password(username,email,auth_token)

                messages.success(request, 'Please check your email to reset password.')

    except Exception as e:
        print(e)

    return render(request,'Accounts/Reset_Password/forgotpassword.html')

def send_mail_after_forgot_password(username,email,token):

    print(username,email,token)

    subject = f'BDESPORT | Password Reset Link... | Username:{username}'
    message = f'Click the Following Link To Reset Your Password- http://127.0.0.1:8000/verifyforgotpassword/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]

    send_mail(subject, message , email_from ,recipient_list )

def verifyforgotpassword(request , auth_token):
    try:

        if request.method == 'POST':
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            try:
                if password != confirm_password:
                    messages.success(request, 'Password Mismatch.')
                    return redirect(f'/verifyforgotpassword/{auth_token}')

                get_profile_obj = Profile.objects.filter(auth_token=auth_token).first()
                get_user_obj = User.objects.get(email =get_profile_obj.email )

                get_user_obj.set_password(confirm_password)
                get_user_obj.save()
                login(request , get_user_obj)
                return redirect('/')


            except Exception as e:
                print(e)

    except Exception as e:
        print(e)

    return render(request,'Accounts/Reset_Password/resetpassword.html')

# Password Reset -------------------------------

# Accounts Views
# --------------------------------------------------------------------


