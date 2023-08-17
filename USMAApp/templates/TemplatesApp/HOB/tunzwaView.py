from django.shortcuts import render,redirect
from USMAApp.models import *
from django.http import JsonResponse
from django.db.models import Q
from TemplatesApp.forms import *
from django.contrib import messages
# Create your views here.

def USMAHome(request):

	return render(request, 'TemplatesApp/home.html')


def UniversitiesView(request):
	universities = Universities.objects.all().order_by('?')
	# form ya kusearch
	form = UniversitySearchForm(request.POST or None)
	if request.method =="POST":
		universities = Universities.objects.filter(UniversityName__icontains=form['UniversityName'].value())


	context = {
		"universities":universities,
		"form":form,
	}

	return render(request, 'TemplatesApp/Universities.html',context)




#--------------------------------COURSES--------------------


#---------------------UDSM------------------COURSES-------------
def AllUdsmUniversityCourses(request):
	courses = UdsmUniversityCourses.objects.all().order_by('?')

	# form ya kusearch
	form = UdsmSearchCourseForm(request.POST or None)
	if request.method =="POST":
		courses = UdsmUniversityCourses.objects.filter(CourseName__icontains=form['CourseName'].value())


	context = {
		"courses":courses,
		"form":form,
	}

	return render(request, 'TemplatesApp/UDSM/UdsmUniversityCourses.html',context)




#---------------------UDOM------------------COURSES-------------
def AllUdomUniversityCourses(request):
	courses = UdomUniversityCourses.objects.all().order_by('?')

	# form ya kusearch
	form = UdomSearchCourseForm(request.POST or None)
	if request.method =="POST":
		courses = UdomUniversityCourses.objects.filter(CourseName__icontains=form['CourseName'].value())


	context = {
		"courses":courses,
		"form":form,
	}

	return render(request, 'TemplatesApp/UDOM/UdomUniversityCourses.html',context)


#---------------------MUST------------------COURSES-------------
def AllMustUniversityCourses(request):
	courses = MustUniversityCourses.objects.all().order_by('?')
	# form ya kusearch
	form = MustSearchCourseForm(request.POST or None)
	if request.method =="POST":
		courses = MustUniversityCourses.objects.filter(CourseName__icontains=form['CourseName'].value())


	context = {
		"courses":courses,
		"form":form,
	}

	return render(request, 'TemplatesApp/MUST/MustUniversityCourses.html',context)


#---------------------DIT------------------COURSES-------------
def AllDitUniversityCourses(request):
	courses = DitUniversityCourses.objects.all().order_by('?')
	# form ya kusearch
	form = DitSearchCourseForm(request.POST or None)
	if request.method =="POST":
		courses = DitUniversityCourses.objects.filter(CourseName__icontains=form['CourseName'].value())


	context = {
		"courses":courses,
		"form":form,
	}

	return render(request, 'TemplatesApp/DIT/DitUniversityCourses.html',context)













#----------------------PROJECTS-----------------------------



#----------------------UDSM PROJECTS----------------------


#-----------------------COMPUTER ENGINEERING PROJECTS--------


def UdsmComputerEngineeringAllProjects(request):
	projects = AllProjects.objects.filter(university__UniversityName__icontains="University of Dar es salaam", CourseName__CourseName__icontains="Computer Engineering")
	
	# form ya kusearch
	form = ProjectSearchForm(request.POST or None)
	if request.method =="POST":
		projects = AllProjects.objects.filter(university__UniversityName__icontains="University of Dar es salaam", CourseName__CourseName__icontains="Computer Engineering",ProjectName__icontains=form['ProjectName'].value())


	context = {
		"projects":projects,
		"form":form,
	}

	return render(request, 'TemplatesApp/UDSM/UdsmComputerEngineeringAllProjects.html',context)

