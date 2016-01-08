#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by WildCat. All rights reserved.

from rest_framework import generics, permissions, pagination
from .models import News
from .serializers import NewsSerializer


class DefaultPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 50


class NewsList(generics.ListAPIView):
    serializer_class = NewsSerializer
    pagination_class = DefaultPagination

    def get_queryset(self):
        return News.objects.all()
