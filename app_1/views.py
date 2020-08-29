from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from datetime import datetime
from .models import Interface, InterfaceType,InterfaceDetail, InterfacefieldDetail as IFD
from .forms import InterfaceForm, InterfaceTypeForm,AssigneeForm,ModifyForm,DetailForm,InterfacedetailForm,InterfacefieldDetail,SchemaTable
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required




@login_required(login_url='login')
def interface_list(request):

    form = InterfaceTypeForm()
    assigneeform = AssigneeForm()
    interfaces=None
    if 'interface_type' in request.session:
        id=request.session['interface_type']
        interfaces=Interface.objects.filter(interface_type=id)
        form.fields['interface_type'].initial=id
    users = User.objects.all()
    return render(request,'interface.html',{'interfaces':interfaces,'form':form, 'assigneeform':assigneeform, 'users':users,})

@login_required(login_url='login')
def filter_interface(request):
    id=request.GET.get('id')
    request.session['interface_type']=id
    interfaces=Interface.objects.filter(interface_type=id)
    data=dict()
    data['html']=render_to_string('interface_filter.html',{'interfaces':interfaces})
    return JsonResponse(data)



@login_required(login_url='login')
def add_interface(request):
    if request.method == 'POST':
        int_type = InterfaceType.objects.get(id=request.session['interface_type'])
        user=User.objects.get(username=request.POST.get('created_by'))
        updated_request = request.POST.copy()
        updated_request.update({'created_by': user,'updated_by': user})
        form = InterfaceForm(updated_request)
        if form.is_valid():
            interface = form.save(commit=False)
            interface.interface_type = int_type
            interface.save()
            return redirect('home')

        
    else:
        form = InterfaceForm()
        form.fields['created_by'].initial = request.user.username
        form.fields['created_on'].initial = datetime.now().date()
        form.fields['updated_by'].initial = request.user.username
        form.fields['updated_on'].initial = datetime.now().date()
        request.session['interface_type'] = request.GET.get('interface_type')
        return render(request,'add_interface.html',{'form':form})

#assign
@login_required(login_url='login')
def assign(request):
    data = dict()
    id = request.GET.get('interface')
    assignee_name = request.GET.get('assignee')
    print(assignee_name)
    interface = Interface.objects.get(id=id)
    user = User.objects.get(username=assignee_name)
    interface.assignee = user
    interface.assign_on = datetime.now().date()
    data['user'] = interface.assignee.username
    data['date'] = interface.assign_on
    interface.save(update_fields=['assignee','assign_on'])
    return JsonResponse(data)



# approve
@login_required(login_url='login')
def approve(request):
    data = dict()
  
    id = request.GET.get('interface')
    interface = Interface.objects.get(id=id)
    if interface.approve_by==None:
        interface.approve_by=request.user
        interface.approve_on = datetime.now().date()
        data['user'] = interface.approve_by.username
        data['date'] = interface.approve_on
    else:
        interface.approve_by=None
        interface.approve_on = None
        data['user'] = None
        data['date'] = None

    # interface.approveby = interface.createdby
    # interface.approveon = datetime.today()
    interface.save(update_fields=['approve_by','approve_on'])
    return JsonResponse(data)

# modify

@login_required(login_url='login')
def modify(request,modify_pk):
    
    interface = get_object_or_404(Interface,pk=modify_pk)
    if request.method=="GET":
        form=ModifyForm()
        form.fields['interface'].initial = interface.interface
        form.fields['description'].initial = interface.description
        form.fields['publisher'].initial = interface.publisher
        form.fields['publisher_schema'].initial = interface.publisher_schema
        form.fields['subscriber'].initial = interface.subscriber
        form.fields['subscriber_schema'].initial = interface.subscriber_schema
        form.fields['created_by'].initial = request.user.username
        form.fields['created_on'].initial = interface.created_on

        form.fields['updated_by'].initial = request.user.username
        form.fields['updated_on'].initial = interface.updated_on
        return render(request,'modify.html',{'form':form})

    else:
        user=User.objects.get(username=request.POST.get('created_by'))
        updated_request = request.POST.copy()
        updated_request.update({'created_by': user,'updated_by':user})
        form = ModifyForm(updated_request,instance=interface)
        if form.is_valid():
            # form=InterfacedetailForm(request.POST,instance=interface)
            detail=form.save(commit=False)
            detail.save()
            return redirect('home')


        form=ModifyForm(request.POST,instance=interface)
        form.save()
        return redirect('home')