#-----------------------ELECTRICAL ENGINEERING PROJECTS--------
def UdsmElectricalEngineeringAllProjects(request):
	projects = AllProjects.objects.filter(university__UniversityName__icontains="University of Dar es salaam", CourseName__CourseName__icontains="Electrical Engineering")
	# form ya kusearch
	form = ProjectSearchForm(request.POST or None)
	if request.method =="POST":
		projects = AllProjects.objects.filter(university__UniversityName__icontains="University of Dar es salaam", CourseName__CourseName__icontains="Electrical Engineering",ProjectName__icontains=form['ProjectName'].value())


	context = {
		"projects":projects,
		"form":form,
	}

	return render(request, 'TemplatesApp/UDSM/UdsmElectricalEngineeringAllProjects.html',context)


#-----------------------ICT  PROJECTS--------
def UdsmICTAllProjects(request):
	projects =AllProjects.objects.filter(university__UniversityName__icontains="University of Dar es salaam", CourseName__CourseName__icontains="ICT")
	# form ya kusearch
	form = ProjectSearchForm(request.POST or None)
	if request.method =="POST":
		projects = AllProjects.objects.filter(university__UniversityName__icontains="University of Dar es salaam", CourseName__CourseName__icontains="ICT", ProjectName__icontains=form['ProjectName'].value())


	context = {
		"projects":projects,
		"form":form,
	}

	return render(request, 'TemplatesApp/UDSM/UdsmICTAllProjects.html',context)


#-----------------------OTHER PROJECTS--------
def UdsmOtherProjectsAllProjects(request):
	projects = AllProjects.objects.filter(university__UniversityName__icontains="University of Dar es salaam", CourseName__CourseName__icontains="Other Projects")
	# form ya kusearch
	form = ProjectSearchForm(request.POST or None)
	if request.method =="POST":
		projects = AllProjects.objects.filter(university__UniversityName__icontains="University of Dar es salaam", CourseName__CourseName__icontains="Other Projects", ProjectName__icontains=form['ProjectName'].value())


	context = {
		"projects":projects,
		"form":form,
	}

	return render(request, 'TemplatesApp/UDSM/UdsmOtherProjectsAllProjects.html',context)


#----------------------------MWISHO WA UDSM PROJECTS----------------










#----------------------UDOM PROJECTS----------------------


#-----------------------COMPUTER ENGINEERING PROJECTS--------


def UdomComputerEngineeringAllProjects(request):
	projects = AllProjects.objects.filter(university__UniversityName__icontains="University of Dodoma", CourseName__CourseName__icontains="Computer Engineering")
	# form ya kusearch
	form = ProjectSearchForm(request.POST or None)
	if request.method =="POST":
		projects = AllProjects.objects.filter(university__UniversityName__icontains="University of Dodoma", CourseName__CourseName__icontains="Computer Engineering", ProjectName__icontains=form['ProjectName'].value())


	context = {
		"projects":projects,
		"form":form,
	}

	return render(request, 'TemplatesApp/UDOM/UdomComputerEngineeringAllProjects.html',context)




#-----------------------ELECTRICAL ENGINEERING PROJECTS--------
def UdomElectricalEngineeringAllProjects(request):
	projects = AllProjects.objects.filter(university__UniversityName__icontains="University of Dodoma", CourseName__CourseName__icontains="Electrical Engineering")
	# form ya kusearch
	form = ProjectSearchForm(request.POST or None)
	if request.method =="POST":
		projects = AllProjects.objects.filter(university__UniversityName__icontains="University of Dodoma", CourseName__CourseName__icontains="Electrical Engineering", ProjectName__icontains=form['ProjectName'].value())


	context = {
		"projects":projects,
		"form":form,
	}

	return render(request, 'TemplatesApp/UDOM/UdomElectricalEngineeringAllProjects.html',context)


#-----------------------ICT  PROJECTS--------
def UdomICTAllProjects(request):
	projects = AllProjects.objects.filter(university__UniversityName__icontains="University of Dodoma", CourseName__CourseName__icontains="ICT")
	# form ya kusearch
	form = ProjectSearchForm(request.POST or None)
	if request.method =="POST":
		projects = AllProjects.objects.filter(university__UniversityName__icontains="University of Dodoma", CourseName__CourseName__icontains="ICT", ProjectName__icontains=form['ProjectName'].value())


	context = {
		"projects":projects,
		"form":form,
	}

	return render(request, 'TemplatesApp/UDOM/UdomICTAllProjects.html',context)


