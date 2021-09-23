from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from prescription.models import Patient, Medicine
from prescription.forms import PatientForm, medForm
from django.views.generic import ListView, DetailView, View, CreateView, DeleteView
from django.views.generic.edit import UpdateView
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import ObjectDoesNotExist





def index(request):
	return render(request, 'prescription/index.html')

def about(request):
    return render(request, 'prescription/about.html')


@method_decorator(login_required, name='dispatch')      #If not login create will open login page.
class CreatePrescription(LoginRequiredMixin, CreateView):
    form_class = PatientForm
    template_name = 'prescription/add_patient.html'

    def get_success_url(self):
    	return reverse('pre_pres', kwargs={'pk':self.object.pk})



class PrePresShow(DetailView):
    model = Patient
    template_name = 'prescription/view_prescription.html'



@method_decorator(login_required, name='dispatch')
class AddMedicineView(LoginRequiredMixin, View):
    def get(self,*args, **kwargs):
        dic= self.kwargs        #It will pass a dict value like {'pk':3} but there pk need a number value like 3
        pk1 = dic['pk']         #For that dic['pk'] will give only 3 value from dic dictionary. you can write id=self.kwargs['pk']
        patient = Patient.objects.get(id=pk1)
        form = medForm
        return render(self.request, 'prescription/add_medicine.html', { 'patient':patient, 'form':form})

    def post(self,*args, **kwargs):
        patient= Patient.objects.get(id=self.kwargs['pk'])
        form = medForm(self.request.POST or None)
        if form.is_valid():
            form = medForm(self.request.POST or None)
            form.save()
            patient = Patient.objects.get(id=self.kwargs['pk'])
            medi = Medicine.objects.latest('id')
            medi.patientname= patient
            medi.save()
            medic = Medicine.objects.latest('id')
            return redirect('print_pres', medic.id)


class PrintPresView(DetailView):
    model = Medicine
    template_name = 'prescription/print_prescription.html'

    def get_context_data(self, *args, **kwargs):
        idd=self.kwargs['pk']
        print(idd, "Newwwwwwww")
        pati= Medicine.objects.get(id=idd)
        print(pati.patientname.id, "iddddddddddddddddd")
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(id=pati.patientname.id)
        return context




#For Old patient:

def old_patient_search(request):
    if request.method=="GET":
        search_id = request.GET.get('search_id')
        updatep=Patient.objects.filter(id=search_id)
    return render(request, 'prescription/old_patient_search.html', {'updatep':updatep})


class OldPatientUpdate(LoginRequiredMixin, UpdateView):
    model = Patient
    fields = ['date','name','others_test', 'age_y', 'age_m', 'age_d','sex','cc','oe','pulse','bp','test',]
    template_name_suffix = '_update'

    def get_success_url(self):
        id=self.kwargs['pk']
        med = Medicine.objects.get(patientname=id)
        return reverse('update_medicine', kwargs={'pk': med.id})


class UpdateMedicineView(LoginRequiredMixin, UpdateView):
    model = Medicine
    fields = ['test_result','next_visit','diagonosis','advice','med1','rule1','med2','rule2','med3',
            'rule3','med4','rule4','med5','rule5','med6','rule6','med7','rule7','med8','rule8','med9','rule9','med10','rule10'
        ]

    template_name_suffix = '_update_form'

    def get_context_data(self, *args, **kwargs):
        idd=self.kwargs['pk']
        pati = Medicine.objects.get(id=idd)
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(id=pati.patientname.id)
        return context


    def get_success_url(self):
    	return reverse('print_pres', kwargs={'pk':self.object.pk})



#Search and Dashboard print and delete

def search(request):
	if request.method=="GET":
		search_id = request.GET.get('search_id')
		updatep=Patient.objects.filter(id=search_id)

	return render(request, 'prescription/search.html', {'updatep':updatep})



class PatientList(LoginRequiredMixin, ListView):
    model = Patient
    paginate_by = 7
    template_name = "home.html"


@login_required
def delete(request, pk):
    user = Patient.objects.get(id=pk)
    user.delete()
    return redirect('patient_list')


def print_search_view(request):
    if request.method=="GET":
        search_id = request.GET.get('search_id')
        patient=Patient.objects.filter(id=search_id)
        return render(request, 'prescription/search_print.html', {'updatep':patient})

    if request.method=="POST":
        search_id = request.GET.get('search_id')
        patient=Patient.objects.get(id=search_id)
        medicine = Medicine.objects.get(patientname=patient)
        return render(request, 'prescription/print_prescription.html', {'patient':patient, 'medicine':medicine})
        