from django.db import models
import datetime
from django.contrib.auth.models import User
from django.db.models.fields import DateField
import uuid

from django_resized import ResizedImageField

from django.core.validators import MinValueValidator
from django.utils.text import slugify


from ckeditor.fields import RichTextField

# Create your models here.


# --------------------------------------------------------
#  Project Model Classes Starts


# ---------------------------------------------------------------------------------------------------------------------------------------------------
# User Profile Model  Starts
# Features Related to - User Profiling, Sign-Up, Login, Verification/Auth.
class Profile(models.Model):
    user        = models.OneToOneField(User , on_delete=models.CASCADE)
    email       = models.EmailField()
    phoneNo     = models.CharField(max_length=11)

    auth_token  = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)

    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
# User Profile Model Ends
# ---------------------------------------------------------------------------------------------------------------------------------------------------

# Tournament Models Starts
# ---------------------------------------------------------------------------------------------------------------------------------------------------
class Player(models.Model):
    name            =   models.CharField(max_length=256)
    gaming_name     =   models.CharField(max_length=266)

    role_selected = (
        ("SafeLane","SafeLane"),
        ("MidLane","MidLane"),
        ("OffLane","OffLane"),
        ("Soft Support","Soft Support"),
        ("Hard Support","Hard Support"),
    )
    role            =   models.CharField(max_length=100, choices = role_selected)

    player_id       =   models.CharField(max_length=256, null=True,blank=True)
    steam_id        =   models.CharField(max_length= 256,null=True,blank=True)
    estimated_mmr   =   models.PositiveIntegerField(null=True,blank=True)

    phoneNo         =   models.CharField(max_length=11,null=True,blank=True)
    email           =   models.EmailField(null=True,blank=True)

    def __str__(self):
        return self.gaming_name
# ---------------------------------------------------------------------------------------------------------------------------------------------------
class Team(models.Model):
    name            =   models.CharField(max_length=256)
    shortname       =   models.CharField(max_length=10,blank=True,null=True)
    slug            =   models.SlugField(max_length=500, unique=True, blank=True)
    logo            =   ResizedImageField(size=[500, 300], upload_to='team/logo/',
                        force_format='PNG',blank=True,
                        default="team/logo/default.png")

    members         =   models.ManyToManyField(Player)

    is_verified     =   models.BooleanField(default=False)

    created_at      =   models.DateTimeField(auto_now_add=True)
    created_by      =   models.ForeignKey(Profile,null=True,blank=True, on_delete = models.CASCADE)

    game            =   models.CharField(max_length=100,null=True,blank=True,default='DOTA 2')

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Team, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
# ---------------------------------------------------------------------------------------------------------------------------------------------------
class  Tournament(models.Model):
    title           =   models.CharField(max_length=256)
    slug            =   models.SlugField(max_length=500, unique=True, blank=True)

    remark          = RichTextField(default='',null=True,blank=True)
    payment_Info    = RichTextField(default='',null=True,blank=True)


    description     =   models.TextField(blank=True,null=True)
    logo            =   models.ImageField(upload_to="tournament/logo/")

    prizepool       =   models.PositiveIntegerField(blank=True,null=True)

    pub_date        =   models.DateField('date published', null=True)
    reg_deadline    =   models.DateField('Registration Deadline', null=True)
    start_date      =   models.DateField('Start date')
    end_date        =   models.DateField('End date')

    # matches_per_day =   models.PositiveIntegerField(validators=[MinValueValidator(1)], null=True,blank=True)

    created_by      =   models.ForeignKey(Profile,null=True,blank=True, on_delete = models.CASCADE)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Tournament, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
# ---------------------------------------------------------------------------------------------------------------------------------------------------
class Fixture(models.Model):
    pub_date = models.DateTimeField('date published', null=True)
    name = models.CharField(max_length=256)
    tournament = models.ForeignKey(Tournament,on_delete=models.CASCADE,null=True,blank=True)

    rounds = models.IntegerField(default=0)
    start_date = models.DateField('Start date')

    matches_per_day = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    current_round = models.IntegerField(default=0)

    def __str__(self):
        return self.name
        # return "{} ".format()
    def save(self, *args, **kwargs):
        pub_date = datetime.datetime.utcnow()
        super(Fixture, self).save(*args, **kwargs)
# ---------------------------------------------------------------------------------------------------------------------------------------------------
class GroupStage(models.Model):
    name = models.CharField(max_length=50)
    tournament = models.ForeignKey(Tournament,on_delete=models.CASCADE,null=True,blank=True)
    group_choices = (
        (1,1),
        (2,2),
        (3,3),
        (4,4),
    )
    group_champion = models.ForeignKey(Team,on_delete=models.CASCADE,null=True,blank=True)
    group = models.PositiveIntegerField(choices=group_choices)
    start_date = models.DateField('Start date GroupStage',null=True,blank=True)
    matches_per_day = models.PositiveIntegerField(validators=[MinValueValidator(1)])

    total_rounds = models.IntegerField(default=0,null=True,blank=True)


    def __str__(self):
        # return self.name
        return "{} - Group {}".format(self.tournament.title,self.group)

    def save(self, *args, **kwargs):
        pub_date = datetime.datetime.utcnow()
        super(GroupStage, self).save(*args, **kwargs)

