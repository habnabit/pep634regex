import re

import pep634regex


def test_considering():
    matched = False
    match pep634regex.considering('spam'):
        case pep634regex.fullmatch('sp.m'):
            matched = True
    assert matched


def test_match_attribute():
    match = None
    match pep634regex.considering('spam'):
        case pep634regex.fullmatch('sp.m') as m:
            match = m
    assert isinstance(m.match, re.Match)
