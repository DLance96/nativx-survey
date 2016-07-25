from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
import utils
import forms


def home(request):
    eat_rating_forms = []
    play_rating_forms = []

    for counter, option in enumerate(utils.get_eat_options(10)):
        form = forms.ActivityRatingForm(request.POST or None, prefix=counter, label=option)
        eat_rating_forms.append(form)
    for counter, option in enumerate(utils.get_play_options(10)):
        form = forms.ActivityRatingForm(request.POST or None, prefix=counter + 10, label=option)
        play_rating_forms.append(form)

    if request.method == 'POST':

        if utils.forms_is_valid(eat_rating_forms) and utils.forms_is_valid(play_rating_forms) \
                and utils.validate_user(request.POST['twitter']):
            for form in eat_rating_forms:
                for field in form:
                    print unicode(field.label)
                instance = form.cleaned_data
                print instance['rating']
            for form in play_rating_forms:
                for field in form:
                    print unicode(field.label)
                instance = form.cleaned_data
                print instance['rating']
            return HttpResponseRedirect(reverse('survey:home'))

    context = {
        'eat_rating_forms': eat_rating_forms,
        'play_rating_forms': play_rating_forms,
    }
    return render(request, "home.html", context)


def finished(request):

    context = {

    }
    return render(request, "finished.html", context)