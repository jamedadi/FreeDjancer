from django.db import models
from django.contrib.auth import get_user_model

from django.utils.translation import gettext_lazy as _

from utils.basemodel import BaseModel

User = get_user_model()


class Project(BaseModel):

    PENDING = 0
    OPEN = 1
    NO_FREELANCER_SELECTED = 2
    CLOSED = 3
    AWAITING_ACCEPTANCE = 4
    ACCEPTED = 5
    IN_PROGRESS = 6
    COMPLETE = 7
    INCOMPLETE = 8

    STATUS = (
        (PENDING, _('pending')),
        (OPEN, _('open')),
        (NO_FREELANCER_SELECTED, _('no freelancer selected')),
        (CLOSED, _('closed')),
        (AWAITING_ACCEPTANCE, _('awaiting acceptance')),
        (ACCEPTED, _('accepted')),
        (IN_PROGRESS, _('in progress')),
        (COMPLETE, _('completed')),
        (INCOMPLETE, _('incomplete')),
    )

    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), max_length=500, )
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('posted by'))
    budget = models.ForeignKey('Budget', on_delete=models.SET_NULL, null=True, verbose_name=_('project budget'))
    status = models.PositiveSmallIntegerField(choices=STATUS, verbose_name='status of project', default=PENDING)
    expire_time = models.DateTimeField(verbose_name=_('expire time of project'))


class Budget(BaseModel):
    title = models.CharField(_('budget'), max_length=50, unique=True)
    min_price = models.BigIntegerField(_('minimum price of project'))
    max_price = models.BigIntegerField(_('maximum price of project'))


class Skill(BaseModel):
    title = models.CharField(_('skill'), max_length=50)


class ProjectSkill(BaseModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='skills')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='projects')


class UserBid(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bids')
    projects = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='bids')


class File(BaseModel):
    name = models.FileField(upload_to='files/')


class ProjectFile(BaseModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='files')
    file = models.ForeignKey(File, on_delete=models.PROTECT, related_name='projects')
