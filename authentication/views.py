from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
# from geeksforgeeks import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
# from django.utils.encoding import force_bytes, force_text
from django.contrib.auth import authenticate, login, logout
from .models import Resident
# from . tokens import generate_token

# Create your views here.
def home(request):
    return render(request, 'authentication/index.html')

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        # if User.objects.filter(username=username):
        #     messages.error(request, "Username already exist! Please try some other username.")
        #     return redirect('home')

        # if User.objects.filter(email=email).exists():
        #     messages.error(request, "Email Already Registered!!")
        #     return redirect('home')

        # if len(username)>20:
        #     messages.error(request, "Username must be under 20 charcters!!")
        #     return redirect('home')

        # if pass1 != pass2:
        #     messages.error(request, "Passwords didn't matched!!")
        #     return redirect('home')

        # if not username.isalnum():
        #     messages.error(request, "Username must be Alpha-Numeric!!")
        #     return redirect('home')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        # myuser.is_active = False
        # myuser.is_active = False
        myuser.save()
        messages.success(
            request,
            "Your Account has been created succesfully!! Please check your email\
            to confirm your email address in order to activate your account."
        )

        # Welcome Email
        # subject = "Welcome to GFG- Django Login!!"
        # message = "Hello " + myuser.first_name + "!! \n" + "Welcome to GFG!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\nAnubhav Madhav"
        # from_email = settings.EMAIL_HOST_USER
        # to_list = [myuser.email]
        # send_mail(subject, message, from_email, to_list, fail_silently=True)

        # Email Address Confirmation Email
        # current_site = get_current_site(request)
        # email_subject = "Confirm your Email @ GFG - Django Login!!"
        # message2 = render_to_string('email_confirmation.html',{

        #     'name': myuser.first_name,
        #     'domain': current_site.domain,
        #     'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
        #     'token': generate_token.make_token(myuser)
        # })
        # email = EmailMessage(
        # email_subject,
        # message2,
        # settings.EMAIL_HOST_USER,
        # [myuser.email],
        # )
        # email.fail_silently = True
        # email.send()

        return redirect('signin')


    return render(request, 'authentication/signup.html')


# def activate(request,uidb64,token):
#     try:
#         uid = force_text(urlsafe_base64_decode(uidb64))
#         myuser = User.objects.get(pk=uid)
#     except (TypeError,ValueError,OverflowError,User.DoesNotExist):
#         myuser = None

#     if myuser is not None and generate_token.check_token(myuser,token):
#         myuser.is_active = True
#         # user.profile.signup_confirmation = True
#         myuser.save()
#         login(request,myuser)
#         messages.success(request, "Your Account has been activated!!")
#         return redirect('signin')
#     else:
#         return render(request,'activation_failed.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            # fname = user.first_name
            messages.success(request, "Logged In Sucessfully!!")
            # return render(request, 'authentication/dashboard.html')
            # return render(request, "authentication/dashboard.html",{"fname":fname})
            return redirect('dashboard')
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')

    return render(request, 'authentication/signin.html')

def dashboard(request):
    return render(request, 'authentication/dashboard.html')

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')

def add(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        birthday = request.POST.get('email')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        age = request.POST.get('age')
        status = request.POST.get('status')
        citizen = request.POST.get('citizen')
        gender = request.POST.get('gender')
        id_type = request.POST.get('id_type')
        id_no = request.POST.get('id_no')
        member = request.POST.get('member')

        resident = Resident.objects.create()

        resident.name = name
        resident.birthday = birthday
        resident.email = email
        resident.phone = phone
        resident.address = address
        resident.age = age
        resident.status = status
        resident.citizen = citizen
        resident.gender = gender
        resident.id_type = id_type
        resident.id_no = id_no
        resident.member = member

        resident.save()

    return render(request, 'authentication/add.html')

def view_list(request):
    return render(request, 'authentication/view.html', {
        'resident' : Resident.objects.all(),
    })

def view_info(request, id):
    resident = Resident.objects.get(pk=id)
    return HttpResponseRedirect(reverse('view_list'))

def delete_list(request, id):
    if request.method == 'POST':
        resident = Resident.objects.get(pk=id)
        resident.delete()
    return HttpResponseRedirect(reverse('view_list'))
