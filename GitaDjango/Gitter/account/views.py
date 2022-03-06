from django.shortcuts import render
from .forms import UserForm, AuthorForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout


@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('blog:home'))


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('blog:home'))

            else:
                return HttpResponse("Account Not Active")
        else:
            print('Somone try login, Failed')
            print('username: {} and password {}'.format(username, password))
            return HttpResponse('Invalid credentials')
    else:
        return render(request, 'login.html')




def register(request):
    registered = False

    if  request.method == 'POST':
        user_form = UserForm(data=request.POST)
        author_form = AuthorForm(data=request.POST)

        if user_form.is_valid() and author_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            author = author_form.save(commit=False)
            author.user = user

            if 'picture' in request.FILES:
                author.picture = request.FILES['picture']

            author.save()

            registered = True
        else:
            print(user_form.errors, author_form.errors)
    else:
        user_form = UserForm()
        author_form = AuthorForm()

    return render(request, 'registration.html', {'registered':registered,
                                                'user_form':user_form,
                                                'author_form':author_form})

