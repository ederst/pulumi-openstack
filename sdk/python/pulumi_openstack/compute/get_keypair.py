# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import _utilities, _tables


class GetKeypairResult:
    """
    A collection of values returned by getKeypair.
    """
    def __init__(__self__, fingerprint=None, id=None, name=None, public_key=None, region=None):
        if fingerprint and not isinstance(fingerprint, str):
            raise TypeError("Expected argument 'fingerprint' to be a str")
        __self__.fingerprint = fingerprint
        """
        The fingerprint of the OpenSSH key.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        See Argument Reference above.
        """
        if public_key and not isinstance(public_key, str):
            raise TypeError("Expected argument 'public_key' to be a str")
        __self__.public_key = public_key
        """
        The OpenSSH-formatted public key of the keypair.
        """
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        __self__.region = region
        """
        See Argument Reference above.
        """


class AwaitableGetKeypairResult(GetKeypairResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetKeypairResult(
            fingerprint=self.fingerprint,
            id=self.id,
            name=self.name,
            public_key=self.public_key,
            region=self.region)


def get_keypair(name=None, region=None, opts=None):
    """
    Use this data source to get the ID and public key of an OpenStack keypair.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_openstack as openstack

    kp = openstack.compute.get_keypair(name="sand")
    ```


    :param str name: The unique name of the keypair.
    :param str region: The region in which to obtain the V2 Compute client.
           If omitted, the `region` argument of the provider is used.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['region'] = region
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('openstack:compute/getKeypair:getKeypair', __args__, opts=opts).value

    return AwaitableGetKeypairResult(
        fingerprint=__ret__.get('fingerprint'),
        id=__ret__.get('id'),
        name=__ret__.get('name'),
        public_key=__ret__.get('publicKey'),
        region=__ret__.get('region'))
