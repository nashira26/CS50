from django.shortcuts import render 
from django.urls import reverse
from django.http import HttpResponseRedirect
from . import util
import random 
import markdown2 

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, name):
    content = util.get_entry(name.strip())
    if content is None:
        return render(request, "encyclopedia/entry.html", {
            "entry_title" : "", 
            "content" : "", 
            "error_message": "Page not found"
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry_title" : name, 
            "content" : markdown2.markdown(content),
            "error_message": ""
        })

def search(request):
    q = request.GET["q"].strip()
    if  util.get_entry(q) is not None:
        return entry(request, q)
    else:
        entry_list = util.list_entries()
        results_list = []
        for entry_name in entry_list:
            if q in entry_name:
                results_list.append(entry_name)
        return render(request, "encyclopedia/search.html", {
            "results" : results_list
        })

def new(request):
    if request.method == "POST":
        entry_list = util.list_entries()
        title = request.POST["new_title"].strip()
        content = request.POST["new_content"].strip()
        if title in entry_list:
            return render(request, "encyclopedia/new.html", {
            "error_message": "Page already exists"
            })   
        else:
            util.save_entry(title, content)
            return entry(request, title)
    else:
        return render(request, "encyclopedia/new.html")
    
def edit(request):
    if request.method == "POST":
        title = request.POST["entry_title"].strip()
        content = request.POST["entry_content"].strip()
        util.save_entry(title, content)
        return entry(request, title)
    else:
        title = request.GET["entry_title"].strip()
        content = util.get_entry(title).strip()
        return render(request, "encyclopedia/edit.html", {
            "entry_title": title,
            "entry_content": content
        })

def random_ent(request):
    random_entry = random.choice(util.list_entries())
    return entry(request, random_entry)