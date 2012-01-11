from django.shortcuts import render_to_response,HttpResponseRedirect
from django.template import RequestContext
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from spreecity.user_management.forms import MemberForm, PartnerForm
from spreecity.user_management.models import Member, Partner

@csrf_exempt
def member_creation(request):   
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['confirm_password']:
                selected_date = '%s-%s-%s' % (form.cleaned_data['year'], form.cleaned_data['month'], form.cleaned_data['date'])
                member_details = Member(
                                        first_name      = form.cleaned_data['first_name'],
                                        last_name       = form.cleaned_data['last_name'],
                                        email           = form.cleaned_data['email'],
                                        country         = form.cleaned_data['country'],
                                        city            = form.cleaned_data['city'],
                                        gender          = 'MALE',
                                        date            = selected_date,
                                        )
                member_details.save()
                auth_user = User.objects.create_user(form.cleaned_data['email'], form.cleaned_data['email'], form.cleaned_data['password'])
                auth_user.is_active = True
                auth_user.is_staff = True
                auth_user.save()
                form = MemberForm()
                msg = "Member created successfully"
                return render_to_response('member.html', {'form': form, 'error': msg },context_instance=RequestContext(request))
            else:
                msg = "Both password and confirm password should be same"
                return render_to_response('member.html', {'form': form, 'error': msg },context_instance=RequestContext(request))    
    else:
        form = MemberForm()
    return render_to_response('member.html', {'form': form },context_instance=RequestContext(request))

@csrf_exempt
def partner_creation(request):   
    if request.method == 'POST':
        form = PartnerForm(request.POST)
        if form.is_valid():
            #if form.cleaned_data['password'] == form.cleaned_data['confirm_password']:
            member_details = Partner(
                                    company_name            = form.cleaned_data['company_name'],
                                    company_country         = form.cleaned_data['company_country'],
                                    business_name           = form.cleaned_data['business_name'],
                                    business_type           = form.cleaned_data['business_type'],
                                    business_description    = form.cleaned_data['business_description'],
                                    mailling_address        = form.cleaned_data['mailling_address'],
                                    zipcode                 = form.cleaned_data['zipcode'],
                                    country                 = form.cleaned_data['country'],
                                    state                   = form.cleaned_data['state'],
                                    city                    = form.cleaned_data['city'],
                                    )
            member_details.save()
#                auth_user = User.objects.create_user(form.cleaned_data['email'], form.cleaned_data['email'], form.cleaned_data['password'])
#                auth_user.is_active = True
#                auth_user.is_staff = True
#                auth_user.save()
            form = PartnerForm()
            msg = "Partner details saved successfully"
            return render_to_response('signup.html', {'form': form, 'error': msg },context_instance=RequestContext(request))
#            else:
#                msg = "Both password and confirm password should be same"
#                return render_to_response('signup.html', {'form': form, 'error': msg },context_instance=RequestContext(request))    
    else:
        form = PartnerForm()
    return render_to_response('signup.html', {'form': form },context_instance=RequestContext(request))