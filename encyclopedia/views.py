from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core.files.storage import default_storage

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
	exist = util.get_entry(entry)
	if exist:
		return render(request, 'encyclopedia/entry.html', {
			'entry': exist
		})
	elif exist is None:
		entries = util.list_entries()
		entries = [i for i in entries if i.lower().find(entry.lower()) != -1]
		return render(request, 'encyclopedia/index.html', {
			'entries': entries
		})

def upload(request):
	
	return HttpResponse(default_storage.exists('entries/Git.md'))


