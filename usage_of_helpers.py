#!/usr/bin/env python

import ovirt_helpers as oh
from ovirt_helpers.sdk.vms import method_using_hosts as direct_import

# you can use anything you want

# something from hosts:
oh.hosts.get_hosts()

# no problem with cycle import
oh.hosts.method_using_vms()

# something from vms:
oh.vms.get_vms()

# no problem with cycle import
oh.vms.method_using_hosts()

# usage of utils
oh.vms.method_using_utils("Hi ovirt helper")

#lsvaty
oh.utils.samplers.timeout_sampler("5")

# import ignoring sdk
oh.vms.method_using_hosts()

# direct import
direct_import()
