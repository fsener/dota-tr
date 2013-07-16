#!/usr/bin/env python
# -*- coding: utf-8 -*-
from player.models import PlayerProfile

def activate_steam(backend, user, social_user, is_new=False, new_association=False, *args, **kwargs): 
    if backend.name == 'twitter': 
        if new_association: 
            data = PlayerProfile(user=user)
            data.has_steam = True
            data.save()