#  logout
@login_required(login_url='login')
def interface_detail(request,num):
    
    interfacedetail=InterfaceDetail.objects.filter(interface=num)
    interface = get_object_or_404(Interface,pk=num)
    if request.method=="GET":
        
        form=DetailForm()
        form.fields['interface'].initial = interface.interface
        form.fields['description'].initial = interface.description
        return render(request,'interface_detail.html',{'form':form,'interfacedetail':interfacedetail,'id':interface.id})

@login_required(login_url='login')
def detail(request,pk):
    interface=Interface.objects.get(id=pk)
    if request.method=="GET":
        form=InterfacedetailForm()
        form.fields['created_by'].initial = request.user.username
        form.fields['created_on'].initial = datetime.now().date()
        form.fields['updated_by'].initial = request.user.username
        form.fields['updated_on'].initial = datetime.now().date()
        return render(request,'detail.html',{'form':form,'id':interface.id})
    else:
        user=User.objects.get(username=request.POST.get('created_by'))
        updated_request = request.POST.copy()
        updated_request.update({'created_by': user,'updated_by': user})
        form = InterfacedetailForm(updated_request)
        if form.is_valid():
            # form=InterfacedetailForm(request.POST)
            detail=form.save(commit=False)
            detail.interface=interface
            detail.save()
            return redirect('interface_detail',num=interface.id)


@login_required(login_url='login')
def detail_modify(request,detail_modify):
    
    interface = get_object_or_404(InterfaceDetail,pk=detail_modify)
    if request.method=="GET":
        form=InterfacedetailForm()
        form.fields['description'].initial = interface.description
        form.fields['comments'].initial = interface.comments
        form.fields['created_by'].initial = request.user.username
        form.fields['created_on'].initial = interface.created_on
        form.fields['updated_by'].initial = request.user.username
        form.fields['updated_on'].initial = interface.created_on
        return render(request,'detail_modify.html',{'form':form,'id':interface.id})

    else:
        user=User.objects.get(username=request.POST.get('created_by'))
        updated_request = request.POST.copy()
        updated_request.update({'created_by': user,'updated_by':user})
        form = InterfacedetailForm(updated_request,instance=interface)
        if form.is_valid():
            # form=InterfacedetailForm(request.POST,instance=interface)
            detail=form.save(commit=False)
            detail.save()
            return redirect('interface_detail',num=interface.interface.id)
@login_required(login_url='login')
def field_detail(request,interface_detail):
    interface = get_object_or_404(InterfaceDetail,pk=interface_detail)
    if_details = IFD.objects.filter(field=interface)
    if request.method=='GET':
        form = InterfacefieldDetail()
        form.fields['Created_by'].initial = request.user.username
        form.fields['Created_on'].initial = datetime.now().date()
        form.fields['Updated_by'].initial = request.user.username
        form.fields['Updated_on'].initial = datetime.now().date()
        
    else:
        user=User.objects.get(username=request.POST.get('Created_by'))
        updated_request = request.POST.copy()
        updated_request.update({'Created_by': user,'Updated_by':user})
        form=InterfacefieldDetail(updated_request)
        if form.is_valid():
            
            interface_field_detail = form.save(commit=False)
            interface_field_detail.field = interface
            interface_field_detail.save()
            # form = InterfacefieldDetail()
            
            return redirect('field_detail',interface_detail=interface_detail)
    return render(request,'field_detail.html',{'form':form,'if_details':if_details,'id':interface.interface.id})


