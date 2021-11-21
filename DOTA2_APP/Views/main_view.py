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
# Main View--------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------
class HomeView(TemplateView):
    now=datetime.datetime.now()
    print("[537] Date: "+ now.strftime("%d-%m-%Y")) #this will print **2018-02-01** that is todays date

    template_name = "frontend/home1.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        get_tournament = Tournament.objects.get(id= 2)

        navbar_Tournament = Tournament.objects.all()
        context['navbar_Tournament'] = navbar_Tournament
        # print(get_tournament)


        context['get_tournament'] = get_tournament

        context['Comment'] = "Testing on creation of new view to frontend template html page"

        return context
# ---------------------------------------------------------------------------------------------------------------------------------------------------
def TournamentInfo(request,slug):
    print(slug)
    get_tournament = Tournament.objects.get(slug=slug)

    navbar_Tournament = Tournament.objects.all()
    context = {
        'get_tournament': get_tournament,
        'navbar_Tournament':navbar_Tournament

        }
    return render(request,"frontend/tournament/joinTournament.html",context)
# ---------------------------------------------------------------------------------------------------------------------------------------------------
# Previous Code For Tournament Regisration View
def RegisterTeam_Prev(request,slug):
    # How to Find Out the Current URL NAME
    current_url = resolve(request.path_info).url_name
    print('Current URL:',current_url)
    # How to Find Out the Current URL NAME
    get_tournament = Tournament.objects.get(slug=slug)
    if request.user.is_authenticated :
        pass
    else:
        return redirect('/register/')

    if request.method == 'POST':
        teamName = request.POST.get('name')
        teamShortName = request.POST.get('shortname')
        logo = request.FILES.get('logo')

        get_created_by = Profile.objects.get(user = request.user)
        print('[Line:137] User:',get_created_by)

        get_All_Participates = TournamentParticipate.objects.all()

        if get_All_Participates.filter(text_teamName =teamName).exists() or get_All_Participates.filter(
                created_by=  get_created_by).exists():
            messages.success(request, 'A Team of Yours already have been registered for this Tournament.!')
            return redirect('/'+slug+'/Registration2')

        else:
            pass


        if Team.objects.filter(name =teamName).exists():
            messages.success(request, 'A Team Already Exists with this Name. Please Try Another Name..!')
            return redirect('/'+slug+'/Registration2')
        else:
            pass
        player1_fullName = request.POST.get('player1_fullName')
        player1_GamingName = request.POST.get('player1_GamingName')
        player1_Role = request.POST.get('player1_Role')
        player1_SteamId = request.POST.get('player1_SteamId')
        player1_PlayerId = request.POST.get('player1_PlayerId')
        player1_phoneNo = request.POST.get('player1_phoneNo')
        player1_email = request.POST.get('player1_email')
        player1_estimated_mmr = Estimate_Player_MMR(player1_PlayerId,slug,request)
        print ('[112] Player1 MMR Got Back:',player1_estimated_mmr)

        player2_fullName = request.POST.get('player2_fullName')
        player2_GamingName = request.POST.get('player2_GamingName')
        player2_Role = request.POST.get('player2_Role')
        player2_SteamId = request.POST.get('player2_SteamId')
        player2_PlayerId = request.POST.get('player2_PlayerId')
        player2_phoneNo = request.POST.get('player2_phoneNo')
        player2_email = request.POST.get('player2_email')
        player2_estimated_mmr = Estimate_Player_MMR(player2_PlayerId,slug,request)
        print ('[124] Player2 MMR Got Back:',player2_estimated_mmr)

        player3_fullName = request.POST.get('player3_fullName')
        player3_GamingName = request.POST.get('player3_GamingName')
        player3_Role = request.POST.get('player3_Role')
        player3_SteamId = request.POST.get('player3_SteamId')
        player3_PlayerId = request.POST.get('player3_PlayerId')
        player3_phoneNo = request.POST.get('player3_phoneNo')
        player3_email = request.POST.get('player3_email')
        player3_estimated_mmr = Estimate_Player_MMR(player3_PlayerId,slug,request)
        print ('[134] Player3 MMR Got Back:',player3_estimated_mmr)

        player4_fullName = request.POST.get('player4_fullName')
        player4_GamingName = request.POST.get('player4_GamingName')
        player4_Role = request.POST.get('player4_Role')
        player4_SteamId = request.POST.get('player4_SteamId')
        player4_PlayerId = request.POST.get('player4_PlayerId')
        player4_phoneNo = request.POST.get('player4_phoneNo')
        player4_email = request.POST.get('player4_email')
        player4_estimated_mmr = Estimate_Player_MMR(player4_PlayerId,slug,request)
        print ('[144] Player4 MMR Got Back:',player4_estimated_mmr)

        player5_fullName = request.POST.get('player5_fullName')
        player5_GamingName = request.POST.get('player5_GamingName')
        player5_Role = request.POST.get('player5_Role')
        player5_SteamId = request.POST.get('player5_SteamId')
        player5_PlayerId = request.POST.get('player5_PlayerId')
        player5_phoneNo = request.POST.get('player5_phoneNo')
        player5_email = request.POST.get('player5_email')
        player5_estimated_mmr = Estimate_Player_MMR(player5_PlayerId,slug,request)
        print ('[154] Player5 MMR Got Back:',player5_estimated_mmr)

        if logo == None or logo == "":
            # print('No Logo Has Been Uploaded/Selected..! Default Logo Will Be Used [Line:107]')
            create_New_Team = Team.objects.create(
                name = teamName,
                shortname = teamShortName,
                created_by = get_created_by,
            )
        else:
            # print('Logo File Uploaded/Selected..! [Line:114]')
            create_New_Team = Team.objects.create(
                name = teamName,
                shortname = teamShortName,
                logo = logo,
                created_by = get_created_by,
            )
        player1_Create_New = Player.objects.create(
            name = player1_fullName,
            gaming_name=player1_GamingName,
            role = player1_Role,
            steam_id =player1_SteamId,
            player_id = player1_PlayerId,
            phoneNo =player1_phoneNo,
            email =player1_email,
            estimated_mmr = player1_estimated_mmr,
        )
        player2_Create_New = Player.objects.create(
            name = player2_fullName,
            gaming_name=player2_GamingName,
            role = player2_Role,
            steam_id =player2_SteamId,
            player_id = player2_PlayerId,
            phoneNo =player2_phoneNo,
            email =player2_email,
            estimated_mmr = player2_estimated_mmr,
        )
        player3_Create_New = Player.objects.create(
            name = player3_fullName,
            gaming_name=player3_GamingName,
            role = player3_Role,
            steam_id =player3_SteamId,
            player_id = player3_PlayerId,
            phoneNo =player3_phoneNo,
            email =player3_email,
            estimated_mmr = player3_estimated_mmr,
        )
        player4_Create_New = Player.objects.create(
            name = player4_fullName,
            gaming_name=player4_GamingName,
            role = player4_Role,
            steam_id =player3_SteamId,
            player_id = player4_PlayerId,
            phoneNo =player4_phoneNo,
            email =player4_email,
            estimated_mmr = player4_estimated_mmr,
        )
        player5_Create_New = Player.objects.create(
            name = player5_fullName,
            gaming_name=player5_GamingName,
            role = player5_Role,
            steam_id =player5_SteamId,
            player_id = player5_PlayerId,
            phoneNo =player5_phoneNo,
            email =player5_email,
            estimated_mmr = player5_estimated_mmr,
        )

        create_New_Team.members.add(player1_Create_New,player2_Create_New,player3_Create_New,player4_Create_New,player5_Create_New)

        tournamentpartipate = TournamentParticipate.objects.create(
            tournament =  get_tournament,
            team = create_New_Team,
            text_teamName = teamName,
            created_by = get_created_by,
        )
        request.session['New_Team'] = teamName
        request.session['prev_slug'] = slug


        return redirect('/Registration-Status/')

    navbar_Tournament = Tournament.objects.all()
    context = {
        'get_tournament': get_tournament,
        'navbar_Tournament': navbar_Tournament,
    }

    return render(request,"frontend/tournament/Register.html",context)
