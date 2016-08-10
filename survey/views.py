import json
import re

from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

import forms
import utils
import personality_analyzer
import commit_to_sql


def home(request):
    eat_ratings = utils.get_eat_options(10)
    play_ratings = utils.get_play_options(10)
    text_form = forms.TextInputForm(request.POST or None)

    if request.method == 'POST':
        if utils.validate_user(request.POST['twitter'] or request.POST['textInput'] is not ""):
            eat_data = []
            play_data = []
            print request.POST
            for eat_rating in utils.get_all_eat_options():
                eat_element = dict()
                eat_element['activity'] = eat_rating
                request_label = eat_rating + '_eat'
                rating = request.POST.get(request_label, False)
                if not rating:
                    pass
                else:
                    eat_element['rating'] = int(rating)
                    eat_data.append(eat_element)
            for play_rating in utils.get_all_play_options():
                play_element = dict()
                play_element['activity'] = play_rating
                request_label = play_rating + '_play'
                rating = request.POST.get(request_label, False)
                if not rating:
                    pass
                else:
                    play_element['rating'] = int(rating)
                    play_data.append(play_element)
            if request.POST['textInput'] != '':
                text = re.sub(r'[^\x00-\x7F]+', ' ', request.POST.get('textInput', False))
                # Remove non-ASCII
                personality_json = json.dumps(personality_analyzer.run_text(text))
            else:
                personality_json = json.dumps(personality_analyzer.run_twitter(request.POST.get('twitter', False)))
            eat_json = json.dumps(eat_data)
            play_json = json.dumps(play_data)
            commit_to_sql.add_record(personality_json, eat_json, play_json)
            return HttpResponseRedirect(reverse('survey:finished'))

    context = {
        'form': text_form,
        'eat_ratings': eat_ratings,
        'play_ratings': play_ratings,
    }
    return render(request, "home.html", context)


def finished(request):
    context = {

    }
    return render(request, "finished.html", context)


def handler404(request):
    response = render_to_response('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response


def handler400(request):
    response = render_to_response('400.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 400
    return response
