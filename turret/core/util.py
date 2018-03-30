# -*- coding: utf-8 -*-

"""Utilities for use in Turret."""

import socket
from collections import OrderedDict
from ipaddress import IPv4Network, IPv6Network, ip_network
from typing import Set, Union

import psutil


def interface_subnets(interface: str) -> Set[Union[IPv4Network, IPv6Network]]:
    """Given a network interface, retrieve the associated IP subnets.

    Args:
        interface: Name of the interface, for example 'eth0' or wlp3s0'.

    Raises:
        ValueError: If the specified interface does not exist and can therefore
            not be found.

    """
    try:
        interface_info = psutil.net_if_addrs()[interface]
    except KeyError:
        raise ValueError('Interface does not exist: {}'.format(interface))

    subnets = set()
    for addr in interface_info:
        if addr.family is socket.AF_INET:
            subnets.add(ip_network((addr.address, addr.netmask), strict=False))
        elif addr.family is socket.AF_INET6:
            # FIXME: IPv6 addresses can be of the form <address>%<interface>
            #        This cannot be directly parsed by the ipaddress module.
            pass
    return subnets


def clean_xml_dict(raw):
    """Recursivly clean a dict returned by 'xmltodict'.

    The cleaning procedure depends on the type of the input:

    Args:
        raw: The raw output returned by 'xmltodict.parse()', or a subvalue of
            such a raw value.

    Returns:
        The cleaned value of the raw input, following the cleaning procedure.

    """
    if isinstance(raw, OrderedDict):
        return {
            key: raw[key] for key in raw
        }

    return raw
