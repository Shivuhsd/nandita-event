from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from . models import Bookings, Feedback, Enquiry, Package
from . forms import BookingForm, FeedbackForm, EnquiryForm, PackageForm
from django.contrib import messages

# Create your views here.

def Home(request):
    form = BookingForm()
    return render(request, 'home.html', {'form': form})

def UserLogin(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Check Your Credentials..')

    return render(request, 'login.html')

def UserLogout(request):
    logout(request)
    return redirect('userlogin')


def UserRegister(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST['email']
        password = request.POST["password"]
        password1 = request.POST["password1"]


        if password != password1:
            pass
        else:
            data = User.objects.create_user(username=username, email=email, password=password)
            data.save()
            return redirect('userlogin')

    return render(request, 'register.html')


def UserBookings(request):
    
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('userbooks')  # Redirect to a success URL
    else:
        form = BookingForm()
    return render(request, 'home.html', {'form': form})


def UserBooks(request):
    books = Bookings.objects.filter(user = request.user)
    context = {
        'books':books
    }
    return render(request, 'userbooks.html', context)


def Feedbacks(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('feedback')  # Redirect to a success URL
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})


def Query(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('query')  # Redirect to a success URL
    else:
        form = EnquiryForm()
    return render(request, 'enquiry.html', {'form':form})





########################################################################
# Admin Functions (Nandita)

def Dashboard(request):
    books = Bookings.objects.all()
    return render(request, 'dash.html', {'books':books})



def Dashfeedback(request):
    feeds = Feedback.objects.all()
    return render(request, 'dashfeed.html', {'feeds':feeds})


def Dashenquiry(request):
    query = Enquiry.objects.all()
    return render(request, 'dashenquery.html', {'query': query})


def DashPackage(request):
    pack = Package.objects.all()
    if request.method == 'POST':
        form = PackageForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('dashpackage')  # Redirect to a success URL
    else:
        form = PackageForm()
    context = {
        'pack':pack,
        'form':form
    }
    return render(request, 'dashpackage.html', context)


def DashPackageEdit(request, pk): 
    pack = Package.objects.get(id = pk)
    form = PackageForm(instance=pack)
    if request.method == 'POST':
        data = PackageForm(request.POST, instance = pack)
        if data.is_valid():
            data.save()
            return redirect('dashpackage')
    else:
        form = PackageForm(instance=pack)

    return render(request, 'dashpackageedit.html', {'form':form})



def DashPackageDelete(request, pk):
    pack = Package.objects.get(id = pk)
    pack.delete()
    return redirect('dashpackage')