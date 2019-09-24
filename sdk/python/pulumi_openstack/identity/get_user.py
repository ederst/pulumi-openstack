# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class GetUserResult:
    """
    A collection of values returned by getUser.
    """
    def __init__(__self__, default_project_id=None, description=None, domain_id=None, enabled=None, idp_id=None, name=None, password_expires_at=None, protocol_id=None, region=None, unique_id=None, id=None):
        if default_project_id and not isinstance(default_project_id, str):
            raise TypeError("Expected argument 'default_project_id' to be a str")
        __self__.default_project_id = default_project_id
        """
        See Argument Reference above.
        """
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        """
        A description of the user.
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
        if idp_id and not isinstance(idp_id, str):
            raise TypeError("Expected argument 'idp_id' to be a str")
        __self__.idp_id = idp_id
        """
        See Argument Reference above.
        """
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        """
        See Argument Reference above.
        """
        if password_expires_at and not isinstance(password_expires_at, str):
            raise TypeError("Expected argument 'password_expires_at' to be a str")
        __self__.password_expires_at = password_expires_at
        """
        See Argument Reference above.
        """
        if protocol_id and not isinstance(protocol_id, str):
            raise TypeError("Expected argument 'protocol_id' to be a str")
        __self__.protocol_id = protocol_id
        """
        See Argument Reference above.
        """
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        __self__.region = region
        """
        The region the user is located in.
        """
        if unique_id and not isinstance(unique_id, str):
            raise TypeError("Expected argument 'unique_id' to be a str")
        __self__.unique_id = unique_id
        """
        See Argument Reference above.
        """
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """
class AwaitableGetUserResult(GetUserResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetUserResult(
            default_project_id=self.default_project_id,
            description=self.description,
            domain_id=self.domain_id,
            enabled=self.enabled,
            idp_id=self.idp_id,
            name=self.name,
            password_expires_at=self.password_expires_at,
            protocol_id=self.protocol_id,
            region=self.region,
            unique_id=self.unique_id,
            id=self.id)

def get_user(domain_id=None,enabled=None,idp_id=None,name=None,password_expires_at=None,protocol_id=None,region=None,unique_id=None,opts=None):
    """
    Use this data source to get the ID of an OpenStack user.
    
    :param str domain_id: The domain this user belongs to.
    :param bool enabled: Whether the user is enabled or disabled. Valid
           values are `true` and `false`.
    :param str idp_id: The identity provider ID of the user.
    :param str name: The name of the user.
    :param str password_expires_at: Query for expired passwords. See the [OpenStack API docs](https://developer.openstack.org/api-ref/identity/v3/#list-users) for more information on the query format.
    :param str protocol_id: The protocol ID of the user.
    :param str unique_id: The unique ID of the user.

    > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/identity_user_v3.html.markdown.
    """
    __args__ = dict()

    __args__['domainId'] = domain_id
    __args__['enabled'] = enabled
    __args__['idpId'] = idp_id
    __args__['name'] = name
    __args__['passwordExpiresAt'] = password_expires_at
    __args__['protocolId'] = protocol_id
    __args__['region'] = region
    __args__['uniqueId'] = unique_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('openstack:identity/getUser:getUser', __args__, opts=opts).value

    return AwaitableGetUserResult(
        default_project_id=__ret__.get('defaultProjectId'),
        description=__ret__.get('description'),
        domain_id=__ret__.get('domainId'),
        enabled=__ret__.get('enabled'),
        idp_id=__ret__.get('idpId'),
        name=__ret__.get('name'),
        password_expires_at=__ret__.get('passwordExpiresAt'),
        protocol_id=__ret__.get('protocolId'),
        region=__ret__.get('region'),
        unique_id=__ret__.get('uniqueId'),
        id=__ret__.get('id'))
