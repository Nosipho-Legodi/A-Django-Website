#from http.client import HTTPResponse
from multiprocessing import context
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import degreeForm
from django.conf import settings
from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login
from django.contrib import messages
#from django.contrib.auth import user,
from .models import degree 

 #Create your views here.
 

def loginPage(request):
	
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('main')
			else:
				messages.info(request, 'Username OR Password Is Incorrect.')

		context = {}
		return render(request, 'search/administration.html', context)

       
    
                    
     
 





    
         
       
def searchh (request):
    return render(request,'search/home.html')

def science (request):
    return render (request, 'search/Science.html')

def  Art (request):
    return render (request, 'search/Art.html')

def education (request):

    return render (request, 'search/education.html')

def commerce (request):

    return render (request, 'search/commerce.html')

def main (request):

    return render (request, 'search/main.html')

def results (request):
    if 'q' in request.GET:
        q = request.GET['q']
        data = degree.objects.filter(course_name__icontains=q)

    else:
        messages.info (request,"Search for the course or career that you desire and if the course/career is offered this message will dissaper but if the course if not found, this messange will remain on your screen")
        data = degree.objects.all()[:0]
        
    context = {
        'data' : data,
 
    }


  
    

    return render(request, 'search/search_course.html', context)

def career (request):
    if 'p' in request.GET:
        p = request.GET['p']
        data = degree.objects.filter(careers_offered__icontains=p)
    elif 'p' == None:
        messages.info(request, 'Username OR password is incorrect')
    else:
        messages.error(request, 'Document deleted.')
       
    context = {
        'data' : data,
        
         
    }
    

    return render(request, 'search/search_course.html', context)

def addCourse(request):
    form = degreeForm()
    if request.method == 'POST':
       form= degreeForm (request.POST)
       if form.is_valid():
          form.save()
          return redirect('main')
        

    
    context = { 'form' : form }
    return render(request, 'search/degree_form.html', context)

#currently getting an error with this function 
def updateCourse(request,pk):
     course = degree.objects.get(id = pk)
     form = degreeForm(instance=course)
     
     if request.method == 'POST':
      form = degreeForm(request.POST,instance = course)
     if form.is_valid():
       form.save() 
     return redirect('main')
     
    
     return render(request, 'search/update.html', {'form': form, 'course' : course})

def delete(request):
    
    return(request, 'search/delete')


 #This next Part is still a work in progress 

def find (request):
    
    subjects = ['Accounting',	'Afrikaans home Language', 'Afrikaans FAL',  'Afrikaans 2nd AL','Physical Science',	'Agricultural Science',	'Agricultural Technology',	'Business studies',	'Computer application technology',	'Consumer Studies',	'Economics', 'English Home', 'English FAL', 'English 2nd AL','Geography','History','Information technology','IsiXhosa Home','IsiXhosa FAL', 'IsiXhosa 2nd AL','IsiNdebele Home', 'IsiNdebele FAL', 'IsiNdebele 2nd AL','IsiZulu Home, FAL, 2nd AL,',	'Sesotho Home','Sesotho FAL','Sesotho 2nd AL','Setswana Home','Setswana FAL','Setswana 2nd AL','Siswati Home','Siswati  FAL','Siswati  2nd', 'Siswati  AL','Xitsonga Home','Xitsonga FAL','Xitsonga 2nd AL','Tshivenda Home', 'Tshivenda FAL','Tshivenda 2nd AL','Life Orientation','Life Sciences','Mathematical Literacy','Mathematics','Religion studies','tourism']
    
  
    list3 = []
    count = 0 
    for z in range(0,101):
        list3.append(z)

    print(list3)


    subjectlist = sorted(subjects)
    h = request.GET.get('sub1')
    i = request.GET.get('sub2')
    j = request.GET.get('sub3')
    k = request.GET.get('sub4')
    l  = request.GET.get('sub5')
    m = request.GET.get('sub6')
    n = request.GET.get('sub7')
    
    subs= [h,i,j,k,l,m,n]  
    
    
    
    final = []
    
    for mn in range (0, len(subjects)):
        final.append(0)
        
    for k in range (0, len(subs)):
        for subj in subjects:
            if (subj == subjects[k]):
                final[k] =  1
            
    print(final)
    

    a = request.GET.get('marks1')
    b = request.GET.get('marks2')
    c = request.GET.get('marks3')
    d = request.GET.get('marks4')
    e = request.GET.get('marks5')
    f = request.GET.get('marks6')
    g = request.GET.get('marks7')

    sum = [a, b, c, d, e, f, g]
    count = 0
    aps = []

    for i in sum:
        if i is not None:
            #count += int(i)

            if (int(i) >= 0 and int(i) <= 29):
                aps.append(0)

            if (int(i) >= 30 and int(i) <= 39):
                aps.append(2)

            if (int(i) >= 40 and int(i) <= 49):
                aps.append(3)

            if (int(i) >= 50 and int(i) <= 59):
                aps.append(4)

            if (int(i) >= 60 and int(i) <= 69):
                aps.append(5)

            if (int(i) >= 70 and int(i) <= 79):
                aps.append(6)

            if (int(i) >= 80 and int(i) <= 100 ):
                aps.append(7)


    points = 0
    for value in aps:
       
        points += value


    print("your aps score is: " + str(points))
    


    if (points != 0):
        point = degree.objects.filter(points_requirements__gte= points)
    else:
        point = degree.objects.filter(points_requirements__gte= points)[:0]
        



   



    
    

    

    



    print( point)
    #for subj in sub1:
    
 # print(subj)

    
    if request.method == 'GET':
        
        
   
        
        return render (request,'search/find_course.html', {'list':subjectlist, "list4" : list3, "points":points, "point": point})

    



  




  




    













