# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['Network']


class Network(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admin_state_up: Optional[pulumi.Input[bool]] = None,
                 availability_zone_hints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dns_domain: Optional[pulumi.Input[str]] = None,
                 external: Optional[pulumi.Input[bool]] = None,
                 mtu: Optional[pulumi.Input[int]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port_security_enabled: Optional[pulumi.Input[bool]] = None,
                 qos_policy_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 segments: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkSegmentArgs']]]]] = None,
                 shared: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 transparent_vlan: Optional[pulumi.Input[bool]] = None,
                 value_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a V2 Neutron network resource within OpenStack.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        network1 = openstack.networking.Network("network1", admin_state_up=True)
        subnet1 = openstack.networking.Subnet("subnet1",
            cidr="192.168.199.0/24",
            ip_version=4,
            network_id=network1.id)
        secgroup1 = openstack.compute.SecGroup("secgroup1",
            description="a security group",
            rules=[openstack.compute.SecGroupRuleArgs(
                cidr="0.0.0.0/0",
                from_port=22,
                ip_protocol="tcp",
                to_port=22,
            )])
        port1 = openstack.networking.Port("port1",
            admin_state_up=True,
            fixed_ips=[openstack.networking.PortFixedIpArgs(
                ip_address="192.168.199.10",
                subnet_id=subnet1.id,
            )],
            network_id=network1.id,
            security_group_ids=[secgroup1.id])
        instance1 = openstack.compute.Instance("instance1",
            networks=[openstack.compute.InstanceNetworkArgs(
                port=port1.id,
            )],
            security_groups=[secgroup1.name])
        ```

        ## Import

        Networks can be imported using the `id`, e.g.

        ```sh
         $ pulumi import openstack:networking/network:Network network_1 d90ce693-5ccf-4136-a0ed-152ce412b6b9
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] admin_state_up: The administrative state of the network.
               Acceptable values are "true" and "false". Changing this value updates the
               state of the existing network.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] availability_zone_hints: An availability zone is used to make
               network resources highly available. Used for resources with high availability
               so that they are scheduled on different availability zones. Changing this
               creates a new network.
        :param pulumi.Input[str] description: Human-readable description of the network. Changing this
               updates the name of the existing network.
        :param pulumi.Input[str] dns_domain: The network DNS domain. Available, when Neutron DNS
               extension is enabled. The `dns_domain` of a network in conjunction with the
               `dns_name` attribute of its ports will be published in an external DNS
               service when Neutron is configured to integrate with such a service.
        :param pulumi.Input[bool] external: Specifies whether the network resource has the
               external routing facility. Valid values are true and false. Defaults to
               false. Changing this updates the external attribute of the existing network.
        :param pulumi.Input[int] mtu: The network MTU. Available for read-only, when Neutron
               `net-mtu` extension is enabled. Available for the modification, when
               Neutron `net-mtu-writable` extension is enabled.
        :param pulumi.Input[str] name: The name of the network. Changing this updates the name of
               the existing network.
        :param pulumi.Input[bool] port_security_enabled: Whether to explicitly enable or disable
               port security on the network. Port Security is usually enabled by default, so
               omitting this argument will usually result in a value of "true". Setting this
               explicitly to `false` will disable port security. Valid values are `true` and
               `false`.
        :param pulumi.Input[str] qos_policy_id: Reference to the associated QoS policy.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create a Neutron network. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               network.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkSegmentArgs']]]] segments: An array of one or more provider segment objects.
        :param pulumi.Input[bool] shared: Specifies whether the network resource can be accessed
               by any tenant or not. Changing this updates the sharing capabilities of the
               existing network.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A set of string tags for the network.
        :param pulumi.Input[str] tenant_id: The owner of the network. Required if admin wants to
               create a network for another tenant. Changing this creates a new network.
        :param pulumi.Input[bool] transparent_vlan: Specifies whether the network resource has the
               VLAN transparent attribute set. Valid values are true and false. Defaults to
               false. Changing this updates the `transparent_vlan` attribute of the existing
               network.
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
            __props__['availability_zone_hints'] = availability_zone_hints
            __props__['description'] = description
            __props__['dns_domain'] = dns_domain
            __props__['external'] = external
            __props__['mtu'] = mtu
            __props__['name'] = name
            __props__['port_security_enabled'] = port_security_enabled
            __props__['qos_policy_id'] = qos_policy_id
            __props__['region'] = region
            __props__['segments'] = segments
            __props__['shared'] = shared
            __props__['tags'] = tags
            __props__['tenant_id'] = tenant_id
            __props__['transparent_vlan'] = transparent_vlan
            __props__['value_specs'] = value_specs
            __props__['all_tags'] = None
        super(Network, __self__).__init__(
            'openstack:networking/network:Network',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            admin_state_up: Optional[pulumi.Input[bool]] = None,
            all_tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            availability_zone_hints: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            dns_domain: Optional[pulumi.Input[str]] = None,
            external: Optional[pulumi.Input[bool]] = None,
            mtu: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            port_security_enabled: Optional[pulumi.Input[bool]] = None,
            qos_policy_id: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            segments: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkSegmentArgs']]]]] = None,
            shared: Optional[pulumi.Input[bool]] = None,
            tags: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            tenant_id: Optional[pulumi.Input[str]] = None,
            transparent_vlan: Optional[pulumi.Input[bool]] = None,
            value_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None) -> 'Network':
        """
        Get an existing Network resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] admin_state_up: The administrative state of the network.
               Acceptable values are "true" and "false". Changing this value updates the
               state of the existing network.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] all_tags: The collection of tags assigned on the network, which have been
               explicitly and implicitly added.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] availability_zone_hints: An availability zone is used to make
               network resources highly available. Used for resources with high availability
               so that they are scheduled on different availability zones. Changing this
               creates a new network.
        :param pulumi.Input[str] description: Human-readable description of the network. Changing this
               updates the name of the existing network.
        :param pulumi.Input[str] dns_domain: The network DNS domain. Available, when Neutron DNS
               extension is enabled. The `dns_domain` of a network in conjunction with the
               `dns_name` attribute of its ports will be published in an external DNS
               service when Neutron is configured to integrate with such a service.
        :param pulumi.Input[bool] external: Specifies whether the network resource has the
               external routing facility. Valid values are true and false. Defaults to
               false. Changing this updates the external attribute of the existing network.
        :param pulumi.Input[int] mtu: The network MTU. Available for read-only, when Neutron
               `net-mtu` extension is enabled. Available for the modification, when
               Neutron `net-mtu-writable` extension is enabled.
        :param pulumi.Input[str] name: The name of the network. Changing this updates the name of
               the existing network.
        :param pulumi.Input[bool] port_security_enabled: Whether to explicitly enable or disable
               port security on the network. Port Security is usually enabled by default, so
               omitting this argument will usually result in a value of "true". Setting this
               explicitly to `false` will disable port security. Valid values are `true` and
               `false`.
        :param pulumi.Input[str] qos_policy_id: Reference to the associated QoS policy.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create a Neutron network. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               network.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NetworkSegmentArgs']]]] segments: An array of one or more provider segment objects.
        :param pulumi.Input[bool] shared: Specifies whether the network resource can be accessed
               by any tenant or not. Changing this updates the sharing capabilities of the
               existing network.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] tags: A set of string tags for the network.
        :param pulumi.Input[str] tenant_id: The owner of the network. Required if admin wants to
               create a network for another tenant. Changing this creates a new network.
        :param pulumi.Input[bool] transparent_vlan: Specifies whether the network resource has the
               VLAN transparent attribute set. Valid values are true and false. Defaults to
               false. Changing this updates the `transparent_vlan` attribute of the existing
               network.
        :param pulumi.Input[Mapping[str, Any]] value_specs: Map of additional options.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["admin_state_up"] = admin_state_up
        __props__["all_tags"] = all_tags
        __props__["availability_zone_hints"] = availability_zone_hints
        __props__["description"] = description
        __props__["dns_domain"] = dns_domain
        __props__["external"] = external
        __props__["mtu"] = mtu
        __props__["name"] = name
        __props__["port_security_enabled"] = port_security_enabled
        __props__["qos_policy_id"] = qos_policy_id
        __props__["region"] = region
        __props__["segments"] = segments
        __props__["shared"] = shared
        __props__["tags"] = tags
        __props__["tenant_id"] = tenant_id
        __props__["transparent_vlan"] = transparent_vlan
        __props__["value_specs"] = value_specs
        return Network(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="adminStateUp")
    def admin_state_up(self) -> pulumi.Output[bool]:
        """
        The administrative state of the network.
        Acceptable values are "true" and "false". Changing this value updates the
        state of the existing network.
        """
        return pulumi.get(self, "admin_state_up")

    @property
    @pulumi.getter(name="allTags")
    def all_tags(self) -> pulumi.Output[Sequence[str]]:
        """
        The collection of tags assigned on the network, which have been
        explicitly and implicitly added.
        """
        return pulumi.get(self, "all_tags")

    @property
    @pulumi.getter(name="availabilityZoneHints")
    def availability_zone_hints(self) -> pulumi.Output[Sequence[str]]:
        """
        An availability zone is used to make
        network resources highly available. Used for resources with high availability
        so that they are scheduled on different availability zones. Changing this
        creates a new network.
        """
        return pulumi.get(self, "availability_zone_hints")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Human-readable description of the network. Changing this
        updates the name of the existing network.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="dnsDomain")
    def dns_domain(self) -> pulumi.Output[str]:
        """
        The network DNS domain. Available, when Neutron DNS
        extension is enabled. The `dns_domain` of a network in conjunction with the
        `dns_name` attribute of its ports will be published in an external DNS
        service when Neutron is configured to integrate with such a service.
        """
        return pulumi.get(self, "dns_domain")

    @property
    @pulumi.getter
    def external(self) -> pulumi.Output[bool]:
        """
        Specifies whether the network resource has the
        external routing facility. Valid values are true and false. Defaults to
        false. Changing this updates the external attribute of the existing network.
        """
        return pulumi.get(self, "external")

    @property
    @pulumi.getter
    def mtu(self) -> pulumi.Output[int]:
        """
        The network MTU. Available for read-only, when Neutron
        `net-mtu` extension is enabled. Available for the modification, when
        Neutron `net-mtu-writable` extension is enabled.
        """
        return pulumi.get(self, "mtu")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the network. Changing this updates the name of
        the existing network.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="portSecurityEnabled")
    def port_security_enabled(self) -> pulumi.Output[bool]:
        """
        Whether to explicitly enable or disable
        port security on the network. Port Security is usually enabled by default, so
        omitting this argument will usually result in a value of "true". Setting this
        explicitly to `false` will disable port security. Valid values are `true` and
        `false`.
        """
        return pulumi.get(self, "port_security_enabled")

    @property
    @pulumi.getter(name="qosPolicyId")
    def qos_policy_id(self) -> pulumi.Output[str]:
        """
        Reference to the associated QoS policy.
        """
        return pulumi.get(self, "qos_policy_id")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V2 Networking client.
        A Networking client is needed to create a Neutron network. If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        network.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def segments(self) -> pulumi.Output[Optional[Sequence['outputs.NetworkSegment']]]:
        """
        An array of one or more provider segment objects.
        """
        return pulumi.get(self, "segments")

    @property
    @pulumi.getter
    def shared(self) -> pulumi.Output[bool]:
        """
        Specifies whether the network resource can be accessed
        by any tenant or not. Changing this updates the sharing capabilities of the
        existing network.
        """
        return pulumi.get(self, "shared")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A set of string tags for the network.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        """
        The owner of the network. Required if admin wants to
        create a network for another tenant. Changing this creates a new network.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter(name="transparentVlan")
    def transparent_vlan(self) -> pulumi.Output[bool]:
        """
        Specifies whether the network resource has the
        VLAN transparent attribute set. Valid values are true and false. Defaults to
        false. Changing this updates the `transparent_vlan` attribute of the existing
        network.
        """
        return pulumi.get(self, "transparent_vlan")

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

