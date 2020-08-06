# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import _utilities, _tables


class GetAvailbilityZonesResult:
    """
    A collection of values returned by getAvailbilityZones.
    """
    def __init__(__self__, id=None, names=None, region=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        __self__.names = names
        """
        The names of the availability zones, ordered alphanumerically.
        """
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        __self__.region = region
        """
        See Argument Reference above.
        """


class AwaitableGetAvailbilityZonesResult(GetAvailbilityZonesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAvailbilityZonesResult(
            id=self.id,
            names=self.names,
            region=self.region)


def get_availbility_zones(region=None, opts=None):
    """
    Use this data source to get a list of Shared File System availability zones
    from OpenStack

    ## Example Usage

    ```python
    import pulumi
    import pulumi_openstack as openstack

    zones = openstack.sharedfilesystem.get_availbility_zones()
    ```


    :param str region: The region in which to obtain the V2 Shared File System
           client. If omitted, the `region` argument of the provider is used.
    """
    __args__ = dict()
    __args__['region'] = region
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('openstack:sharedfilesystem/getAvailbilityZones:getAvailbilityZones', __args__, opts=opts).value

    return AwaitableGetAvailbilityZonesResult(
        id=__ret__.get('id'),
        names=__ret__.get('names'),
        region=__ret__.get('region'))
