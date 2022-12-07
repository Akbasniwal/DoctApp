from django.shortcuts import render
from django.contrib.auth.models import User
from home.models import *
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from datetime import *
from .helpers import send_forget_pass_mail
import uuid
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home(request):
    c = {
        'images': ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg']
    }
    return render(request, 'home.html', c)


def dashboard(request):
    p, d, a = None, None, None
    if request.user.is_authenticated:
        try:
            p = Patient.objects.get(user=request.user)
        except:
            try:
                d = Doctor.objects.get(user=request.user)
            except:
                return redirect('admin/')
        return render(request, 'dashboard.html', {'p': p, 'd': d, 'a': a})
    else:
        return redirect('plogin')


def plogin(request):
    error = ""
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['password']
        usr = authenticate(username=u, password=p)
        if usr:
            try:
                pat = Patient.objects.get(user=usr)
                if pat.type == 'patient':
                    login(request, usr)
                    error = "no"
                else:
                    error = "yes"
            except:
                error = "yes"
        else:
            error = "yes"
    return render(request, 'plogin.html', {'error': error})


def dlogin(request):
    error = ""
    if request.method == "POST":
        u = request.POST['username']
        p = request.POST['password']
        usr = authenticate(username=u, password=p)
        if usr:
            try:
                doct = Doctor.objects.get(user=usr)
                if doct.type == 'doctor':
                    login(request, usr)
                    error = "no"
                else:
                    error = "yes"
            except:
                error = "yes"
        else:
            error = "yes"
    d = {'error': error}
    return render(request, 'dlogin.html', d)


def signup(request):
    error = ""
    u = ""
    if request.method == 'POST':
        f = request.POST['fname']
        l = request.POST['lname']
        dob = request.POST['dob']
        g = request.POST['gender']
        m = request.POST['mobile']
        e = request.POST['email']
        p = request.POST['pwd']
        try:
            u = 'PAT'+str(len(Patient.objects.all()))
            # calculate age
            yr, mn, dy = int(dob[:4]), int(dob[5:7]), int(dob[8:])
            today = date.today()
            age = today.year - yr - \
                ((today.month, today.day) < (mn, dy))

            usr = User.objects.create_user(
                username=u, email=e, first_name=f, last_name=l, password=p)
            today = date.today()
            Patient.objects.create(
                user=usr, gender=g, mobile=m, type="patient", dob=dob, age=age)
            error = "no"
            # subject = 'Thanks for registring'
            # message = f'Welcome to Ak Hospitals'
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = [e, ]
            # send_mail(subject, message, email_from, recipient_list)
        except:
            error = "yes"
    d = {'error': error, 'u': u}
    return render(request, 'signup.html', d)


def Logout(request):
    logout(request)
    return redirect(plogin)


def search(request):
    name = request.GET.get('name')
    sp = request.GET.get('spel')
    idd = request.GET.get('id')
    if name or sp or idd:
        doct = Doctor.objects.filter(
            specialization__contains=sp, user__first_name__contains=name, user__username__contains=idd)
    else:
        doct = Doctor.objects.all()
        sp = name = idd = ''
    return render(request, 'search.html', {'doctors': doct, 'size': len(doct), 'name': name, 'spel': sp, 'id': idd})


@login_required
def bookapp(request, id=None):
    d, mode, p = '', '', ''
    try:
        d = Doctor.objects.get(user__username=id)
    except:
        pass
    try:
        if request.method == 'POST':
            md = request.POST.get('mode')
            p = Patient.objects.get(user__username=request.user)
            x = len(Appointment.objects.all())
            Appointment.objects.create(
                app_id=x, patient=p, doctor=d, mode=md)
            messages.success(
                request, 'Booked Appointment Successfully,wait for approval for 2 hours')
    except Exception as e:
        messages.error(
            request, e)
    return render(request, 'bookapp.html', {'doctor': d})


def change_password(request, token):
    c = {}
    profile_obj = None
    try:
        profile_obj = Patient.objects.get(forgot_pass_token=token)
        c['user_id'] = profile_obj.user.id
    except:
        try:
            profile_obj = Doctor.objects.get(forgot_pass_token=token)
            c['user_id'] = profile_obj.user.id
        except:
            c['user_id'] = 'used'
            pass
    if request.method == "POST":
        password = request.POST['pass']
        cpass = request.POST['cpass']
        uid = request.POST['uid']
        if uid == None:
            return redirect(f'change-password/{token}/')
        if password != cpass:
            messages.error(request, 'both passwords should be equal')
            return redirect(f'change-password/{token}/')
        user_obj = User.objects.get(id=uid)
        user_obj.set_password(password)
        user_obj.save()
        profile_obj.forgot_pass_token = None
        profile_obj.save()
        return redirect('plogin')
    return render(request, 'change-password.html', c)


def forgot_pass(request):
    error = ""
    uid = None
    try:
        if request.method == 'POST':
            uname = request.POST.get('uname')
            email = request.POST.get('email')
            if User.objects.filter(email=email, username=uname):
                try:
                    user = User.objects.get(email=email, username=uname)
                    token = str(uuid.uuid4())
                    fname = user.get_full_name()
                    try:
                        p = Patient.objects.get(user=user)
                        p.forgot_pass_token = token
                        p.save()
                    except:
                        try:
                            d = Doctor.objects.get(user=user)
                            d.forgot_pass_token = token
                            d.save()
                        except:
                            error = "yes"
                    if error == "":
                        send_forget_pass_mail(fname, user.email, token)
                        error = "no"

                except:
                    error = "yes"
            else:
                error = "yes"
    except:
        error = "yes"
    if error == "yes":
        messages.error(request, 'Given email is not registered')
    if error == "no":
        messages.success(request, 'Email sent Check your Inbox')
    return render(request, 'forgot_pass.html')
