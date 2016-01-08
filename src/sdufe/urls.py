#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by WildCat. All rights reserved.

from django.conf.urls import url, include

from .api import NewsList

news_urls = [
    url(r'^$', NewsList.as_view(), name='user-list')
]

urlpatterns = [
    url(r'^news', include(news_urls))
]
