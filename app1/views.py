from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from datetime import *

from django.urls import reverse_lazy

from app1.forms import regisform,signupform
from django.http import HttpResponse
from app1.models import jana,details
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic.list import ListView

from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def homepage(req):
    d=datetime.now()
    print('current time is:',d)
    name='janaRthan'
    return render(req,'home.html',{'time':d,'name':name})
def aboutpage(r):
    a=14
    return render(r,'about.html',{'data':a})
def coursepage(req):
    cor=['python','java','c','c++','web designing','django']
    return render(req,'course.html',{'course':cor})

#CRUD
def createpage(rq):
    frm=regisform(rq.POST or None)
    if frm.is_valid():
        frm.save()
        return redirect('/read/')
    return render(rq,'reg.html',{'myform':frm})
@login_required()
def readpage(req):
    data=jana.objects.all()
    return render(req,'read.html',{'data':data})
@login_required()
def updatepage(req,id):
    data = get_object_or_404(jana, pk=id)
    frm=regisform(req.POST or None,instance=data)
    if req.method=='POST':
        frm.save()
        return redirect('/read/')
    return render(req,'update.html',{'myform':frm})
@login_required()
def deletepage(req,id):
    data=get_object_or_404(jana,pk=id)
    if req.method=='POST':
        data.delete()
        return redirect('/read/')
    return render(req,'delete.html',{'user':data.name})

#Classy views:

class create(CreateView):
    model = details
    fields = '__all__'
    template_name = 'create.html'
    success_url =reverse_lazy( 'displaypage')
class display(ListView):
    model = details
    template_name = 'display.html'
    context_object_name = 'object'
class edit(UpdateView):
    model = details
    fields = '__all__'
    template_name = 'edit.html'
    success_url = '/display'
    def get_object(self, queryset=None):
        obj=get_object_or_404(details,pk=self.kwargs['id'])
        return obj
class remove(DeleteView):
    model = details
    fields='__all__'
    template_name = 'remove.html'
    success_url = reverse_lazy('displaypage')
    def get_object(self, queryset=None):
        obj=get_object_or_404(details,pk=self.kwargs['id'])
        return obj

#Django Authentication:
def signuppage(req):
    frm=UserCreationForm(req.POST or None)
    if frm.is_valid():
        frm.save()
        return HttpResponse('New User Created Successfully')
    return render(req,'signup.html',{'myform':frm})
def signuppage(req):
    frm=signupform(req.POST or None)
    if frm.is_valid():
        frm.save()
        return HttpResponse('New User Created Successfully')
    return render(req,'signup.html',{'myform':frm})

def staffpage(rq):
    return render(rq,'staff.html')