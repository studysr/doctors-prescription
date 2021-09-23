from django.db import models
from django.urls import reverse

import datetime
today=datetime.date.today().strftime("%Y-%m-%d")



CATEGORY_CHOICES_SEX=(
	('M','Male'),
	('F','Female'),
	)

class Test(models.Model):
	title= models.CharField(max_length=200)

	def __str__(self):
		return self.title





class Patient(models.Model):
	name= models.CharField(max_length=100, null=True)
	age_y= models.IntegerField(null=True, blank=True)
	age_m= models.IntegerField(null=True, blank=True, default=0)
	age_d= models.IntegerField(null=True, blank=True, default=0)
	sex= models.CharField(choices=CATEGORY_CHOICES_SEX, max_length=100)
	cc= models.CharField(max_length=300, null=True, blank=True)
	oe= models.CharField(max_length=300, null=True, blank=True)
	pulse= models.CharField(max_length=50, null=True, blank=True)
	bp= models.CharField(max_length=50, null=True, blank=True)
	test = models.ManyToManyField(Test, blank=True)
	others_test= models.CharField(max_length=400, null=True, blank=True)
	date=models.DateField(auto_now=False,auto_now_add=False,default=today)
	status= models.BooleanField(default=False)

	def __str__(self):
		return self.name



class Medicine(models.Model):
	patientname = models.ForeignKey(Patient, on_delete=models.CASCADE, null=True, blank=True)
	test_result= models.TextField(blank=True)
	date = models.DateTimeField(auto_now_add=True)
	next_visit = models.IntegerField(default=0, null= True, blank=True)
	diagonosis = models.CharField(max_length=200, null=True, blank=True)
	advice = models.CharField(max_length=200, null=True, blank=True)
	med1= models.CharField(max_length=200, null=True, blank=True)
	rule1= models.CharField(max_length=200, null=True, blank=True)
	med2= models.CharField(max_length=200, null=True, blank=True)
	rule2= models.CharField(max_length=200, null=True, blank=True)
	med3= models.CharField(max_length=200, null=True, blank=True)
	rule3= models.CharField(max_length=200, null=True, blank=True)
	med4= models.CharField(max_length=200, null=True, blank=True)
	rule4= models.CharField(max_length=200, null=True, blank=True)
	med5= models.CharField(max_length=200, null=True, blank=True)
	rule5= models.CharField(max_length=200, null=True, blank=True)
	med6= models.CharField(max_length=200, null=True, blank=True)
	rule6= models.CharField(max_length=200, null=True, blank=True)
	med7= models.CharField(max_length=200, null=True, blank=True)
	rule7= models.CharField(max_length=200, null=True, blank=True)
	med8= models.CharField(max_length=200, null=True, blank=True)
	rule8= models.CharField(max_length=200, null=True, blank=True)
	med9= models.CharField(max_length=200, null=True, blank=True)
	rule9= models.CharField(max_length=200, null=True, blank=True)
	med10= models.CharField(max_length=200, null=True, blank=True)
	rule10= models.CharField(max_length=200, null=True, blank=True)

	def __str__(self):
		return self.patientname.name


	def only_date(self):
		return self.date.strftime('%e %b %Y')