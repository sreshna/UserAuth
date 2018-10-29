from django.http import HttpResponse
from django.shortcuts import render
import wikipedia as wiki


# Create your views here.

def search_form(request):
    return render(request, 'search_form.html')


def search(request):
    try:
        result = wiki.page(title=request.GET['q']).html()
    except wiki.DisambiguationError as e:
        return render(request, template_name="suggestions.html", context={"options": e.options})
        # return HttpResponse(e.options)
        # s = wiki.random(e.options)
        # HttpResponse("try searching:")
        # result = '\n'.join(wiki.search(request.GET['q']))
    except:
        return HttpResponse('You submitted an empty form')
    return HttpResponse(result)


def suggest(request):
    result = wiki.WikipediaPage(title=request.GET['q']).html()
    return HttpResponse(result)
