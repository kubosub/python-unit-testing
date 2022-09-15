'''Pytest functions for testing integer_add.py'''

import pytest
import integer_add

def test_main_addition(capsys):
    '''Test adding two integers'''
    integer_add.main(['5', '3'])

    out, err = capsys.readouterr()
    assert out == '8\n'
    assert err == ''

def test_main_addition_with_one_negative_integer(capsys):
    '''Negative number'''
    integer_add.main(['8', '-3'])

    out, err = capsys.readouterr()
    assert out == '5\n'
    assert err == ''

def test_main_addition_with_two_negative_integers(capsys):
    '''Two negative numbers'''
    integer_add.main(['-7', '-2'])

    out, err = capsys.readouterr()
    assert out == '-9\n'
    assert err == ''

def test_main_addition_with_zero_value(capsys):
    '''Zeroes'''
    integer_add.main(['0', '0'])

    out, err = capsys.readouterr()
    assert out == '0\n'
    assert err == ''

def test_main_addition_with_non_integer(capsys):
    '''If a non-integer is passed it should equal 0'''
    integer_add.main(['asdf', '10'])

    out, err = capsys.readouterr()
    assert out == '10\n'
    assert err == ''

def test_main_addition_with_two_non_integer(capsys):
    '''If a non-integer is passed it should equal 0'''
    integer_add.main(['qwer', 'asdf'])

    out, err = capsys.readouterr()
    assert out == '0\n'
    assert err == ''

def test_main_addition_with_two_large_integers(capsys):
    '''Large numbers'''
    integer_add.main(['847187409', '749172673'])

    out, err = capsys.readouterr()
    assert out == '1596360082\n'
    assert err == ''

def test_main_addition_with_three_integers():
    '''Error test with too many arguments'''
    with pytest.raises(SystemExit) as error:
        integer_add.main(['1', '2', '3'])

    assert error.type == SystemExit
    assert error.value.code == 2

def test_main_error_no_arguments():
    '''Error test with no arguments'''
    with pytest.raises(SystemExit) as error:
        integer_add.main()

    assert error.type == SystemExit
    assert error.value.code == 2

def test_main_error_one_argument():
    '''Error test with only one argument'''
    with pytest.raises(SystemExit) as error:
        integer_add.main(['33'])

    assert error.type == SystemExit
    assert error.value.code == 2
