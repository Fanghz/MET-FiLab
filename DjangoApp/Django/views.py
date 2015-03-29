from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from Django import models as m
from django.template import RequestContext, loader
from django.shortcuts import render, redirect
from django import forms
from Django.models import User 

# Import reverse_lazy method for reversing names to URLs
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.shortcuts import render_to_response
from django.db import connection

import datetime
import time
import json

'''
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
'''
def failedbanks(request):
    return render_to_response('failedbanks.html',{})

def test(request):
    return render_to_response('test.html',{})

def stockprice(request):
    if request.method == 'POST':
        start_date = request.POST.get('startDate','')
        end_date = request.POST.get('endDate','')
        symbol = request.POST.get('symbol', '')
        #Stock_Price
        stockprice = m.YahooStock.objects.filter(symbol=symbol, date__gte=start_date, date__lte=end_date)
        stocks = []
        for stock in stockprice:
            unix_date = int(time.mktime(stock.date.timetuple())*1000)
            stock = [unix_date,stock.open_price]
            stocks.append(stock)
        fp = open('static/js/stock.json','w+')
        json.dump(stocks,fp)
        fp.flush()
        #Sentiment
        senti_dict = dict();
        count_dict = dict();
        results = []
        year = start_date[0:4]
        sentiments = m.AlexEquity1999.objects.filter(ticker=symbol)
        if year == '1999':
            sentiments = m.AlexEquity1999.objects.filter(ticker=symbol, date__gte=start_date, date__lte=end_date)
        if year == '2000':
            sentiments = m.AlexEquity2000.objects.filter(ticker=symbol, date__gte=start_date, date__lte=end_date)
        if year == '2001':
            sentiments = m.AlexEquity2001.objects.filter(ticker=symbol, date__gte=start_date, date__lte=end_date)
        if year == '2002':
            sentiments = m.AlexEquity2002.objects.filter(ticker=symbol, date__gte=start_date, date__lte=end_date)
        if year == '2003':
            sentiments = m.AlexEquity2003.objects.filter(ticker=symbol, date__gte=start_date, date__lte=end_date)
        if year == '2004':
            sentiments = m.AlexEquity2004.objects.filter(ticker=symbol, date__gte=start_date, date__lte=end_date)
        if year == '2005':
            sentiments = m.AlexEquity2005.objects.filter(ticker=symbol, date__gte=start_date, date__lte=end_date)
        if year == '2006':
            sentiments = m.AlexEquity2006.objects.filter(ticker=symbol, date__gte=start_date, date__lte=end_date)
        if year == '2007':
            sentiments = m.AlexEquity2007.objects.filter(ticker=symbol, date__gte=start_date, date__lte=end_date)
        if year == '2008':
            sentiments = m.AlexEquity2008.objects.filter(ticker=symbol, date__gte=start_date, date__lte=end_date)
        if year == '2009':
            sentiments = m.AlexEquity2009.objects.filter(ticker=symbol, date__gte=start_date, date__lte=end_date)
        if year == '2010':
            sentiments = m.AlexEquity2010.objects.filter(ticker=symbol, date__gte=start_date, date__lte=end_date)
        if year == '2011':
            sentiments = m.AlexEquity2011.objects.filter(ticker=symbol, date__gte=start_date, date__lte=end_date)
        if year == '2012':
            sentiments = m.AlexEquity2012.objects.filter(ticker=symbol, date__gte=start_date, date__lte=end_date)
        if year == '2013':
            sentiments = m.AlexEquity2013.objects.filter(ticker=symbol, date__gte=start_date, date__lte=end_date)
        if year == '2014':
            sentiments = m.AlexEquity2014.objects.filter(ticker=symbol, date__gte=start_date, date__lte=end_date)
        for item in sentiments:
            date = int(time.mktime(item.date.timetuple())*1000)
            minute_sentiment = item.sentiment * item.confidence * item.relevance / item.novelty
            if(date in senti_dict):
                senti_dict[date] += minute_sentiment
                count_dict[date] += 1
            else:
                senti_dict[date] = minute_sentiment
                count_dict[date] = 1
        for key in sorted(senti_dict):
            senti_dict[key] /= count_dict[key]
            result = [key,senti_dict[key]]
            results.append(result)
        fp = open('static/js/sentiment.json','w+')
        json.dump(results,fp)
        fp.flush()
        return render_to_response('failedbanks.html', {})
    #    js_stock = json.dumps(stocks)
    #    return HttpResponse(json.dumps(stocks),content_type="application/json")
    #    return render_to_response('results.html', {
    #        'stockprice':js_stock
    #        })
           

class UserForm(forms.Form):
    username = forms.CharField(label='Username:',max_length=100)
    password = forms.CharField(label='Password:',widget=forms.PasswordInput())
    email = forms.CharField(label='Email:')

def register(request):
    if request.method == "POST":
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            email = uf.cleaned_data['email']
            user = User()
            user.username = username
            user.password = password
            user.email = email
            user.save()
            return render_to_response('success.html',{'username':username})
    else:
        uf = UserForm()
    return render_to_response('register.html',{'uf':uf})

def login(request):
    if request.method == 'POST':
        uf = UserForm(request.POST)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            user = User.objects.filter(username__exact = username,password__exact = password)
            if user:
                return render_to_response('failedbanks.html',{'username':username})
            else:
                return HttpResponseRedirect('/login/')
    else:
        uf = UserForm()
    return render_to_response('login.html',{'uf':uf})
