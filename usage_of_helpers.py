#!/usr/bin/env python

import ovirt_helpers as oh

# you can use anything you want

# something from hosts:
oh.sdk.hosts.get_hosts()

# no problem with cycle import
oh.sdk.hosts.method_using_vms()

# something from vms:
oh.sdk.vms.get_vms()

# no problem with cycle import
oh.sdk.vms.method_using_hosts()

# usage of utils
oh.sdk.vms.method_using_utils("Hi ovirt helper")
