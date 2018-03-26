# -*- coding: utf-8 -*-
# pylint: disable=redefined-outer-name

"""Unit tests for the `xml_to_raw_dict` function."""

from collections import OrderedDict

import pytest

from turret.raw.nmap import xml_to_raw_dict


@pytest.fixture
def sample_data():
    """Load and return the sample dataset."""
    with open('tests/data/local_nmap.xml') as file:
        return file.read()


def test_type(sample_data):
    """The output type is expected to be an OrderedDict.

    The rest of the output is dependent on the 'xmltodict' package and will
    therefore not be tested.
    """
    assert isinstance(xml_to_raw_dict(sample_data), OrderedDict)
