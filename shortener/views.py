from django.shortcuts import get_object_or_404, redirect

from django.shortcuts import render
from .models import URL

from . import forms

from django.http import HttpResponseRedirect
from django.views.generic.base import View

# generate random integer values
from random import seed
from random import randint
# seed random number generator

seed(1)


# The location of a character in the string matters.
chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvw"
charsLen = len(chars)

class IndexView(View):
	def get(self, request, *args, **kwargs):
		form = forms.ShortUrlForm()
		context = {'form':form}        
		return render(request, "index.html", context=context)
	
	def post(self,request, *args, **kwargs):
		form = forms.ShortUrlForm(self.request.POST)
		if form.is_valid():
			#when you have priary field which is not assigned yet
			url = form.save(commit=False)

			url.full_url = form.cleaned_data.get('full_url')
			#genrating random numbers
			num = randint(0,1000000)
			temp = num

			#creating hash
			shorthash = ""
			while num:
				shorthash = chars[num % charsLen] + shorthash
				num //= charsLen
			print("No collison",shorthash)

			#checking collison
			url_exist = get_object_or_404(URL, url_hash=shorthash)
			if url_exist:
				new_num = str(temp) + str(request.user.id)
				shorthash = ""
				while new_num:
					shorthash = chars[new_num % charsLen] + shorthash
					new_num //= charsLen
				print("No collison",shorthash)
			
			url.url_hash = shorthash
			url.save()
			
			shorturl = 'https://teachmebro.com/' + shorthash
			request.session['shorturl'] = shorturl
		return redirect(self.request.path)
        
# def root(request, url_hash):
#     url = get_object_or_404(URL, url_hash=url_hash)
#     url.clicked()

#     return redirect(url.full_url)


def shortlink(request):
	return render(request, 'shortlink.html')


# def shorturl(request):
# 	if request.method == 'POST':
# 		form = forms.ShortUrlForm(request.POST)
# 		if form.is_valid():
# 			#when you have priary field which is not assigned yet
# 			url = form.save(commit=False)

# 			url.full_url = form.cleaned_data.get('full_url')
# 			#genrating random numbers
# 			num = randint(0,1000000)
# 			temp = num

# 			#creating hash
# 			shorthash = ""
# 			while num:
# 				shorthash = chars[num % charsLen] + shorthash
# 				num //= charsLen
# 			print("No collison",shorthash)

# 			#checking collison
# 			url_exist = get_object_or_404(URL, url_hash=shorthash)
# 			if url_exist:
# 				new_num = str(temp) + str(request.user.id)
# 				shorthash = ""
# 				while new_num:
# 					shorthash = chars[new_num % charsLen] + shorthash
# 					new_num //= charsLen
# 				print("No collison",shorthash)
			
# 			url.url_hash = shorthash
# 			url.save()
			
# 			shorturl = 'https://teachmebro.com/' + shorthash
# 			request.session['shorturl'] = shorturl

# 			return redirect(request.path)
# 	else:
# 		form = forms.ShortUrlForm()
# 	return render(request, 'index.html', {'form': form})
	
