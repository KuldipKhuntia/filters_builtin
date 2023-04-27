from django.shortcuts import render

# Create your views here.
def built_in_filter(request):
    import datetime
    dt=datetime.datetime.now()
    d={'data':'i Am a cOOl BOy','dt':dt,}



    return render(request,'built_in_filter.html',d)
