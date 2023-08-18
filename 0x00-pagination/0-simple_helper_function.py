#!/usr/bin/env python3
"""The module contains pagination exercise"""


def index_range(page, page_size):
    """returns start and end index"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
