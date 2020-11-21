from django.shortcuts import render
from secondapp.models import AccessRecord,Topic,Webpage,User
from secondapp.forms import NewUserForm
# Create your views here.


def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    context = {'access_records':webpages_list}
    return render(request,'secondapp/index.html',context)

def users(request):
    user_list = User.objects.order_by('first_name')
    context = {'users' : user_list}
    return render(request,'secondapp/users.html',context)


def signUpUserForm(request):

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return users(request)
        else:
            print("Error Form Invalid")
    
    return render(request,'secondapp/signup.html',{'form':form})