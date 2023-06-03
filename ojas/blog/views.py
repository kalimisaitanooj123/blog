from django.shortcuts import render,HttpResponseRedirect,redirect
from django.views import generic
from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
# Create your views here.
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,authenticate,PasswordChangeForm

from .forms import *
from .models import *

def add(request):
    if request.method=="POST":
        data=Blog1(request.POST)                     #form
        if data.is_valid():
            n=data.cleaned_data["name"]
            t=data.cleaned_data["title"]
            c=data.cleaned_data["content"]
            result=Blog(name=n,title=t,content=c)   #model
            result.save()
            data=Blog1()                                #model
    else:
        data=Blog1()                                        #form
    data1=Blog.objects.all()
    return render(request,"1.html",{"data":data,"data1":data1})

def update(request,id):
    if request.method=="POST":
        a=Blog.objects.get(pk=id)
        b=Blog1(request.POST,instance=a)
        if b.is_valid():
            b.save()
            messages.success(request,"successfully updated")
    else:
        a=Blog.objects.get(pk=id)
        b=Blog1(instance=a)
    return render(request,"2.html",{"data":b})


def delete(request,id):
    a=Blog.objects.get(pk=id)
    a.delete()
    return render(request,"3.html")

# def fake(request):
#     return render(request,"7.html")


def home(request):
    data1 = Blog.objects.all()
    return render(request,"home.html",{'data':data1})

def adm(request):
    response = redirect('/admin/')
    return response

def about(request):
    return render(request,"about.html")

def Contactinfo(request):
    if request.method=='POST':
        data=Contactus(request.POST)
        if data.is_valid():
            n=data.cleaned_data["name"]
            e=data.cleaned_data["Email"]
            c=data.cleaned_data["comments"]
            p=data.cleaned_data["phone"]
            result=Contact(name=n,Email=e,comments=c,phone=p)

            result.save()
            messages.success(request, 'commented successfully!!!')
    else:
        data=Contactus()
    con=Contact.objects.all()
    return render(request,"contact.html",{"data1":data,"con1":con})




def delw(request):
    return render(request,"4.html")

def create_account(request):
    return render(request,"create.html")

def login(request):
    return render(request,"login.html")


from django.shortcuts import render, HttpResponseRedirect
from django.contrib import messages
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.
#Signup
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request,'Account Created Successfully!!!')
            fm.save()
    else:
        fm = SignUpForm()
    return render(request,'signup.html',{'form':fm})


#Login
def user_login(request):
    if not request.user.is_authenticated:

        if request.method == "POST":
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'Logged in successfully!!!')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request,'userlogin.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')


#Profile
def user_profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{'name':request.user})
    else:
        return HttpResponseRedirect('/login/')


# class PostList(generic.ListView):
#     queryset = Post.objects.filter(status=1).order_by("-created_on")
#     template_name = "index.html"
#     paginate_by = 3


#Logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


def changeform_details(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            sign = PasswordChangeForm(user = request.user,data=request.POST)
            if sign.is_valid():
                sign.save()
                update_session_auth_hash(request,sign.user)
                messages.success(request,"password changed successfully!!!")
                return HttpResponseRedirect('/profile/')
        else:
            sign = PasswordChangeForm(user=request.user)
        return render(request,'changepassword.html',{'sign':sign})
    else:
        return HttpResponseRedirect('/login/')

class PostDetail(generic.DetailView):
    model = Blog
    template_name = 'post_detail.html'