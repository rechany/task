from django.shortcuts import render, redirect
from django.contrib import messages, auth
from .models import District, Branch, AccountType, User, Material,Customer
from django.contrib.auth.models import User

# Create your views here.




def home(request):
    districts = District.objects.all()
    return render(request, "home.html", {'districts': districts})




def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, "login.html")
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Registration successful')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, "register.html")

def application(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        name = request.POST['name']
        dob = request.POST['dob']
        age = request.POST['age']
        gender = request.POST['gender']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        address = request.POST['address']
        district_id = request.POST['district']
        branch_id = request.POST['branch']
        account_type_id = request.POST['account_type']
        materials_provide_ids = request.POST.getlist('materials')
        district = District.objects.get(id=district_id)
        branch = Branch.objects.get(id=branch_id)
        account_type = AccountType.objects.get(id=account_type_id)
        materials_provide = Material.objects.filter(id__in=materials_provide_ids)
        customer = Customer(name=name, dob=dob, age=age, gender=gender, phone_number=phone_number, email=email, address=address, district=district, branch=branch, account_type=account_type)
        customer.save()
        customer.materials_provide.set(materials_provide)
        messages.success(request, 'Application submitted successfully')
        return redirect('logout')
    else:
        districts = District.objects.all()
        account_types = AccountType.objects.all()
        materials_provide = Material.objects.all()
        return render(request, 'application.html', {'districts': districts, 'account_types': account_types, 'materials_provide': materials_provide})

def logout(request):
    if request.session.get('user_id'):
        del request.session['user_id']
    return redirect('login')

def branches(request):
    branches = Branch.objects.all()
    return render(request, 'branch.html', {'branches': branches})