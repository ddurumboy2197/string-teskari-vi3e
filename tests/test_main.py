# test_string_reversal.py
import pytest

def test_string_reversal():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string("abc") == "cba"

def test_string_reversal_empty_string():
    assert reverse_string("") == ""

def test_string_reversal_single_character():
    assert reverse_string("a") == "a"

def test_string_reversal_multiple_characters():
    assert reverse_string("hello") == "olleh"

def reverse_string(s):
    return s[::-1]
