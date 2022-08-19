from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _

from utils.basemodel import BaseModel


class User(AbstractBaseUser):
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    bids_left = models.SmallIntegerField(_('bids left'), default=5)
    avatar = models.ImageField(_('avatar'), upload_to='avatar/', blank=True)
    has_kyc = models.BooleanField(_('KYC'), default=False)

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()


class Relation(BaseModel):
    from_user = models.ForeignKey(
        User, related_name='followings', verbose_name=_('followed by'), on_delete=models.CASCADE
    )
    to_user = models.ForeignKey(
        User, related_name='followers', verbose_name=_('followed to'), on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = _('Relation')
        verbose_name_plural = _('Relations')

    def __str__(self):
        return f"{self.from_user} -> {self.to_user}"


class Portfolio(BaseModel):
    user = models.ForeignKey(User, related_name='portfolios', on_delete=models.CASCADE, verbose_name='belong to')
    title = models.CharField(_('title'), max_length=50)
    description = models.TextField(_('description'), max_length=500)
    cover = models.ImageField(_('avatar'), upload_to='portfolio/')

    class Meta:
        verbose_name = 'portfolio',
        verbose_name_plural = 'portfolios'


class PortfolioFile(BaseModel):
    from jobs.models import File
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='files')
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='portfolios')


class UserSkill(BaseModel):
    from jobs.models import Skill
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='users')
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='skills')


