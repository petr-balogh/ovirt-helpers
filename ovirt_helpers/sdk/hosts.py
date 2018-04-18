import ovirt_helpers

def get_hosts():
    print("Hi here are hosts: h1, h2, h3")

def method_using_vms():
    ovirt_helpers.vms.get_vms()
