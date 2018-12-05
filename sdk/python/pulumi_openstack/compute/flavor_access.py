# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from .. import utilities, tables

class FlavorAccess(pulumi.CustomResource):
    """
    Manages a project access for flavor V2 resource within OpenStack.
    
    Note: You _must_ have admin privileges in your OpenStack cloud to use
    this resource.
    
    ---
    """
    def __init__(__self__, __name__, __opts__=None, flavor_id=None, region=None, tenant_id=None):
        """Create a FlavorAccess resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, str):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not flavor_id:
            raise TypeError('Missing required property flavor_id')
        __props__['flavor_id'] = flavor_id

        __props__['region'] = region

        if not tenant_id:
            raise TypeError('Missing required property tenant_id')
        __props__['tenant_id'] = tenant_id

        super(FlavorAccess, __self__).__init__(
            'openstack:compute/flavorAccess:FlavorAccess',
            __name__,
            __props__,
            __opts__)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

