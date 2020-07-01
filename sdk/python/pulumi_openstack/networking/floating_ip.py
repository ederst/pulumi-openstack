# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables


class FloatingIp(pulumi.CustomResource):
    address: pulumi.Output[str]
    """
    The actual/specific floating IP to obtain. By default,
    non-admin users are not able to specify a floating IP, so you must either be
    an admin user or have had a custom policy or role applied to your OpenStack
    user or project.
    """
    all_tags: pulumi.Output[list]
    """
    The collection of tags assigned on the floating IP, which have
    been explicitly and implicitly added.
    """
    description: pulumi.Output[str]
    """
    Human-readable description for the floating IP.
    """
    dns_domain: pulumi.Output[str]
    """
    The floating IP DNS domain. Available, when Neutron
    DNS extension is enabled. The data in this attribute will be published in an
    external DNS service when Neutron is configured to integrate with such a
    service. Changing this creates a new floating IP.
    """
    dns_name: pulumi.Output[str]
    """
    The floating IP DNS name. Available, when Neutron DNS
    extension is enabled. The data in this attribute will be published in an
    external DNS service when Neutron is configured to integrate with such a
    service. Changing this creates a new floating IP.
    """
    fixed_ip: pulumi.Output[str]
    """
    Fixed IP of the port to associate with this floating IP. Required if
    the port has multiple fixed IPs.
    """
    pool: pulumi.Output[str]
    """
    The name of the pool from which to obtain the floating
    IP. Changing this creates a new floating IP.
    """
    port_id: pulumi.Output[str]
    """
    ID of an existing port with at least one IP address to
    associate with this floating IP.
    """
    region: pulumi.Output[str]
    """
    The region in which to obtain the V2 Networking client.
    A Networking client is needed to create a floating IP that can be used with
    another networking resource, such as a load balancer. If omitted, the
    `region` argument of the provider is used. Changing this creates a new
    floating IP (which may or may not have a different address).
    """
    subnet_id: pulumi.Output[str]
    """
    The subnet ID of the floating IP pool. Specify this if
    the floating IP network has multiple subnets.
    """
    tags: pulumi.Output[list]
    """
    A set of string tags for the floating IP.
    """
    tenant_id: pulumi.Output[str]
    """
    The target tenant ID in which to allocate the floating
    IP, if you specify this together with a port_id, make sure the target port
    belongs to the same tenant. Changing this creates a new floating IP (which
    may or may not have a different address)
    """
    value_specs: pulumi.Output[dict]
    """
    Map of additional options.
    """
    def __init__(__self__, resource_name, opts=None, address=None, description=None, dns_domain=None, dns_name=None, fixed_ip=None, pool=None, port_id=None, region=None, subnet_id=None, tags=None, tenant_id=None, value_specs=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a V2 floating IP resource within OpenStack Neutron (networking)
        that can be used for load balancers.
        These are similar to Nova (compute) floating IP resources,
        but only compute floating IPs can be used with compute instances.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        floatip1 = openstack.networking.FloatingIp("floatip1", pool="public")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address: The actual/specific floating IP to obtain. By default,
               non-admin users are not able to specify a floating IP, so you must either be
               an admin user or have had a custom policy or role applied to your OpenStack
               user or project.
        :param pulumi.Input[str] description: Human-readable description for the floating IP.
        :param pulumi.Input[str] dns_domain: The floating IP DNS domain. Available, when Neutron
               DNS extension is enabled. The data in this attribute will be published in an
               external DNS service when Neutron is configured to integrate with such a
               service. Changing this creates a new floating IP.
        :param pulumi.Input[str] dns_name: The floating IP DNS name. Available, when Neutron DNS
               extension is enabled. The data in this attribute will be published in an
               external DNS service when Neutron is configured to integrate with such a
               service. Changing this creates a new floating IP.
        :param pulumi.Input[str] fixed_ip: Fixed IP of the port to associate with this floating IP. Required if
               the port has multiple fixed IPs.
        :param pulumi.Input[str] pool: The name of the pool from which to obtain the floating
               IP. Changing this creates a new floating IP.
        :param pulumi.Input[str] port_id: ID of an existing port with at least one IP address to
               associate with this floating IP.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create a floating IP that can be used with
               another networking resource, such as a load balancer. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               floating IP (which may or may not have a different address).
        :param pulumi.Input[str] subnet_id: The subnet ID of the floating IP pool. Specify this if
               the floating IP network has multiple subnets.
        :param pulumi.Input[list] tags: A set of string tags for the floating IP.
        :param pulumi.Input[str] tenant_id: The target tenant ID in which to allocate the floating
               IP, if you specify this together with a port_id, make sure the target port
               belongs to the same tenant. Changing this creates a new floating IP (which
               may or may not have a different address)
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

            __props__['address'] = address
            __props__['description'] = description
            __props__['dns_domain'] = dns_domain
            __props__['dns_name'] = dns_name
            __props__['fixed_ip'] = fixed_ip
            if pool is None:
                raise TypeError("Missing required property 'pool'")
            __props__['pool'] = pool
            __props__['port_id'] = port_id
            __props__['region'] = region
            __props__['subnet_id'] = subnet_id
            __props__['tags'] = tags
            __props__['tenant_id'] = tenant_id
            __props__['value_specs'] = value_specs
            __props__['all_tags'] = None
        super(FloatingIp, __self__).__init__(
            'openstack:networking/floatingIp:FloatingIp',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, address=None, all_tags=None, description=None, dns_domain=None, dns_name=None, fixed_ip=None, pool=None, port_id=None, region=None, subnet_id=None, tags=None, tenant_id=None, value_specs=None):
        """
        Get an existing FloatingIp resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address: The actual/specific floating IP to obtain. By default,
               non-admin users are not able to specify a floating IP, so you must either be
               an admin user or have had a custom policy or role applied to your OpenStack
               user or project.
        :param pulumi.Input[list] all_tags: The collection of tags assigned on the floating IP, which have
               been explicitly and implicitly added.
        :param pulumi.Input[str] description: Human-readable description for the floating IP.
        :param pulumi.Input[str] dns_domain: The floating IP DNS domain. Available, when Neutron
               DNS extension is enabled. The data in this attribute will be published in an
               external DNS service when Neutron is configured to integrate with such a
               service. Changing this creates a new floating IP.
        :param pulumi.Input[str] dns_name: The floating IP DNS name. Available, when Neutron DNS
               extension is enabled. The data in this attribute will be published in an
               external DNS service when Neutron is configured to integrate with such a
               service. Changing this creates a new floating IP.
        :param pulumi.Input[str] fixed_ip: Fixed IP of the port to associate with this floating IP. Required if
               the port has multiple fixed IPs.
        :param pulumi.Input[str] pool: The name of the pool from which to obtain the floating
               IP. Changing this creates a new floating IP.
        :param pulumi.Input[str] port_id: ID of an existing port with at least one IP address to
               associate with this floating IP.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create a floating IP that can be used with
               another networking resource, such as a load balancer. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               floating IP (which may or may not have a different address).
        :param pulumi.Input[str] subnet_id: The subnet ID of the floating IP pool. Specify this if
               the floating IP network has multiple subnets.
        :param pulumi.Input[list] tags: A set of string tags for the floating IP.
        :param pulumi.Input[str] tenant_id: The target tenant ID in which to allocate the floating
               IP, if you specify this together with a port_id, make sure the target port
               belongs to the same tenant. Changing this creates a new floating IP (which
               may or may not have a different address)
        :param pulumi.Input[dict] value_specs: Map of additional options.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["address"] = address
        __props__["all_tags"] = all_tags
        __props__["description"] = description
        __props__["dns_domain"] = dns_domain
        __props__["dns_name"] = dns_name
        __props__["fixed_ip"] = fixed_ip
        __props__["pool"] = pool
        __props__["port_id"] = port_id
        __props__["region"] = region
        __props__["subnet_id"] = subnet_id
        __props__["tags"] = tags
        __props__["tenant_id"] = tenant_id
        __props__["value_specs"] = value_specs
        return FloatingIp(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
