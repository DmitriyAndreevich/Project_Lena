from django.shortcuts import redirect
from django.shortcuts import render
from .models import Projects, Posts, Contact
from django.core.mail import EmailMessage
from django.contrib import messages
from .forms import ContactForm




def index(request):
	projects = Projects.objects.all()
	posts = Posts.objects.all()
	if request.method == "POST":
		form = ContactForm(request.POST)
		if form.is_valid():
			result = form.save()
			print('form saved')
			messages.add_message(request, messages.INFO, 'Hello world.')
			messages.success(request, "Отлично! Ваше письмо отправлено!")
		else:
			messages.warning(request, "Упс! Что-то пошло не так!")
	return render(request, 'index.html', locals())
