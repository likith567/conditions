from django.shortcuts import render

# Create your views here.
def hai(request):
    d = {'a':10,'c':50,'e':110}
    return render(request,'hai.html',d)