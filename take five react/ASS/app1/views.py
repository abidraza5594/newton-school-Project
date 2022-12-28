from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    r=[i for i in range(1,100)]
    paginator=Paginator(r,5)
    page=request.GET.get("page")
    r=paginator.get_page(page)
    
    return render(request,'home.html',{'r':r})