from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin # This is needed for object oriented programming. A class should only inherit one class. A Mixin is another class that can be inherited from allwoing for a class to inherit more classes essentially.
from django.urls import reverse_lazy

from django.contrib.auth import get_user_model
from .models import Issue

# from .managers import CustomUserManager

class IssueDetailView(DetailView):
    template_name = "issues/issue_detail.html"
    model = Issue
# Create your views here.
class MyIssuedListView(ListView):
    template_name = "issues/issue_list.html"
    model = Issue 
    # Refer to class video for more information: FSDI 112-2 C30 @ 02hr:29min
    def get_context_data(self, **kwargs): #Keyword arguments. All list views have this get_context_data() method. 
        context = super().get_context_data(**kwargs) # The get method returns records that matched the name = "published". you can also use it like this, .get(name="published")
        context["issue_list"] = Issue.objects.filter(requester=self.request.user # Ensuring that the data is returned based on the author logged in.
                                          ).order_by("created_on"
                                          ).reverse()
        return context
class IssueListView(ListView):
    template_name = "issues/issue_list.html"
    model = Issue

class IssueDetailView(DetailView):
    template_name = "issues/issue_detail.html"
    model = Issue

class IssueCreateView(LoginRequiredMixin, CreateView):
    template_name = "issues/new.html" 
    model = Issue
    success_url = reverse_lazy("issue_list")
    fields = ["assignee", "title", "summary", "description",  "impact", "urgency", "status"]

    def form_valid(self, form): # This overrides the default form_valid() method of Django 
        form.instance.requester = self.request.user # Allows the requester to request the user model.
        return super().form_valid(form) # Super() calls the form method

class IssueDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): # REMEMBER, Mixin order matters for validations.
    model = Issue
    # success_url ="/issues" # You can specify success urlurl to redirect after successfully
    template_name = "issues/delete.html" # deleting object
    success_url = reverse_lazy("issue_list") # From Django's urls module. Redirects after successfully deleting object
    # Test for UserPassesTestMixin that the user needs to pass
    def test_func(self):
        issue_obj = self.get_object()
        return issue_obj.requester == self.request.user

class IssueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):  # REMEMBER, Mixin order matters for validations.
    template_name = "issues/edit.html"
    model = Issue
    success_url = reverse_lazy("issue_list") 
    fields = ["assignee", "title", "summary", "description",  "impact", "urgency", "status"] # Fields will be showed on the page
    # Test for UserPassesTestMixin that the user needs to pass
    def test_func(self):
        issue_obj = self.get_object()
        return issue_obj.requester == self.request.user

# class UserProfileUpdateView(UpdateView):
#     template_name = "issues/user_profile.html"
#     success_url = reverse_lazy("issue_list")
#     model = User

#     def get_initial(self):
#         initial = super(UserProfileUpdateView, self).get_initial()
#         try:
#             current_group = self.object.groups.get()
#         except:
#             # exception can occur if the edited user has no groups
#             # or has more than one group
#             pass
#         else:
#             initial['group'] = current_group.pk
#         return initial

#     def get_form_class(self):
#         return UserProfileForm

#     def form_valid(self, form):
#         self.object.groups.clear()
#         self.object.groups.add(form.cleaned_data['group'])
#         return super(UserProfileUpdateView, self).form_valid(form)
    