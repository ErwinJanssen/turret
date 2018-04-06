# -*- coding: utf-8 -*-
# pylint: disable=unidiomatic-typecheck

"""Unit tests for the `clean_xml_dict` function."""

from collections import OrderedDict

from turret.core.util import clean_xml_dict


def test_empty_ordered_dict():
    """Expects an empty normal dict."""
    raw = OrderedDict()
    clean = clean_xml_dict(raw)

    assert type(clean) is dict
    assert not clean


def test_simple_ordered_dict():
    """Expects a normal dict where the keys are cleaned."""
    raw = OrderedDict([
        ('element', '@value should not be cleaned'),
        ('@attribute', 'some value'),
    ])
    clean = clean_xml_dict(raw)

    assert type(clean) is dict
    assert clean == {
        'element': '@value should not be cleaned',
        'attribute': 'some value',
    }


def test_nested_ordered_dict():
    """Expects the nested dict to be cleaned."""
    raw = OrderedDict([
        ('nested', OrderedDict([
            ('key', 'value'),
            ('@attr', 'attr value'),
        ])),
        ('key', 'another value'),
    ])
    clean = clean_xml_dict(raw)

    assert type(clean) is dict
    assert type(clean['nested']) is dict
    assert clean == {
        'nested': {
            'key': 'value',
            'attr': 'attr value',
        },
        'key': 'another value',
    }