# Previous Code For Tournament Regisration View Ends
# ---------------------------------------------------------------------------------------------------------------------------------------------------
def Estimate_Player_MMR(get_player_ID,slug,request):
    try:
        # print('[77] Player ID :',get_player_ID)
        r = requests.get("https://api.opendota.com/api/players/"+get_player_ID).json()
        r1 = r['mmr_estimate']
        r2 = r1['estimate']
        return r2
    except Exception as e:
        print('[79] Exception Error Message:',e)
        messages.success(request, 'Invalid Player ID Provided of Player')
        return redirect('/'+slug+'/Registration2')

def RegisterTeam_Final(request,slug):
    # How to Find Out the Current URL NAME
    current_url = resolve(request.path_info).url_name
    print('Current URL:',current_url)
    # How to Find Out the Current URL NAME




    if request.user.is_authenticated :
        pass
    else:
        return redirect('/register/')

    get_tournament = Tournament.objects.get(slug=slug)
    get_All_Participates = TournamentParticipate.objects.all()
    get_created_by = Profile.objects.get(user = request.user)

    if get_All_Participates.filter(created_by=  get_created_by).exists():
        return redirect('/Registration-Status/')

    if request.method == 'POST':
        teamName = request.POST.get('name')
        teamShortName = request.POST.get('shortname')
        logo = request.FILES.get('logo')

        if get_All_Participates.filter(text_teamName =teamName).exists() or get_All_Participates.filter(
                created_by=  get_created_by).exists():
            messages.success(request, 'A Team of Yours already have been registered for this Tournament.!')
            return redirect('/'+slug+'/Registration')
        else:
            pass

        if Team.objects.filter(name =teamName).exists():
            messages.success(request, 'A Team Already Exists with this Name. Please Try Another Name..!')
            return redirect('/'+slug+'/Registration2')
        else:
            pass

        player1_fullName = request.POST.get('player1_fullName')
        player1_GamingName = request.POST.get('player1_GamingName')
        player1_Role = request.POST.get('player1_Role')
        player1_SteamId = request.POST.get('player1_SteamId')
        player1_PlayerId = request.POST.get('player1_PlayerId')
        player1_phoneNo = request.POST.get('player1_phoneNo')
        player1_email = request.POST.get('player1_email')
        player1_estimated_mmr = Estimate_Player_MMR(player1_PlayerId,slug,request)
        print ('[112] Player1 MMR Got Back:',player1_estimated_mmr)

        player2_fullName = request.POST.get('player2_fullName')
        player2_GamingName = request.POST.get('player2_GamingName')
        player2_Role = request.POST.get('player2_Role')
        player2_SteamId = request.POST.get('player2_SteamId')
        player2_PlayerId = request.POST.get('player2_PlayerId')
        player2_phoneNo = request.POST.get('player2_phoneNo')
        player2_email = request.POST.get('player2_email')
        player2_estimated_mmr = Estimate_Player_MMR(player2_PlayerId,slug,request)
        print ('[124] Player2 MMR Got Back:',player2_estimated_mmr)

        player3_fullName = request.POST.get('player3_fullName')
        player3_GamingName = request.POST.get('player3_GamingName')
        player3_Role = request.POST.get('player3_Role')
        player3_SteamId = request.POST.get('player3_SteamId')
        player3_PlayerId = request.POST.get('player3_PlayerId')
        player3_phoneNo = request.POST.get('player3_phoneNo')
        player3_email = request.POST.get('player3_email')
        player3_estimated_mmr = Estimate_Player_MMR(player3_PlayerId,slug,request)
        print ('[134] Player3 MMR Got Back:',player3_estimated_mmr)

        player4_fullName = request.POST.get('player4_fullName')
        player4_GamingName = request.POST.get('player4_GamingName')
        player4_Role = request.POST.get('player4_Role')
        player4_SteamId = request.POST.get('player4_SteamId')
        player4_PlayerId = request.POST.get('player4_PlayerId')
        player4_phoneNo = request.POST.get('player4_phoneNo')
        player4_email = request.POST.get('player4_email')
        player4_estimated_mmr = Estimate_Player_MMR(player4_PlayerId,slug,request)
        print ('[144] Player4 MMR Got Back:',player4_estimated_mmr)

        player5_fullName = request.POST.get('player5_fullName')
        player5_GamingName = request.POST.get('player5_GamingName')
        player5_Role = request.POST.get('player5_Role')
        player5_SteamId = request.POST.get('player5_SteamId')
        player5_PlayerId = request.POST.get('player5_PlayerId')
        player5_phoneNo = request.POST.get('player5_phoneNo')
        player5_email = request.POST.get('player5_email')
        player5_estimated_mmr = Estimate_Player_MMR(player5_PlayerId,slug,request)
        print ('[154] Player5 MMR Got Back:',player5_estimated_mmr)

        if logo == None or logo == "":
            # print('No Logo Has Been Uploaded/Selected..! Default Logo Will Be Used [Line:107]')
            create_New_Team = Team.objects.create(
                name = teamName,
                shortname = teamShortName,
                created_by = get_created_by,
            )
        else:
            # print('Logo File Uploaded/Selected..! [Line:114]')
            create_New_Team = Team.objects.create(
                name = teamName,
                shortname = teamShortName,
                logo = logo,
                created_by = get_created_by,
            )
        player1_Create_New = Player.objects.create(
            name = player1_fullName,
            gaming_name=player1_GamingName,
            role = player1_Role,
            steam_id =player1_SteamId,
            player_id = player1_PlayerId,
            phoneNo =player1_phoneNo,
            email =player1_email,
            estimated_mmr = player1_estimated_mmr,
        )
        player2_Create_New = Player.objects.create(
            name = player2_fullName,
            gaming_name=player2_GamingName,
            role = player2_Role,
            steam_id =player2_SteamId,
            player_id = player2_PlayerId,
            phoneNo =player2_phoneNo,
            email =player2_email,
            estimated_mmr = player2_estimated_mmr,
        )
        player3_Create_New = Player.objects.create(
            name = player3_fullName,
            gaming_name=player3_GamingName,
            role = player3_Role,
            steam_id =player3_SteamId,
            player_id = player3_PlayerId,
            phoneNo =player3_phoneNo,
            email =player3_email,
            estimated_mmr = player3_estimated_mmr,
        )
        player4_Create_New = Player.objects.create(
            name = player4_fullName,
            gaming_name=player4_GamingName,
            role = player4_Role,
            steam_id =player3_SteamId,
            player_id = player4_PlayerId,
            phoneNo =player4_phoneNo,
            email =player4_email,
            estimated_mmr = player4_estimated_mmr,
        )
        player5_Create_New = Player.objects.create(
            name = player5_fullName,
            gaming_name=player5_GamingName,
            role = player5_Role,
            steam_id =player5_SteamId,
            player_id = player5_PlayerId,
            phoneNo =player5_phoneNo,
            email =player5_email,
            estimated_mmr = player5_estimated_mmr,
        )

        create_New_Team.members.add(player1_Create_New,player2_Create_New,player3_Create_New,player4_Create_New,player5_Create_New)

        tournamentpartipate = TournamentParticipate.objects.create(
            tournament =  get_tournament,
            team = create_New_Team,
            text_teamName = teamName,
            created_by = get_created_by,
        )
        request.session['New_Team'] = teamName
        request.session['prev_slug'] = slug

        return redirect('/Registration-Status/')

    navbar_Tournament = Tournament.objects.all()
    context = {
        'get_tournament': get_tournament,
        'navbar_Tournament': navbar_Tournament,
    }
    return render(request,"frontend/tournament/Register.html",context)
