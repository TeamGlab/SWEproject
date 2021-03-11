from django.test import TestCase
from django.test import SimpleTestCase
from django.contrib.auth.models import User
from math import sqrt

# MAKE SURE TEST CASES START WITH 'test'!!!!!!!!

# Use this if you don't need the database (inherit from SimpleTestCase)
class ExampleTestCases(SimpleTestCase):
	# overriden method, performs any preliminary work before running test cases
	def setUp(self): 
		self.x = 1
		self.y = 2

	# shows how to use values from setUp
	def testCase1(self):
		self.assertEquals(self.x, self.y - 1)

	# basic math test
	def testCase2(self):
		a = 1
		b = -3
		c = 2
		root1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
		root2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
		self.assertEquals(0, a*root1**2 + b*root1 + c)


# Use this if you need the database (makes a mock database and inherits from TestCase)
class ExampleTestCasesWithDatabase(TestCase):
	
	def setUp(self):
		self.joe = User.objects.create_user(username="joe")

	def testDatabaseUsers(self):
		if User.objects.filter(username="joe").exists():
			print("User joe created successfully") # this will show up in xml log on CircleCI website
		else:
			raise Exception("User not created")

	def testPasswordChange(self):
		badPassword = '123'
		self.joe.set_password(badPassword)
		self.joe.save()

		from django.contrib.auth.hashers import check_password
		passwordMatch = check_password(badPassword, User.objects.filter(username="joe")[0].password)
		assert(passwordMatch)

