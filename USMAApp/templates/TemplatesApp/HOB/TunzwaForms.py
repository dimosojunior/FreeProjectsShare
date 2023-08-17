from USMAApp.models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


class UniversitySearchForm(forms.ModelForm):
	
	UniversityName = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'university', 'placeholder' : 'Search University'})

	)
	
	class Meta:
		model = Universities
		fields =['UniversityName']


class UdsmSearchCourseForm(forms.ModelForm):
	
	CourseName = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'course', 'placeholder' : 'Search Course'})

	)
	
	class Meta:
		model = UdsmUniversityCourses
		fields =['CourseName']


class UdomSearchCourseForm(forms.ModelForm):
	
	CourseName = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'course', 'placeholder' : 'Search Course'})

	)
	
	class Meta:
		model = UdomUniversityCourses
		fields =['CourseName']


class MustSearchCourseForm(forms.ModelForm):
	
	CourseName = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'course', 'placeholder' : 'Search Course'})

	)
	
	class Meta:
		model = MustUniversityCourses
		fields =['CourseName']


class DitSearchCourseForm(forms.ModelForm):
	
	CourseName = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'course', 'placeholder' : 'Search Course'})

	)
	
	class Meta:
		model = DitUniversityCourses
		fields =['CourseName']



class HobSearchForm(forms.ModelForm):
	
	CategoryName = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'hob', 'placeholder' : 'Search Expert Category'})

	)
	
	class Meta:
		model = Hob
		fields =['CategoryName']





#-------------------------------SEARCH EXPERT----------------------------

class WebsitesExpertsSearchForm(forms.ModelForm):
	
	StudentName = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'expert', 'placeholder' : 'Search Expert'})

	)
	
	class Meta:
		model = WebsitesExperts
		fields =['StudentName']

class MobileApplicationsExpertsSearchForm(forms.ModelForm):
	
	StudentName = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'expert', 'placeholder' : 'Search Expert'})

	)
	
	class Meta:
		model = MobileApplicationsExperts
		fields =['StudentName']

class GraphicsDesignerExpertsSearchForm(forms.ModelForm):
	
	StudentName = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'expert', 'placeholder' : 'Search Expert'})

	)
	
	class Meta:
		model = GraphicsDesignerExperts
		fields =['StudentName']



class ComputerMaintenanceExpertsSearchForm(forms.ModelForm):
	
	StudentName = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'expert', 'placeholder' : 'Search Expert'})

	)
	
	class Meta:
		model = ComputerMaintenanceExperts
		fields =['StudentName']




class MachineLearningExpertsSearchForm(forms.ModelForm):
	
	StudentName = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'expert', 'placeholder' : 'Search Expert'})

	)
	
	class Meta:
		model = MachineLearningExperts
		fields =['StudentName']



class ComputerVisionExpertsSearchForm(forms.ModelForm):
	
	StudentName = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'expert', 'placeholder' : 'Search Expert'})

	)
	
	class Meta:
		model = ComputerVisionExperts
		fields =['StudentName']



class AutomationExpertsSearchForm(forms.ModelForm):
	
	StudentName = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'expert', 'placeholder' : 'Search Expert'})

	)
	
	class Meta:
		model = AutomationExperts
		fields =['StudentName']




class DataAnalysisandVisualizationExpertsSearchForm(forms.ModelForm):
	
	StudentName = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'expert', 'placeholder' : 'Search Expert'})

	)
	
	class Meta:
		model = DataAnalysisandVisualizationExperts
		fields =['StudentName']




#---------------------------MWISHO WA EXPERTS SEARCH FORM--------------


















#---------------------------PROJECTS FORM-------------------


class ProjectSearchForm(forms.ModelForm):
	
	ProjectName = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'project', 'placeholder' : 'Search Project'})

	)
	
	class Meta:
		model = AllProjects
		fields =['ProjectName']





#---------------------------ADD PROJECTS FORMS-------------------


class AddProjectForm(forms.ModelForm):
	
	class Meta:
		model = AllProjects
		fields ='__all__'
		#fields= ["university","ProjectName", "StudentName", "CourseName","Year"]