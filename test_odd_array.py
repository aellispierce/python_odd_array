from odd_array import *

def test_a_class_exists():
    assert OddArray


def test_b_initializer_takes_array_parameter():
    assert OddArray([1, 3, 5])


def test_c_to_list():
    odd_array = OddArray([1, 3, 5])
    assert  [1, 3, 5] == odd_array.list()


def test_d_add_number():
    odd_array = OddArray([1, 3, 5])
    odd_array.add(7)
    assert [1, 3, 5, 7] == odd_array.list()


def test_e_initialize_with_evens():
    odd_array = OddArray([1, 2, 3, 4, 5])
    assert [1, 3, 5] == odd_array.list()


def test_f_add_evens():
    odd_array = OddArray([1, 3, 5])
    odd_array.add(2)
    assert [1, 3, 5] == odd_array.list()


def test_g_add_negatives():
    odd_array = OddArray([-1, -2, 3, 4, -5])
    odd_array.add(-4)
    assert [-1, 3, -5] ==  odd_array.list()


def test_h_add_decimals():
    odd_array = OddArray([1, 3.2, 5])
    odd_array.add(2.1)
    assert [1, 5] == odd_array.list()

def test_i_add_strings():
    odd_array = OddArray([1, "Bob", 2])
    odd_array.add("Jen")
    assert [1] == odd_array.list()
