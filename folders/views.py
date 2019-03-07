import os
from pathlib import Path
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


path='C:/Users/NagaDurga/Documents/'


##############Display All Folders Base on Path given
def dirstruc(request):
	global list_dirc
	list_dirc = os.listdir(path)
	return render(request,'form.html',{'list_dirc':list_dirc})

################Filtering Subfolders in dropdown
def subfoldes(request):
	global select_sub_fold
	select_sub_fold = request.GET.get('id', None)
	print(select_sub_fold)
	global sub_folders 
	sub_folders= os.listdir(path+str(select_sub_fold)+'/')
	return render(request,'form1.html',{'sub_folders':sub_folders})



######################Filterning  Subfolders in another Subfolders
def subfoldes2(request):
	global select_sub_fold2
	select_sub_fold2 = request.GET.get('id', None)
	global sub_folders2 
	sub_folders2= os.listdir(path+str(select_sub_fold)+'/'+str(select_sub_fold2)+'/')
	print(sub_folders2)
	return render(request,'sub_folds.html',{'sub_folders2':sub_folders2})






##################listing Slelected Folder and corresponding Subfolders	
def display_list(request):
	print("listing Slelected Folder and corresponding Subfolders")
	context={'select_sub_fold':select_sub_fold,'sub_folders':sub_folders,"select_sub_fold2":select_sub_fold2,"sub_folders2":sub_folders2}
	return render(request,'display_list.html',context)


###############Redirect to Form

def redirect(request):
	render(request,'form.html',{'list_dirc':list_dirc})

