#-----------------------OTHER PROJECTS--------
def UdomOtherProjectsAllProjects(request):
	projects = AllProjects.objects.filter(university__UniversityName__icontains="University of Dodoma", CourseName__CourseName__icontains="Other Projects")
	# form ya kusearch
	form = ProjectSearchForm(request.POST or None)
	if request.method =="POST":
		projects = AllProjects.objects.filter(university__UniversityName__icontains="University of Dodoma", CourseName__CourseName__icontains="Other Projects", ProjectName__icontains=form['ProjectName'].value())


	context = {
		"projects":projects,
		"form":form,
	}

	return render(request, 'TemplatesApp/UDOM/UdomOtherProjectsAllProjects.html',context)


#----------------------------MWISHO WA UDOM PROJECTS----------------












#----------------------MUST PROJECTS----------------------


#-----------------------COMPUTER ENGINEERING PROJECTS--------


def MustComputerEngineeringAllProjects(request):
	projects = AllProjects.objects.filter(university__UniversityName__icontains="Mbeya University", CourseName__CourseName__icontains="Computer Engineering")
	# form ya kusearch
	form = ProjectSearchForm(request.POST or None)
	if request.method =="POST":
		projects = AllProjects.objects.filter(university__UniversityName__icontains="Mbeya University", CourseName__CourseName__icontains="Computer Engineering",ProjectName__icontains=form['ProjectName'].value())


	context = {
		"projects":projects,
		"form":form,
	}

	return render(request, 'TemplatesApp/MUST/MustComputerEngineeringAllProjects.html',context)


#-----------------------ELECTRICAL ENGINEERING PROJECTS--------
def MustElectricalEngineeringAllProjects(request):
	projects = AllProjects.objects.filter(university__UniversityName__icontains="Mbeya University", CourseName__CourseName__icontains="Electrical Engineering")
	# form ya kusearch
	form = ProjectSearchForm(request.POST or None)
	if request.method =="POST":
		projects = AllProjects.objects.filter(university__UniversityName__icontains="Mbeya University", CourseName__CourseName__icontains="Electrical Engineering", ProjectName__icontains=form['ProjectName'].value())


	context = {
		"projects":projects,
		"form":form,
	}

	return render(request, 'TemplatesApp/MUST/MustElectricalEngineeringAllProjects.html',context)


#-----------------------ICT  PROJECTS--------
def MustICTAllProjects(request):
	projects = AllProjects.objects.filter(university__UniversityName__icontains="Mbeya University", CourseName__CourseName__icontains="ICT")
	# form ya kusearch
	form = ProjectSearchForm(request.POST or None)
	if request.method =="POST":
		projects = AllProjects.objects.filter(university__UniversityName__icontains="Mbeya University", CourseName__CourseName__icontains="ICT", ProjectName__icontains=form['ProjectName'].value())


	context = {
		"projects":projects,
		"form":form,
	}

	return render(request, 'TemplatesApp/MUST/MustICTAllProjects.html',context)


#-----------------------OTHER PROJECTS--------
def MustOtherProjectsAllProjects(request):
	projects = AllProjects.objects.filter(university__UniversityName__icontains="Mbeya University", CourseName__CourseName__icontains="Other Projects")
	# form ya kusearch
	form = ProjectSearchForm(request.POST or None)
	if request.method =="POST":
		projects = AllProjects.objects.filter(university__UniversityName__icontains="Mbeya University", CourseName__CourseName__icontains="Other Projects", ProjectName__icontains=form['ProjectName'].value())


	context = {
		"projects":projects,
		"form":form,
	}

	return render(request, 'TemplatesApp/MUST/MustOtherProjectsAllProjects.html',context)


#----------------------------MWISHO WA MUST PROJECTS----------------











#----------------------DIT PROJECTS----------------------


#-----------------------COMPUTER ENGINEERING PROJECTS--------


