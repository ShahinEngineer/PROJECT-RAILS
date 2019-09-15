from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .forms import PastesFrom

from django.template import RequestContext
from .models import Pastes
from django.shortcuts import render_to_response


def showform(request):
    return render(request, 'hellow_word.html')

def index(request):
    results=None
    text=""
    title=""
    if request.method == 'GET' and 'q' in request.GET:
        query = request.GET.get('q')
        try:
            query=int(query)
        except ValueError:
            query=None
            results=None
        if query:
            print("good nice")
            results=Pastes.objects.get(id=query)
            text=results.text
            title=results.title
            print(results)
            
            context = RequestContext(request)
            #return render_to_response('hellow_word.html', {"results": results,},)       
    
    form=PastesFrom(request.POST or None)
    form.fields["title"].initial = "title"
    form.fields["text"].initial = "text"
    if form.is_valid():
        form.save()
        print("welcome") 
    else:   
        print("bade")
    context={'form':form,"result":results}
    return render(request, 'hellow_word.html',context)
    

def search(request):
    query = request.GET.get('q')
    try:
        query=int(query)
    except ValueError:
        query=None
        results=None
    if query:
        print("good nice")
        results=Pastes.objects.get(id=query)
        
        context = RequestContext(request)
        return render_to_response('hellow_word.html', {"results": results,}, context_instance=context)




