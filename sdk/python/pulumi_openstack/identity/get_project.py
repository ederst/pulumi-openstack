# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetProjectResult:
    """
    A collection of values returned by getProject.
    """
    def __init__(__self__, description=None, domain_id=None, enabled=None, id=None, is_domain=None, name=None, parent_id=None, region=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        """
        The description of the project.
        """
        if domain_id and not isinstance(domain_id, str):
            raise TypeError("Expected argument 'domain_id' to be a str")
        __self__.domain_id = domain_id
        """
        See Argument Reference above.
        """
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        __self__.enabled = enabled
        """
        See Argument Reference above.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
        if is_domain and not isinstance(is_domain, bool):
            raise TypeError("Expected argument 'is_domain' to be a bool")
        __self__.is_domain = is_domain
        """
        See Argument Reference above.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        See Argument Reference above.
        """
        if parent_id and not isinstance(parent_id, str):
            raise TypeError("Expected argument 'parent_id' to be a str")
        __self__.parent_id = parent_id
        """
        See Argument Reference above.
        """
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        __self__.region = region
        """
        The region the project is located in.
        """
class AwaitableGetProjectResult(GetProjectResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProjectResult(
            description=self.description,
            domain_id=self.domain_id,
            enabled=self.enabled,
            id=self.id,
            is_domain=self.is_domain,
            name=self.name,
            parent_id=self.parent_id,
            region=self.region)

def get_project(domain_id=None,enabled=None,is_domain=None,name=None,parent_id=None,region=None,opts=None):
    """
    Use this data source to get the ID of an OpenStack project.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/identity_project_v3.html.markdown.


    :param str domain_id: The domain this project belongs to.
    :param bool enabled: Whether the project is enabled or disabled. Valid
           values are `true` and `false`.
    :param bool is_domain: Whether this project is a domain. Valid values
           are `true` and `false`.
    :param str name: The name of the project.
    :param str parent_id: The parent of this project.
    :param str region: The region the project is located in.
    """
    __args__ = dict()


    __args__['domainId'] = domain_id
    __args__['enabled'] = enabled
    __args__['isDomain'] = is_domain
    __args__['name'] = name
    __args__['parentId'] = parent_id
    __args__['region'] = region
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('openstack:identity/getProject:getProject', __args__, opts=opts).value

    return AwaitableGetProjectResult(
        description=__ret__.get('description'),
        domain_id=__ret__.get('domainId'),
        enabled=__ret__.get('enabled'),
        id=__ret__.get('id'),
        is_domain=__ret__.get('isDomain'),
        name=__ret__.get('name'),
        parent_id=__ret__.get('parentId'),
        region=__ret__.get('region'))
