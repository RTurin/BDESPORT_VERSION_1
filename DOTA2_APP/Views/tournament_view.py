from django.shortcuts import render,redirect,reverse

from django.contrib.auth.models import User

from django.contrib import messages

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from django.views.generic import View, TemplateView, CreateView, FormView, DetailView, ListView, UpdateView,DeleteView


from django.utils.http import is_safe_url
from django.conf import settings

from django.template import loader
from django.http import HttpResponse, request
from django.db.models import Q


from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy, reverse
# Models Imports
from DOTA2_APP.models import *

# Forms Import
from DOTA2_APP.forms import *

from django.urls import resolve
import json
import requests
from django.contrib.auth.models import User

import datetime




def test_view(request):
    getTournament = Tournament.objects.get(id=2)
    navbar_Tournament = Tournament.objects.all()
    template = loader.get_template('frontend/tournament/TournamentPage.html')
    context = {
        'getTournament': 'None',
        'navbar_Tournament':'None',

        # Groups Points Table
        'get_GroupStage_data1':'None',
        'get_GroupStage_data2':'None',
        'get_GroupStage_data3':'None',
        'get_GroupStage_data4':'None',
        # Groups Points Table

        # Group Stage Matches
        'getAll_groupStage_matches':'None',
        # Group Stage Matches

        'fixture': 'None',
        'getTournament': getTournament,
        'navbar_Tournament':navbar_Tournament,
    }
    return HttpResponse(template.render(context, request))