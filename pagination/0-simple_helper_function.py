def index_range(page, page_size):
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.
    """
    end_index = page * page_size
    start_index = end_index - page_size
    return (start_index, end_index)
