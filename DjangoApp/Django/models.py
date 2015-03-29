# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.contrib import admin


class DjangoComment(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    message = models.TextField(blank=True)
    created_at = models.DateTimeField()
    post = models.ForeignKey('DjangoPost')

    class Meta:
        managed = False
        db_table = 'Django_comment'


class DjangoPost(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content = models.CharField(max_length=256)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Django_post'


class DjangoRegister(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Django_register'
        

class User(models.Model):
    username = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    email = models.EmailField()

admin.site.register(User)

class UnComtrade(models.Model):
    period = models.TextField(db_column='Period')  # Field name made lowercase. This field type is a guess.
    tradeflow = models.CharField(db_column='TradeFlow', max_length=6)  # Field name made lowercase.
    reporter = models.CharField(db_column='Reporter', max_length=60)  # Field name made lowercase.
    partner = models.CharField(db_column='Partner', max_length=60)  # Field name made lowercase.
    commoditycode = models.CharField(db_column='CommodityCode', max_length=10)  # Field name made lowercase.
    commoditydescription = models.CharField(db_column='CommodityDescription', max_length=60, blank=True)  # Field name made lowercase.
    tradevalue = models.IntegerField(db_column='TradeValue', blank=True, null=True)  # Field name made lowercase.
    netweight = models.IntegerField(db_column='NetWeight', blank=True, null=True)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=45, blank=True)  # Field name made lowercase.
    tradequantity = models.IntegerField(db_column='TradeQuantity', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(db_column='Flag', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UN_Comtrade'


class AlexCountry(models.Model):
    country = models.CharField(primary_key=True, max_length=5)
    country_name = models.CharField(max_length=50, blank=True)
    iso2code = models.CharField(max_length=5, blank=True)
    stock_exchange_symbol = models.CharField(max_length=30, blank=True)

    class Meta:
        managed = False
        db_table = 'alex_country'


class AlexEconomicindex(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_economicindex_'


class AlexEconomicindex1999(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_economicindex_1999'


class AlexEconomicindex2000(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_economicindex_2000'


class AlexEconomicindex2001(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_economicindex_2001'


class AlexEconomicindex2002(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_economicindex_2002'


class AlexEconomicindex2003(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_economicindex_2003'


class AlexEconomicindex2004(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_economicindex_2004'


class AlexEconomicindex2005(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_economicindex_2005'


class AlexEconomicindex2006(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_economicindex_2006'


class AlexEconomicindex2007(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_economicindex_2007'


class AlexEconomicindex2008(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_economicindex_2008'


class AlexEconomicindex2009(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_economicindex_2009'


class AlexEconomicindex2010(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_economicindex_2010'


class AlexEconomicindex2011(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_economicindex_2011'


class AlexEconomicindex2012(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    rowid = models.CharField(primary_key=True, unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_economicindex_2012'
 #       unique_together = ('newsid', 'timestamp','country')


class AlexEconomicindex2013(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_economicindex_2013'


class AlexEconomicindex2014(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_economicindex_2014'


class AlexEquity(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    ticker = models.CharField(max_length=15)
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    subjects = models.CharField(max_length=100)
    relevance = models.FloatField()
    rowid = models.CharField(primary_key=True,unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_equity_'


class AlexEquity1999(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    ticker = models.CharField(max_length=15)
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    subjects = models.CharField(max_length=100)
    relevance = models.FloatField()
    rowid = models.CharField(primary_key=True,unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_equity_1999'


class AlexEquity2000(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    ticker = models.CharField(max_length=15)
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    subjects = models.CharField(max_length=100)
    relevance = models.FloatField()
    rowid = models.CharField(primary_key=True,unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_equity_2000'


class AlexEquity2001(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    ticker = models.CharField(max_length=15)
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    subjects = models.CharField(max_length=100)
    relevance = models.FloatField()
    rowid = models.CharField(primary_key=True,unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_equity_2001'


class AlexEquity2002(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    ticker = models.CharField(max_length=15)
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    subjects = models.CharField(max_length=100)
    relevance = models.FloatField()
    rowid = models.CharField(primary_key=True,unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_equity_2002'


class AlexEquity2003(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    ticker = models.CharField(max_length=15)
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    subjects = models.CharField(max_length=100)
    relevance = models.FloatField()
    rowid = models.CharField(primary_key=True,unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_equity_2003'


class AlexEquity2004(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    ticker = models.CharField(max_length=15)
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    subjects = models.CharField(max_length=100)
    relevance = models.FloatField()
    rowid = models.CharField(primary_key=True,unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_equity_2004'


class AlexEquity2005(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    ticker = models.CharField(max_length=15)
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    subjects = models.CharField(max_length=100)
    relevance = models.FloatField()
    rowid = models.CharField(primary_key=True,unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_equity_2005'


class AlexEquity2006(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    ticker = models.CharField(max_length=15)
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    subjects = models.CharField(max_length=100)
    relevance = models.FloatField()
    rowid = models.CharField(primary_key=True,unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_equity_2006'


class AlexEquity2007(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    ticker = models.CharField(max_length=15)
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    subjects = models.CharField(max_length=100)
    relevance = models.FloatField()
    rowid = models.CharField(primary_key=True,unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_equity_2007'


class AlexEquity2008(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    ticker = models.CharField(max_length=15)
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    subjects = models.CharField(max_length=100)
    relevance = models.FloatField()
    rowid = models.CharField(primary_key=True,unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_equity_2008'


class AlexEquity2009(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    ticker = models.CharField(max_length=15)
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    subjects = models.CharField(max_length=100)
    relevance = models.FloatField()
    rowid = models.CharField(primary_key=True,unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_equity_2009'


class AlexEquity2010(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    ticker = models.CharField(max_length=15)
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    subjects = models.CharField(max_length=100)
    relevance = models.FloatField()
    rowid = models.CharField(primary_key=True,unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_equity_2010'


class AlexEquity2011(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    ticker = models.CharField(max_length=15)
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    subjects = models.CharField(max_length=100)
    relevance = models.FloatField()
    rowid = models.CharField(primary_key=True,unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_equity_2011'


class AlexEquity2012(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    ticker = models.CharField(max_length=15)
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    subjects = models.CharField(max_length=100)
    relevance = models.FloatField()
    rowid = models.CharField(primary_key=True,unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_equity_2012'


class AlexEquity2013(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    ticker = models.CharField(max_length=15)
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    subjects = models.CharField(max_length=100)
    relevance = models.FloatField()
    rowid = models.CharField(primary_key=True,unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_equity_2013'


class AlexEquity2014(models.Model):
    newsid = models.CharField(db_column='newsID', max_length=50)  # Field name made lowercase.
    timestamp = models.DateTimeField()
    ticker = models.CharField(max_length=15)
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    sentiment = models.IntegerField()
    confidence = models.FloatField()
    novelty = models.IntegerField()
    subjects = models.CharField(max_length=100)
    relevance = models.FloatField()
    rowid = models.CharField(primary_key=True,unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'alex_equity_2014'


class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup)
    permission = models.ForeignKey('AuthPermission')

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=50)
    content_type = models.ForeignKey('DjangoContentType')
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField()
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=75)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    group = models.ForeignKey(AuthGroup)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser)
    permission = models.ForeignKey(AuthPermission)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.IntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', blank=True, null=True)
    user = models.ForeignKey(AuthUser)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=100)
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'


class DjangoMigrations(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Eurostoxx50(models.Model):
    ticker = models.CharField(max_length=10, blank=True)
    exchange_center = models.CharField(max_length=10, blank=True)

    class Meta:
        managed = False
        db_table = 'eurostoxx50'


class FdicBanklist(models.Model):
    stname = models.CharField(max_length=30, blank=True)
    cert = models.CharField(primary_key=True, max_length=5)
    active = models.IntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=30, blank=True)
    dateupdt = models.DateField(blank=True, null=True)
    effdate = models.DateField(blank=True, null=True)
    endefymd = models.CharField(max_length=10, blank=True)
    estymd = models.CharField(max_length=10, blank=True)
    inactive = models.IntegerField(blank=True, null=True)
    insdate = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True)
    newcert = models.CharField(max_length=5, blank=True)
    stalp = models.CharField(max_length=2, blank=True)
    stcnty = models.CharField(max_length=5, blank=True)
    webaddr = models.CharField(max_length=50, blank=True)
    zip = models.CharField(max_length=5, blank=True)
    county = models.CharField(max_length=20, blank=True)
    rowid = models.CharField(unique=True, max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'fdic_banklist'


class ThomCountry(models.Model):
    country = models.CharField(primary_key=True, max_length=5)
    country_name = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'thom_country'


class ThomCurrency(models.Model):
    currency = models.CharField(primary_key=True, max_length=5)
    currency_name = models.CharField(max_length=50, blank=True)

    class Meta:
        managed = False
        db_table = 'thom_currency'


class ThomDailycountry(models.Model):
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    marketrisk = models.FloatField(blank=True, null=True)
    tradebalance = models.FloatField(blank=True, null=True)
    budgetdeficit = models.FloatField(blank=True, null=True)
    centralbank = models.FloatField(blank=True, null=True)
    consumersentiment = models.FloatField(blank=True, null=True)
    crediteasytight = models.FloatField(blank=True, null=True)
    ddefault = models.FloatField(blank=True, null=True)
    economicconflict = models.FloatField(blank=True, null=True)
    economicgrowth = models.FloatField(blank=True, null=True)
    economicuncertainty = models.FloatField(blank=True, null=True)
    electionsentiment = models.FloatField(blank=True, null=True)
    financialinstability = models.FloatField(blank=True, null=True)
    fiscalpolicyloosetight = models.FloatField(blank=True, null=True)
    govanger = models.FloatField(blank=True, null=True)
    govcorruption = models.FloatField(blank=True, null=True)
    govinstability = models.FloatField(blank=True, null=True)
    inflation = models.FloatField(blank=True, null=True)
    interestrate = models.FloatField(blank=True, null=True)
    investmentflow = models.FloatField(blank=True, null=True)
    monetarypolicyloosetight = models.FloatField(blank=True, null=True)
    naturaldisaster = models.FloatField(blank=True, null=True)
    regimechange = models.FloatField(blank=True, null=True)
    socialinequality = models.FloatField(blank=True, null=True)
    socialunrest = models.FloatField(blank=True, null=True)
    unemployment = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_dailycountry'


class ThomDailycurrency(models.Model):
    currency = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    priceforecast = models.FloatField(blank=True, null=True)
    carrytrade = models.FloatField(blank=True, null=True)
    currencypeginstability = models.FloatField(blank=True, null=True)
    pricemomentum = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_dailycurrency'


class ThomMinutecountry(models.Model):
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    marketrisk = models.FloatField(blank=True, null=True)
    tradebalance = models.FloatField(blank=True, null=True)
    budgetdeficit = models.FloatField(blank=True, null=True)
    centralbank = models.FloatField(blank=True, null=True)
    consumersentiment = models.FloatField(blank=True, null=True)
    crediteasytight = models.FloatField(blank=True, null=True)
    defaults = models.FloatField(blank=True, null=True)
    economicconflict = models.FloatField(blank=True, null=True)
    economicgrowth = models.FloatField(blank=True, null=True)
    economicuncertainty = models.FloatField(blank=True, null=True)
    electionsentiment = models.FloatField(blank=True, null=True)
    financialinstability = models.FloatField(blank=True, null=True)
    fiscalpolicyloosetight = models.FloatField(blank=True, null=True)
    govanger = models.FloatField(blank=True, null=True)
    govcorruption = models.FloatField(blank=True, null=True)
    govinstability = models.FloatField(blank=True, null=True)
    inflation = models.FloatField(blank=True, null=True)
    interestrate = models.FloatField(blank=True, null=True)
    investmentflow = models.FloatField(blank=True, null=True)
    monetarypolicyloosetight = models.FloatField(blank=True, null=True)
    naturaldisaster = models.FloatField(blank=True, null=True)
    regimechange = models.FloatField(blank=True, null=True)
    socialinequality = models.FloatField(blank=True, null=True)
    socialunrest = models.FloatField(blank=True, null=True)
    unemployment = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecountry_'


class ThomMinutecountry1998(models.Model):
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    marketrisk = models.FloatField(blank=True, null=True)
    tradebalance = models.FloatField(blank=True, null=True)
    budgetdeficit = models.FloatField(blank=True, null=True)
    centralbank = models.FloatField(blank=True, null=True)
    consumersentiment = models.FloatField(blank=True, null=True)
    crediteasytight = models.FloatField(blank=True, null=True)
    defaults = models.FloatField(blank=True, null=True)
    economicconflict = models.FloatField(blank=True, null=True)
    economicgrowth = models.FloatField(blank=True, null=True)
    economicuncertainty = models.FloatField(blank=True, null=True)
    electionsentiment = models.FloatField(blank=True, null=True)
    financialinstability = models.FloatField(blank=True, null=True)
    fiscalpolicyloosetight = models.FloatField(blank=True, null=True)
    govanger = models.FloatField(blank=True, null=True)
    govcorruption = models.FloatField(blank=True, null=True)
    govinstability = models.FloatField(blank=True, null=True)
    inflation = models.FloatField(blank=True, null=True)
    interestrate = models.FloatField(blank=True, null=True)
    investmentflow = models.FloatField(blank=True, null=True)
    monetarypolicyloosetight = models.FloatField(blank=True, null=True)
    naturaldisaster = models.FloatField(blank=True, null=True)
    regimechange = models.FloatField(blank=True, null=True)
    socialinequality = models.FloatField(blank=True, null=True)
    socialunrest = models.FloatField(blank=True, null=True)
    unemployment = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecountry_1998'


class ThomMinutecountry1999(models.Model):
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    marketrisk = models.FloatField(blank=True, null=True)
    tradebalance = models.FloatField(blank=True, null=True)
    budgetdeficit = models.FloatField(blank=True, null=True)
    centralbank = models.FloatField(blank=True, null=True)
    consumersentiment = models.FloatField(blank=True, null=True)
    crediteasytight = models.FloatField(blank=True, null=True)
    defaults = models.FloatField(blank=True, null=True)
    economicconflict = models.FloatField(blank=True, null=True)
    economicgrowth = models.FloatField(blank=True, null=True)
    economicuncertainty = models.FloatField(blank=True, null=True)
    electionsentiment = models.FloatField(blank=True, null=True)
    financialinstability = models.FloatField(blank=True, null=True)
    fiscalpolicyloosetight = models.FloatField(blank=True, null=True)
    govanger = models.FloatField(blank=True, null=True)
    govcorruption = models.FloatField(blank=True, null=True)
    govinstability = models.FloatField(blank=True, null=True)
    inflation = models.FloatField(blank=True, null=True)
    interestrate = models.FloatField(blank=True, null=True)
    investmentflow = models.FloatField(blank=True, null=True)
    monetarypolicyloosetight = models.FloatField(blank=True, null=True)
    naturaldisaster = models.FloatField(blank=True, null=True)
    regimechange = models.FloatField(blank=True, null=True)
    socialinequality = models.FloatField(blank=True, null=True)
    socialunrest = models.FloatField(blank=True, null=True)
    unemployment = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecountry_1999'


class ThomMinutecountry2000(models.Model):
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    marketrisk = models.FloatField(blank=True, null=True)
    tradebalance = models.FloatField(blank=True, null=True)
    budgetdeficit = models.FloatField(blank=True, null=True)
    centralbank = models.FloatField(blank=True, null=True)
    consumersentiment = models.FloatField(blank=True, null=True)
    crediteasytight = models.FloatField(blank=True, null=True)
    defaults = models.FloatField(blank=True, null=True)
    economicconflict = models.FloatField(blank=True, null=True)
    economicgrowth = models.FloatField(blank=True, null=True)
    economicuncertainty = models.FloatField(blank=True, null=True)
    electionsentiment = models.FloatField(blank=True, null=True)
    financialinstability = models.FloatField(blank=True, null=True)
    fiscalpolicyloosetight = models.FloatField(blank=True, null=True)
    govanger = models.FloatField(blank=True, null=True)
    govcorruption = models.FloatField(blank=True, null=True)
    govinstability = models.FloatField(blank=True, null=True)
    inflation = models.FloatField(blank=True, null=True)
    interestrate = models.FloatField(blank=True, null=True)
    investmentflow = models.FloatField(blank=True, null=True)
    monetarypolicyloosetight = models.FloatField(blank=True, null=True)
    naturaldisaster = models.FloatField(blank=True, null=True)
    regimechange = models.FloatField(blank=True, null=True)
    socialinequality = models.FloatField(blank=True, null=True)
    socialunrest = models.FloatField(blank=True, null=True)
    unemployment = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecountry_2000'


class ThomMinutecountry2001(models.Model):
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    marketrisk = models.FloatField(blank=True, null=True)
    tradebalance = models.FloatField(blank=True, null=True)
    budgetdeficit = models.FloatField(blank=True, null=True)
    centralbank = models.FloatField(blank=True, null=True)
    consumersentiment = models.FloatField(blank=True, null=True)
    crediteasytight = models.FloatField(blank=True, null=True)
    defaults = models.FloatField(blank=True, null=True)
    economicconflict = models.FloatField(blank=True, null=True)
    economicgrowth = models.FloatField(blank=True, null=True)
    economicuncertainty = models.FloatField(blank=True, null=True)
    electionsentiment = models.FloatField(blank=True, null=True)
    financialinstability = models.FloatField(blank=True, null=True)
    fiscalpolicyloosetight = models.FloatField(blank=True, null=True)
    govanger = models.FloatField(blank=True, null=True)
    govcorruption = models.FloatField(blank=True, null=True)
    govinstability = models.FloatField(blank=True, null=True)
    inflation = models.FloatField(blank=True, null=True)
    interestrate = models.FloatField(blank=True, null=True)
    investmentflow = models.FloatField(blank=True, null=True)
    monetarypolicyloosetight = models.FloatField(blank=True, null=True)
    naturaldisaster = models.FloatField(blank=True, null=True)
    regimechange = models.FloatField(blank=True, null=True)
    socialinequality = models.FloatField(blank=True, null=True)
    socialunrest = models.FloatField(blank=True, null=True)
    unemployment = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecountry_2001'


class ThomMinutecountry2002(models.Model):
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    marketrisk = models.FloatField(blank=True, null=True)
    tradebalance = models.FloatField(blank=True, null=True)
    budgetdeficit = models.FloatField(blank=True, null=True)
    centralbank = models.FloatField(blank=True, null=True)
    consumersentiment = models.FloatField(blank=True, null=True)
    crediteasytight = models.FloatField(blank=True, null=True)
    defaults = models.FloatField(blank=True, null=True)
    economicconflict = models.FloatField(blank=True, null=True)
    economicgrowth = models.FloatField(blank=True, null=True)
    economicuncertainty = models.FloatField(blank=True, null=True)
    electionsentiment = models.FloatField(blank=True, null=True)
    financialinstability = models.FloatField(blank=True, null=True)
    fiscalpolicyloosetight = models.FloatField(blank=True, null=True)
    govanger = models.FloatField(blank=True, null=True)
    govcorruption = models.FloatField(blank=True, null=True)
    govinstability = models.FloatField(blank=True, null=True)
    inflation = models.FloatField(blank=True, null=True)
    interestrate = models.FloatField(blank=True, null=True)
    investmentflow = models.FloatField(blank=True, null=True)
    monetarypolicyloosetight = models.FloatField(blank=True, null=True)
    naturaldisaster = models.FloatField(blank=True, null=True)
    regimechange = models.FloatField(blank=True, null=True)
    socialinequality = models.FloatField(blank=True, null=True)
    socialunrest = models.FloatField(blank=True, null=True)
    unemployment = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecountry_2002'


class ThomMinutecountry2003(models.Model):
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    marketrisk = models.FloatField(blank=True, null=True)
    tradebalance = models.FloatField(blank=True, null=True)
    budgetdeficit = models.FloatField(blank=True, null=True)
    centralbank = models.FloatField(blank=True, null=True)
    consumersentiment = models.FloatField(blank=True, null=True)
    crediteasytight = models.FloatField(blank=True, null=True)
    defaults = models.FloatField(blank=True, null=True)
    economicconflict = models.FloatField(blank=True, null=True)
    economicgrowth = models.FloatField(blank=True, null=True)
    economicuncertainty = models.FloatField(blank=True, null=True)
    electionsentiment = models.FloatField(blank=True, null=True)
    financialinstability = models.FloatField(blank=True, null=True)
    fiscalpolicyloosetight = models.FloatField(blank=True, null=True)
    govanger = models.FloatField(blank=True, null=True)
    govcorruption = models.FloatField(blank=True, null=True)
    govinstability = models.FloatField(blank=True, null=True)
    inflation = models.FloatField(blank=True, null=True)
    interestrate = models.FloatField(blank=True, null=True)
    investmentflow = models.FloatField(blank=True, null=True)
    monetarypolicyloosetight = models.FloatField(blank=True, null=True)
    naturaldisaster = models.FloatField(blank=True, null=True)
    regimechange = models.FloatField(blank=True, null=True)
    socialinequality = models.FloatField(blank=True, null=True)
    socialunrest = models.FloatField(blank=True, null=True)
    unemployment = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecountry_2003'


class ThomMinutecountry2004(models.Model):
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    marketrisk = models.FloatField(blank=True, null=True)
    tradebalance = models.FloatField(blank=True, null=True)
    budgetdeficit = models.FloatField(blank=True, null=True)
    centralbank = models.FloatField(blank=True, null=True)
    consumersentiment = models.FloatField(blank=True, null=True)
    crediteasytight = models.FloatField(blank=True, null=True)
    defaults = models.FloatField(blank=True, null=True)
    economicconflict = models.FloatField(blank=True, null=True)
    economicgrowth = models.FloatField(blank=True, null=True)
    economicuncertainty = models.FloatField(blank=True, null=True)
    electionsentiment = models.FloatField(blank=True, null=True)
    financialinstability = models.FloatField(blank=True, null=True)
    fiscalpolicyloosetight = models.FloatField(blank=True, null=True)
    govanger = models.FloatField(blank=True, null=True)
    govcorruption = models.FloatField(blank=True, null=True)
    govinstability = models.FloatField(blank=True, null=True)
    inflation = models.FloatField(blank=True, null=True)
    interestrate = models.FloatField(blank=True, null=True)
    investmentflow = models.FloatField(blank=True, null=True)
    monetarypolicyloosetight = models.FloatField(blank=True, null=True)
    naturaldisaster = models.FloatField(blank=True, null=True)
    regimechange = models.FloatField(blank=True, null=True)
    socialinequality = models.FloatField(blank=True, null=True)
    socialunrest = models.FloatField(blank=True, null=True)
    unemployment = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecountry_2004'


class ThomMinutecountry2005(models.Model):
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    marketrisk = models.FloatField(blank=True, null=True)
    tradebalance = models.FloatField(blank=True, null=True)
    budgetdeficit = models.FloatField(blank=True, null=True)
    centralbank = models.FloatField(blank=True, null=True)
    consumersentiment = models.FloatField(blank=True, null=True)
    crediteasytight = models.FloatField(blank=True, null=True)
    defaults = models.FloatField(blank=True, null=True)
    economicconflict = models.FloatField(blank=True, null=True)
    economicgrowth = models.FloatField(blank=True, null=True)
    economicuncertainty = models.FloatField(blank=True, null=True)
    electionsentiment = models.FloatField(blank=True, null=True)
    financialinstability = models.FloatField(blank=True, null=True)
    fiscalpolicyloosetight = models.FloatField(blank=True, null=True)
    govanger = models.FloatField(blank=True, null=True)
    govcorruption = models.FloatField(blank=True, null=True)
    govinstability = models.FloatField(blank=True, null=True)
    inflation = models.FloatField(blank=True, null=True)
    interestrate = models.FloatField(blank=True, null=True)
    investmentflow = models.FloatField(blank=True, null=True)
    monetarypolicyloosetight = models.FloatField(blank=True, null=True)
    naturaldisaster = models.FloatField(blank=True, null=True)
    regimechange = models.FloatField(blank=True, null=True)
    socialinequality = models.FloatField(blank=True, null=True)
    socialunrest = models.FloatField(blank=True, null=True)
    unemployment = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecountry_2005'


class ThomMinutecountry2006(models.Model):
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    marketrisk = models.FloatField(blank=True, null=True)
    tradebalance = models.FloatField(blank=True, null=True)
    budgetdeficit = models.FloatField(blank=True, null=True)
    centralbank = models.FloatField(blank=True, null=True)
    consumersentiment = models.FloatField(blank=True, null=True)
    crediteasytight = models.FloatField(blank=True, null=True)
    defaults = models.FloatField(blank=True, null=True)
    economicconflict = models.FloatField(blank=True, null=True)
    economicgrowth = models.FloatField(blank=True, null=True)
    economicuncertainty = models.FloatField(blank=True, null=True)
    electionsentiment = models.FloatField(blank=True, null=True)
    financialinstability = models.FloatField(blank=True, null=True)
    fiscalpolicyloosetight = models.FloatField(blank=True, null=True)
    govanger = models.FloatField(blank=True, null=True)
    govcorruption = models.FloatField(blank=True, null=True)
    govinstability = models.FloatField(blank=True, null=True)
    inflation = models.FloatField(blank=True, null=True)
    interestrate = models.FloatField(blank=True, null=True)
    investmentflow = models.FloatField(blank=True, null=True)
    monetarypolicyloosetight = models.FloatField(blank=True, null=True)
    naturaldisaster = models.FloatField(blank=True, null=True)
    regimechange = models.FloatField(blank=True, null=True)
    socialinequality = models.FloatField(blank=True, null=True)
    socialunrest = models.FloatField(blank=True, null=True)
    unemployment = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecountry_2006'


class ThomMinutecountry2007(models.Model):
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    marketrisk = models.FloatField(blank=True, null=True)
    tradebalance = models.FloatField(blank=True, null=True)
    budgetdeficit = models.FloatField(blank=True, null=True)
    centralbank = models.FloatField(blank=True, null=True)
    consumersentiment = models.FloatField(blank=True, null=True)
    crediteasytight = models.FloatField(blank=True, null=True)
    defaults = models.FloatField(blank=True, null=True)
    economicconflict = models.FloatField(blank=True, null=True)
    economicgrowth = models.FloatField(blank=True, null=True)
    economicuncertainty = models.FloatField(blank=True, null=True)
    electionsentiment = models.FloatField(blank=True, null=True)
    financialinstability = models.FloatField(blank=True, null=True)
    fiscalpolicyloosetight = models.FloatField(blank=True, null=True)
    govanger = models.FloatField(blank=True, null=True)
    govcorruption = models.FloatField(blank=True, null=True)
    govinstability = models.FloatField(blank=True, null=True)
    inflation = models.FloatField(blank=True, null=True)
    interestrate = models.FloatField(blank=True, null=True)
    investmentflow = models.FloatField(blank=True, null=True)
    monetarypolicyloosetight = models.FloatField(blank=True, null=True)
    naturaldisaster = models.FloatField(blank=True, null=True)
    regimechange = models.FloatField(blank=True, null=True)
    socialinequality = models.FloatField(blank=True, null=True)
    socialunrest = models.FloatField(blank=True, null=True)
    unemployment = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecountry_2007'


class ThomMinutecountry2008(models.Model):
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    marketrisk = models.FloatField(blank=True, null=True)
    tradebalance = models.FloatField(blank=True, null=True)
    budgetdeficit = models.FloatField(blank=True, null=True)
    centralbank = models.FloatField(blank=True, null=True)
    consumersentiment = models.FloatField(blank=True, null=True)
    crediteasytight = models.FloatField(blank=True, null=True)
    defaults = models.FloatField(blank=True, null=True)
    economicconflict = models.FloatField(blank=True, null=True)
    economicgrowth = models.FloatField(blank=True, null=True)
    economicuncertainty = models.FloatField(blank=True, null=True)
    electionsentiment = models.FloatField(blank=True, null=True)
    financialinstability = models.FloatField(blank=True, null=True)
    fiscalpolicyloosetight = models.FloatField(blank=True, null=True)
    govanger = models.FloatField(blank=True, null=True)
    govcorruption = models.FloatField(blank=True, null=True)
    govinstability = models.FloatField(blank=True, null=True)
    inflation = models.FloatField(blank=True, null=True)
    interestrate = models.FloatField(blank=True, null=True)
    investmentflow = models.FloatField(blank=True, null=True)
    monetarypolicyloosetight = models.FloatField(blank=True, null=True)
    naturaldisaster = models.FloatField(blank=True, null=True)
    regimechange = models.FloatField(blank=True, null=True)
    socialinequality = models.FloatField(blank=True, null=True)
    socialunrest = models.FloatField(blank=True, null=True)
    unemployment = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecountry_2008'


class ThomMinutecountry2009(models.Model):
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    marketrisk = models.FloatField(blank=True, null=True)
    tradebalance = models.FloatField(blank=True, null=True)
    budgetdeficit = models.FloatField(blank=True, null=True)
    centralbank = models.FloatField(blank=True, null=True)
    consumersentiment = models.FloatField(blank=True, null=True)
    crediteasytight = models.FloatField(blank=True, null=True)
    defaults = models.FloatField(blank=True, null=True)
    economicconflict = models.FloatField(blank=True, null=True)
    economicgrowth = models.FloatField(blank=True, null=True)
    economicuncertainty = models.FloatField(blank=True, null=True)
    electionsentiment = models.FloatField(blank=True, null=True)
    financialinstability = models.FloatField(blank=True, null=True)
    fiscalpolicyloosetight = models.FloatField(blank=True, null=True)
    govanger = models.FloatField(blank=True, null=True)
    govcorruption = models.FloatField(blank=True, null=True)
    govinstability = models.FloatField(blank=True, null=True)
    inflation = models.FloatField(blank=True, null=True)
    interestrate = models.FloatField(blank=True, null=True)
    investmentflow = models.FloatField(blank=True, null=True)
    monetarypolicyloosetight = models.FloatField(blank=True, null=True)
    naturaldisaster = models.FloatField(blank=True, null=True)
    regimechange = models.FloatField(blank=True, null=True)
    socialinequality = models.FloatField(blank=True, null=True)
    socialunrest = models.FloatField(blank=True, null=True)
    unemployment = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecountry_2009'


class ThomMinutecountry2010(models.Model):
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    marketrisk = models.FloatField(blank=True, null=True)
    tradebalance = models.FloatField(blank=True, null=True)
    budgetdeficit = models.FloatField(blank=True, null=True)
    centralbank = models.FloatField(blank=True, null=True)
    consumersentiment = models.FloatField(blank=True, null=True)
    crediteasytight = models.FloatField(blank=True, null=True)
    defaults = models.FloatField(blank=True, null=True)
    economicconflict = models.FloatField(blank=True, null=True)
    economicgrowth = models.FloatField(blank=True, null=True)
    economicuncertainty = models.FloatField(blank=True, null=True)
    electionsentiment = models.FloatField(blank=True, null=True)
    financialinstability = models.FloatField(blank=True, null=True)
    fiscalpolicyloosetight = models.FloatField(blank=True, null=True)
    govanger = models.FloatField(blank=True, null=True)
    govcorruption = models.FloatField(blank=True, null=True)
    govinstability = models.FloatField(blank=True, null=True)
    inflation = models.FloatField(blank=True, null=True)
    interestrate = models.FloatField(blank=True, null=True)
    investmentflow = models.FloatField(blank=True, null=True)
    monetarypolicyloosetight = models.FloatField(blank=True, null=True)
    naturaldisaster = models.FloatField(blank=True, null=True)
    regimechange = models.FloatField(blank=True, null=True)
    socialinequality = models.FloatField(blank=True, null=True)
    socialunrest = models.FloatField(blank=True, null=True)
    unemployment = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecountry_2010'


class ThomMinutecountry2011(models.Model):
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    marketrisk = models.FloatField(blank=True, null=True)
    tradebalance = models.FloatField(blank=True, null=True)
    budgetdeficit = models.FloatField(blank=True, null=True)
    centralbank = models.FloatField(blank=True, null=True)
    consumersentiment = models.FloatField(blank=True, null=True)
    crediteasytight = models.FloatField(blank=True, null=True)
    defaults = models.FloatField(blank=True, null=True)
    economicconflict = models.FloatField(blank=True, null=True)
    economicgrowth = models.FloatField(blank=True, null=True)
    economicuncertainty = models.FloatField(blank=True, null=True)
    electionsentiment = models.FloatField(blank=True, null=True)
    financialinstability = models.FloatField(blank=True, null=True)
    fiscalpolicyloosetight = models.FloatField(blank=True, null=True)
    govanger = models.FloatField(blank=True, null=True)
    govcorruption = models.FloatField(blank=True, null=True)
    govinstability = models.FloatField(blank=True, null=True)
    inflation = models.FloatField(blank=True, null=True)
    interestrate = models.FloatField(blank=True, null=True)
    investmentflow = models.FloatField(blank=True, null=True)
    monetarypolicyloosetight = models.FloatField(blank=True, null=True)
    naturaldisaster = models.FloatField(blank=True, null=True)
    regimechange = models.FloatField(blank=True, null=True)
    socialinequality = models.FloatField(blank=True, null=True)
    socialunrest = models.FloatField(blank=True, null=True)
    unemployment = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecountry_2011'


class ThomMinutecountry2012(models.Model):
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    marketrisk = models.FloatField(blank=True, null=True)
    tradebalance = models.FloatField(blank=True, null=True)
    budgetdeficit = models.FloatField(blank=True, null=True)
    centralbank = models.FloatField(blank=True, null=True)
    consumersentiment = models.FloatField(blank=True, null=True)
    crediteasytight = models.FloatField(blank=True, null=True)
    defaults = models.FloatField(blank=True, null=True)
    economicconflict = models.FloatField(blank=True, null=True)
    economicgrowth = models.FloatField(blank=True, null=True)
    economicuncertainty = models.FloatField(blank=True, null=True)
    electionsentiment = models.FloatField(blank=True, null=True)
    financialinstability = models.FloatField(blank=True, null=True)
    fiscalpolicyloosetight = models.FloatField(blank=True, null=True)
    govanger = models.FloatField(blank=True, null=True)
    govcorruption = models.FloatField(blank=True, null=True)
    govinstability = models.FloatField(blank=True, null=True)
    inflation = models.FloatField(blank=True, null=True)
    interestrate = models.FloatField(blank=True, null=True)
    investmentflow = models.FloatField(blank=True, null=True)
    monetarypolicyloosetight = models.FloatField(blank=True, null=True)
    naturaldisaster = models.FloatField(blank=True, null=True)
    regimechange = models.FloatField(blank=True, null=True)
    socialinequality = models.FloatField(blank=True, null=True)
    socialunrest = models.FloatField(blank=True, null=True)
    unemployment = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecountry_2012'


class ThomMinutecountry2013(models.Model):
    country = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    marketrisk = models.FloatField(blank=True, null=True)
    tradebalance = models.FloatField(blank=True, null=True)
    budgetdeficit = models.FloatField(blank=True, null=True)
    centralbank = models.FloatField(blank=True, null=True)
    consumersentiment = models.FloatField(blank=True, null=True)
    crediteasytight = models.FloatField(blank=True, null=True)
    defaults = models.FloatField(blank=True, null=True)
    economicconflict = models.FloatField(blank=True, null=True)
    economicgrowth = models.FloatField(blank=True, null=True)
    economicuncertainty = models.FloatField(blank=True, null=True)
    electionsentiment = models.FloatField(blank=True, null=True)
    financialinstability = models.FloatField(blank=True, null=True)
    fiscalpolicyloosetight = models.FloatField(blank=True, null=True)
    govanger = models.FloatField(blank=True, null=True)
    govcorruption = models.FloatField(blank=True, null=True)
    govinstability = models.FloatField(blank=True, null=True)
    inflation = models.FloatField(blank=True, null=True)
    interestrate = models.FloatField(blank=True, null=True)
    investmentflow = models.FloatField(blank=True, null=True)
    monetarypolicyloosetight = models.FloatField(blank=True, null=True)
    naturaldisaster = models.FloatField(blank=True, null=True)
    regimechange = models.FloatField(blank=True, null=True)
    socialinequality = models.FloatField(blank=True, null=True)
    socialunrest = models.FloatField(blank=True, null=True)
    unemployment = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecountry_2013'


class ThomMinutecurrency(models.Model):
    currency = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    priceforecast = models.FloatField(blank=True, null=True)
    carrytrade = models.FloatField(blank=True, null=True)
    currencypeginstability = models.FloatField(blank=True, null=True)
    pricemomentum = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecurrency_'


class ThomMinutecurrency1998(models.Model):
    currency = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    priceforecast = models.FloatField(blank=True, null=True)
    carrytrade = models.FloatField(blank=True, null=True)
    currencypeginstability = models.FloatField(blank=True, null=True)
    pricemomentum = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecurrency_1998'


class ThomMinutecurrency1999(models.Model):
    currency = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    priceforecast = models.FloatField(blank=True, null=True)
    carrytrade = models.FloatField(blank=True, null=True)
    currencypeginstability = models.FloatField(blank=True, null=True)
    pricemomentum = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecurrency_1999'


class ThomMinutecurrency2000(models.Model):
    currency = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    priceforecast = models.FloatField(blank=True, null=True)
    carrytrade = models.FloatField(blank=True, null=True)
    currencypeginstability = models.FloatField(blank=True, null=True)
    pricemomentum = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecurrency_2000'


class ThomMinutecurrency2001(models.Model):
    currency = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    priceforecast = models.FloatField(blank=True, null=True)
    carrytrade = models.FloatField(blank=True, null=True)
    currencypeginstability = models.FloatField(blank=True, null=True)
    pricemomentum = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecurrency_2001'


class ThomMinutecurrency2002(models.Model):
    currency = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    priceforecast = models.FloatField(blank=True, null=True)
    carrytrade = models.FloatField(blank=True, null=True)
    currencypeginstability = models.FloatField(blank=True, null=True)
    pricemomentum = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecurrency_2002'


class ThomMinutecurrency2003(models.Model):
    currency = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    priceforecast = models.FloatField(blank=True, null=True)
    carrytrade = models.FloatField(blank=True, null=True)
    currencypeginstability = models.FloatField(blank=True, null=True)
    pricemomentum = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecurrency_2003'


class ThomMinutecurrency2004(models.Model):
    currency = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    priceforecast = models.FloatField(blank=True, null=True)
    carrytrade = models.FloatField(blank=True, null=True)
    currencypeginstability = models.FloatField(blank=True, null=True)
    pricemomentum = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecurrency_2004'


class ThomMinutecurrency2005(models.Model):
    currency = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    priceforecast = models.FloatField(blank=True, null=True)
    carrytrade = models.FloatField(blank=True, null=True)
    currencypeginstability = models.FloatField(blank=True, null=True)
    pricemomentum = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecurrency_2005'


class ThomMinutecurrency2006(models.Model):
    currency = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    priceforecast = models.FloatField(blank=True, null=True)
    carrytrade = models.FloatField(blank=True, null=True)
    currencypeginstability = models.FloatField(blank=True, null=True)
    pricemomentum = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecurrency_2006'


class ThomMinutecurrency2007(models.Model):
    currency = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    priceforecast = models.FloatField(blank=True, null=True)
    carrytrade = models.FloatField(blank=True, null=True)
    currencypeginstability = models.FloatField(blank=True, null=True)
    pricemomentum = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecurrency_2007'


class ThomMinutecurrency2008(models.Model):
    currency = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    priceforecast = models.FloatField(blank=True, null=True)
    carrytrade = models.FloatField(blank=True, null=True)
    currencypeginstability = models.FloatField(blank=True, null=True)
    pricemomentum = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecurrency_2008'


class ThomMinutecurrency2009(models.Model):
    currency = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    priceforecast = models.FloatField(blank=True, null=True)
    carrytrade = models.FloatField(blank=True, null=True)
    currencypeginstability = models.FloatField(blank=True, null=True)
    pricemomentum = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecurrency_2009'


class ThomMinutecurrency2010(models.Model):
    currency = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    priceforecast = models.FloatField(blank=True, null=True)
    carrytrade = models.FloatField(blank=True, null=True)
    currencypeginstability = models.FloatField(blank=True, null=True)
    pricemomentum = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecurrency_2010'


class ThomMinutecurrency2011(models.Model):
    currency = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    priceforecast = models.FloatField(blank=True, null=True)
    carrytrade = models.FloatField(blank=True, null=True)
    currencypeginstability = models.FloatField(blank=True, null=True)
    pricemomentum = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecurrency_2011'


class ThomMinutecurrency2012(models.Model):
    currency = models.CharField(max_length=5)
    date = models.DateField()
    time = models.TimeField()
    source = models.CharField(max_length=10)
    buzz = models.FloatField(blank=True, null=True)
    sentiment = models.FloatField(blank=True, null=True)
    optimism = models.FloatField(blank=True, null=True)
    fear = models.FloatField(blank=True, null=True)
    joy = models.FloatField(blank=True, null=True)
    trust = models.FloatField(blank=True, null=True)
    violence = models.FloatField(blank=True, null=True)
    conflict = models.FloatField(blank=True, null=True)
    urgency = models.FloatField(blank=True, null=True)
    uncertainty = models.FloatField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    priceforecast = models.FloatField(blank=True, null=True)
    carrytrade = models.FloatField(blank=True, null=True)
    currencypeginstability = models.FloatField(blank=True, null=True)
    pricemomentum = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'thom_minutecurrency_2012'


class Ticker(models.Model):
    country = models.CharField(max_length=5)
    ticker = models.CharField(max_length=10)
    ticker_name = models.CharField(max_length=100, blank=True)
    stock_exchange = models.CharField(max_length=20, blank=True)

    class Meta:
        managed = False
        db_table = 'ticker'


class Topticker(models.Model):
    ticker = models.CharField(primary_key=True, max_length=10)
    ticker_name = models.CharField(max_length=100, blank=True)

    class Meta:
        managed = False
        db_table = 'topticker'


class WorldbankCountry(models.Model):
    code = models.CharField(primary_key=True, max_length=5)
    long_name = models.CharField(max_length=100, blank=True)
    short_name = models.CharField(max_length=30, blank=True)
    wb2code = models.CharField(max_length=2, blank=True)
    income_group = models.CharField(max_length=50, blank=True)
    region = models.CharField(max_length=50, blank=True)
    lend_category = models.CharField(max_length=50, blank=True)
    other_group = models.CharField(max_length=50, blank=True)
    currency_unit = models.CharField(max_length=50, blank=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'worldbank_country'


class WorldbankDevindicator(models.Model):
    country = models.CharField(max_length=5)
    series = models.CharField(max_length=100)
    year = models.IntegerField()
    data = models.FloatField(blank=True, null=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'worldbank_devindicator'


class WorldbankSeries(models.Model):
    code = models.CharField(primary_key=True, max_length=100)
    name = models.CharField(max_length=200, blank=True)
    short_definition = models.CharField(max_length=300, blank=True)
    source = models.CharField(max_length=200, blank=True)
    topic = models.CharField(max_length=100, blank=True)
    periodicity = models.CharField(max_length=50, blank=True)
    base_period = models.CharField(max_length=50, blank=True)
    aggregation_method = models.CharField(max_length=50, blank=True)
    rowid = models.CharField(unique=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'worldbank_series'


class YahooStock(models.Model):
    symbol = models.CharField(max_length=10)
    exchange_symbol = models.CharField(max_length=10)
    date = models.DateField()
    open_price = models.FloatField(blank=True, null=True)
    high_price = models.FloatField(blank=True, null=True)
    low_price = models.FloatField(blank=True, null=True)
    close_price = models.FloatField(blank=True, null=True)
    volume = models.IntegerField(blank=True, null=True)
    adj_close = models.FloatField(blank=True, null=True)
    rowid = models.CharField(primary_key=True, unique=True, max_length=40, blank=True)

    class Meta:
        managed = False
        db_table = 'yahoo_stock'
