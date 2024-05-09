from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from courses.models import Course
from services.models import Services
from team.models import Team
from contact_form.models import ContactMessage
from gallery.models import class_Photo
from trainer.models import Trainer
#home page Views
def home(request):
    services = Services.objects.all()
    teamData=Team.objects.all()
    data={
        'services': services,
        'teamData':teamData
    }
    return render(request,"index.html",data)

def service_detail(request, service_id):
    service = get_object_or_404(Services, pk=service_id)
    return render(request, 'service_details.html', {'service': service})

#course page view
def cources(request):
    courseData=Course.objects.all()[:6] # limit for only six courses
    Data1={
        'courseData':courseData
    }
    return render(request,"cources.html",Data1)
# Blog page View
def blog(request):
    return render(request,"blog.html")

# contact_us view
def contact_us(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        
        # Save data to the database
        contact_message = ContactMessage.objects.create(
            name=name,
            email=email,
            phone=phone,
            message=message
        )
        
        success_message = "Thank you for your message!"
        return render(request, 'contact_us.html', {'success_message': success_message})
    else: 
        return render(request, 'contact_us.html')


def about_us(request):
    trainers = Trainer.objects.all()
    return render(request,"about_us.html",{'trainers': trainers})

def gallery(request):
     photos = class_Photo.objects.all()

     return render(request, 'gallery.html', {'photos': photos})

def tutorials(request):
    return render(request,"tutorials.html")

def solvedcoding(request):
    return render(request,'solved_coding.html')

def interview_prepration(request):
    return render(request,'interview_prepration.html')

