#!/usr/bin/env python
# -*- coding: utf-8 -*-
from player.models import PlayerProfile

def activate_steam(backend, user, social_user, is_new=False, new_association=False, *args, **kwargs): 
    if backend.name == 'steam': 
        if new_association: 
            profile, created = PlayerProfile.objects.get_or_create(user_id=user.id, defaults={'age': 0})
            profile.has_steam = True
            profile.save()