def DitComputerEngineeringAllProjects(request):
	projects = AllProjects.objects.filter(university__UniversityName__icontains="DIT", CourseName__CourseName__icontains="Computer Engineering")
	# form ya kusearch
	form = ProjectSearchForm(request.POST or None)
	if request.method =="POST":
		projects = AllProjects.objects.filter(university__UniversityName__icontains="DIT", CourseName__CourseName__icontains="Computer Engineering", ProjectName__icontains=form['ProjectName'].value())


	context = {
		"projects":projects,
		"form":form,
	}

	return render(request, 'TemplatesApp/DIT/DitComputerEngineeringAllProjects.html',context)

#-----------------------ELECTRICAL ENGINEERING PROJECTS--------
def DitElectricalEngineeringAllProjects(request):
	projects = AllProjects.objects.filter(university__UniversityName__icontains="DIT", CourseName__CourseName__icontains="Electrical Engineering")
	# form ya kusearch
	form = ProjectSearchForm(request.POST or None)
	if request.method =="POST":
		projects = AllProjects.objects.filter(university__UniversityName__icontains="DIT", CourseName__CourseName__icontains="Electrical Engineering",ProjectName__icontains=form['ProjectName'].value())


	context = {
		"projects":projects,
		"form":form,
	}

	return render(request, 'TemplatesApp/DIT/DitElectricalEngineeringAllProjects.html',context)


#-----------------------ICT  PROJECTS--------
def DitICTAllProjects(request):
	projects =AllProjects.objects.filter(university__UniversityName__icontains="DIT", CourseName__CourseName__icontains="ICT")
	# form ya kusearch
	form = ProjectSearchForm(request.POST or None)
	if request.method =="POST":
		projects = AllProjects.objects.filter(university__UniversityName__icontains="DIT", CourseName__CourseName__icontains="ICT", ProjectName__icontains=form['ProjectName'].value())


	context = {
		"projects":projects,
		"form":form,
	}

	return render(request, 'TemplatesApp/DIT/DitICTAllProjects.html',context)


#-----------------------OTHER PROJECTS--------
def DitOtherProjectsAllProjects(request):
	projects = AllProjects.objects.filter(university__UniversityName__icontains="DIT", CourseName__CourseName__icontains="Other Projects")
	# form ya kusearch
	form = ProjectSearchForm(request.POST or None)
	if request.method =="POST":
		projects = AllProjects.objects.filter(university__UniversityName__icontains="DIT", CourseName__CourseName__icontains="Other Projects", ProjectName__icontains=form['ProjectName'].value())


	context = {
		"projects":projects,
		"form":form,
	}

	return render(request, 'TemplatesApp/DIT/DitOtherProjectsAllProjects.html',context)


#----------------------------MWISHO WA DIT PROJECTS----------------















#----------------------------READ PROJECT------------------

def ReadProject(request,id):
	ReadProject = AllProjects.objects.get(id=id)

	context = {
		"ReadProject":ReadProject,
	}

	return render(request, 'TemplatesApp/ReadProject.html',context)















#-------------------------------HOB------------------------------


def HobsView(request):
	hobs = Hob.objects.all().order_by('?')

	form = HobSearchForm(request.POST or None)
	if request.method =="POST":
		hobs = Hob.objects.filter(CategoryName__icontains=form['CategoryName'].value())


	context = {
		"hobs":hobs,
		"form":form,
	}

	return render(request, 'TemplatesApp/HOB/HobsView.html',context)




# -------------------WEBSITES EXPERTS-------------
def AllWebsitesExperts(request):
	experts = WebsitesExperts.objects.all().order_by('?')
	# form ya kusearch
	form = WebsitesExpertsSearchForm(request.POST or None)
	if request.method =="POST":
		experts = WebsitesExperts.objects.filter(StudentName__icontains=form['StudentName'].value())


	context = {
		"experts":experts,
		"form":form,
	}

	return render(request, 'TemplatesApp/HOB/AllWebsitesExperts.html',context)



# -------------------Mobile App EXPERTS-------------
def AllMobileApplicationsExperts(request):
	experts = MobileApplicationsExperts.objects.all().order_by('?')

	context = {
		"experts":experts,
	}

	return render(request, 'TemplatesApp/HOB/AllMobileApplicationsExperts.html',context)


