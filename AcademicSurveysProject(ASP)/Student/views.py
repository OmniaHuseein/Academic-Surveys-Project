from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView

from AcademicSurveysProject.decorators import admin_required, admin_or_profile_student_required
from Home.forms import UserCreate, UserUpdate
from .forms import StudentForm
from .models import Student


@method_decorator([login_required, admin_required], name='dispatch')
class StudentOption(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'Student/student_option.html')


@method_decorator([login_required, admin_or_profile_student_required], name='dispatch')
class StudentRead(DetailView):
    model = Student
    template_name = 'Student/student_read.html'
    slug_field = 'user__id_number'


@method_decorator([login_required, admin_required], name='dispatch')
class StudentList(ListView):
    model = Student
    template_name = 'Student/student_list.html'


@method_decorator([login_required, admin_required], name='dispatch')
class StudentCreate(SuccessMessageMixin, CreateView):
    """
    Creates new Student along with associated user
    """
    template_name = 'Student/student_form.html'
    form_class = StudentForm
    second_form_class = UserCreate
    success_message = 'Student profile saved successfully'

    def get_context_data(self, **kwargs):
        context = super(StudentCreate, self).get_context_data(**kwargs)
        if 'user_form' not in context:
            context['user_form'] = self.second_form_class
        return context

    def form_valid(self, form):
        user_form = UserCreate(self.request.POST)
        if user_form.is_valid():
            user = user_form.save()
            student = form.save(commit=False)
            student.user = user
            student.user.is_student = True
            student.save()
            user.save()
        else:
            return self.form_invalid(form)
        return redirect(self.success_url)

    def form_invalid(self, form):
        user_form = UserCreate(self.request.POST)
        return self.render_to_response(self.get_context_data(form=form, user_form=user_form))


@method_decorator([login_required, admin_required], name='dispatch')
class StudentUpdate(SuccessMessageMixin, UpdateView):
    """
    Update Student profile along with associated user
    """
    model = Student
    template_name = 'Student/student_update.html'
    form_class = StudentForm
    second_form_class = UserUpdate
    success_message = 'Student profile saved successfully'
    slug_field = 'user__id_number'

    def get_success_url(self):
        return reverse('student:read', kwargs={'slug': str(self.object.user.id_number), })

    def get_context_data(self, **kwargs):
        context = super(StudentUpdate, self).get_context_data(**kwargs)
        context['user_form'] = self.second_form_class(self.request.POST or None, instance=self.object.user)
        return context

    def form_valid(self, form):
        user_form = UserUpdate(self.request.POST, instance=self.object.user)
        if user_form.is_valid():
            user_form.save()
        else:
            return self.form_invalid(form)
        return super(StudentUpdate, self).form_valid(form)

    def form_invalid(self, form):
        user_form = UserCreate(self.request.POST)
        return self.render_to_response(self.get_context_data(form=form, user_form=user_form))
