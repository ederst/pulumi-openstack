# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetRoleResult:
    """
    A collection of values returned by getRole.
    """
    def __init__(__self__, domain_id=None, name=None, region=None, id=None):
        if domain_id and not isinstance(domain_id, str):
            raise TypeError("Expected argument 'domain_id' to be a str")
        __self__.domain_id = domain_id
        """
        See Argument Reference above.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        See Argument Reference above.
        """
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        __self__.region = region
        """
        See Argument Reference above.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
class AwaitableGetRoleResult(GetRoleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRoleResult(
            domain_id=self.domain_id,
            name=self.name,
            region=self.region,
            id=self.id)

def get_role(domain_id=None,name=None,region=None,opts=None):
    """
    Use this data source to get the ID of an OpenStack role.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/identity_role_v3.html.markdown.
    """
    __args__ = dict()

    __args__['domainId'] = domain_id
    __args__['name'] = name
    __args__['region'] = region
    if opts is None:
        opts = pulumi.ResourceOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('openstack:identity/getRole:getRole', __args__, opts=opts).value

    return AwaitableGetRoleResult(
        domain_id=__ret__.get('domainId'),
        name=__ret__.get('name'),
        region=__ret__.get('region'),
        id=__ret__.get('id'))
