#!/usr/bin/env python3
"""A module for a function"""


def index_range(page, page_size):
    return (((page-1) * page_size), (page * page_size))
