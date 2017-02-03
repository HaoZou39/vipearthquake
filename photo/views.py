from django.shortcuts import render
import os 
from photo.models import posts
# Create your views here.
from django.template import Context,loader,RequestContext
from django.shortcuts import render, get_object_or_404
from django.forms import ModelForm
from django.http import HttpResponse, Http404,HttpResponseRedirect,HttpResponseNotFound
import ctypes
from PIL import Image
from PIL.ExifTags import TAGS
import pyexiv2
from shutil import copyfile

def photo(request):

	post = posts.objects.all()
	filenames = next(os.walk('C:/Users/Hao Zou/vipearthquake/static/images'))[2]
	if(request.POST.get('change')):
		text = request.POST.get('textinput');
	if(request.POST.get('append')):
		text = request.POST.get('textinput');
	if(request.POST.get('chan')):
		newname = request.POST.get('filename');
	if(request.POST.get('copy')):
		newname = request.POST.get('filename');
	if(request.POST.get('sort1')):
		filenames = list(reversed(filenames));
		filenames = list(reversed(filenames));
	if(request.POST.get('sort')):
		filenames = list(reversed(filenames));
	if(request.POST.get('add')):
		key = request.POST.get('key');
		comment = request.POST.get('comment');
	if(request.POST.get('show')):
		for checkbox in filenames:
			values = request.POST.get(checkbox);
			if values != None:
					for (k,v) in Image.open("C:/Users/Hao Zou/vipearthquake/static/images/%s" %values)._getexif().items():
						if TAGS.get(k) != None:
							ctypes.windll.user32.MessageBoxW(0,"%s = %s "%(TAGS.get(k),v), "12345",1)
	
	def change(values,text):

		temp = Image.open('C:/Users/Hao Zou/vipearthquake/static/images/%s' %values)
		temp.save('C:/Users/Hao Zou/vipearthquake/static/%s' %values)
		metadata = pyexiv2.ImageMetadata('C:/Users/Hao Zou/vipearthquake/static/%s' %values)
		metadata.read()
		key = 'Exif.Image.ImageDescription'
		metadata[key] = pyexiv2.ExifTag(key, text)
		metadata.write()
		copyfile('C:/Users/Hao Zou/vipearthquake/static/%s' %values,'C:/Users/Lenovo User/Downloads/%s' %values)
		os.remove('C:/Users/Hao Zou/vipearthquake/static/%s' %values)

	def append(values,text):
			copyfile('C:/Users/Hao Zou/vipearthquake/static/images/%s' %values,'C:/Users/Hao Zou/vipearthquake/static/%s' %values)
			metadata = pyexiv2.ImageMetadata('C:/Users/Hao Zou/vipearthquake/static/images/%s' %values)
			metadata.read()
			key = 'Exif.Image.ImageDescription'
			tag = metadata['Exif.Image.ImageDescription']
			final = text + tag.value
			metadata[key] = pyexiv2.ExifTag(key, final)
			metadata.write()
			copyfile('C:/Users/Hao Zou/vipearthquake/static/%s' %values,'C:/Users/Lenovo User/Downloads/%s' %values)
			os.remove('C:/Users/Hao Zou/vipearthquake/static/%s' %values)

	def chan(values,newname):
		temp = Image.open('C:/Users/Hao Zou/vipearthquake/static/images/%s' %values)
		name = newname+values
		temp.save('C:/Users/Hao Zou/vipearthquake/static/images/%s' %name)
		os.remove('C:/Users/Hao Zou/vipearthquake/static/images/%s' %values)

	def copy(values,newname):
		name = newname+values
		copyfile('C:/Users/Hao Zou/vipearthquake/static/images/%s' %values,'C:/Users/Lenovo User/Downloads/%s' %name)

	def add(values,key,comment):
		metadata = pyexiv2.ImageMetadata('C:/Users/Hao Zou/vipearthquake/static/images/%s' %values)
		metadata.read()
		key = 'Exif.Photo.UserComment'
		metadata[key] = pyexiv2.ExifTag(key,comment)
		metadata.write()

	if(request.POST.get('change')):
		for checkbox in filenames:
			values = request.POST.get(checkbox);
			if values != None:
				change(values,text);

	if(request.POST.get('append')):
		for checkbox in filenames:
			values = request.POST.get(checkbox);
			if values != None:
				append(values,text);
	
	if(request.POST.get('chan')):
		for checkbox in filenames:
			values = request.POST.get(checkbox);
			if values != None:
				chan(values,newname);

	if(request.POST.get('copy')):
		for checkbox in filenames:
			values = request.POST.get(checkbox);
			if values != None:
				copy(values,newname);
	
	if(request.POST.get('add')):
		for checkbox in filenames:
			values = request.POST.get(checkbox);
			if values != None:
				add(values,key,comment);	

	return render(request,'index.html',{'filenames':filenames})