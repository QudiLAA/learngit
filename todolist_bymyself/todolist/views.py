#coding:utf-8
from django.shortcuts import render,redirect,HttpResponse
from todolist.models import *
from django.conf import settings
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger

# Create your views here.

def global_setting(request):
    SITE_NAME=settings.SITE_NAME
    SITE_DESC=settings.SITE_DESC
    return locals()

# def getpage(request,item_list):
#     paginator=Paginator(item_list,4)
#     try:
#         page=int(request.GET.get('page',1))
#         item_list=paginator.page(page)
#     except (InvalidPage, EmptyPage, PageNotAnInteger):
#         item_list=paginator.page(1)
#     return item_list

def index(request):
    item_list=Item.objects.all().order_by('-pub_date')
    paginator=Paginator(item_list,4)
    try:
        page=int(request.GET.get('page',1))
        item_list=paginator.page(page)
    except (InvalidPage, EmptyPage, PageNotAnInteger):
        item_list=paginator.page(1)
    return render(request, 'index.html', locals())

def add(request):
    try:
        content=request.GET.get('item', None)
        if len(content)>0:
            obj=Item.objects.create(content=content)
            if obj:
                return redirect('/index2/')
    except Exception as e:
        print e
    return render(request, 'message.html',{'message':u'添加失败'})

def edit(request):
    try:
        item_id=request.GET.get('item_id', None)
        content=request.GET.get('item', None)
        if len(item_id)>0 and len(content)>0:
            obj=Item.objects.get(pk=item_id)
            obj.content=content
            obj.save()
        return redirect('/index2/')
    except Exception as e:
        print e
    return render(request, 'message.html',{'message':u'修改失败'})


def delete(request):
    try:
        item_id=request.GET.get('item_id', None)
        if len(item_id)>0:
            obj=Item.objects.get(pk=item_id)
            obj.delete()
        return redirect('/index2/')
    except Exception as e:
        print e
    return render(request, 'message.html',{'message':u'删除失败'})

def done(request):
    try:
        item_id=request.GET.get('item_id', None)
        if len(item_id)>0:
            obj=Item.objects.get(pk=item_id)
            obj.is_done=False if obj.is_done else True
            obj.save()
        return redirect('/index2/')
    except Exception as e:
        print e
    return render(request, 'message.html',{'message':u'修改失败'})
