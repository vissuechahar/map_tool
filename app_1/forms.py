from .models import Interface, InterfaceType,InterfaceDetail,InterfacefieldDetail,SchemaTable
from django import forms
from django.contrib.auth.models import User


class InterfaceForm(forms.ModelForm):
    class Meta:
        model = Interface
        exclude = ('approve_on','approve_by','assignee','assign_on','interface_type')
        readonly_fields = ('created_by','created_on' ,'updated_by','updated_on',)
        widgets = {
            'interface': forms.TextInput(attrs={'class':'form-control-sm col-sm-8','style':'border:none; background-color:#F0F0F0' }),
            'description': forms.TextInput(attrs={'class':'form-control-sm col-sm-8','style':'border:none;background-color:#F0F0F0;'}),
            'publisher': forms.TextInput(attrs={'class':'form-control-sm col-sm-8','style':'border:none;background-color:#F0F0F0;'}),
            'publisher_schema':forms.Select(attrs={'class':'form-control-sm col-sm-8','style':'border:none;background-color:#F0F0F0;'}),
            'subscriber': forms.TextInput(attrs={'class':'form-control-sm col-sm-8','style':'border:none;background-color:#F0F0F0;'}),
            'subscriber_schema': forms.Select(attrs={'class':'form-control-sm col-sm-8','style':'border:none;background-color:#F0F0F0;'}),
            'created_by': forms.TextInput(attrs={'readonly':'readonly','class':'form-control-sm col-sm-8','style':'border:none;background-color:#F0F0F0;'}),
            'updated_by': forms.TextInput(attrs={'readonly':'readonly','class':'form-control-sm col-sm-8','style':'border:none;background-color:#F0F0F0;'}),
            'updated_on': forms.TextInput(attrs={'readonly':'readonly','class':'form-control-sm col-sm-8','style':'border:none;background-color:#F0F0F0;'}),
            'created_on':forms.TextInput(attrs={'readonly':'readonly','class':'form-control-sm col-sm-8','style':'border:none;background-color:#F0F0F0;'}),
        }

        


class InterfaceTypeForm(forms.ModelForm):
    class Meta:
        model = Interface
        fields = ('interface_type',)
        widget={'interface_type': forms.TextInput(attrs={'class':'form-control-sm col-sm-12','style':'border:none; background-color:#F0F0F0' }),}

class AssigneeForm(forms.ModelForm):
    company_name = forms.CharField(max_length=30, widget=forms.TextInput(), )
    class Meta:
        model = User
        fields= ('first_name','last_name','username','is_active','company_name')

class ModifyForm(forms.ModelForm):
    class Meta:
        model = Interface
        exclude = ('approve_on','approve_by','assignee','assign_on','interface_type')
        readonly_fields = ('created_by','created_on','updated_by','updated_on' )
        widgets = {
            'interface': forms.TextInput(attrs={'class':'form-control-sm col-sm-8','style':'border:none; background-color:#F0F0F0' }),
            'description': forms.TextInput(attrs={'class':'form-control-sm col-sm-8','style':'border:none; background-color:#F0F0F0'}),
            'publisher': forms.TextInput(attrs={'class':'form-control-sm col-sm-8','style':'border:none; background-color:#F0F0F0'}),
            'publisher_schema':forms.Select(attrs={'class':'form-control-sm col-sm-8','style':'border:none; background-color:#F0F0F0'}),
            'subscriber': forms.TextInput(attrs={'class':'form-control-sm col-sm-8','style':'border:none; background-color:#F0F0F0'}),
            'subscriber_schema': forms.Select(attrs={'class':'form-control-sm col-sm-8','style':'border:none; background-color:#F0F0F0'}),
            'created_by': forms.TextInput(attrs={'readonly':'readonly','class':'form-control-sm col-sm-8','style':'border:none; background-color:#F0F0F0'}),
            'updated_by': forms.TextInput(attrs={'readonly':'readonly','class':'form-control-sm col-sm-8','style':'border:none; background-color:#F0F0F0'}),
            'updated_on': forms.TextInput(attrs={'readonly':'readonly','class':'form-control-sm col-sm-8','style':'border:none; background-color:#F0F0F0'}),
            'created_on':forms.TextInput(attrs={'readonly':'readonly','class':'form-control-sm col-sm-8','style':'border:none; background-color:#F0F0F0'}),
        }



