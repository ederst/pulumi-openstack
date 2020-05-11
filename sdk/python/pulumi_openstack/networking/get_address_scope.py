# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetAddressScopeResult:
    """
    A collection of values returned by getAddressScope.
    """
    def __init__(__self__, id=None, ip_version=None, name=None, project_id=None, region=None, shared=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if ip_version and not isinstance(ip_version, float):
            raise TypeError("Expected argument 'ip_version' to be a float")
        __self__.ip_version = ip_version
        """
        See Argument Reference above.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        See Argument Reference above.
        """
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        __self__.project_id = project_id
        """
        See Argument Reference above.
        """
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        __self__.region = region
        if shared and not isinstance(shared, bool):
            raise TypeError("Expected argument 'shared' to be a bool")
        __self__.shared = shared
        """
        See Argument Reference above.
        """
class AwaitableGetAddressScopeResult(GetAddressScopeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAddressScopeResult(
            id=self.id,
            ip_version=self.ip_version,
            name=self.name,
            project_id=self.project_id,
            region=self.region,
            shared=self.shared)

def get_address_scope(ip_version=None,name=None,project_id=None,region=None,shared=None,opts=None):
    """
    Use this data source to get the ID of an available OpenStack address-scope.

    ## Example Usage



    ```python
    import pulumi
    import pulumi_openstack as openstack

    public_addressscope = openstack.networking.get_address_scope(ip_version=4,
        name="public_addressscope",
        shared=True)
    ```



    :param float ip_version: IP version.
    :param str name: Name of the address-scope.
    :param str project_id: The owner of the address-scope.
    :param str region: The region in which to obtain the V2 Neutron client.
           A Neutron client is needed to retrieve address-scopes. If omitted, the
           `region` argument of the provider is used.
    :param bool shared: Indicates whether this address-scope is shared across
           all projects.
    """
    __args__ = dict()


    __args__['ipVersion'] = ip_version
    __args__['name'] = name
    __args__['projectId'] = project_id
    __args__['region'] = region
    __args__['shared'] = shared
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('openstack:networking/getAddressScope:getAddressScope', __args__, opts=opts).value

    return AwaitableGetAddressScopeResult(
        id=__ret__.get('id'),
        ip_version=__ret__.get('ipVersion'),
        name=__ret__.get('name'),
        project_id=__ret__.get('projectId'),
        region=__ret__.get('region'),
        shared=__ret__.get('shared'))
