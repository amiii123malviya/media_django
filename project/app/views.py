from django.shortcuts import render
from .forms import StudentForm
# Create your views here.
def home(request):
    my_dict ={}
    my_dict['form'] = StudentForm
    return render(request,'home.html',my_dict)

def register(request):
    print(request.POST)
    print(request.FILES)
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            my_dict ={}
            my_dict['form']=StudentForm
            my_dict['msg']="register successfull"
            return render(request, 'home.html', my_dict)
        else:
            msg = 'found some error'
            return render(request,'home.html',{'key':msg})
    return render(request,'home.html')



