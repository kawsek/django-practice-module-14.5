from django.shortcuts import render
from . forms import contactForm

# Create your views here.
def home(request):
    return render(request, 'home.html')



def about(request):
    # print(request.POST)
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        return render(request, 'about.html', {'name' : name, 'email' : email})
    else:
        return render(request, 'about.html')
def submit_form(request):
    return render(request, 'form.html')

def djangoForm(request):
    form = contactForm(request.POST)
    if form.is_valid():
        print(form.cleaned_data)
    return render(request, 'django_form.html',{'form' : form})
