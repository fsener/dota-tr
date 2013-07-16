#!/usr/bin/env python
# -*- coding: utf-8 -*-

from registration.forms import RegistrationForm
from django import forms
from player.models import PlayerProfile

class PlayerRegForm(RegistrationForm):
    age = forms.IntegerField(label="Yaş", min_value=0)