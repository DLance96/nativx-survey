from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
import utils
import forms
import json
import personality_analyzer
import commit_to_sql
import re


def home(request):
    eat_rating_forms = []
    play_rating_forms = []
    text_form = forms.TextInputForm(request.POST or None)

    for counter, option in enumerate(utils.get_eat_options(10)):
        form = forms.ActivityRatingForm(request.POST or None, prefix=counter, label=option)
        eat_rating_forms.append(form)
    for counter, option in enumerate(utils.get_play_options(10)):
        form = forms.ActivityRatingForm(request.POST or None, prefix=counter + 10, label=option)
        play_rating_forms.append(form)

    if request.method == 'POST':
        if utils.forms_is_valid(eat_rating_forms) and utils.forms_is_valid(play_rating_forms) \
                and (utils.validate_user(request.POST['twitter']) or request.POST['textInput'] is not ""):
            eat_data = []
            play_data = []
            for form in eat_rating_forms:
                eat_element = {}
                for field in form:
                    eat_element['activity'] = unicode(field.label)
                instance = form.cleaned_data
                eat_element['rating'] = instance['rating']
                eat_data.append(eat_element)
            for form in play_rating_forms:
                play_element = {}
                for field in form:
                    play_element['activity'] = unicode(field.label)
                instance = form.cleaned_data
                play_element['rating'] = instance['rating']
                play_data.append(play_element)
            if request.POST['textInput'] is not "":
                text = re.sub(r'[^\x00-\x7F]+', ' ', request.POST['textInput'])
                                                # Remove non-ASCII
                personality_json = json.dumps(personality_analyzer.run_text(text))
            else:
                personality_json = json.dumps(personality_analyzer.run_twitter(request.POST['twitter']))
            eat_json = json.dumps(eat_data)
            play_json = json.dumps(play_data)
            commit_to_sql.add_record(personality_json, eat_json, play_json)
            return HttpResponseRedirect(reverse('survey:finished'))

    context = {
        'form': text_form,
        'eat_rating_forms': eat_rating_forms,
        'play_rating_forms': play_rating_forms,
    }
    return render(request, "home.html", context)


def finished(request):

    context = {

    }
    return render(request, "finished.html", context)