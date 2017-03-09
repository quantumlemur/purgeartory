from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm, UserCreationForm

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data.get('username'),
                password=form.cleaned_data.get('password1')
            )
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def home(request):
    if request.user.is_authenticated():
        return redirect('/loggedin')
    return render(request, 'core/home.html')

@login_required
def loggedin(request):
    return render(request, 'core/login_landing.html')

def whoami(request):
    return render(request, 'core/home.html')