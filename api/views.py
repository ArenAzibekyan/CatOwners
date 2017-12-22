from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CatForm
from .models import Cat


@login_required
def MyCats(request):
    catList = Cat.objects.raw('SELECT * FROM api_cat WHERE owner_id = {0}'.format(request.user.id))
    if not len(list(catList)):
        catList = None
    return render(
        request=request,
        template_name='mycats.html',
        context={
            'catList': catList
        }
    )


@login_required
def AddCat(request):
    unique = None
    form = CatForm()
    if request.method == 'POST':
        form = CatForm(request.POST)
        if form.is_valid():
            newCat, created = Cat.objects.get_or_create(name=form.cleaned_data['name'])
            if created:
                for field in ('name', 'birthday', 'breed', 'hairiness'):
                    setattr(newCat, field, form.cleaned_data[field])
                newCat.owner_id = request.user.id
                newCat.save()
                return redirect('mycats')
            else:
                unique = 'Котик с таким именем уже существует'
    return render(request=request,
                  template_name='addcat.html',
                  context={
                      'form': form,
                      'unique': unique
                  })


@login_required
def SetupCat(request):
    if request.method == 'GET':
        # проверка параметра
        if not 'catName' in request.GET:
            return render(request=request,
                          template_name='setupcat_fail.html',
                          context={
                              'errorMes': 'Ошибка параметра запроса'
                          })
        catName = request.GET['catName']
        catObj = Cat.objects.raw(
            'SELECT * FROM api_cat WHERE name = \'{0}\' AND owner_id = {1}'.format(catName, request.user.id)
        )
        # всего 1 котик должен найтись
        if len(list(catObj)) != 1:
            return render(request=request,
                          template_name='setupcat_fail.html',
                          context={
                              'errorMes': 'Ошибка БД'
                          })
        # нашелся
        catObj = catObj[0]
        formData = {
            'name': catObj.name,
            'birthday': catObj.birthday,
            'breed': catObj.breed,
            'hairiness': catObj.hairiness
        }
        form = CatForm(formData)
        if form.is_valid():
            return render(request=request,
                          template_name='setupcat.html',
                          context={
                              'form': form
                          })
        else:
            return render(request=request,
                          template_name='setupcat_fail.html',
                          context={
                              'errorMes': 'Ошибка формы'
                          })
    elif request.method == 'POST':
        form = CatForm(request.POST)
        if form.is_valid():
            catObj, created = Cat.objects.get_or_create(name=form.cleaned_data['name'])
            catObj.birthday = form.cleaned_data['birthday']
            catObj.breed = form.cleaned_data['breed']
            catObj.hairiness = form.cleaned_data['hairiness']
            if created:
                catObj.owner_id = request.user.id
            catObj.save()
            return redirect('mycats')
        else:
            return render(request=request,
                          template_name='setupcat.html',
                          context={
                              'form': form
                          })
    else:
        return redirect('mycats')


@login_required
def DeleteCat(request):
    if request.method == 'GET':
        if not 'catName' in request.GET:
            return render(request=request,
                          template_name='deletecat_failed.html',
                          context={
                              'errorMes': 'Ошибка параметра запроса'
                          })
        catName = request.GET['catName']
        try:
            catObj = Cat.objects.get(name=catName)
            catObj.delete()
        except:
            return render(request=request,
                          template_name='deletecat_failed.html',
                          context={
                              'errorMes': 'Произошла ошибка при удалении'
                          })
        else:
            return redirect('mycats')
    else:
        return render(request=request,
                      template_name='deletecat_failed.html',
                      context={
                          'errorMes': 'Требуется GET-запрос'
                      })