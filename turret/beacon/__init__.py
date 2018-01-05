# -*- coding: utf-8 -*-

"""
Secure communication between Turret nodes.

In order for Turret to operate as a distributed system in a variaty of
environments, there must be a way for nodes to securely discover each other and
communicate. This communication is done with Beacon. Beacon provides a way
for nodes to securely establish their peers in both safe and hostile
environments. Communication between nodes will be encrypted be default,
unencrypted communication will be available for debug purposes.

Because Turret nodes will operate is both safe and hostile environments,
Beacon can be configured to hide Turret from non-trusted probes. That is, only
trusted Turret peers will be able to find it. Additionaly, Beacon can deploy
various tactics to communicate with other Turret nodes without being detected.
This can include stenography (including data in other data, like an image) or
by using covert channels (including the data in a request to a different
service, knowing that the other Turret node can view this communication).
"""
