from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from Django import models as m
from django.template import Context, loader

from django.shortcuts import render, redirect

# Import reverse_lazy method for reversing names to URLs
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# @login_required
def home(request):
    posts = m.Post.objects.all()
    users = m.Register.objects.all()
    template = loader.get_template('index.html')
    context = Context({
        'post_list': posts,
        'user_list': users

    })
    return HttpResponse(template.render(context))


def index(request):
  # The current user object is available as request.user. If the
  # user is authenticated, is_authenticated() method of the User
  # object returns True, else it returns False. If the user is logged in
  # redirect to the home page, else to the login page.
  # reverse_lazy() method takes a URL pattern name and returns the URL path.
  # Here it is used to get the URL paths of home and login pages.
  if request.user.is_authenticated():
    return redirect(reverse_lazy('newHome'))
  else:
    return redirect(reverse_lazy('login'))


