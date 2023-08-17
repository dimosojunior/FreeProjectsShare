
from django.urls import path
from . import views


urlpatterns = [
    path('', views.USMAHome, name="USMAHome"),
    path('Universities/', views.UniversitiesView, name="Universities"),



#-------------------------UDSM---------------------------
    path('AllUdsmUniversityCourses/', views.AllUdsmUniversityCourses, name="AllUdsmUniversityCourses"),
    
    path('UdsmComputerEngineeringAllProjects/', views.UdsmComputerEngineeringAllProjects, name="UdsmComputerEngineeringAllProjects"),
    path('UdsmElectricalEngineeringAllProjects/', views.UdsmElectricalEngineeringAllProjects, name="UdsmElectricalEngineeringAllProjects"),
    path('UdsmICTAllProjects/', views.UdsmICTAllProjects, name="UdsmICTAllProjects"),
    path('UdsmOtherProjectsAllProjects/', views.UdsmOtherProjectsAllProjects, name="UdsmOtherProjectsAllProjects"),






#-------------------------UDOM---------------------------
    path('AllUdomUniversityCourses/', views.AllUdomUniversityCourses, name="AllUdomUniversityCourses"),
    
    path('UdomComputerEngineeringAllProjects/', views.UdomComputerEngineeringAllProjects, name="UdomComputerEngineeringAllProjects"),
    path('UdomElectricalEngineeringAllProjects/', views.UdomElectricalEngineeringAllProjects, name="UdomElectricalEngineeringAllProjects"),
    path('UdomICTAllProjects/', views.UdomICTAllProjects, name="UdomICTAllProjects"),
    path('UdomOtherProjectsAllProjects/', views.UdomOtherProjectsAllProjects, name="UdomOtherProjectsAllProjects"),




#-------------------------MUST---------------------------
    path('AllMustUniversityCourses/', views.AllMustUniversityCourses, name="AllMustUniversityCourses"),
    
    path('MustComputerEngineeringAllProjects/', views.MustComputerEngineeringAllProjects, name="MustComputerEngineeringAllProjects"),
    path('MustElectricalEngineeringAllProjects/', views.MustElectricalEngineeringAllProjects, name="MustElectricalEngineeringAllProjects"),
    path('MustICTAllProjects/', views.MustICTAllProjects, name="MustICTAllProjects"),
    path('MustOtherProjectsAllProjects/', views.MustOtherProjectsAllProjects, name="MustOtherProjectsAllProjects"),



#-------------------------DIT---------------------------
    path('AllDitUniversityCourses/', views.AllDitUniversityCourses, name="AllDitUniversityCourses"),
    
    path('DitComputerEngineeringAllProjects/', views.DitComputerEngineeringAllProjects, name="DitComputerEngineeringAllProjects"),
    path('DitElectricalEngineeringAllProjects/', views.DitElectricalEngineeringAllProjects, name="DitElectricalEngineeringAllProjects"),
    path('DitICTAllProjects/', views.DitICTAllProjects, name="DitICTAllProjects"),
    path('DitOtherProjectsAllProjects/', views.DitOtherProjectsAllProjects, name="DitOtherProjectsAllProjects"),






#----------------------READ PROJECT-------------------------
    path('ReadProject/<int:id>/', views.ReadProject, name="ReadProject"),











#-----------------------------HOB----------------------------------



	path('Hob/', views.HobsView, name="HobsView"),


	path('AllWebsitesExperts/', views.AllWebsitesExperts, name="AllWebsitesExperts"),
	path('AllMobileApplicationsExperts/', views.AllMobileApplicationsExperts, name="AllMobileApplicationsExperts"),
	path('AllGraphicsDesignerExperts/', views.AllGraphicsDesignerExperts, name="AllGraphicsDesignerExperts"),
	path('AllComputerMaintenanceExperts/', views.AllComputerMaintenanceExperts, name="AllComputerMaintenanceExperts"),
	path('AllMachineLearningExperts/', views.AllMachineLearningExperts, name="AllMachineLearningExperts"),
	path('AllComputerVisionExperts/', views.AllComputerVisionExperts, name="AllComputerVisionExperts"),
	path('AllAutomationExperts/', views.AllAutomationExperts, name="AllAutomationExperts"),
	path('AllDataAnalysisandVisualizationExperts/', views.AllDataAnalysisandVisualizationExperts, name="AllDataAnalysisandVisualizationExperts"),

 






 #----------------------------ARTICLES----------------------------



 	path('Articles/', views.ArticlesView, name="ArticlesView"),

 	path('AllAIArticles/', views.AllAIArticles, name="AllAIArticles"),
 	path('AllWebsiteArticles/', views.AllWebsiteArticles, name="AllWebsiteArticles"),
 	path('AllMobileApplicationsArticles/', views.AllMobileApplicationsArticles, name="AllMobileApplicationsArticles"),




#--------------------------READ ARTICLE----------------------

	path('ReadArticle/<int:id>/', views.ReadArticle, name="ReadArticle"),









#--------------------------ADD ARTICLES----------------------------------------
	path('AddAiArtcle/', views.AddAiArtcle, name="AddAiArtcle"),
	path('AddMobileAppArtcle/', views.AddMobileAppArtcle, name="AddMobileAppArtcle"),
	path('AddWebsitesArtcle/', views.AddWebsitesArtcle, name="AddWebsitesArtcle"),











#----------------------------SEARCH-----------------------------
 	path('search_university_autocomplete/', views.search_university_autocomplete, name="search_university_autocomplete"),


#-------------------------------SEARCH COURSES-------------------
 	path('udsm_search_university_autocomplete/', views.udsm_search_university_autocomplete, name="udsm_search_university_autocomplete"),
 	path('udom_search_university_autocomplete/', views.udom_search_university_autocomplete, name="udom_search_university_autocomplete"),
 	path('must_search_university_autocomplete/', views.must_search_university_autocomplete, name="must_search_university_autocomplete"),
 	path('dit_search_university_autocomplete/', views.dit_search_university_autocomplete, name="dit_search_university_autocomplete"),




#------------------------SEARCH PROJECT-------------------------
	path('project_search_university_autocomplete/', views.project_search_university_autocomplete, name="project_search_university_autocomplete"),


#------------------------SEARCH HOB-------------------------
	path('search_hob_autocomplete/', views.search_hob_autocomplete, name="search_hob_autocomplete"),


#------------------------SEARCH EXPERTS-------------------------
	path('websites_experts_search_autocomplete/', views.websites_experts_search_autocomplete, name="websites_experts_search_autocomplete"),
	path('graphics_experts_search_autocomplete/', views.graphics_experts_search_autocomplete, name="graphics_experts_search_autocomplete"),
	path('mobile_application_experts_search_autocomplete/', views.mobile_application_experts_search_autocomplete, name="mobile_application_experts_search_autocomplete"),
	path('computer_maintenance_experts_search_autocomplete/', views.computer_maintenance_experts_search_autocomplete, name="computer_maintenance_experts_search_autocomplete"),
	path('machine_learning_experts_search_autocomplete/', views.machine_learning_experts_search_autocomplete, name="machine_learning_experts_search_autocomplete"),
	path('computer_vision_experts_search_autocomplete/', views.computer_vision_experts_search_autocomplete, name="computer_vision_experts_search_autocomplete"),
	path('automation_experts_search_autocomplete/', views.automation_experts_search_autocomplete, name="automation_experts_search_autocomplete"),
	path('data_analysis_experts_search_autocomplete/', views.data_analysis_experts_search_autocomplete, name="data_analysis_experts_search_autocomplete"),







#------------------------SEARCH ARTICLES-------------------------
	path('all_articles_search_autocomplete/', views.all_articles_search_autocomplete, name="all_articles_search_autocomplete"),

	path('AI_articles_search_autocomplete/', views.AI_articles_search_autocomplete, name="AI_articles_search_autocomplete"),
	path('Websites_articles_search_autocomplete/', views.Websites_articles_search_autocomplete, name="Websites_articles_search_autocomplete"),
	path('Mobile_App_articles_search_autocomplete/', views.Mobile_App_articles_search_autocomplete, name="Mobile_App_articles_search_autocomplete"),









#------------------CONTACT ME----------------------------
	path('ContactMe/', views.ContactMe, name="ContactMe"),








#----------------------------------READ EXPERT---------------------------
	path('ReadExpert/<int:id>/', views.ReadExpert, name="ReadExpert"),



#-------------------------------ADD PROJECT------------------------


#---------------------------MUST-----------------------------
	path('AddMustComputerEngineeringProject/', views.AddMustComputerEngineeringProject, name="AddMustComputerEngineeringProject"),
	path('AddMustElectricalEngineeringProject/', views.AddMustElectricalEngineeringProject, name="AddMustElectricalEngineeringProject"),
	path('AddMustIctEngineeringProject/', views.AddMustIctEngineeringProject, name="AddMustIctEngineeringProject"),
	path('AddMustOtherEngineeringProject/', views.AddMustOtherEngineeringProject, name="AddMustOtherEngineeringProject"),


#---------------------------UDSM-----------------------------
	path('AddUdsmComputerEngineeringProject/', views.AddUdsmComputerEngineeringProject, name="AddUdsmComputerEngineeringProject"),
	path('AddUdsmElectricalEngineeringProject/', views.AddUdsmElectricalEngineeringProject, name="AddUdsmElectricalEngineeringProject"),
	path('AddUdsmIctEngineeringProject/', views.AddUdsmIctEngineeringProject, name="AddUdsmIctEngineeringProject"),
	path('AddUdsmOtherEngineeringProject/', views.AddUdsmOtherEngineeringProject, name="AddUdsmOtherEngineeringProject"),


#---------------------------UDOM-----------------------------
	path('AddUdomComputerEngineeringProject/', views.AddUdomComputerEngineeringProject, name="AddUdomComputerEngineeringProject"),
	path('AddUdomElectricalEngineeringProject/', views.AddUdomElectricalEngineeringProject, name="AddUdomElectricalEngineeringProject"),
	path('AddUdomIctEngineeringProject/', views.AddUdomIctEngineeringProject, name="AddUdomIctEngineeringProject"),
	path('AddUdomOtherEngineeringProject/', views.AddUdomOtherEngineeringProject, name="AddUdomOtherEngineeringProject"),



#---------------------------DIT-----------------------------
	path('AddDitComputerEngineeringProject/', views.AddDitComputerEngineeringProject, name="AddDitComputerEngineeringProject"),
	path('AddDitElectricalEngineeringProject/', views.AddDitElectricalEngineeringProject, name="AddDitElectricalEngineeringProject"),
	path('AddDitIctEngineeringProject/', views.AddDitIctEngineeringProject, name="AddDitIctEngineeringProject"),
	path('AddDitOtherEngineeringProject/', views.AddDitOtherEngineeringProject, name="AddDitOtherEngineeringProject"),


]
