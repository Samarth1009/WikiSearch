from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from subprocess import run,PIPE
import  sys

def index(request):
    return render(request,'index.html')
def next(request):
    inp=request.GET.get('text','default')
    out=run([sys.executable,'E:\Programming\IR Project\wikisearch\search\WikiSearchEngine\\query.py',inp],shell=False,stdout=PIPE)
    print(out)
    return render(request,'next.html',{'data':out.stdout})


# Create your views here.
