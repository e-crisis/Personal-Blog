# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse
from .models import About, Entry, Comment
from django.template import loader
from django.http import Http404
from django.urls import reverse


def index(request):
    latest_entry_list = Entry.objects.order_by('-pub_date')[:10]
    template = loader.get_template('blog/index.html')
    context = {
        'latest_entry_list': latest_entry_list
    }
    return HttpResponse(template.render(context))


def detail(request, blog_id):
    try:
        entry = Entry.objects.get(pk=blog_id)
    except Entry.DoesNotExist:
        raise Http404("This blog post does not exist")
    return render(request, 'blog/detail.html', {'entry': entry})

def edit_entry(request, blog_id):
    entry = Entry.objects.get(pk=blog_id)
    return render(request, 'blog/edit.html', {'entry': entry})

def submit_edit_entry(request, blog_id):
    entry = Entry.objects.get(pk=blog_id)
    entry.body_text = request.POST.get('text', "no edit")
    return HttpResponseRedirect(reverse('blog:detail', args=(entry.id,)))


def new_entry(request):
    return HttpResponse("Make new entry and post button will post it in database as a new object in the model Entry")



