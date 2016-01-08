#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by WildCat. All rights reserved.

from rest_framework import serializers

from .models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'category', 'date', 'editor', 'content')
