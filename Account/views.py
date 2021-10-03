from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from .forms import ProfileForm, SignupForm
from django.contrib import messages


#Login's form )manual)
def login_view(request):
    template_name = 'Account/login.html'
    context = {}

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if not User.objects.filter(username=username).exists():
            messages.error(request, "کاربری با این مشخصات پیدا نشد")
            return render(request, template_name, context)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "خوش آمدید")
            return redirect('account:profile')
        else:
            messages.error(request, "نام کاربری یا پسورد اشتباه است ")
            return render(request, template_name, context)
            
    return render(request, template_name, context)




#Logout manual form 
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    messages.success(request, "به امید دیدار")
    return redirect('account:login')


#profile's form
@login_required(login_url='/account/login/')
def profile_view(request):
    template_name = 'Account/profile.html'
    context = {}
    form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            age = form.cleaned_data['age']
            n_code = form.cleaned_data['n_code']
            phone = form.cleaned_data['phone']
            bio = form.cleaned_data['bio']
            gender = form.cleaned_data['gender']
            cv = form.cleaned_data['cv']
            
            user.profile.age = age
            user.profile.n_code = n_code
            user.profile.gender = gender
            user.profile.phone = phone
            user.profile.bio = bio
            if cv:
                user.profile.cv = cv
            
            form.save()
            messages.success(request, "پروفایل با موفقیت بروزرسانی شد ")
            return redirect('account:profile')
    context["form"] = form
    return render(request, template_name, context)


#Signup's form 
def signup_view(request):
    if request.user.is_authenticated :
        return redirect('account:profile')
    template_name = 'Account/signup.html'
    context = {}
    form = SignupForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            age = form.cleaned_data['age']
            n_code = form.cleaned_data['n_code']
            phone = form.cleaned_data['phone']
            gender = form.cleaned_data['gender']
            cv = form.cleaned_data['cv']
            
            user.profile.age = age
            user.profile.n_code = n_code
            user.profile.gender = gender
            user.profile.phone = phone
            if cv:
                user.profile.cv = cv
            user.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, "اکانت جدید با موفقیت ساخته شد ")
            return redirect('account:profile')
    context["form"] = form
    return render(request, template_name, context)