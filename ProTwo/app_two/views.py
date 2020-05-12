from django.shortcuts import render
from django.http import HttpResponse
from django.urls import path
from app_two.models import User, My_Model

# Create your views here.
def index(request):
    return HttpResponse("<em>My Second Project</em>")

def help(request):
    my_file = {'insert_me': "HELP PAGE!!!"}
    return render(request,'app_two/help.html', context=my_file)

def users(request):
    users_list = User.objects.order_by('first_name')
    my_dict = {'access_users': users_list }
    return render(request,'app_two/users.html',context=my_dict)

def form(request):
    form = My_Model

    if request.method == 'POST':
        form = My_Model(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request,'app_two/form.html')


    my_form = {'access_form': form_entry}
    return render(request,'app_two/form.html',{'form': form})
