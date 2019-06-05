from django.db import models

class Stock(models.Model):
    isin = models.CharField(max_length=200,  primary_key=True)
    name = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    price = models.CharField(max_length=200)

class Histr(models.Model):
    isin = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    price = models.CharField(max_length=200)


class sStock(models.Model):
    ISIN = models.CharField(max_length=500,  primary_key=True)
    link = models.CharField(max_length=200)
    currency = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    markCap = models.CharField(max_length=200)
    divCap = models.CharField(max_length=200)
    divCapZero = models.CharField(max_length=200)
    divCapOne = models.CharField(max_length=200)
    divCapTwo = models.CharField(max_length=200)
    divCapThird = models.CharField(max_length=200)
    divCapFour = models.CharField(max_length=200)
    divCapFive = models.CharField(max_length=200)
    divCapSix = models.CharField(max_length=200)
    resCap = models.CharField(max_length=200)
    ownZero = models.CharField(max_length=200)
    ownOne = models.CharField(max_length=200)
    ownTwo = models.CharField(max_length=200)
    ownThree = models.CharField(max_length=200)
    ownFour = models.CharField(max_length=200)
    ownFive = models.CharField(max_length=200)
    ownSix = models.CharField(max_length=200)
    forCap = models.CharField(max_length=200)
    forZero = models.CharField(max_length=200)
    forOne = models.CharField(max_length=200)
    forThree = models.CharField(max_length=200)
    forFour = models.CharField(max_length=200)
    forFive = models.CharField(max_length=200)
    forSix = models.CharField(max_length=200)
    
