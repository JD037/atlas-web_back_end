#!/usr/bin/env python3
"""
This module implements simple pagination for a dataset of popular
baby names.
It includes a 'Server' class that provides functionality to
access and paginate the dataset.
The 'get_page' method within the Server class
takes two integer parameters, 'page' and 'page_size',
"""

import csv
import math
from typing import List, Tuple


def index_range(page, page_size):
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset."""
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0
        start_index, end_index = index_range(page, page_size)
        if start_index >= len(self.__dataset):
            return []
        return self.__dataset[start_index:min(end_index, len(self.__dataset))]
