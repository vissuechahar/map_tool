from django.db import models
from django.contrib.auth.models import User

publisher_schema_options = (('TS', 'Trade Stone'),('O','Others'))
subscriber_schema_options = (('RMS','RMS'),('DMS','DMS'))

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)

class InterfaceType(models.Model):
    name=models.CharField(max_length=50,blank=True)
    def __str__(self):
        return self.name

    
class Interface(models.Model):
    interface=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    publisher=models.CharField(max_length=50)
    publisher_schema=models.CharField(max_length=4,choices=publisher_schema_options)
    subscriber=models.CharField(max_length=50)
    subscriber_schema=models.CharField(max_length=4,choices=subscriber_schema_options)
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    created_on=models.DateField(blank=True,null=True)
    updated_by=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,related_name='updateby')
    updated_on=models.DateField(blank=True,null=True,) 
    interface_type = models.ForeignKey(InterfaceType,on_delete=models.CASCADE)
    approve_by=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,related_name='approveby')
    approve_on=models.DateField(auto_now=True,blank=True,null=True,) 
    assignee = models.ForeignKey(User,on_delete=models.CASCADE,related_name='assign_to',blank=True,null=True,)
    assign_on = models.DateField(auto_now=True,blank=True,null=True,)
    def __str__(self):
        return self.interface


class InterfaceDetail(models.Model):
    interface=models.ForeignKey(Interface,on_delete=models.CASCADE,null=True)
    description=models.CharField(max_length=50) 
    comments=models.CharField(max_length=50) 
    created_by=models.ForeignKey(User,on_delete=models.CASCADE)
    created_on=models.DateField(blank=True,null=True)
    updated_by=models.ForeignKey(User,blank=True,null=True,on_delete=models.CASCADE,related_name='update_by')
    updated_on=models.DateField(blank=True,null=True,) 


class SchemaTable(models.Model):
    schema_name =models.CharField(max_length=50)  
    table_name  =models.CharField(max_length=50)  
    column_name =models.CharField(max_length=50)   
    field_type  =models.CharField(max_length=50,blank=True)  
    field_length =models.CharField(max_length=50,blank=True) 
    properties  =models.CharField(max_length=50,blank=True)  
    default_value =models.CharField(max_length=100,blank=True) 

class InterfacefieldDetail(models.Model):
    field=models.ForeignKey(InterfaceDetail,on_delete=models.CASCADE)    
    pub_table =models.CharField(max_length=50)        
    pub_column  =models.CharField(max_length=50)        
    pub_field_type =models.CharField(max_length=50)     
    pub_field_length =models.CharField(max_length=50)   
    pub_column_seq   = models.IntegerField(blank=True,null=True)             
    pub_properties  =models.CharField(max_length=50)    
    pub_default_value =models.CharField(max_length=100,blank=True)  
    pub_min_occurs  = models.IntegerField(blank=True,null=True)                  
    pub_max_occurs  = models.IntegerField(blank=True,null=True)                  
    sub_table  =models.CharField(max_length=50)         
    sub_column =models.CharField(max_length=50)         
    sub_field_type =models.CharField(max_length=50)    
    sub_field_length =models.CharField(max_length=50)   
    sub_column_seq  = models.IntegerField(blank=True,null=True)              
    sub_properties =models.CharField(max_length=50)     
    sub_default_value =models.CharField(max_length=50)  
    sub_min_occurs  = models.IntegerField(blank=True,null=True)                  
    sub_max_occurs  = models.IntegerField(blank=True,null=True)                 
    Conversion_rule =models.CharField(max_length=250)    
    Comments  =models.CharField(max_length=250,blank=True)       
    Created_by =models.ForeignKey(User,on_delete=models.CASCADE,related_name='created_by')      
    Created_on =models.DateField(blank=True,null=True)    
    Updated_by =models.ForeignKey(User,on_delete=models.CASCADE,related_name='updated_by')
    Updated_on =models.DateField(blank=True,null=True)   