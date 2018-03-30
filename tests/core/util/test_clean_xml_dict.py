# -*- coding: utf-8 -*-

"""Unit tests for the `clean_xml_dict` function."""

from collections import OrderedDict

from turret.core.util import clean_xml_dict


def test_ordered_dict():
    """The output should be a regular dictionary, where the keys are cleaed."""
    raw = OrderedDict()
    clean = clean_xml_dict(raw)

    # pylint: disable=unidiomatic-typecheck
    assert type(clean) == dict
    assert not clean
