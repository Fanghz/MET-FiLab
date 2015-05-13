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
import math

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


def index(request):
    return render_to_response('index.html',{'stock_show':'false','worldbank_show':'false'})
    '''
    if request.method == 'POST':
        if request.POST.get('datasource','') == 'yahoo':
            start_date = request.POST.get('startDate','')
            end_date = request.POST.get('endDate','')
            symbol = request.POST.get('symbol', '')
            #Stock_Price
            stockprice = m.YahooStock.objects.filter(symbol=symbol, date__gte=start_date, date__lte=end_date)
            stocks = []
            daily_returns = []
            for stock in stockprice:
                unix_date = int(time.mktime(stock.date.timetuple())*1000)
                eachstock = [unix_date,stock.open_price]
                stocks.append(eachstock)
                daily_return = [unix_date,math.log(stock.close_price/stock.open_price)]
                daily_returns.append(daily_return)
            fp = open('static/js/stock.json','w+')
            json.dump(stocks,fp)
            fp.flush()
            fp = open('static/js/daily.json','w+')
            json.dump(daily_returns,fp)
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
                minute_sentiment = (item.sentiment * item.confidence * item.relevance / item.novelty)
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
            #return render_to_response('index.html', {'stock_price':stockprice,'stock_show':'true','worldbank_show':'false'})
            callback = request.GET['callback']
            li = []
            return HttpResponse('%s(%s)'%(callback, json.dumps(li))) 
        else:
            countries = request.POST.getlist('country')
            indicators = request.POST.getlist('indicator')
            cursor = connection.cursor()
            if len(countries)==1 and len(indicators)>=1:
                multiIndicators = []
                country = countries[0]
                for indicator in indicators:
                    indi = []
                    year_indi = dict()
                    for x in range(1960,2014):
                        year_indi[x] = 0
                    cursor.execute("select year from worldbank_series as S, worldbank_devindicator as D where D.country=%s and S.code=D.series and D.data is not null and name=%s",[country,indicator])
                    fetchall = cursor.fetchall()
                    for year in fetchall:
                        index = int(year[0])
                        year_indi[index] += 1
                    for key in sorted(year_indi):
                        indi.append(year_indi[key])
                    multiIndicators.append(indi)
                fp = open('static/js/aaaaa.json','w+')
                json.dump(multiIndicators,fp)
                fp.flush()
                return render_to_response('index.html', {})
                
            cursor = connection.cursor()
            cursor.execute("select country,series,year,topic from worldbank_devindicator as D, worldbank_series as S  where D.data IS NOT NULL and D.series=S.code and topic like %s and country=%s",[topic,country])
            fetchall = cursor.fetchall()

            indicators = []
            year_dict = dict();
            for obj in fetchall:
                if(obj[2] in year_dict):
                    year_dict[obj[2]] += 1
                else:
                    year_dict[obj[2]] = 1
            for key in sorted(year_dict):
                epoch = datetime.datetime(1970, 1, 1)
                t = datetime.datetime(key, 1, 1)
                diff = t-epoch
                unix_date = (diff.days*24*3600+5*3600)*1000
                year_count = [unix_date,year_dict[key]]
                indicators.append(year_count)
            fp = open('static/js/indicator.json','w+')
            json.dump(indicators,fp)
            fp.flush()
            return render_to_response('index.html', {'stock_show':'false','worldbank_show':'true'})
    else:
    '''

def getstockform(request):
    start_date = request.GET.get('startDate','')
    end_date = request.GET.get('endDate','')
    symbol = request.GET.get('symbol', '')
    #Stock_Price
    cursor = connection.cursor()
    cursor.execute("select symbol,exchange_symbol,date,open_price,high_price,low_price,close_price,volume,adj_close from yahoo_stock where symbol=%s and date>=%s and date<=%s",[symbol,start_date,end_date])
    fetchall = cursor.fetchall()
    stocks = []
    for stock in fetchall:
        each_stock_row = [stock[0],stock[1],stock[2].strftime('%Y-%m-%d'),stock[3],stock[4],stock[5],stock[6],stock[7],stock[8]]
        stocks.append(each_stock_row)
    callback = request.GET['callback']
    return HttpResponse('%s(%s)'%(callback, json.dumps(stocks)))    

def getsentimentform(request):
    start_date = request.GET.get('startDate','')
    end_date = request.GET.get('endDate','')
    symbol = request.GET.get('symbol', '')
    senti_dict = dict()
    count_dict = dict()
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
        #date = int(time.mktime(item.date.timetuple())*1000)
        date = str(item.date)
        minute_sentiment = (item.sentiment * item.confidence * item.relevance / item.novelty)
        rowid = item.rowid
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
    print results
    callback = request.GET['callback']
    return HttpResponse('%s(%s)'%(callback, json.dumps(results)))

