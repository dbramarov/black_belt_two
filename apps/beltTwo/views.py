from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.urlresolvers import reverse
from .models import User, Quotes, Favorites
from django.db.models import Count 

def index(request):
	user = User.objects.get(id = request.session['user'])
	data = {
	'user': User.objects.get(id = request.session['user']),
	'quotes': Quotes.objects.all().exclude(favs__user = user),
	'favs': Favorites.objects.filter(user = user)
	}
	return render(request, 'beltTwo/index.html', data)

def create(request):
	user = User.objects.get(id = request.session['user'])
	data = {
	'by': request.POST['quotedBy'],
	'message': request.POST['message'],
	'user': user
	}
	result = Quotes.objects.validate(data)
	if result[0]:
		return redirect(reverse('black:my_index'))
	else:
		for err in result[1]:
			messages.error(request, err)
		return redirect(reverse('black:my_index'))

def user(request, id):
	data = {
	'user': User.objects.get(id = id),
	'count': User.objects.filter(id=id).annotate(num_quotes=Count('posted_quotes')),
	'quotes': Quotes.objects.filter(user=id)
	}
	return render(request, 'beltTwo/user.html', data)

def fav(request, id):
	quotes = Quotes.objects.get(id=id)
	user = User.objects.get(id = request.session['user'])
	check = Favorites.objects.filter(user=user).filter(quotes=quotes)
	if not check:
		Favorites.objects.create(quotes=quotes, user=user)
	else:
		messages.error(request, "This is already one of your favorites!")	
	return redirect(reverse('black:my_index'))

def delete(request, id):
	Favorites.objects.get(id=id).delete()
	return redirect(reverse('black:my_index'))
