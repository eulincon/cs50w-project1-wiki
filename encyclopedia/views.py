from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.files.storage import default_storage
from django.core.files import File

from . import util


def index(request):
		q = request.GET.get('q')
		if q is None:
			return render(request, "encyclopedia/index.html", {
		        "entries": util.list_entries()
		    })
		elif q is not None:
			return HttpResponseRedirect(f'{q}')

def newpage(request):
	return render(request, 'encyclopedia/newpage.html',{})

def entry(request, entry):
	content = util.get_entry(entry)
	if content:
		return render(request, 'encyclopedia/entry.html', {
			'title': entry,
			'entry': content
		})
	elif content is None:
		entries = util.list_entries()
		entries = [i for i in entries if i.lower().find(entry.lower()) != -1]
		return render(request, 'encyclopedia/index.html', {
			'entries': entries
		})

def upload(request):
	title = request.POST.get('title')
	content = request.POST.get('content')
	if default_storage.exists(f'entries/{title}.md'):
		return HttpResponse('Error: Directory already content')
		#Undone
	else:
		util.save_entry(title, content)
		return HttpResponseRedirect(f'{title}')

def editpage(request, entry='git'):
	title = entry
	content = util.get_entry(entry)
	if request.method == 'GET':
		return render(request, 'encyclopedia/editpage.html',{
			'title': title,
			'content': content
		})
	elif request.method == 'POST':
		title = request.POST.get('title')
		content = request.POST.get('content')
		util.save_entry(title, content)
		return HttpResponseRedirect(f'{title}')


