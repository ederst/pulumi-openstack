# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class SecurityService(pulumi.CustomResource):
    """
    Use this resource to configure a security service.
    
    A security service stores configuration information for clients for
    authentication and authorization (AuthN/AuthZ). For example, a share server
    will be the client for an existing service such as LDAP, Kerberos, or
    Microsoft Active Directory.
    
    Minimum supported Manila microversion is 2.7.
    """
    def __init__(__self__, __name__, __opts__=None, description=None, dns_ip=None, domain=None, name=None, ou=None, password=None, region=None, server=None, type=None, user=None):
        """Create a SecurityService resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['description'] = description

        __props__['dns_ip'] = dns_ip

        __props__['domain'] = domain

        __props__['name'] = name

        __props__['ou'] = ou

        __props__['password'] = password

        __props__['region'] = region

        __props__['server'] = server

        if not type:
            raise TypeError('Missing required property type')
        __props__['type'] = type

        __props__['user'] = user

        __props__['project_id'] = None

        super(SecurityService, __self__).__init__(
            'openstack:sharedfilesystem/securityService:SecurityService',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
