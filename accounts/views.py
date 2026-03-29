from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

from .models import User, Profile


# 🔷 REGISTER
# ... existing imports (like User, Profile, login, render, redirect) ...

def register_view(request):
    if request.method == 'POST':
        # Safely get the POST data
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')

        # 1. Check if Username or Email already exists in the database
        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/register.html', {
                'error': 'This username already exists. Please choose another.'
            })
            
        if User.objects.filter(email=email).exists():
            return render(request, 'accounts/register.html', {
                'error': 'This email is already registered. Please log in instead.'
            })

        # 2. Domain validation for Students
        if role == 'student' and not email.endswith('@mmcoe.edu.in'):
            return render(request, 'accounts/register.html', {
                'error': 'Students must use a valid @mmcoe.edu.in email address.'
            })

        # 3. Domain validation for Teachers / Admins
        if role in ['teacher', 'admin'] and not email.endswith('@mmcoe.edu.in'):
            return render(request, 'accounts/register.html', {
                'error': 'Staff/Teachers must use a valid @mmcoe.edu.in email address.'
            })

        # 4. Domain validation for Alumni
        if role == 'alumni' and not email.endswith('@gmail.com'):
            return render(request, 'accounts/register.html', {
                'error': 'Alumni must use a regular @gmail.com email address.'
            })

        # Create user (Make sure to pass 'email' into create_user!)
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            role=role
        )

        # 🔥 Handle admin properly
        if role == 'admin':
            user.is_staff = True
            user.is_superuser = True
            user.save()

        # Create profile
        Profile.objects.get_or_create(user=user)

        login(request, user)

        return redirect('edit_profile')

    return render(request, 'accounts/register.html')


# 🔷 LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            # 🔥 Role-based redirect
            if user.role == 'student':
                return redirect('mentor_list')

            elif user.role == 'alumni':
                return redirect('mentor_requests')

            elif user.role == 'teacher':
                return redirect('home')

            elif user.role == 'admin':
                return redirect('/admin/')

        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})

    # ✅ For GET request (very important)
    return render(request, 'accounts/login.html')




# 🔷 LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')


# 🔷 PROFILE VIEW
@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})


# 🔷 EDIT PROFILE
@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        profile.bio = request.POST.get('bio')
        profile.skills = request.POST.get('skills')
        profile.department = request.POST.get('department')
        profile.year = request.POST.get('year')

        # 🔥 HANDLE IMAGE UPLOAD
        if request.FILES.get('image'):
            profile.image = request.FILES['image']

        profile.save()

        return redirect('profile')

    return render(request, 'accounts/edit_profile.html', {'profile': profile})