from django.shortcuts import render
from django.template import Context,loader,RequestContext
from django.shortcuts import render, get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponse, Http404,HttpResponseRedirect,HttpResponseNotFound
import ctypes  # An included library with Python install.


def calc(request):
	def add(x,y):
	#	x = driver.find_element_by_name("box1")
	#	y = driver.find_element_by_name("box2")
		ctypes.windll.user32.MessageBoxA(0,"x+y = "+str(x+y), "Answer", 0)
	def mul(x,y):
	#	x = driver.find_element_by_name("box1")
	#	y = driver.find_element_by_name("box2")
		ctypes.windll.user32.MessageBoxA(0, "x*y = "+str(x*y), "Answer", 0)	
	def sub(x,y):
	#	x = driver.find_element_by_name("box1")
	#	y = driver.find_element_by_name("box2")
		ctypes.windll.user32.MessageBoxA(0, "x-y = "+str(x-y), "Answer", 0)
	if(request.GET.get('add')):
		x = float(request.GET.get("box1"))
		y = float(request.GET.get("box2"))
		add(x,y)
	if(request.GET.get('mul')):
		x = float(request.GET.get("box1"))
		y = float(request.GET.get("box2"))
		mul(x,y)
	if(request.GET.get('sub')):
		x = float(request.GET.get("box1"))
		y = float(request.GET.get("box2"))
		sub(x,y)
	return render(request, 'calc.html')

	

