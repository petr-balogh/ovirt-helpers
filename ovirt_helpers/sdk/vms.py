import ovirt_helpers as oh

def get_vms():
    print("Hi here are VMs: v1, v2, v3")

def method_using_hosts():
    oh.sdk.hosts.get_hosts()

def method_using_utils(param):
    print("Utils says: %s" % oh.utils.samplers.timeout_sampler(param))
