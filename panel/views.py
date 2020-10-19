from panel.forms import RegistrationForm
from django.shortcuts import redirect,render

def index(request):
    print()

def registration(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        context['form'] = form
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            context['form'] = form
            return render(request, 'pattern.html', context)

#if there's GET request  or smth else

    else:
        if request.user.is_authenticated:
            return redirect("index")
        else:
            form = RegistrationForm()
            context['form'] = form
            return render(request,'pattern.html',context)

