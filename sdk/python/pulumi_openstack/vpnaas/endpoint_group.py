# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class EndpointGroup(pulumi.CustomResource):
    description: pulumi.Output[str]
    """
    The human-readable description for the group.
    Changing this updates the description of the existing group.
    """
    endpoints: pulumi.Output[list]
    """
    List of endpoints of the same type, for the endpoint group. The values will depend on the type.
    Changing this creates a new group.
    """
    name: pulumi.Output[str]
    """
    The name of the group. Changing this updates the name of
    the existing group.
    """
    region: pulumi.Output[str]
    """
    The region in which to obtain the V2 Networking client.
    A Networking client is needed to create an endpoint group. If omitted, the
    `region` argument of the provider is used. Changing this creates a new
    group.
    """
    tenant_id: pulumi.Output[str]
    """
    The owner of the group. Required if admin wants to
    create an endpoint group for another project. Changing this creates a new group.
    """
    type: pulumi.Output[str]
    """
    The type of the endpoints in the group. A valid value is subnet, cidr, network, router, or vlan.
    Changing this creates a new group.
    """
    value_specs: pulumi.Output[dict]
    """
    Map of additional options.
    """
    def __init__(__self__, resource_name, opts=None, description=None, endpoints=None, name=None, region=None, tenant_id=None, type=None, value_specs=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a V2 Neutron Endpoint Group resource within OpenStack.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        group1 = openstack.vpnaas.EndpointGroup("group1",
            endpoints=[
                "10.2.0.0/24",
                "10.3.0.0/24",
            ],
            type="cidr")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The human-readable description for the group.
               Changing this updates the description of the existing group.
        :param pulumi.Input[list] endpoints: List of endpoints of the same type, for the endpoint group. The values will depend on the type.
               Changing this creates a new group.
        :param pulumi.Input[str] name: The name of the group. Changing this updates the name of
               the existing group.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create an endpoint group. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               group.
        :param pulumi.Input[str] tenant_id: The owner of the group. Required if admin wants to
               create an endpoint group for another project. Changing this creates a new group.
        :param pulumi.Input[str] type: The type of the endpoints in the group. A valid value is subnet, cidr, network, router, or vlan.
               Changing this creates a new group.
        :param pulumi.Input[dict] value_specs: Map of additional options.
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
            __props__['endpoints'] = endpoints
            __props__['name'] = name
            __props__['region'] = region
            __props__['tenant_id'] = tenant_id
            __props__['type'] = type
            __props__['value_specs'] = value_specs
        super(EndpointGroup, __self__).__init__(
            'openstack:vpnaas/endpointGroup:EndpointGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, description=None, endpoints=None, name=None, region=None, tenant_id=None, type=None, value_specs=None):
        """
        Get an existing EndpointGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The human-readable description for the group.
               Changing this updates the description of the existing group.
        :param pulumi.Input[list] endpoints: List of endpoints of the same type, for the endpoint group. The values will depend on the type.
               Changing this creates a new group.
        :param pulumi.Input[str] name: The name of the group. Changing this updates the name of
               the existing group.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create an endpoint group. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               group.
        :param pulumi.Input[str] tenant_id: The owner of the group. Required if admin wants to
               create an endpoint group for another project. Changing this creates a new group.
        :param pulumi.Input[str] type: The type of the endpoints in the group. A valid value is subnet, cidr, network, router, or vlan.
               Changing this creates a new group.
        :param pulumi.Input[dict] value_specs: Map of additional options.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["description"] = description
        __props__["endpoints"] = endpoints
        __props__["name"] = name
        __props__["region"] = region
        __props__["tenant_id"] = tenant_id
        __props__["type"] = type
        __props__["value_specs"] = value_specs
        return EndpointGroup(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