# ---------------------------------------------------------------------------------------------------------------------------------------------------
class TournamentParticipate(models.Model):

    team            =   models.ForeignKey(Team,on_delete=models.CASCADE)
    text_teamName   =   models.CharField(max_length=100,null=True,blank=True)

    tournament      =   models.ForeignKey(Tournament,on_delete=models.CASCADE)

    created_at      =   models.DateTimeField(auto_now_add=True)
    created_by      =   models.ForeignKey(Profile,on_delete=models.CASCADE, null=True,blank=True)
    is_verified     =   models.BooleanField(default=False)
    rank = models.IntegerField(blank=True,null=True)
    fixture = models.ForeignKey(Fixture, on_delete=models.CASCADE,
                                blank=True,null=True,related_name="players")



    def __str__(self):
        # return "{} ({})" . format(self.team.name, self.tournament.title)

        return self.team.name
# ---------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------------------------------------------
class GroupStageMatch(models.Model):
    class Meta:
        verbose_name = "Group Stage Matche"
    tournament = models.ForeignKey(Tournament,on_delete=models.CASCADE
                                   ,null=True,blank=True)
    date = models.DateField("Match Date",null=True,blank=True)
    time = models.TimeField('Match Time',null=True,blank=True)

    dota2_match_id = models.CharField(max_length=200,null=True,blank=True)
    match_number = models.IntegerField(blank=True, null=True)

    group = models.ForeignKey(GroupStage,on_delete=models.CASCADE ,related_name="groupstage_matches"
                              ,null=True,blank=True)

    round = models.IntegerField(default=1)
    match_round = models.IntegerField(null=True,blank=True)
    team_1 = models.ForeignKey(
        TournamentParticipate, blank=True, null=True,on_delete=models.CASCADE,related_name="team1_groupStage")
    team_2 = models.ForeignKey(
        TournamentParticipate, blank=True, null=True,on_delete=models.CASCADE,related_name="team2_groupStage")

    MATCH_STATUS = (
        ("TBD", "TBD"),
        ("Scheduled", "Scheduled"),
        ('Finished', 'Finished')
    )
    status = models.CharField(
        max_length=30, choices=MATCH_STATUS, default='TBD',null=True,blank=True)

    team_1_score = models.PositiveIntegerField(default=0)
    team_2_score = models.PositiveIntegerField(default=0)

    winner = models.ForeignKey(
        TournamentParticipate,on_delete=models.CASCADE, blank=True, null=True, related_name="matches_won_groupStage")

    def __str__(self):
        if self.status == "TBD":
            return "Upcoming Match No# {} - {} vs {}".format(self.match_number,self.status,self.status)


        if self.status == "Scheduled":
            return "{} vs {}".format(self.team_1.team.name, self.team_2.team.name)

        if self.status == "Finished":
            return"{} {} vs {} {}".format(self.team_1.team.name, self.team_1_score,
                                          self.team_2_score,self.team_2.team.name)

    def get_GroupStage_Data(self):
        return [
            str(self.team_1) if self.team_1 else None,
            str(self.team_2) if self.team_1 else None,
        ]

# ---------------------------------------------------------------------------------------------------------------------------------------------------
class GroupStagePointTable(models.Model):
    class Meta:
        verbose_name= 'Group Stage Point Table'

    group = models.ForeignKey(GroupStage,on_delete=models.CASCADE ,related_name="groupstage_PointsTable"
                              ,null=True,blank=True)
    team = models.ForeignKey(TournamentParticipate,on_delete=models.CASCADE,null=True,blank=True)

    played  = models.PositiveIntegerField(default=0,null=True,blank=True)
    win     = models.PositiveIntegerField(default=0,null=True,blank=True)
    loss    = models.PositiveIntegerField(default=0,null=True,blank=True)
    points  = models.PositiveIntegerField(default=0,null=True,blank=True)

    matches = models.ManyToManyField(GroupStageMatch,blank=True)
    qualified_status = models.BooleanField(default=False)

    def __str__(self):
        return self.team.team.name
