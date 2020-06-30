from django.shortcuts import render,redirect
from homepage.forms import LogForm,RegistrationForm
from homepage.models import LogIn,Registration
from django.contrib import messages
# Create your views here.


def homepage1(request):
    #Render to the home page
    return render(request,"home.html")


def login(request):
    #Validates the login Credentials and allows login to only Registered user.
    if request.method=='POST':
        form=LogForm(request.POST)
        data=Registration.objects.all()
        if form.is_valid():
            ext=form.cleaned_data
            for i in data:
                name=ext.get('Username')
                paswd=ext.get('Password')
                if i.Username == name and i.Password == paswd:
                    return render(request,'display.html',{'form':i})
            else:
                messages.error(request, 'Invalid Credentials')
        form = LogForm()
        return render(request, "login.html", {'form': form})


def register(request):
    #Validates user credential during registration like passward length,
    #Unique user name and valid message regardingly.
    if request.method == "POST":
        k,val=False,'3'
        form2 = RegistrationForm(request.POST)
        if form2.is_valid():
            k = True
            if len(request.POST.get('Password')) == 8:
                uname=request.POST.get('Username')
                for i in Registration.objects.all():
                    if i.Username == uname:
                        val='2'
                        break
                else:
                    try:
                        form2.save()
                        messages.success(request,'Registered Successfully')
                        return render(request,'home.html')
                    except:
                        pass
            else:
                val='1'
        form2 = RegistrationForm()
        return render(request, "registration.html", {'form2': form2,"flag":k,'val':val})