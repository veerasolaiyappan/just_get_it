from django.shortcuts import render
from django.http import HttpResponse
# from .forms import UserForm
from .models import Forms

# Create your views here.

def form(requests):
	return render(requests, 'forms/forms.html')


def table(requests):

	user_form = UserForm()
	if requests.method == POST:
		user_form = UserForm(requests.POST,requests.FILES)
		if user_form.is_valid():
			user_form.save()

	context = { "form": user_form,}
			


	return render(requests,'forms/table.html',context)
