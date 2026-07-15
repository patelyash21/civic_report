from django.contrib import messages

from django.shortcuts import render, redirect
from .forms import ReportForm
from .models import Report
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required



@login_required
def dashboard(request):
    reports = Report.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {'reports': reports})
# Create your views here.


def login_view(request):
    if request.method == 'POST':
        # Handle login logic here
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profile')
        else:
            # Return an error message or redirect to the login page
            messages.error(request, 'Invalid username or password')
            
    return render(request, 'login.html')

def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')

def report_list(request):
    reports = Report.objects.all()
    return render(request, 'report_list.html', {'reports': reports})

def map_view(request):
    return render(request, 'map.html')

def notification(request):
    return render(request, 'notification.html')

@login_required
def user_profile(request):
    return render(request, 'profile.html',{'user': request.user})

def about_view(request):
    return render(request, 'about.html')

def contact_view(request):
    return render(request, 'contact.html')

def register_views(request):
    from django.shortcuts import render, redirect
from django.contrib.auth.models import User

def register_views(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # check if username exists
        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {"error": "Username already exists"})

        # create user
        User.objects.create_user(username=username, password=password)

        return redirect("home")

    return render(request, "register.html")

def report_detail(request,id):

    report = Report.objects.get(id=id)

    return render(
        request,
        'report_detail.html',
        {'report':report}
    )
@login_required
def create_report(request):

    if request.method == "POST":

        title = request.POST.get("title")
        category = request.POST.get("category")
        description = request.POST.get("description")

        latitude = request.POST.get("latitude")
        longitude = request.POST.get("longitude")

        image = request.FILES.get("image")

        Report.objects.create(

            user=request.user,

            title=title,
            category=category,
            description=description,

            latitude=latitude,
            longitude=longitude,

            image=image
        )

        return redirect("dashboard")

    return render(request, "create_report.html")