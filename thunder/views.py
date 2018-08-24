from django.shortcuts import render,get_object_or_404,get_list_or_404
from .models import DyttItem
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage


# Create your views here.
def index(request):
    film_all = get_list_or_404(DyttItem)
    p = Paginator(film_all,20)
    page = request.GET.get("page")

    try:
        film_list = p.page(page)
    except PageNotAnInteger:
        film_list = p.page(1)
    except EmptyPage:
        film_list = p.page(p.num_pages)

    return render(request,'thunder/index.html',{"film_list":film_list})




def detail(request,film_id):
    film = get_object_or_404(DyttItem,pk=film_id)
    return render(request,'thunder/detail.html',{"film":film})
