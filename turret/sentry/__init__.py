# -*- coding: utf-8 -*-

"""
Sets Turret into Sentry mode, passively monitoring it's environment.

In this case environment includes, but is not limited to:
- The system Turret is running on (processes, hardware, users, etc.)
- The network the system is located in (other nodes in the network, IP
  addresses, DNS servers, DHCP configuration).
- Communication with other systems (network traffic, ), also outside the
  current network.

Passively means Turret will be as quiet as possible on the network, and light
on the system it is running on. It should be difficult to detect Turret is mode
of operation. For active reconnaissance, use Scout.

The informaion will can be stored in a database. This can be an inmemory sqlite
database, or an external database like PostgreSQL or Elasticsearch. This can
also include a periodic agration of the result to a remote sytem or other
Turret node (for the latter, Beacon will be used.). This might be usefull to
conserve bandwidth, or if Turret is used in a hostile environment.
"""
