from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Student
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from pprint import pprint

qna = [
    ('In a three sided figure, it’s always in your sight. Located exactly opposite to the angle which is right.', 'Samos'),
    ('The mule and the donkey shared weight on the basis of this theory.', 'Alexandria'),
    ('I am celebrated in March and July. In July if you want me whole;  and in March if you want me in decimals.', 'Syracuse'),
    ('This mathematician’s actual name is one letter different from a footballer from the same country. You will need a series of detectives to find him though.', 'Pisa'),
    ('I have a fixed base but I must be raised to produce a given number.','Merchiston Tower'),
    ('I have 3 laws but it does not revolve around Newton; my laws revolve around the sun in an elliptical shape. ', 'Weil der stadt'),
    ('I describe a chance on the basis of prior knowledge of condition that might be related to event.', 'London'),
    ('From the beginning of eternity to the end of time and space. To the beginning of everything and end of every place.', 'Basel'),
    ('Keep to the left and I mean nothing. Put me on the right and i change everything. But beyond a point the rules change. Coz after that point I play an opposite game.', 'Pataliputra'),
    (' This person was a genius at decrypting messages by a machine whose name matches with the annual cultural fest of R.A. Podar College during WW2.', 'London'),
    ('Hint:<br>1st word: The football team which was nicknamed "Invincibles" in the 2003-04 season<br>2nd word: The inverse of a trigonometric function','ARSENAL TAN'),
]
import time
@login_required
def quiz_page(request):
    # time.sleep(2)
    global qna
    usr = Student.objects.get(id=request.user.id)
    if request.method == "POST":
        q_no = usr.ques_answered  # index from 0
        ans = request.POST['answer']
        if qna[q_no][1].lower() == ans.lower():
            print('CORRECT!')
            usr.ques_answered = usr.ques_answered + 1
            usr.attempt_for_q = 5
            usr.save()
        else:
            print("INCORRECT")
            usr.attempt_for_q = usr.attempt_for_q - 1
            usr.save()

        return HttpResponseRedirect(reverse("quiz:quiz"))
    else:
        q_no = usr.ques_answered

        if usr.shown_at_time==None or q_no == 0 and usr.attempt_for_q==5:
            usr.shown_at_time = int(datetime.timestamp(datetime.now()))
            usr.save()

        shown_at_time = usr.shown_at_time
        time_remaining = 2101+shown_at_time-int(datetime.timestamp(datetime.now()))

        if time_remaining < 0:
            return render(request, "quiz/thankyou.html")

        if q_no == 11 or usr.attempt_for_q <= 0:
            return render(request, "quiz/thankyou.html")

        context = {}
        context['q_no'] = "Question number: " + str(q_no+1)

        if q_no == 10:
            usr.attempt_for_q = 3
            usr.save()
            context['q_no'] = "Find the Anagram:"
        
        context['time_remaining'] = time_remaining
        context['que_statement'] = qna[q_no][0]# + "-" + qna[q_no][1]

        return render(request, "quiz/quiz.html", context=context)

class instructions(LoginRequiredMixin, generic.TemplateView):
    template_name = "quiz/instructions.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class login(LoginView):
    template_name = "quiz/login.html"
    redirect_authenticated_user = True
    extra_context = {next: 'quiz/'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = '/instuctions'
        return context


class logout(LogoutView):
    template_name = "quiz/logout.html"
    def get(self,request):
        return HttpResponseRedirect(reverse('quiz:login'))
