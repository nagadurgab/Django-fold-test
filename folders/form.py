from django.forms import ModelForm
from django import forms
from . import views 


#####Filtering SubFolders for Selected Folder
class DisplayForm(forms.ModelForm):
    	folders=dirstruc()
    	print(folders)
    	def __init__(self, *args, **kwargs):
    		super().__init__(*args, **kwargs)
    		if 'id' in self.data:
    			try:
    				sub_fold = int(self.data.get('id'))
    				sub_folders=os.listdir('C:/Users/NagaDurga/Documents/'+sub_fold)
    			except (ValueError, TypeError):
    			 pass  


class DisplayForm1(forms.ModelForm):
        folders=subfoldes()
        print(folders)
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            if 'id' in self.data:
                try:
                    sub_fold = int(self.data.get('id'))
                    print(sub_fold)
                    sub_folders2=os.listdir(sub_folders+sub_fold)
                    print(sub_folders2)
                except (ValueError, TypeError):
                 pass  # invalid input from the client; ignore and fallback to empty City queryset








          