def getformindicator(request):
    countries = request.GET.getlist('country')
    indicators = request.GET.getlist('indicator')
    cursor = connection.cursor()
    res = []
    if len(countries)==1 and len(indicators)>=1:
        for indicator in indicators:
            cursor.execute("select name,year,data,country from worldbank_devindicator as D,worldbank_series as S where D.series=S.code and name=%s and country=%s and D.data IS NOT NULL;",[indicator,countries[0]])
            fetchall = cursor.fetchall()
            for obj in fetchall:
                row = []
                row.append(obj[0])
                row.append(obj[1])
                row.append(obj[2])
                row.append(obj[3])
                res.append(row)
        fp = open('static/js/ccccc.json','w+')
        json.dump(res,fp)
        fp.flush()
        callback = request.GET['callback']
        return HttpResponse('%s(%s)'%(callback, json.dumps(res)))
    elif len(countries)>1 and len(indicators)==1:
        indicator = indicators[0]
        print 1111111111111
        print indicator
        print 111111111111
        for country in countries:
            print country
            cursor.execute("select name,year,data,country from worldbank_devindicator as D,worldbank_series as S where D.series=S.code and name=%s and country=%s and D.data IS NOT NULL;",[indicator,country])
            fetchall = cursor.fetchall()
            for obj in fetchall:
                row = []
                row.append(obj[0])
                row.append(obj[1])
                row.append(obj[2])
                row.append(obj[3])
                res.append(row)
        print res
        fp = open('static/js/dddddddd.json','w+')
        json.dump(res,fp)
        fp.flush()
        callback = request.GET['callback']
        return HttpResponse('%s(%s)'%(callback, json.dumps(res)))

def getstockprice(request):
    start_date = request.GET.get('startDate','')
    end_date = request.GET.get('endDate','')
    symbol = request.GET.get('symbol', '')
    #Stock_Price
    stockprice = m.YahooStock.objects.filter(symbol=symbol, date__gte=start_date, date__lte=end_date)
    sentiment_stock_result = []
    stocks = []
    for stock in stockprice:
        unix_date = int(time.mktime(stock.date.timetuple())*1000)
        eachstock = [unix_date,stock.open_price]
        stocks.append(eachstock)
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
        minute_sentiment = (item.sentiment * item.confidence * item.relevance / item.novelty)
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
    sentiment_stock_result.append(results)
    sentiment_stock_result.append(stocks)
    callback = request.GET['callback']
    return HttpResponse('%s(%s)'%(callback, json.dumps(sentiment_stock_result)))

def getsentiment(request):
    start_date = request.GET.get('startDate','')
    end_date = request.GET.get('endDate','')
    symbol = request.GET.get('symbol', '')
    #Stock_Price
    stockprice = m.YahooStock.objects.filter(symbol=symbol, date__gte=start_date, date__lte=end_date)
    sentiment_daily_result = []
    daily_returns = []
    for stock in stockprice:
        unix_date = int(time.mktime(stock.date.timetuple())*1000)
        daily_return = [unix_date,math.log(stock.close_price/stock.open_price)]
        daily_returns.append(daily_return)
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
        minute_sentiment = (item.sentiment * item.confidence * item.relevance / item.novelty)
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
    sentiment_daily_result.append(results)
    sentiment_daily_result.append(daily_returns)
    callback = request.GET['callback']
    return HttpResponse('%s(%s)'%(callback, json.dumps(sentiment_daily_result))) 

'''
def gettopicerror(request):
    if request.method == 'POST':
        if request.POST.get('datasource','') == 'worldbank':
            topic = request.POST.get('topic','')
            topic = '%' + topic + '%'
            country = request.POST.get('country','')
            start_date = request.POST.get('startDate','')
            end_date = request.POST.get('endDate','')

            cursor = connection.cursor()
            cursor.execute("select country,series,year,topic from worldbank_devindicator as D, worldbank_series as S  where D.data IS NOT NULL and D.series=S.code and topic like %s and country=%s",[topic,country])
            fetchall = cursor.fetchall()

            indicators = []
            year_dict = dict();
            for obj in fetchall:
                if(obj[2] in year_dict):
                    year_dict[obj[2]] += 1
                else:
                    year_dict[obj[2]] = 1
            for key in sorted(year_dict):
                epoch = datetime.datetime(1970, 1, 1)
                t = datetime.datetime(key, 1, 1)
                diff = t-epoch
                unix_date = (diff.days*24*3600+5*3600)*1000
                year_count = [unix_date,year_dict[key]]
                indicators.append(year_count)
            fp = open('static/js/indicator.json','w+')
            json.dump(indicators,fp)
            fp.flush()
            return render_to_response('failedbanks.html', {'stock_show':'false','worldbank_show':'true'})

def gettopic(request):
    test = m.WorldbankSeries.objects.order_by().values('topic').distinct()
    li = []
    for one in test:
        li.append(one)
    fp = open('static/js/tttttt.json','w+')
    json.dump(li,fp)
    fp.flush()
    return HttpResponse(json.dump(li))
'''

