# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['FloatingIp']


class FloatingIp(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 address: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dns_domain: Optional[pulumi.Input[str]] = None,
                 dns_name: Optional[pulumi.Input[str]] = None,
                 fixed_ip: Optional[pulumi.Input[str]] = None,
                 pool: Optional[pulumi.Input[str]] = None,
                 port_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 value_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
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

        ## Import

        Floating IPs can be imported using the `id`, e.g.

        ```sh
         $ pulumi import openstack:networking/floatingIp:FloatingIp floatip_1 2c7f39f3-702b-48d1-940c-b50384177ee1
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
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A set of string tags for the floating IP.
        :param pulumi.Input[str] tenant_id: The target tenant ID in which to allocate the floating
               IP, if you specify this together with a port_id, make sure the target port
               belongs to the same tenant. Changing this creates a new floating IP (which
               may or may not have a different address)
        :param pulumi.Input[Mapping[str, Any]] value_specs: Map of additional options.
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
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['address'] = address
            __props__['description'] = description
            __props__['dns_domain'] = dns_domain
            __props__['dns_name'] = dns_name
            __props__['fixed_ip'] = fixed_ip
            if pool is None and not opts.urn:
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
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            address: Optional[pulumi.Input[str]] = None,
            all_tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            dns_domain: Optional[pulumi.Input[str]] = None,
            dns_name: Optional[pulumi.Input[str]] = None,
            fixed_ip: Optional[pulumi.Input[str]] = None,
            pool: Optional[pulumi.Input[str]] = None,
            port_id: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            subnet_id: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            tenant_id: Optional[pulumi.Input[str]] = None,
            value_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None) -> 'FloatingIp':
        """
        Get an existing FloatingIp resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] address: The actual/specific floating IP to obtain. By default,
               non-admin users are not able to specify a floating IP, so you must either be
               an admin user or have had a custom policy or role applied to your OpenStack
               user or project.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] all_tags: The collection of tags assigned on the floating IP, which have
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
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A set of string tags for the floating IP.
        :param pulumi.Input[str] tenant_id: The target tenant ID in which to allocate the floating
               IP, if you specify this together with a port_id, make sure the target port
               belongs to the same tenant. Changing this creates a new floating IP (which
               may or may not have a different address)
        :param pulumi.Input[Mapping[str, Any]] value_specs: Map of additional options.
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

    @property
    @pulumi.getter
    def address(self) -> pulumi.Output[str]:
        """
        The actual/specific floating IP to obtain. By default,
        non-admin users are not able to specify a floating IP, so you must either be
        an admin user or have had a custom policy or role applied to your OpenStack
        user or project.
        """
        return pulumi.get(self, "address")

    @property
    @pulumi.getter(name="allTags")
    def all_tags(self) -> pulumi.Output[Sequence[str]]:
        """
        The collection of tags assigned on the floating IP, which have
        been explicitly and implicitly added.
        """
        return pulumi.get(self, "all_tags")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Human-readable description for the floating IP.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="dnsDomain")
    def dns_domain(self) -> pulumi.Output[str]:
        """
        The floating IP DNS domain. Available, when Neutron
        DNS extension is enabled. The data in this attribute will be published in an
        external DNS service when Neutron is configured to integrate with such a
        service. Changing this creates a new floating IP.
        """
        return pulumi.get(self, "dns_domain")

    @property
    @pulumi.getter(name="dnsName")
    def dns_name(self) -> pulumi.Output[str]:
        """
        The floating IP DNS name. Available, when Neutron DNS
        extension is enabled. The data in this attribute will be published in an
        external DNS service when Neutron is configured to integrate with such a
        service. Changing this creates a new floating IP.
        """
        return pulumi.get(self, "dns_name")

    @property
    @pulumi.getter(name="fixedIp")
    def fixed_ip(self) -> pulumi.Output[str]:
        """
        Fixed IP of the port to associate with this floating IP. Required if
        the port has multiple fixed IPs.
        """
        return pulumi.get(self, "fixed_ip")

    @property
    @pulumi.getter
    def pool(self) -> pulumi.Output[str]:
        """
        The name of the pool from which to obtain the floating
        IP. Changing this creates a new floating IP.
        """
        return pulumi.get(self, "pool")

    @property
    @pulumi.getter(name="portId")
    def port_id(self) -> pulumi.Output[str]:
        """
        ID of an existing port with at least one IP address to
        associate with this floating IP.
        """
        return pulumi.get(self, "port_id")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V2 Networking client.
        A Networking client is needed to create a floating IP that can be used with
        another networking resource, such as a load balancer. If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        floating IP (which may or may not have a different address).
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[Optional[str]]:
        """
        The subnet ID of the floating IP pool. Specify this if
        the floating IP network has multiple subnets.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A set of string tags for the floating IP.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        """
        The target tenant ID in which to allocate the floating
        IP, if you specify this together with a port_id, make sure the target port
        belongs to the same tenant. Changing this creates a new floating IP (which
        may or may not have a different address)
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter(name="valueSpecs")
    def value_specs(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        Map of additional options.
        """
        return pulumi.get(self, "value_specs")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