# ---------------------------------------------------------------------------------------------------------------------------------------------------
def AfterRegistration(request):

    if  request.user.is_authenticated:
       pass
    else:
        return redirect('/')

    get_team = TournamentParticipate.objects.filter(created_by =Profile.objects.get(user= request.user)).first()
    print('[260] New Team',get_team)

    navbar_Tournament = Tournament.objects.all()
    context = {
        'get_team':get_team,
        'navbar_Tournament': navbar_Tournament,
    }
    return render(request,"frontend/tournament/AfterRegistration.html",context)
# ---------------------------------------------------------------------------------------------------------------------------------------------------
def Payment_View(request,slug):
    get_tournament = Tournament.objects.get(slug=slug)

    if  request.user.is_authenticated:
        pass
    else:
        return redirect('/')

    get_Profile = Profile.objects.get(user = request.user)
    get_team = TournamentParticipate.objects.filter(created_by =Profile.objects.get(user= request.user)).first()

    if Payment.objects.filter(team = get_team,).exists() and Payment.objects.filter(team = get_team,form_submitted = True).exists():
        print('[466] Form Submitted')
        return redirect('/Payment-Status/'+slug)
    else:
        print('[467] Form Not Submitted')
        pass

    if request.method == 'POST':
        phoneNo = request.POST.get('phoneNo')
        tranxid = request.POST.get('tranxid')

        sumbit_payment_info = Payment.objects.create(
            tournament = get_tournament,
            team = get_team,
            paid_with_mobileNo = phoneNo,
            Transection_Id = tranxid,
            sumbitted_by = get_Profile,
            form_submitted = True,
        )
        messages.success(request, 'Your Payment Info has been submitted. We will get in Touch with You Soon..!')
        return redirect('/Payment-Status/'+slug)

    navbar_Tournament = Tournament.objects.all()
    context = {
        'get_tournament': get_tournament,
        # 'get_payment_record':get_payment_record,
        'navbar_Tournament':navbar_Tournament,
    }
    return render(request,"frontend/tournament/Payment.html",context)
