ovirt_helpers
-------------

This is just example of suggested structure of new package for ovirt helpers.

Some examples of usage you can see in the file [usage_of_helpers.py](./usage_of_helpers.py)

When you execute the file above, this is its output:
```
Hi here are hosts: h1, h2, h3
Hi here are VMs: v1, v2, v3
Hi here are VMs: v1, v2, v3
Hi here are hosts: h1, h2, h3
Utils says: Hi ovirt helper
```

So if we will just import the package itself inside the modules in sdk package
we can easily avoid circular imports. I guess that there is no need to use any
hl or ll package because it doesn't solve anything if you need import inside
ll something circularly (e.g. from vms something from hosts and vice versa).

Avoid ll, hl will makes things much more simplier as we want to have
[KISS](https://en.wikipedia.org/wiki/KISS_principle) approach here.

I got some ideas from this link [stack overflow](https://stackoverflow.com/questions/7336802/how-to-avoid-circular-imports-in-python)
