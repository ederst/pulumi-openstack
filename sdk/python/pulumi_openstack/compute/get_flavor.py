# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetFlavorResult(object):
    """
    A collection of values returned by getFlavor.
    """
    def __init__(__self__, extra_specs=None, is_public=None, region=None, id=None):
        if extra_specs and not isinstance(extra_specs, dict):
            raise TypeError('Expected argument extra_specs to be a dict')
        __self__.extra_specs = extra_specs
        """
        Key/Value pairs of metadata for the flavor.
        """
        if is_public and not isinstance(is_public, bool):
            raise TypeError('Expected argument is_public to be a bool')
        __self__.is_public = is_public
        """
        Whether the flavor is public or private.
        """
        if region and not isinstance(region, str):
            raise TypeError('Expected argument region to be a str')
        __self__.region = region
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_flavor(disk=None, min_disk=None, min_ram=None, name=None, ram=None, region=None, rx_tx_factor=None, swap=None, vcpus=None):
    """
    Use this data source to get the ID of an available OpenStack flavor.
    """
    __args__ = dict()

    __args__['disk'] = disk
    __args__['minDisk'] = min_disk
    __args__['minRam'] = min_ram
    __args__['name'] = name
    __args__['ram'] = ram
    __args__['region'] = region
    __args__['rxTxFactor'] = rx_tx_factor
    __args__['swap'] = swap
    __args__['vcpus'] = vcpus
    __ret__ = await pulumi.runtime.invoke('openstack:compute/getFlavor:getFlavor', __args__)

    return GetFlavorResult(
        extra_specs=__ret__.get('extraSpecs'),
        is_public=__ret__.get('isPublic'),
        region=__ret__.get('region'),
        id=__ret__.get('id'))
