from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from users.models import *
from .models import *
from .forms import *
from django.db.models import Sum
# Create your views here.

@login_required
def profil(request):
    if request.method == 'POST':
        form = Userprofilform(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.info(request, "Saqlandi ")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.success(request, "Yaroqsiz maʼlumot !")
    else:
        form = Userprofilform(instance=request.user)
    context = {
        'form': form,
        'user': request.user,
    }
    return render(request, 'main/profil.html',context)


@login_required
def index(request):
    context = {
        'users': User.objects.filter(is_superuser=False).annotate(summa=Sum('qarz__summa')),
        'user': request.user,
    }
    return render(request, 'main/index.html',context)

@login_required
def detail(request,pk):
    user_id = get_object_or_404(User, id=pk)
    if request.method == 'POST':
        form = QarzForm(request.POST)
        if form.is_valid():
            qarz = form.save(commit=False)
            qarz.author = user_id
            qarz.save()
            messages.info(request, "Saqlandi ")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.success(request, "Yaroqsiz maʼlumot !")
    else:
        form = QarzForm(instance=request.user)
    context = {
        'form':form,
        'user_id':user_id,
        'qarzlar':Qarz.objects.filter(author=user_id),
        'user': request.user,
    }
    return render(request, 'main/detail.html',context)

@login_required
def qarz_delete(request, pk):
    qarz = get_object_or_404(Qarz, id=pk)
    qarz.delete()
    messages.info(request, "O'chirildi!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def creatuser(request):
    if request.method == 'POST':
        form = NewIshchiForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Saqlandi ")
            return redirect(reverse('index'))
        else:
            messages.success(request, "Yaroqsiz maʼlumot.")
    form = NewIshchiForm()
    context = {
        'form': form,
        'user': request.user,
    }
    return render(request, 'main/creatuser.html',context)


@login_required
def profil2(request):
    if request.method == 'POST':
        form = Userprofilform(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.info(request, "Saqlandi")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            messages.success(request, "Yaroqsiz maʼlumot !")
    else:
        form = Userprofilform(instance=request.user)
    context = {
        'form': form,
        'user': request.user,
    }
    return render(request, 'consumer/profil2.html',context)

@login_required
def index2(request):
    context = {
        'qarzlar': Qarz.objects.filter(author=request.user),
        'user': request.user,
    }
    return render(request, 'consumer/index2.html',context)