# ---------------------------------------------------------------------------------------------------------------------------------------------------
def PaymentStatus(request,slug):

    if  request.user.is_authenticated:
        pass
    else:
        return redirect('/')

    get_team = TournamentParticipate.objects.filter(created_by =Profile.objects.get(user= request.user)).first()

    get_tournament = Tournament.objects.get(slug=slug)
    get_Profile = Profile.objects.get(user = request.user)


    get_payment_record = Payment.objects.get(tournament = get_tournament, sumbitted_by = Profile.objects.get(user= request.user) )
    print('[495] Payment Record:',get_payment_record)

    if get_payment_record.form_submitted == False:
        return redirect('/Payment-Instruction/'+slug)

    navbar_Tournament = Tournament.objects.all()
    context = {
        'get_tournament': get_tournament,
        'get_payment_record':get_payment_record,
        'navbar_Tournament':navbar_Tournament,
    }
    return render(request,"frontend/tournament/PaymentStatus.html",context)
# ---------------------------------------------------------------------------------------------------------------------------------------------------
def Tournament_View(request,slug):
    getTournament = Tournament.objects.get(slug=slug)
    navbar_Tournament = Tournament.objects.all()

    if GroupStage.objects.filter(tournament = getTournament,group=1).exists():
        get_Group1 = GroupStage.objects.get(tournament = getTournament,group=1)
        get_GroupStage_data1 = GroupStagePointTable.objects.filter(group =get_Group1).order_by("-points")
    else:
        get_GroupStage_data1 = 'None'
    if GroupStage.objects.filter(tournament = getTournament,group=2).exists():
        get_Group2 = GroupStage.objects.get(tournament = getTournament,group=2)
        get_GroupStage_data2 = GroupStagePointTable.objects.filter(group =get_Group2).order_by("-points")
    else:
        get_GroupStage_data2 = 'None'
    if GroupStage.objects.filter(tournament = getTournament,group=3).exists():
        get_Group3 = GroupStage.objects.get(tournament = getTournament,group=3)
        get_GroupStage_data3 = GroupStagePointTable.objects.filter(group =get_Group3).order_by("-points")
    else:
        get_GroupStage_data3 = 'None'
    if GroupStage.objects.filter(tournament = getTournament,group=4).exists():
        get_Group4 = GroupStage.objects.get(tournament = getTournament,group=4)
        get_GroupStage_data4 = GroupStagePointTable.objects.filter(group =get_Group4).order_by("-points")
    else:
        get_GroupStage_data4 = 'None'

    if GroupStageMatch.objects.filter(tournament = getTournament,round =1).exists():
        getAll_groupStage_matches1 = GroupStageMatch.objects.filter(
            tournament = getTournament,round =1).order_by('match_number')
    else:
        getAll_groupStage_matches1 = "None"



    if GroupStageMatch.objects.filter(tournament = getTournament,round =2).exists():
        getAll_groupStage_matches2 = GroupStageMatch.objects.filter(
            tournament = getTournament,round =2).order_by('match_number')
    else:
        getAll_groupStage_matches2 = "None"

    if GroupStageMatch.objects.filter(tournament = getTournament,round =3).exists():
        getAll_groupStage_matches3= GroupStageMatch.objects.filter(
            tournament = getTournament,round =3).order_by('match_number')
    else:
        getAll_groupStage_matches3 = "None"


    fixture = Fixture.objects.filter(tournament = getTournament).prefetch_related(
        "matches").prefetch_related("players").get()

    teams, results = get_bracket_info(fixture)

    template = loader.get_template('frontend/tournament/TournamentPage.html')
    # template = loader.get_template('bracket/testbracket.html')

    # BRACKET DESIGN 2 - From CODEPEN
    # template = loader.get_template('bracket/bracket_design_2/bracket_design_2.html')

    # BRACKET DESIGN 2 - From CODEPEN
    # print(json.dumps(results))
    context = {
            'getTournament': getTournament,
            'navbar_Tournament':navbar_Tournament,

            # Groups Points Table
            'get_GroupStage_data1':get_GroupStage_data1,
            'get_GroupStage_data2':get_GroupStage_data2,
            'get_GroupStage_data3':get_GroupStage_data3,
            'get_GroupStage_data4':get_GroupStage_data4,
            # Groups Points Table

            # Group Stage Matches
            'getAll_groupStage_matches1':getAll_groupStage_matches1,
            'getAll_groupStage_matches2':getAll_groupStage_matches2,
            'getAll_groupStage_matches3':getAll_groupStage_matches3,
            # Group Stage Matches

            'fixture': fixture,
            'teams':json.dumps(teams),
            'results': json.dumps(results),
        }
    return HttpResponse(template.render(context, request))