class DetailForm(forms.ModelForm):
    
    class Meta:
        model = Interface
        exclude = ('approve_on','approve_by','assignee','assign_on','interface_type','publisher','publisher_schema','subscriber','subscriber_schema','created_by','created_on' ,'updated_by','updated_on')
        widgets = {'interface': forms.TextInput(attrs={'readonly':'readonly','class':'form-control-sm col-sm-12','style':'border:1px solid black;color:white;font-weight:bold; background-color:rgb(214, 218, 216)'}),
        'description': forms.TextInput(attrs={'readonly':'readonly','class':'form-control-sm col-sm-12','style':'border:1px solid black; color:white;font-weight:bold; background-color:rgb(214, 218, 216)'}),}
        

     
class InterfacedetailForm(forms.ModelForm):
    class Meta:
        model = InterfaceDetail
        fields = ('description','comments','created_by','created_on','updated_by','updated_on')
        widgets = {'created_by': forms.TextInput(attrs={'readonly':'readonly','class':'form-control-sm col-sm-8','style':'border:none; background-color:#F0F0F0'}),'updated_by': forms.TextInput(attrs={'readonly':'readonly','class':'form-control-sm col-sm-8','style':'border:none; background-color:#F0F0F0'}),'updated_on': forms.TextInput(attrs={'readonly':'readonly','class':'form-control-sm col-sm-8','style':'border:none; background-color:#F0F0F0'}),'created_on':forms.TextInput(attrs={'readonly':'readonly','class':'form-control-sm col-sm-8','style':'border:none; background-color:#F0F0F0'}),
        'description': forms.TextInput(attrs={'class':'form-control-sm col-sm-8','style':'border:none; background-color:#F0F0F0'}),'comments': forms.TextInput(attrs={'class':'form-control-sm col-sm-8','style':'border:none; background-color:#F0F0F0'}),}
    
    
class InterfacefieldDetail(forms.ModelForm):

    pub_table = forms.ModelChoiceField(required=True, queryset=SchemaTable.objects.all().values_list('table_name',flat=True).order_by('table_name'),to_field_name='table_name')
    pub_column = forms.ModelChoiceField(required=True, queryset=SchemaTable.objects.all().values_list('column_name',flat=True).order_by('column_name'),to_field_name='column_name')
    pub_field_type = forms.ModelChoiceField(required=True, queryset=SchemaTable.objects.all().values_list('field_type',flat=True).order_by('field_type'),to_field_name='field_type')
    sub_table = forms.ModelChoiceField(required=True, queryset=SchemaTable.objects.all().values_list('table_name',flat=True).order_by('table_name'),to_field_name='table_name')
    sub_column = forms.ModelChoiceField(required=True, queryset=SchemaTable.objects.all().values_list('column_name',flat=True).order_by('column_name'),to_field_name='column_name')
    sub_field_type= forms.ModelChoiceField(required=True, queryset=SchemaTable.objects.all().values_list('field_type',flat=True).order_by('field_type'),to_field_name='field_type')
    class Meta:
        model = InterfacefieldDetail
        fields=('pub_table','pub_column','pub_field_type','pub_field_length','pub_column_seq','pub_properties','pub_default_value','pub_min_occurs','pub_max_occurs', 'sub_table','sub_column','sub_field_type','sub_field_length','sub_column_seq','sub_properties','sub_default_value','sub_min_occurs','sub_max_occurs','Conversion_rule','Comments','Created_by','Created_on','Updated_by','Updated_on') 
        widgets = {
            'Created_by': forms.TextInput(attrs={'readonly':'readonly',}),
            'Updated_by': forms.TextInput(attrs={'readonly':'readonly',}),
            'Created_on': forms.TextInput(attrs={'readonly':'readonly',}),
            'Updated_on': forms.TextInput(attrs={'readonly':'readonly',}),
        }  