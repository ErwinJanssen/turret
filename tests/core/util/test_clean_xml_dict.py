# -*- coding: utf-8 -*-

"""Unit tests for the `clean_xml_dict` function."""

from collections import OrderedDict

from turret.core.util import clean_xml_dict


def test_ordered_dict():
    """The output should be a regular dict, where the keys are cleaned."""
    raw = OrderedDict()
    clean = clean_xml_dict(raw)

    # pylint: disable=unidiomatic-typecheck
    assert type(clean) == dict
    assert not clean

    raw = OrderedDict([
        ('element', 'some value'),
        ('@attribute', 'other value'),
    ])
    clean = clean_xml_dict(raw)

    assert clean == {
        'element': 'some value',
        'attribute': 'other value',
    }

    raw = OrderedDict([
        ('nested', OrderedDict([
            ('key', 'value'),
            ('@attr', 'attr value'),
        ])),
        ('key', 'another value'),
    ])
    clean = clean_xml_dict(raw)
    assert clean == {
        'nested': {
            'key': 'value',
            'attr': 'attr value',
        },
        'key': 'another value',
    }
