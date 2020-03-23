# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class SecurityService(pulumi.CustomResource):
    description: pulumi.Output[str]
    """
    The human-readable description for the security service.
    Changing this updates the description of the existing security service.
    """
    dns_ip: pulumi.Output[str]
    """
    The security service DNS IP address that is used inside the
    tenant network.
    """
    domain: pulumi.Output[str]
    """
    The security service domain.
    """
    name: pulumi.Output[str]
    """
    The name of the security service. Changing this updates the name
    of the existing security service.
    """
    ou: pulumi.Output[str]
    """
    The security service ou. An organizational unit can be added to
    specify where the share ends up. New in Manila microversion 2.44.
    """
    password: pulumi.Output[str]
    """
    The user password, if you specify a user.
    """
    project_id: pulumi.Output[str]
    """
    The owner of the Security Service.
    """
    region: pulumi.Output[str]
    """
    The region in which to obtain the V2 Shared File System client.
    A Shared File System client is needed to create a security service. If omitted, the
    `region` argument of the provider is used. Changing this creates a new
    security service.
    """
    server: pulumi.Output[str]
    """
    The security service host name or IP address.
    """
    type: pulumi.Output[str]
    """
    The security service type - can either be active\_directory,
    kerberos or ldap.  Changing this updates the existing security service.
    """
    user: pulumi.Output[str]
    """
    The security service user or group name that is used by the
    tenant.
    """
    def __init__(__self__, resource_name, opts=None, description=None, dns_ip=None, domain=None, name=None, ou=None, password=None, region=None, server=None, type=None, user=None, __props__=None, __name__=None, __opts__=None):
        """
        Use this resource to configure a security service.

        A security service stores configuration information for clients for
        authentication and authorization (AuthN/AuthZ). For example, a share server
        will be the client for an existing service such as LDAP, Kerberos, or
        Microsoft Active Directory.

        Minimum supported Manila microversion is 2.7.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/sharedfilesystem_securityservice_v2.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The human-readable description for the security service.
               Changing this updates the description of the existing security service.
        :param pulumi.Input[str] dns_ip: The security service DNS IP address that is used inside the
               tenant network.
        :param pulumi.Input[str] domain: The security service domain.
        :param pulumi.Input[str] name: The name of the security service. Changing this updates the name
               of the existing security service.
        :param pulumi.Input[str] ou: The security service ou. An organizational unit can be added to
               specify where the share ends up. New in Manila microversion 2.44.
        :param pulumi.Input[str] password: The user password, if you specify a user.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Shared File System client.
               A Shared File System client is needed to create a security service. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               security service.
        :param pulumi.Input[str] server: The security service host name or IP address.
        :param pulumi.Input[str] type: The security service type - can either be active\_directory,
               kerberos or ldap.  Changing this updates the existing security service.
        :param pulumi.Input[str] user: The security service user or group name that is used by the
               tenant.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['description'] = description
            __props__['dns_ip'] = dns_ip
            __props__['domain'] = domain
            __props__['name'] = name
            __props__['ou'] = ou
            __props__['password'] = password
            __props__['region'] = region
            __props__['server'] = server
            if type is None:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
            __props__['user'] = user
            __props__['project_id'] = None
        super(SecurityService, __self__).__init__(
            'openstack:sharedfilesystem/securityService:SecurityService',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, description=None, dns_ip=None, domain=None, name=None, ou=None, password=None, project_id=None, region=None, server=None, type=None, user=None):
        """
        Get an existing SecurityService resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The human-readable description for the security service.
               Changing this updates the description of the existing security service.
        :param pulumi.Input[str] dns_ip: The security service DNS IP address that is used inside the
               tenant network.
        :param pulumi.Input[str] domain: The security service domain.
        :param pulumi.Input[str] name: The name of the security service. Changing this updates the name
               of the existing security service.
        :param pulumi.Input[str] ou: The security service ou. An organizational unit can be added to
               specify where the share ends up. New in Manila microversion 2.44.
        :param pulumi.Input[str] password: The user password, if you specify a user.
        :param pulumi.Input[str] project_id: The owner of the Security Service.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Shared File System client.
               A Shared File System client is needed to create a security service. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               security service.
        :param pulumi.Input[str] server: The security service host name or IP address.
        :param pulumi.Input[str] type: The security service type - can either be active\_directory,
               kerberos or ldap.  Changing this updates the existing security service.
        :param pulumi.Input[str] user: The security service user or group name that is used by the
               tenant.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["description"] = description
        __props__["dns_ip"] = dns_ip
        __props__["domain"] = domain
        __props__["name"] = name
        __props__["ou"] = ou
        __props__["password"] = password
        __props__["project_id"] = project_id
        __props__["region"] = region
        __props__["server"] = server
        __props__["type"] = type
        __props__["user"] = user
        return SecurityService(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