# ------------------- Graphics EXPERTS-------------
def AllGraphicsDesignerExperts(request):
	experts = GraphicsDesignerExperts.objects.all().order_by('?')

	context = {
		"experts":experts,
	}

	return render(request, 'TemplatesApp/HOB/AllGraphicsDesignerExperts.html',context)



# ------------------- COMPUTER MAINTENANCE EXPERTS-------------
def AllComputerMaintenanceExperts(request):
	experts = ComputerMaintenanceExperts.objects.all().order_by('?')

	context = {
		"experts":experts,
	}

	return render(request, 'TemplatesApp/HOB/AllComputerMaintenanceExperts.html',context)


# ------------------- MACHINE LEARNING  EXPERTS-------------
def AllMachineLearningExperts(request):
	experts = MachineLearningExperts.objects.all().order_by('?')

	context = {
		"experts":experts,
	}

	return render(request, 'TemplatesApp/HOB/AllMachineLearningExperts.html',context)



# ------------------- COMPUTER VISION  EXPERTS-------------
def AllComputerVisionExperts(request):
	experts = ComputerVisionExperts.objects.all().order_by('?')

	context = {
		"experts":experts,
	}

	return render(request, 'TemplatesApp/HOB/AllComputerVisionExperts.html',context)



# ------------------- AUTOMATION  EXPERTS   -------------
def AllAutomationExperts(request):
	experts = AutomationExperts.objects.all().order_by('?')

	context = {
		"experts":experts,
	}

	return render(request, 'TemplatesApp/HOB/AllAutomationExperts.html',context)




# ------------------- DATA ANALYSIS  EXPERTS   -------------
def AllDataAnalysisandVisualizationExperts(request):
	experts = DataAnalysisandVisualizationExperts.objects.all().order_by('?')

	context = {
		"experts":experts,
	}

	return render(request, 'TemplatesApp/HOB/AllDataAnalysisandVisualizationExperts.html',context)







#----------------------------READ EXPERT------------------

def ReadExpert(request,id):
	ReadExpert = AllProjects.objects.get(id=id)

	context = {
		"ReadExpert":ReadExpert,
	}

	return render(request, 'TemplatesApp/ReadExpert.html',context)












#---------------------------ARTICLES-------------------------------




# ------------------- ALL ARTICLES-------------
def ArticlesView(request):
	articles = Articles.objects.all().order_by('?')

	context = {
		"articles":articles,
	}

	return render(request, 'TemplatesApp/ARTICLES/ArticlesView.html',context)


# ------------------- AI ARTICLES-------------
def AllAIArticles(request):
	articles = AIArticles.objects.all().order_by('?')

	context = {
		"articles":articles,
	}

	return render(request, 'TemplatesApp/ARTICLES/AllAIArticles.html',context)


# ------------------- WEBSITES ARTICLES-------------
def AllWebsiteArticles(request):
	articles = WebsiteArticles.objects.all().order_by('?')

	context = {
		"articles":articles,
	}

	return render(request, 'TemplatesApp/ARTICLES/AllWebsiteArticles.html',context)


# ------------------- MOBILE APP ARTICLES-------------
def AllMobileApplicationsArticles(request):
	articles = MobileApplicationsArticles.objects.all().order_by('?')

	context = {
		"articles":articles,
	}

	return render(request, 'TemplatesApp/ARTICLES/AllMobileApplicationsArticles.html',context)









