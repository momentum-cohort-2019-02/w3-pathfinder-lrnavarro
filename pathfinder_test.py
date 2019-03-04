import pytest
from pathfinder import get_2d_array, get_smallest_min, get_int_array, get_largest_max

def test_get_2d_array():
    simple_array = get_2d_array("test_data.txt")
    assert len(simple_array) == 4
    assert len(simple_array[0]) == 5

def test_get_smallest_min():
    simple_array = get_2d_array("test_data.txt")
    assert get_smallest_min(get_int_array(simple_array)) == 1

def test_get_largetst_max():
    simple_array = get_2d_array("test_data.txt")
    assert get_largest_max(get_int_array(simple_array)) == 9