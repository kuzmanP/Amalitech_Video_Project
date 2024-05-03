from django.contrib.auth import authenticate, login
from .models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

from django.core.mail import EmailMessage
from django.core.mail import send_mail                   #for mail services

from Amalitech_Project import settings
from account.tokens import generate_token
from django.contrib.sites.shortcuts import get_current_site

from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
# Create your views here.
def index(request):
    authenticated = False
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(username=username,password=password)
        authenticated=True
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('login')
    return render(request,'matrix-admin/authentication-login.html')



def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username Already Exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email Exists')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.is_active = False
                user.save()

                # Email welcome
                subject = 'Welcome to Rift Video App'
                current_site = get_current_site(request)

                activation_url = f"{current_site.domain}/activate/{urlsafe_base64_encode(force_bytes(user.pk))}/{generate_token.make_token(user)}"

                message = f"Hello {user.username}!\n\nWelcome to Rift Video App. Thank you for signing up. " \
                          f"To activate your account, please click the following link:\n\n{activation_url}\n\n" \
                          f"If you didn't sign up for an account on Rift Video App, you can ignore this email.\n\n" \
                          f"Thank you,\nThe Rift Team"

                send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email])

                messages.info(request, 'Account Successfully created. We have sent a confirmation email to activate your account.')
                return redirect('index')
    return render(request, 'matrix-admin/authentication-register.html')


def forgetPassword(request):
    if request.method == "POST":
        password_reset_form = PasswordResetForm(request.POST)
        if password_reset_form.is_valid():
            data = password_reset_form.cleaned_data['email']
            associated_users = User.objects.filter(Q(email=data))
            if associated_users.exists():
                for user in associated_users:
                    subject = "Password Reset Requested"
                    email_template_name = "accounts/password/password_reset.txt"
                    c = {
                        "email": user.email,
                        'domain': '127.0.0.1:8000',
                        'site_name': 'Website',
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "user": user,
                        'token': default_token_generator.make_token(user),
                        'protocol': 'http',
                    }
                    email = render_to_string(email_template_name, c)
                    try:
                        send_mail(subject, email, 'admin@example.com', [user.email], fail_silently=False)
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return render(request, 'password/password_reset_done.html')

                    messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
                    return redirect("/")
    password_reset_form = PasswordResetForm()
    return render(request,'password/password_reset.html',{"password_reset_form":password_reset_form})