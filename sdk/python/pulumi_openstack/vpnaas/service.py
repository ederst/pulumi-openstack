# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['Service']


class Service(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admin_state_up: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 router_id: Optional[pulumi.Input[str]] = None,
                 subnet_id: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 value_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a V2 Neutron VPN service resource within OpenStack.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        service1 = openstack.vpnaas.Service("service1",
            admin_state_up=True,
            router_id="14a75700-fc03-4602-9294-26ee44f366b3")
        ```

        ## Import

        Services can be imported using the `id`, e.g.

        ```sh
         $ pulumi import openstack:vpnaas/service:Service service_1 832cb7f3-59fe-40cf-8f64-8350ffc03272
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] admin_state_up: The administrative state of the resource. Can either be up(true) or down(false).
               Changing this updates the administrative state of the existing service.
        :param pulumi.Input[str] description: The human-readable description for the service.
               Changing this updates the description of the existing service.
        :param pulumi.Input[str] name: The name of the service. Changing this updates the name of
               the existing service.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create a VPN service. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               service.
        :param pulumi.Input[str] router_id: The ID of the router. Changing this creates a new service.
        :param pulumi.Input[str] subnet_id: SubnetID is the ID of the subnet. Default is null.
        :param pulumi.Input[str] tenant_id: The owner of the service. Required if admin wants to
               create a service for another project. Changing this creates a new service.
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

            __props__['admin_state_up'] = admin_state_up
            __props__['description'] = description
            __props__['name'] = name
            __props__['region'] = region
            if router_id is None and not opts.urn:
                raise TypeError("Missing required property 'router_id'")
            __props__['router_id'] = router_id
            __props__['subnet_id'] = subnet_id
            __props__['tenant_id'] = tenant_id
            __props__['value_specs'] = value_specs
            __props__['external_v4_ip'] = None
            __props__['external_v6_ip'] = None
            __props__['status'] = None
        super(Service, __self__).__init__(
            'openstack:vpnaas/service:Service',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            admin_state_up: Optional[pulumi.Input[bool]] = None,
            description: Optional[pulumi.Input[str]] = None,
            external_v4_ip: Optional[pulumi.Input[str]] = None,
            external_v6_ip: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            router_id: Optional[pulumi.Input[str]] = None,
            status: Optional[pulumi.Input[str]] = None,
            subnet_id: Optional[pulumi.Input[str]] = None,
            tenant_id: Optional[pulumi.Input[str]] = None,
            value_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None) -> 'Service':
        """
        Get an existing Service resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] admin_state_up: The administrative state of the resource. Can either be up(true) or down(false).
               Changing this updates the administrative state of the existing service.
        :param pulumi.Input[str] description: The human-readable description for the service.
               Changing this updates the description of the existing service.
        :param pulumi.Input[str] external_v4_ip: The read-only external (public) IPv4 address that is used for the VPN service.
        :param pulumi.Input[str] external_v6_ip: The read-only external (public) IPv6 address that is used for the VPN service.
        :param pulumi.Input[str] name: The name of the service. Changing this updates the name of
               the existing service.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create a VPN service. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               service.
        :param pulumi.Input[str] router_id: The ID of the router. Changing this creates a new service.
        :param pulumi.Input[str] status: Indicates whether IPsec VPN service is currently operational. Values are ACTIVE, DOWN, BUILD, ERROR, PENDING_CREATE, PENDING_UPDATE, or PENDING_DELETE.
        :param pulumi.Input[str] subnet_id: SubnetID is the ID of the subnet. Default is null.
        :param pulumi.Input[str] tenant_id: The owner of the service. Required if admin wants to
               create a service for another project. Changing this creates a new service.
        :param pulumi.Input[Mapping[str, Any]] value_specs: Map of additional options.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["admin_state_up"] = admin_state_up
        __props__["description"] = description
        __props__["external_v4_ip"] = external_v4_ip
        __props__["external_v6_ip"] = external_v6_ip
        __props__["name"] = name
        __props__["region"] = region
        __props__["router_id"] = router_id
        __props__["status"] = status
        __props__["subnet_id"] = subnet_id
        __props__["tenant_id"] = tenant_id
        __props__["value_specs"] = value_specs
        return Service(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="adminStateUp")
    def admin_state_up(self) -> pulumi.Output[Optional[bool]]:
        """
        The administrative state of the resource. Can either be up(true) or down(false).
        Changing this updates the administrative state of the existing service.
        """
        return pulumi.get(self, "admin_state_up")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The human-readable description for the service.
        Changing this updates the description of the existing service.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="externalV4Ip")
    def external_v4_ip(self) -> pulumi.Output[str]:
        """
        The read-only external (public) IPv4 address that is used for the VPN service.
        """
        return pulumi.get(self, "external_v4_ip")

    @property
    @pulumi.getter(name="externalV6Ip")
    def external_v6_ip(self) -> pulumi.Output[str]:
        """
        The read-only external (public) IPv6 address that is used for the VPN service.
        """
        return pulumi.get(self, "external_v6_ip")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the service. Changing this updates the name of
        the existing service.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V2 Networking client.
        A Networking client is needed to create a VPN service. If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        service.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="routerId")
    def router_id(self) -> pulumi.Output[str]:
        """
        The ID of the router. Changing this creates a new service.
        """
        return pulumi.get(self, "router_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Indicates whether IPsec VPN service is currently operational. Values are ACTIVE, DOWN, BUILD, ERROR, PENDING_CREATE, PENDING_UPDATE, or PENDING_DELETE.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> pulumi.Output[Optional[str]]:
        """
        SubnetID is the ID of the subnet. Default is null.
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        """
        The owner of the service. Required if admin wants to
        create a service for another project. Changing this creates a new service.
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

