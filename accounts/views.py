from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from .forms import *
from .filters import *
from django.contrib import messages

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
        
            # Authenticate user
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                print(user)
                return redirect('landingpage')
    
    # If form is not valid or authentication fails, redirect to homepage
    return redirect('homepage')

def homepage(request):
    signupform = SignUpForm()
    loginform = LoginForm()
    return render(request, "Main/index.html", {'signupform': signupform, 'loginform':loginform})

def landingpage(request):
    return render(request, 'Main/landingpage.html')

def logout_button(request):
    logout(request)
    return redirect('homepage')

def admin_interface(request):
    return render(request, 'Main/Admin/admin_interface.html')

def create(request):
    signupform = UserDetailForm()
    if request.method == 'POST':
        form = UserDetailForm(request.POST)
        if form.is_valid():
            form.save()

            # Extract data from POST request
            email = request.POST.get('email')
            permissions = request.POST.get('permissions')



            # Create a UserPermissionLog instance

            Userpermissionlog.objects.create(
                email=email,
                permissions=permissions,
                status=1,
                created_at=timezone.now()
            )
            
            return render(request, 'Main/landingpage.html')
    return render(request, 'Main/landingpage.html', {'signupform': signupform})

def user_list(request):
    queryset = UserDetail.objects.filter(status=1)
    user_filter = UserDetailFilter(request.GET, queryset=queryset)
    return render(request, 'Main/landingpage.html', {'filter': user_filter})

def update_or_delete(request):
    if request.method == "POST":
        if "Update" not in request.POST:
            user_ids = request.POST.getlist('users')
            users = UserDetail.objects.filter(id__in=user_ids)
            users.update(
                status=0,
                activation_end_date=timezone.now()  # Set activation_end_date to the current time
            )
            Userpermissionlog.objects.create(
                email= UserDetail.objects.filter(id__in=user_ids).values('email'),
                permissions= UserDetail.objects.filter(id__in=user_ids).values('permissions'),
                status=0,
                created_at=timezone.now()
            )
            messages.success(request, "Selected users have been deactivated successfully.")
        elif "Update" in request.POST:
            user_id = request.POST.get('user_id')
            user = get_object_or_404(UserDetail, id=user_id)
            users = UserDetail.objects.filter(id__in=user_id)
            
            if user.permissions != request.POST.get('permissions', user.permissions):
                Userpermissionlog.objects.create(
                email=request.POST.get('email', user.email),
                permissions=request.POST.get('permissions', user.permissions),
                status=1,
                created_at=timezone.now()
                )

            users.update(
                name = request.POST.get('name', user.name),
                email = request.POST.get('email', user.email),
                role =  request.POST.get('role', user.role),
                department = request.POST.get('department', user.department),
                entity_name = request.POST.get('entity_name', user.entity_name),
                cluster_name = request.POST.get('cluster_name', user.cluster_name),
                part_of_group_reporting = request.POST.get('part_of_group_reporting', user.part_of_group_reporting),
                permissions = request.POST.get('permissions', user.permissions)
            )
            
            messages.success(request, "User details have been updated successfully.")
        
        return redirect('view')  # Redirect to your view page after updating or deleting
    return redirect('view')  # Redirect if the request method is not POST

def view_user_activity_logs(request):
    # Fetch user activity logs
    logs = Userpermissionlog.objects.all().order_by('email')
    
    context = {
        'logs': logs
    }
    
    return render(request, 'Main/landingpage.html', context)