def getcountry(request):
    test = m.WorldbankCountry.objects.order_by('short_name')
    li = []
    for one in test:
        d = {}
        d['label'] = one.code
        d['name'] = one.short_name
        li.append(d)
    print li
    fp = open('static/js/country.json','w+')
    json.dump(li,fp)
    fp.flush()
    callback = request.GET['callback']
    return HttpResponse('%s(%s)'%(callback, json.dumps(li)))


def indicator(request):
    topics = request.GET.getlist('topics')
    indicator_filter = request.GET.getlist('filter')
    li = []
    indi_dict = dict();
    cursor = connection.cursor()
    if len(indicator_filter) ==0:
        for topic in topics:
            cursor.execute("select name from worldbank_series where topic=%s",[topic])
            fetchall = cursor.fetchall()
            for obj in fetchall:
                if obj[0] not in indi_dict:
                    indi_dict[obj[0]]=1;
                    indicators = {}
                    indicators['indicator'] = obj[0]
                    li.append(indicators)
    elif len(indicator_filter)>0:
        indi_filter = '%' + indicator_filter[0] + '%'
        for topic in topics:
            cursor.execute("select name from worldbank_series where topic=%s and name like %s",[topic,indi_filter])
            fetchall = cursor.fetchall()
            for obj in fetchall:
                if obj[0] not in indi_dict:
                    indi_dict[obj[0]]=1;
                    indicators = {}
                    indicators['indicator'] = obj[0]
                    li.append(indicators)
    callback = request.GET['callback']
    return HttpResponse('%s(%s)'%(callback, json.dumps(li))) 

def getindicator(request):
    countries = request.GET.getlist('country')
    indicators = request.GET.getlist('indicator')
    cursor = connection.cursor()
    if len(countries)==1 and len(indicators)>=1:
        multiIndicators = []
        country = countries[0]
        indicatorIndex = []
        for indicator in indicators:
            indicatorIndex.append(indicator)
        multiIndicators.append(indicatorIndex)
        for indicator in indicators:
            indi = []
            year_indi = dict()
            for x in range(1960,2014):
                year_indi[x] = 0
            cursor.execute("select year,data from worldbank_series as S, worldbank_devindicator as D where D.country=%s and S.code=D.series and D.data is not null and name=%s",[country,indicator])
            fetchall = cursor.fetchall()
            for obj in fetchall:
                index = int(obj[0])
                year_indi[index] = obj[1]
            for key in sorted(year_indi):
                indi.append(year_indi[key])
            multiIndicators.append(indi)
        for country in countries:
            cursor.execute("select short_name from worldbank_country where code=%s",[country])
            fetchall = cursor.fetchall()
            for country_name in fetchall:
                multiIndicators.append(country_name)
        fp = open('static/js/aaaaa.json','w+')
        json.dump(multiIndicators,fp)
        fp.flush()
        callback = request.GET['callback']
        return HttpResponse('%s(%s)'%(callback, json.dumps(multiIndicators)))
    elif len(countries)>1 and len(indicators)==1:
        multiCountries = []
        indicator = indicators[0]
        countryIndex = []
        for country in countries:
            cursor.execute("select short_name from worldbank_country where code=%s",[country])
            fetchall = cursor.fetchall()
            for country_name in fetchall:
                countryIndex.append(country_name)
        multiCountries.append(countryIndex)
        for country in countries:
            indi = []
            year_indi = dict()
            for x in range(1960,2014):
                year_indi[x] = 0
            cursor.execute("select year,data from worldbank_series as S, worldbank_devindicator as D where D.country=%s and S.code=D.series and D.data is not null and name=%s",[country,indicator])
            fetchall = cursor.fetchall()
            for obj in fetchall:
                index = int(obj[0])
                year_indi[index] = obj[1]
            for key in sorted(year_indi):
                indi.append(year_indi[key])
            multiCountries.append(indi)
        multiCountries.append(indicator)
        fp = open('static/js/bbbbb.json','w+')
        json.dump(multiCountries,fp)
        fp.flush()
        callback = request.GET['callback']
        return HttpResponse('%s(%s)'%(callback, json.dumps(multiCountries)))

def g20(request):
    return render_to_response('g20.html',{})

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