def search_university_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(UniversityName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    university = Universities.objects.filter(search)
    mylist= []
    mylist += [x.UniversityName for x in university]
    return JsonResponse(mylist, safe=False)


def udsm_search_university_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(CourseName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    course = UdsmUniversityCourses.objects.filter(search)
    mylist= []
    mylist += [x.CourseName for x in course]
    return JsonResponse(mylist, safe=False)

def udom_search_university_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(CourseName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    course = UdomUniversityCourses.objects.filter(search)
    mylist= []
    mylist += [x.CourseName for x in course]
    return JsonResponse(mylist, safe=False)


def must_search_university_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(CourseName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    course = MustUniversityCourses.objects.filter(search)
    mylist= []
    mylist += [x.CourseName for x in course]
    return JsonResponse(mylist, safe=False)


def dit_search_university_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(CourseName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    course = DitUniversityCourses.objects.filter(search)
    mylist= []
    mylist += [x.CourseName for x in course]
    return JsonResponse(mylist, safe=False)







#-----------------------PROJECT SEARCH------------------

def project_search_university_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(ProjectName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    project = AllProjects.objects.filter(search)
    mylist= []
    mylist += [x.ProjectName for x in project]
    return JsonResponse(mylist, safe=False)




#-----------------------HOB SEARCH------------------

def search_hob_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(CategoryName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    hob = Hob.objects.filter(search)
    mylist= []
    mylist += [x.CategoryName for x in hob]
    return JsonResponse(mylist, safe=False)






#---------------------------SEARCH EXPERTS----------------------




#----------------------- SEARCH WEBSITES EXPERTS------------------
def websites_experts_search_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(StudentName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    expert = WebsitesExperts.objects.filter(search)
    mylist= []
    mylist += [x.StudentName for x in expert]
    return JsonResponse(mylist, safe=False)

#----------------------- SEARCH GRAPHICS EXPERTS------------------
def graphics_experts_search_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(StudentName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    expert = GraphicsDesignerExperts.objects.filter(search)
    mylist= []
    mylist += [x.StudentName for x in expert]
    return JsonResponse(mylist, safe=False)

#----------------------- SEARCH MOBILE APP EXPERTS------------------
def mobile_application_experts_search_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(StudentName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    expert = MobileApplicationsExperts.objects.filter(search)
    mylist= []
    mylist += [x.StudentName for x in expert]
    return JsonResponse(mylist, safe=False)


#----------------------- SEARCH COMPUTER MAINTENANCE EXPERTS------------------
def computer_maintenance_experts_search_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(StudentName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    expert = ComputerMaintenanceExperts.objects.filter(search)
    mylist= []
    mylist += [x.StudentName for x in expert]
    return JsonResponse(mylist, safe=False)


#----------------------- SEARCH MACHINE LEARNING EXPERTS------------------
def machine_learning_experts_search_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(StudentName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    expert = MachineLearningExperts.objects.filter(search)
    mylist= []
    mylist += [x.StudentName for x in expert]
    return JsonResponse(mylist, safe=False)


#----------------------- SEARCH COMPUTER VISION EXPERTS------------------
def computer_vision_experts_search_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(StudentName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    expert = ComputerVisionExperts.objects.filter(search)
    mylist= []
    mylist += [x.StudentName for x in expert]
    return JsonResponse(mylist, safe=False)


#----------------------- SEARCH AUTOMATION  EXPERTS------------------
def automation_experts_search_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(StudentName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    expert = AutomationExperts.objects.filter(search)
    mylist= []
    mylist += [x.StudentName for x in expert]
    return JsonResponse(mylist, safe=False)


#----------------------- SEARCH DATA ANALYSIS EXPERTS------------------
def data_analysis_experts_search_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(StudentName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    expert = DataAnalysisandVisualizationExperts.objects.filter(search)
    mylist= []
    mylist += [x.StudentName for x in expert]
    return JsonResponse(mylist, safe=False)









#------------------------ADD PROJECT------------------










#---------------------------MUST------------------------------


def AddMustComputerEngineeringProject(request):
	form = AddProjectForm()


	if request.method == "POST":
		ProjectName = request.POST.get('ProjectName')
		form = AddProjectForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"{ProjectName} Added Successfuly")
			return redirect('MustComputerEngineeringAllProjects')

		messages.info(request, "There is a problem when you are creating a new project")
		return redirect('AddMustComputerEngineeringProject')


	context = {
		"form":form,
	}

	return render(request, 'TemplatesApp/AddProject/MUST/AddMustComputerEngineeringProject.html',context)




def AddMustElectricalEngineeringProject(request):
	form = AddProjectForm()


	if request.method == "POST":
		ProjectName = request.POST.get('ProjectName')
		form = AddProjectForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"{ProjectName} Added Successfuly")
			return redirect('MustElectricalEngineeringAllProjects')

		messages.info(request, "There is a problem when you are creating a new project")
		return redirect('AddMustElectricalEngineeringProject')


	context = {
		"form":form,
	}

	return render(request, 'TemplatesApp/AddProject/MUST/AddMustElectricalEngineeringProject.html',context)




def AddMustIctEngineeringProject(request):
	form = AddProjectForm()


	if request.method == "POST":
		ProjectName = request.POST.get('ProjectName')
		form = AddProjectForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"{ProjectName} Added Successfuly")
			return redirect('MustICTAllProjects')

		messages.info(request, "There is a problem when you are creating a new project")
		return redirect('AddMustIctEngineeringProject')


	context = {
		"form":form,
	}

	return render(request, 'TemplatesApp/AddProject/MUST/AddMustIctEngineeringProject.html',context)




def AddMustOtherEngineeringProject(request):
	form = AddProjectForm()


	if request.method == "POST":
		ProjectName = request.POST.get('ProjectName')
		form = AddProjectForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"{ProjectName} Added Successfuly")
			return redirect('MustOtherProjectsAllProjects')

		messages.info(request, "There is a problem when you are creating a new project")
		return redirect('AddMustOtherEngineeringProject')


	context = {
		"form":form,
	}

	return render(request, 'TemplatesApp/AddProject/MUST/AddMustOtherEngineeringProject.html',context)























#---------------------------UDSM------------------------------


def AddUdsmComputerEngineeringProject(request):
	form = AddProjectForm()


	if request.method == "POST":
		ProjectName = request.POST.get('ProjectName')
		form = AddProjectForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"{ProjectName} Added Successfuly")
			return redirect('UdsmComputerEngineeringAllProjects')

		messages.info(request, "There is a problem when you are creating a new project")
		return redirect('AddUdsmComputerEngineeringProject')


	context = {
		"form":form,
	}

	return render(request, 'TemplatesApp/AddProject/UDSM/AddUdsmComputerEngineeringProject.html',context)




def AddUdsmElectricalEngineeringProject(request):
	form = AddProjectForm()


	if request.method == "POST":
		ProjectName = request.POST.get('ProjectName')
		form = AddProjectForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"{ProjectName} Added Successfuly")
			return redirect('UdsmElectricalEngineeringAllProjects')

		messages.info(request, "There is a problem when you are creating a new project")
		return redirect('AddUdsmElectricalEngineeringProject')


	context = {
		"form":form,
	}

	return render(request, 'TemplatesApp/AddProject/UDSM/AddUdsmElectricalEngineeringProject.html',context)




def AddUdsmIctEngineeringProject(request):
	form = AddProjectForm()


	if request.method == "POST":
		ProjectName = request.POST.get('ProjectName')
		form = AddProjectForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"{ProjectName} Added Successfuly")
			return redirect('UdsmICTAllProjects')

		messages.info(request, "There is a problem when you are creating a new project")
		return redirect('AddUdsmIctEngineeringProject')


	context = {
		"form":form,
	}

	return render(request, 'TemplatesApp/AddProject/UDSM/AddUdsmIctEngineeringProject.html',context)




def AddUdsmOtherEngineeringProject(request):
	form = AddProjectForm()


	if request.method == "POST":
		ProjectName = request.POST.get('ProjectName')
		form = AddProjectForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"{ProjectName} Added Successfuly")
			return redirect('UdsmOtherProjectsAllProjects')

		messages.info(request, "There is a problem when you are creating a new project")
		return redirect('AddUdsmOtherEngineeringProject')

	context = {
		"form":form,
	}

	return render(request, 'TemplatesApp/AddProject/UDSM/AddUdsmOtherEngineeringProject.html',context)





#------------------------------UDOM-------------------------------




def AddUdomComputerEngineeringProject(request):
	form = AddProjectForm()


	if request.method == "POST":
		ProjectName = request.POST.get('ProjectName')
		form = AddProjectForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"{ProjectName} Added Successfuly")
			return redirect('UdomComputerEngineeringAllProjects')

		messages.info(request, "There is a problem when you are creating a new project")
		return redirect('AddUdomComputerEngineeringProject')


	context = {
		"form":form,
	}

	return render(request, 'TemplatesApp/AddProject/UDOM/AddUdomComputerEngineeringProject.html',context)




def AddUdomElectricalEngineeringProject(request):
	form = AddProjectForm()


	if request.method == "POST":
		ProjectName = request.POST.get('ProjectName')
		form = AddProjectForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"{ProjectName} Added Successfuly")
			return redirect('UdomElectricalEngineeringAllProjects')

		messages.info(request, "There is a problem when you are creating a new project")
		return redirect('AddUdomElectricalEngineeringProject')


	context = {
		"form":form,
	}

	return render(request, 'TemplatesApp/AddProject/UDOM/AddUdomElectricalEngineeringProject.html',context)




def AddUdomIctEngineeringProject(request):
	form = AddProjectForm()


	if request.method == "POST":
		ProjectName = request.POST.get('ProjectName')
		form = AddProjectForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"{ProjectName} Added Successfuly")
			return redirect('UdomICTAllProjects')

		messages.info(request, "There is a problem when you are creating a new project")
		return redirect('AddUdomIctEngineeringProject')


	context = {
		"form":form,
	}

	return render(request, 'TemplatesApp/AddProject/UDOM/AddUdomIctEngineeringProject.html',context)




def AddUdomOtherEngineeringProject(request):
	form = AddProjectForm()


	if request.method == "POST":
		ProjectName = request.POST.get('ProjectName')
		form = AddProjectForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"{ProjectName} Added Successfuly")
			return redirect('UdomOtherProjectsAllProjects')

		messages.info(request, "There is a problem when you are creating a new project")
		return redirect('AddUdomOtherEngineeringProject')

	context = {
		"form":form,
	}

	return render(request, 'TemplatesApp/AddProject/UDOM/AddUdomOtherEngineeringProject.html',context)








#------------------------------DIT-------------------------------




def AddDitComputerEngineeringProject(request):
	form = AddProjectForm()


	if request.method == "POST":
		ProjectName = request.POST.get('ProjectName')
		form = AddProjectForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"{ProjectName} Added Successfuly")
			return redirect('DitComputerEngineeringAllProjects')

		messages.info(request, "There is a problem when you are creating a new project")
		return redirect('AddDitComputerEngineeringProject')


	context = {
		"form":form,
	}

	return render(request, 'TemplatesApp/AddProject/DIT/AddDitComputerEngineeringProject.html',context)




def AddDitElectricalEngineeringProject(request):
	form = AddProjectForm()


	if request.method == "POST":
		ProjectName = request.POST.get('ProjectName')
		form = AddProjectForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"{ProjectName} Added Successfuly")
			return redirect('DitElectricalEngineeringAllProjects')

		messages.info(request, "There is a problem when you are creating a new project")
		return redirect('AddDitElectricalEngineeringProject')


	context = {
		"form":form,
	}

	return render(request, 'TemplatesApp/AddProject/DIT/AddDitElectricalEngineeringProject.html',context)




def AddDitIctEngineeringProject(request):
	form = AddProjectForm()


	if request.method == "POST":
		ProjectName = request.POST.get('ProjectName')
		form = AddProjectForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"{ProjectName} Added Successfuly")
			return redirect('DitICTAllProjects')

		messages.info(request, "There is a problem when you are creating a new project")
		return redirect('AddDitIctEngineeringProject')


	context = {
		"form":form,
	}

	return render(request, 'TemplatesApp/AddProject/DIT/AddDitIctEngineeringProject.html',context)




def AddDitOtherEngineeringProject(request):
	form = AddProjectForm()


	if request.method == "POST":
		ProjectName = request.POST.get('ProjectName')
		form = AddProjectForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"{ProjectName} Added Successfuly")
			return redirect('DitOtherProjectsAllProjects')

		messages.info(request, "There is a problem when you are creating a new project")
		return redirect('AddDitOtherEngineeringProject')

	context = {
		"form":form,
	}

	return render(request, 'TemplatesApp/AddProject/DIT/AddDitOtherEngineeringProject.html',context)