def get_bracket_info(fixture):
    results = []
    teams = list(map(lambda x: x.get_player_names(), fixture.matches.filter(match_round=1).order_by('id')))
    # print ("Teams Data")
    # print (teams)
    # print ("----------------")
    for r in range(1, fixture.rounds+1):
        # print("Round",r)
        results.append(list(map(lambda x: x.get_result_values(), fixture.matches.filter(match_round=r).order_by('id'))))
        # print ("Results Data")
        # print (results)
    return teams, results

# ---------------------------------------------------------------------------------------------------------------------------------------------------
def Team_View(request,slug):
    getTeam = Team.objects.get(slug=slug)

    if TournamentParticipate.objects.filter(team = getTeam).exists():
        # print("Found")
        get_Tournaments_Records = TournamentParticipate.objects.filter(team= getTeam).order_by("id")
    else:
        print("Not Found")
    for t in get_Tournaments_Records:
        print('[626] Tournament:',t.tournament)

    navbar_Tournament = Tournament.objects.all()
    context = {
        'getTeam': getTeam,
        'navbar_Tournament':navbar_Tournament,
        'get_Tournaments_Records':get_Tournaments_Records,
    }
    return render(request,"frontend/Team/teamPage.html",context)
# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Main View--------------------------------------------------------------------