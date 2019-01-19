# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetProjectResult(object):
    """
    A collection of values returned by getProject.
    """
    def __init__(__self__, description=None, domain_id=None, region=None, id=None):
        if description and not isinstance(description, str):
            raise TypeError('Expected argument description to be a str')
        __self__.description = description
        """
        The description of the project.
        """
        if domain_id and not isinstance(domain_id, str):
            raise TypeError('Expected argument domain_id to be a str')
        __self__.domain_id = domain_id
        """
        See Argument Reference above.
        """
        if region and not isinstance(region, str):
            raise TypeError('Expected argument region to be a str')
        __self__.region = region
        """
        The region the project is located in.
        """
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_project(domain_id=None, enabled=None, is_domain=None, name=None, parent_id=None, region=None):
    """
    Use this data source to get the ID of an OpenStack project.
    """
    __args__ = dict()

    __args__['domainId'] = domain_id
    __args__['enabled'] = enabled
    __args__['isDomain'] = is_domain
    __args__['name'] = name
    __args__['parentId'] = parent_id
    __args__['region'] = region
    __ret__ = await pulumi.runtime.invoke('openstack:identity/getProject:getProject', __args__)

    return GetProjectResult(
        description=__ret__.get('description'),
        domain_id=__ret__.get('domainId'),
        region=__ret__.get('region'),
        id=__ret__.get('id'))
