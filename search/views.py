from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
import wikipedia as wiki


# Create your views here.

def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    try:
        title = request.GET['q']
        result = wiki.page(title=title).html()
    except wiki.DisambiguationError as e:
        print(e.options)
        return render(request, template_name="home.html",
                      context={"options": e.options})

    except:
        return HttpResponse('You submitted an empty form')
    return render(request, template_name="search.html",
                  context={"article": {
                      "title": title,
                      "html_content": result
                  }})


def suggest(request):
    title = request.GET['q']
    result = wiki.WikipediaPage(title=title).html()
    return render(request, template_name="home.html",
                  context={"article": {
                      "title": title,
                      "html_content": result
                  }})