# ---------------------------------------------------------------------------------------------------------------------------------------------------
class Match(models.Model):
    class Meta:
        verbose_name = "Matches"
    @property
    def description(self):
        return repr(self)
    @property
    def name(self):
        if self.match_number:
            return "{} - Match {}".format(self.fixture.name, self.match_number)
        else:
            return "{}".format(self.fixture.name)


    date = models.DateField('Match Date', null=True, blank=True)
    match_number = models.IntegerField(blank=True, null=True)

    fixture = models.ForeignKey(Fixture,on_delete=models.CASCADE ,related_name="matches",null=True,blank=True)
    match_round = models.IntegerField()

    left_previous = models.OneToOneField(
        'self', blank=True, null=True, related_name="left_next_match",on_delete=models.CASCADE )
    right_previous = models.OneToOneField(
        'self', blank=True, null=True, related_name="right_next_match",on_delete=models.CASCADE )

    player_1 = models.ForeignKey(
        TournamentParticipate, blank=True, null=True, related_name="left_matches",on_delete=models.CASCADE )
    player_2 = models.ForeignKey(
        TournamentParticipate, blank=True, null=True, related_name="right_matches",on_delete=models.CASCADE )

    MATCH_STATUS = [
        ("BYE", 'BYE'),
        ("Not Scheduled", 'Not Scheduled'),
        ("Scheduled", "Scheduled"),
        ('Finished', 'Finished')
    ]
    status = models.CharField(
        max_length=30, choices=MATCH_STATUS, default='Not Scheduled')

    player_1_score = models.PositiveIntegerField(null=True, blank=True)
    player_2_score = models.PositiveIntegerField(null=True, blank=True)

    winner = models.ForeignKey(
        TournamentParticipate,on_delete=models.CASCADE, blank=True, null=True, related_name="matches_won")

    def __str__(self):
        return "{}: {}".format(self.name, self.description)

    def __repr__(self):
        if self.status == 'Finished':
            return "{} {}-{} {}".format(self.player_1, self.player_1_score, self.player_2_score, self.player_2)

        _right = "BYE"
        _left = "BYE"

        if self.player_1:
            _left = "{}".format(self.player_1)
        elif self.left_previous:
            _left = "Winners (Match {})".format(self.left_previous.match_number)

        if self.player_2:
            _right = "{}".format(self.player_2)
        elif  self.right_previous:
            _right = "Winners (Match {})".format(self.right_previous.match_number)

        if _right == "BYE" and _left == "BYE":
            _right = "TBD"
            _left = "TBD"

        return "{} vs {}".format(_left, _right)

    def save(self,*args,**kwargs):
        self.status = "Not Scheduled"
        self.winner = None

        if self.player_1 and self.player_2:
            self.status = "Scheduled"
            self.player_1_score = self.player_1_score or 0
            self.player_2_score = self.player_2_score or 0

            if self.player_1_score == self.player_2_score:
                self.player_1_score = None
                self.player_2_score = None
                self.winner=None

            elif self.player_1_score > self.player_2_score:

                self.winner = self.player_1
                self.status = "Finished"
            else:
                self.winner = self.player_2
                self.status = "Finished"

        elif self.player_1 or self.player_2:
            self.player_1_score = None
            self.player_2_score = None

            if not (self.player_1 or self.left_previous):
                self.status = 'BYE'
                self.winner = self.player_2

            elif not (self.player_2 or self.right_previous):
                self.status = 'BYE'
                self.winner = self.player_1

        super(Match, self).save(*args, **kwargs)


        if self.winner:
            try:
                _next_left = self.left_next_match
                if _next_left:
                    _next_left.player_1 = self.winner
                    _next_left.save()
            except:
                pass

            try:
                _next_right = self.right_next_match
                if _next_right:
                    _next_right.player_2 = self.winner
                    _next_right.save()
            except:
                pass

        if self.status=="Finished":
            self.fixture.current_round = max(self.fixture.current_round, self.match_round)
            self.fixture.save()

    def is_bye(self):
        return self.status == 'BYE', self.player_1 or self.player_2

    def get_player_names(self):
        return [
            str(self.player_1) if self.player_1 else None,
            str(self.player_2) if self.player_2 else None,
        ]

    def get_result_values(self):
        return [self.player_1_score, self.player_2_score,]

# ---------------------------------------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------------------------------------------------------
class Payment(models.Model):
    tournament          = models.ForeignKey(Tournament,on_delete=models.CASCADE)
    methods = (
        ("BKash","BKash"),
        ("Rocket","Rocket"),
        ("Nagad","Nagad"),
    )
    payment_method_used = models.CharField(max_length=50,choices=methods,null=True,blank=True,default="BKash")
    entry_fee           = models.PositiveIntegerField(null=True,blank=True)

    team                = models.ForeignKey(TournamentParticipate,on_delete=models.CASCADE,null=True,blank=True)

    paid_with_mobileNo  = models.CharField(max_length=11,null=True,blank=True)
    Transection_Id      = models.CharField(max_length=200,null=True,blank=True)
    paid_at             = models.DateTimeField(auto_now_add=True)

    form_submitted      = models.BooleanField(default=False)
    is_verified         = models.BooleanField(default=False)

    tranx_success       = models.BooleanField(default=False)
    sumbitted_by        = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return "{} For Tournament {}" .format(self.Transection_Id, self.tournament.title)
# ---------------------------------------------------------------------------------------------------------------------------------------------------


# Tournament Models Ends
#  Project Model Classes Ends
# --------------------------------------------------------





