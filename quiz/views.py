from django.http import Http404
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from .forms import CustomUserCreationForm
from .models import QuizModel


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class QuizView(ListView):
    model = QuizModel
    context_object_name = 'quiz_list'
    template_name = 'quiz_list.html'

    def quiz_view(request, quiz_id):
        quiz = QuizModel.objects.get(pk=quiz_id)
        if quiz is not None:
            return render(request, 'quiz_list.html', {'quiz': quiz})
        else:
            raise Http404('quiz doesnt exist')
