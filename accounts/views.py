from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Images,Files
from django.contrib.auth.models import User

from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .forms import ImageForm,FileForm,UserForm
#
# # Create your views here.
#
#
#

class ImageListView(ListView,LoginRequiredMixin):
    model = Images
    template_name='uploads.html'



class FileListView(ListView):
    model = Files
    template_name='files_list.html'



class Timeline(ListView):
    model = Images
    template_name='timeline.html'




class SignUp(CreateView):
    form_class = UserForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

class AddImage(CreateView):
    form_class = ImageForm
    # model = Images
    success_url = reverse_lazy('accounts:imagelist')
    template_name = 'addimage.html'

class AddFile(CreateView):
    form_class = FileForm
    # model = Files
    success_url = reverse_lazy('accounts:filelist')
    template_name = 'addfile.html'



class Homepage(TemplateView):
    template_name='index.html'
#
class TestPage(TemplateView):
    template_name='test.html'
#
class ThanksPage(TemplateView):
    template_name='thanks.html'
