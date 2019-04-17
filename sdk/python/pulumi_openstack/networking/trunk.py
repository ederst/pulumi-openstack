# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class Trunk(pulumi.CustomResource):
    admin_state_up: pulumi.Output[bool]
    """
    Administrative up/down status for the trunk
    (must be "true" or "false" if provided). Changing this updates the
    `admin_state_up` of an existing trunk.
    """
    all_tags: pulumi.Output[list]
    """
    The collection of tags assigned on the trunk, which have been
    explicitly and implicitly added.
    """
    description: pulumi.Output[str]
    """
    Human-readable description of the trunk. Changing this
    updates the name of the existing trunk.
    """
    name: pulumi.Output[str]
    """
    A unique name for the trunk. Changing this
    updates the `name` of an existing trunk.
    """
    port_id: pulumi.Output[str]
    """
    The ID of the port to be used as the parent port of the
    trunk. This is the port that should be used as the compute instance network
    port. Changing this creates a new trunk.
    """
    region: pulumi.Output[str]
    """
    The region in which to obtain the V2 networking client.
    A networking client is needed to create a trunk. If omitted, the
    `region` argument of the provider is used. Changing this creates a new
    trunk.
    """
    sub_ports: pulumi.Output[list]
    """
    The set of ports that will be made subports of the trunk.
    The structure of each subport is described below.
    """
    tags: pulumi.Output[list]
    """
    A set of string tags for the port.
    """
    tenant_id: pulumi.Output[str]
    """
    The owner of the Trunk. Required if admin wants
    to create a trunk on behalf of another tenant. Changing this creates a new trunk.
    """
    def __init__(__self__, resource_name, opts=None, admin_state_up=None, description=None, name=None, port_id=None, region=None, sub_ports=None, tags=None, tenant_id=None, __name__=None, __opts__=None):
        """
        Manages a networking V2 trunk resource within OpenStack.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] admin_state_up: Administrative up/down status for the trunk
               (must be "true" or "false" if provided). Changing this updates the
               `admin_state_up` of an existing trunk.
        :param pulumi.Input[str] description: Human-readable description of the trunk. Changing this
               updates the name of the existing trunk.
        :param pulumi.Input[str] name: A unique name for the trunk. Changing this
               updates the `name` of an existing trunk.
        :param pulumi.Input[str] port_id: The ID of the port to be used as the parent port of the
               trunk. This is the port that should be used as the compute instance network
               port. Changing this creates a new trunk.
        :param pulumi.Input[str] region: The region in which to obtain the V2 networking client.
               A networking client is needed to create a trunk. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               trunk.
        :param pulumi.Input[list] sub_ports: The set of ports that will be made subports of the trunk.
               The structure of each subport is described below.
        :param pulumi.Input[list] tags: A set of string tags for the port.
        :param pulumi.Input[str] tenant_id: The owner of the Trunk. Required if admin wants
               to create a trunk on behalf of another tenant. Changing this creates a new trunk.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['admin_state_up'] = admin_state_up

        __props__['description'] = description

        __props__['name'] = name

        if port_id is None:
            raise TypeError("Missing required property 'port_id'")
        __props__['port_id'] = port_id

        __props__['region'] = region

        __props__['sub_ports'] = sub_ports

        __props__['tags'] = tags

        __props__['tenant_id'] = tenant_id

        __props__['all_tags'] = None

        super(Trunk, __self__).__init__(
            'openstack:networking/trunk:Trunk',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

