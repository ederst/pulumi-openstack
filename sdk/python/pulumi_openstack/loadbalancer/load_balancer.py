# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class LoadBalancer(pulumi.CustomResource):
    admin_state_up: pulumi.Output[bool]
    """
    The administrative state of the Loadbalancer.
    A valid value is true (UP) or false (DOWN).
    """
    description: pulumi.Output[str]
    """
    Human-readable description for the Loadbalancer.
    """
    flavor_id: pulumi.Output[str]
    """
    The UUID of a flavor. Changing this creates a new
    loadbalancer.
    """
    loadbalancer_provider: pulumi.Output[str]
    """
    The name of the provider. Changing this
    creates a new loadbalancer.
    """
    name: pulumi.Output[str]
    """
    Human-readable name for the Loadbalancer. Does not have
    to be unique.
    """
    region: pulumi.Output[str]
    """
    The region in which to obtain the V2 Networking client.
    A Networking client is needed to create an LB member. If omitted, the
    `region` argument of the provider is used. Changing this creates a new
    LB member.
    """
    security_group_ids: pulumi.Output[list]
    """
    A list of security group IDs to apply to the
    loadbalancer. The security groups must be specified by ID and not name (as
    opposed to how they are configured with the Compute Instance).
    """
    tenant_id: pulumi.Output[str]
    """
    Required for admins. The UUID of the tenant who owns
    the Loadbalancer.  Only administrative users can specify a tenant UUID
    other than their own.  Changing this creates a new loadbalancer.
    """
    vip_address: pulumi.Output[str]
    """
    The ip address of the load balancer.
    Changing this creates a new loadbalancer.
    """
    vip_port_id: pulumi.Output[str]
    """
    The Port ID of the Load Balancer IP.
    """
    vip_subnet_id: pulumi.Output[str]
    """
    The network on which to allocate the
    Loadbalancer's address. A tenant can only create Loadbalancers on networks
    authorized by policy (e.g. networks that belong to them or networks that
    are shared).  Changing this creates a new loadbalancer.
    """
    def __init__(__self__, resource_name, opts=None, admin_state_up=None, description=None, flavor_id=None, loadbalancer_provider=None, name=None, region=None, security_group_ids=None, tenant_id=None, vip_address=None, vip_subnet_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a V2 loadbalancer resource within OpenStack.

        ## Example Usage



        ```python
        import pulumi
        import pulumi_openstack as openstack

        lb1 = openstack.loadbalancer.LoadBalancer("lb1", vip_subnet_id="d9415786-5f1a-428b-b35f-2f1523e146d2")
        ```


        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] admin_state_up: The administrative state of the Loadbalancer.
               A valid value is true (UP) or false (DOWN).
        :param pulumi.Input[str] description: Human-readable description for the Loadbalancer.
        :param pulumi.Input[str] flavor_id: The UUID of a flavor. Changing this creates a new
               loadbalancer.
        :param pulumi.Input[str] loadbalancer_provider: The name of the provider. Changing this
               creates a new loadbalancer.
        :param pulumi.Input[str] name: Human-readable name for the Loadbalancer. Does not have
               to be unique.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create an LB member. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               LB member.
        :param pulumi.Input[list] security_group_ids: A list of security group IDs to apply to the
               loadbalancer. The security groups must be specified by ID and not name (as
               opposed to how they are configured with the Compute Instance).
        :param pulumi.Input[str] tenant_id: Required for admins. The UUID of the tenant who owns
               the Loadbalancer.  Only administrative users can specify a tenant UUID
               other than their own.  Changing this creates a new loadbalancer.
        :param pulumi.Input[str] vip_address: The ip address of the load balancer.
               Changing this creates a new loadbalancer.
        :param pulumi.Input[str] vip_subnet_id: The network on which to allocate the
               Loadbalancer's address. A tenant can only create Loadbalancers on networks
               authorized by policy (e.g. networks that belong to them or networks that
               are shared).  Changing this creates a new loadbalancer.
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

            __props__['admin_state_up'] = admin_state_up
            __props__['description'] = description
            __props__['flavor_id'] = flavor_id
            __props__['loadbalancer_provider'] = loadbalancer_provider
            __props__['name'] = name
            __props__['region'] = region
            __props__['security_group_ids'] = security_group_ids
            __props__['tenant_id'] = tenant_id
            __props__['vip_address'] = vip_address
            if vip_subnet_id is None:
                raise TypeError("Missing required property 'vip_subnet_id'")
            __props__['vip_subnet_id'] = vip_subnet_id
            __props__['vip_port_id'] = None
        super(LoadBalancer, __self__).__init__(
            'openstack:loadbalancer/loadBalancer:LoadBalancer',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, admin_state_up=None, description=None, flavor_id=None, loadbalancer_provider=None, name=None, region=None, security_group_ids=None, tenant_id=None, vip_address=None, vip_port_id=None, vip_subnet_id=None):
        """
        Get an existing LoadBalancer resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] admin_state_up: The administrative state of the Loadbalancer.
               A valid value is true (UP) or false (DOWN).
        :param pulumi.Input[str] description: Human-readable description for the Loadbalancer.
        :param pulumi.Input[str] flavor_id: The UUID of a flavor. Changing this creates a new
               loadbalancer.
        :param pulumi.Input[str] loadbalancer_provider: The name of the provider. Changing this
               creates a new loadbalancer.
        :param pulumi.Input[str] name: Human-readable name for the Loadbalancer. Does not have
               to be unique.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create an LB member. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               LB member.
        :param pulumi.Input[list] security_group_ids: A list of security group IDs to apply to the
               loadbalancer. The security groups must be specified by ID and not name (as
               opposed to how they are configured with the Compute Instance).
        :param pulumi.Input[str] tenant_id: Required for admins. The UUID of the tenant who owns
               the Loadbalancer.  Only administrative users can specify a tenant UUID
               other than their own.  Changing this creates a new loadbalancer.
        :param pulumi.Input[str] vip_address: The ip address of the load balancer.
               Changing this creates a new loadbalancer.
        :param pulumi.Input[str] vip_port_id: The Port ID of the Load Balancer IP.
        :param pulumi.Input[str] vip_subnet_id: The network on which to allocate the
               Loadbalancer's address. A tenant can only create Loadbalancers on networks
               authorized by policy (e.g. networks that belong to them or networks that
               are shared).  Changing this creates a new loadbalancer.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["admin_state_up"] = admin_state_up
        __props__["description"] = description
        __props__["flavor_id"] = flavor_id
        __props__["loadbalancer_provider"] = loadbalancer_provider
        __props__["name"] = name
        __props__["region"] = region
        __props__["security_group_ids"] = security_group_ids
        __props__["tenant_id"] = tenant_id
        __props__["vip_address"] = vip_address
        __props__["vip_port_id"] = vip_port_id
        __props__["vip_subnet_id"] = vip_subnet_id
        return LoadBalancer(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

