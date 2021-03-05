from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserCreationForm
from django.http import HttpResponse, HttpResponseRedirect

def signup(request):
    """ 계정생성 """

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            id = form.cleaned_data.get('userID')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(userID=id, password=raw_password)
            login(request, user)
            return HttpResponseRedirect(request.POST['index'])
            # return redirect('alit:index')
    else:
        form = UserCreationForm()
    return render(request, 'common/signup.html', {'form': form})

def profile(request):
    """ 프로필 수정 """

