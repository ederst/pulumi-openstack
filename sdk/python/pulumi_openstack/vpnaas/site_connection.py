# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['SiteConnection']


class SiteConnection(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admin_state_up: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 dpds: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['SiteConnectionDpdArgs']]]]] = None,
                 ikepolicy_id: Optional[pulumi.Input[str]] = None,
                 initiator: Optional[pulumi.Input[str]] = None,
                 ipsecpolicy_id: Optional[pulumi.Input[str]] = None,
                 local_ep_group_id: Optional[pulumi.Input[str]] = None,
                 local_id: Optional[pulumi.Input[str]] = None,
                 mtu: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 peer_address: Optional[pulumi.Input[str]] = None,
                 peer_cidrs: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 peer_ep_group_id: Optional[pulumi.Input[str]] = None,
                 peer_id: Optional[pulumi.Input[str]] = None,
                 psk: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 value_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 vpnservice_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a V2 Neutron IPSec site connection resource within OpenStack.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        conn1 = openstack.vpnaas.SiteConnection("conn1",
            ikepolicy_id=openstack_vpnaas_ike_policy_v2["policy_2"]["id"],
            ipsecpolicy_id=openstack_vpnaas_ipsec_policy_v2["policy_1"]["id"],
            local_ep_group_id=openstack_vpnaas_endpoint_group_v2["group_2"]["id"],
            peer_address="192.168.10.1",
            peer_ep_group_id=openstack_vpnaas_endpoint_group_v2["group_1"]["id"],
            psk="secret",
            vpnservice_id=openstack_vpnaas_service_v2["service_1"]["id"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] admin_state_up: The administrative state of the resource. Can either be up(true) or down(false).
               Changing this updates the administrative state of the existing connection.
        :param pulumi.Input[str] description: The human-readable description for the connection.
               Changing this updates the description of the existing connection.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['SiteConnectionDpdArgs']]]] dpds: A dictionary with dead peer detection (DPD) protocol controls.
        :param pulumi.Input[str] ikepolicy_id: The ID of the IKE policy. Changing this creates a new connection.
        :param pulumi.Input[str] initiator: A valid value is response-only or bi-directional. Default is bi-directional.
        :param pulumi.Input[str] ipsecpolicy_id: The ID of the IPsec policy. Changing this creates a new connection.
        :param pulumi.Input[str] local_ep_group_id: The ID for the endpoint group that contains private subnets for the local side of the connection.
               You must specify this parameter with the peer_ep_group_id parameter unless
               in backward- compatible mode where peer_cidrs is provided with a subnet_id for the VPN service.
               Changing this updates the existing connection.
        :param pulumi.Input[str] local_id: An ID to be used instead of the external IP address for a virtual router used in traffic between instances on different networks in east-west traffic.
               Most often, local ID would be domain name, email address, etc.
               If this is not configured then the external IP address will be used as the ID.
        :param pulumi.Input[float] mtu: The maximum transmission unit (MTU) value to address fragmentation.
               Minimum value is 68 for IPv4, and 1280 for IPv6.
        :param pulumi.Input[str] name: The name of the connection. Changing this updates the name of
               the existing connection.
        :param pulumi.Input[str] peer_address: The peer gateway public IPv4 or IPv6 address or FQDN.
        :param pulumi.Input[List[pulumi.Input[str]]] peer_cidrs: Unique list of valid peer private CIDRs in the form < net_address > / < prefix > .
        :param pulumi.Input[str] peer_ep_group_id: The ID for the endpoint group that contains private CIDRs in the form < net_address > / < prefix > for the peer side of the connection.
               You must specify this parameter with the local_ep_group_id parameter unless in backward-compatible mode
               where peer_cidrs is provided with a subnet_id for the VPN service.
        :param pulumi.Input[str] peer_id: The peer router identity for authentication. A valid value is an IPv4 address, IPv6 address, e-mail address, key ID, or FQDN.
               Typically, this value matches the peer_address value.
               Changing this updates the existing policy.
        :param pulumi.Input[str] psk: The pre-shared key. A valid value is any string.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create an IPSec site connection. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               site connection.
        :param pulumi.Input[str] tenant_id: The owner of the connection. Required if admin wants to
               create a connection for another project. Changing this creates a new connection.
        :param pulumi.Input[Mapping[str, Any]] value_specs: Map of additional options.
        :param pulumi.Input[str] vpnservice_id: The ID of the VPN service. Changing this creates a new connection.
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
            __props__['dpds'] = dpds
            if ikepolicy_id is None:
                raise TypeError("Missing required property 'ikepolicy_id'")
            __props__['ikepolicy_id'] = ikepolicy_id
            __props__['initiator'] = initiator
            if ipsecpolicy_id is None:
                raise TypeError("Missing required property 'ipsecpolicy_id'")
            __props__['ipsecpolicy_id'] = ipsecpolicy_id
            __props__['local_ep_group_id'] = local_ep_group_id
            __props__['local_id'] = local_id
            __props__['mtu'] = mtu
            __props__['name'] = name
            if peer_address is None:
                raise TypeError("Missing required property 'peer_address'")
            __props__['peer_address'] = peer_address
            __props__['peer_cidrs'] = peer_cidrs
            __props__['peer_ep_group_id'] = peer_ep_group_id
            if peer_id is None:
                raise TypeError("Missing required property 'peer_id'")
            __props__['peer_id'] = peer_id
            if psk is None:
                raise TypeError("Missing required property 'psk'")
            __props__['psk'] = psk
            __props__['region'] = region
            __props__['tenant_id'] = tenant_id
            __props__['value_specs'] = value_specs
            if vpnservice_id is None:
                raise TypeError("Missing required property 'vpnservice_id'")
            __props__['vpnservice_id'] = vpnservice_id
        super(SiteConnection, __self__).__init__(
            'openstack:vpnaas/siteConnection:SiteConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            admin_state_up: Optional[pulumi.Input[bool]] = None,
            description: Optional[pulumi.Input[str]] = None,
            dpds: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['SiteConnectionDpdArgs']]]]] = None,
            ikepolicy_id: Optional[pulumi.Input[str]] = None,
            initiator: Optional[pulumi.Input[str]] = None,
            ipsecpolicy_id: Optional[pulumi.Input[str]] = None,
            local_ep_group_id: Optional[pulumi.Input[str]] = None,
            local_id: Optional[pulumi.Input[str]] = None,
            mtu: Optional[pulumi.Input[float]] = None,
            name: Optional[pulumi.Input[str]] = None,
            peer_address: Optional[pulumi.Input[str]] = None,
            peer_cidrs: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            peer_ep_group_id: Optional[pulumi.Input[str]] = None,
            peer_id: Optional[pulumi.Input[str]] = None,
            psk: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            tenant_id: Optional[pulumi.Input[str]] = None,
            value_specs: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            vpnservice_id: Optional[pulumi.Input[str]] = None) -> 'SiteConnection':
        """
        Get an existing SiteConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] admin_state_up: The administrative state of the resource. Can either be up(true) or down(false).
               Changing this updates the administrative state of the existing connection.
        :param pulumi.Input[str] description: The human-readable description for the connection.
               Changing this updates the description of the existing connection.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['SiteConnectionDpdArgs']]]] dpds: A dictionary with dead peer detection (DPD) protocol controls.
        :param pulumi.Input[str] ikepolicy_id: The ID of the IKE policy. Changing this creates a new connection.
        :param pulumi.Input[str] initiator: A valid value is response-only or bi-directional. Default is bi-directional.
        :param pulumi.Input[str] ipsecpolicy_id: The ID of the IPsec policy. Changing this creates a new connection.
        :param pulumi.Input[str] local_ep_group_id: The ID for the endpoint group that contains private subnets for the local side of the connection.
               You must specify this parameter with the peer_ep_group_id parameter unless
               in backward- compatible mode where peer_cidrs is provided with a subnet_id for the VPN service.
               Changing this updates the existing connection.
        :param pulumi.Input[str] local_id: An ID to be used instead of the external IP address for a virtual router used in traffic between instances on different networks in east-west traffic.
               Most often, local ID would be domain name, email address, etc.
               If this is not configured then the external IP address will be used as the ID.
        :param pulumi.Input[float] mtu: The maximum transmission unit (MTU) value to address fragmentation.
               Minimum value is 68 for IPv4, and 1280 for IPv6.
        :param pulumi.Input[str] name: The name of the connection. Changing this updates the name of
               the existing connection.
        :param pulumi.Input[str] peer_address: The peer gateway public IPv4 or IPv6 address or FQDN.
        :param pulumi.Input[List[pulumi.Input[str]]] peer_cidrs: Unique list of valid peer private CIDRs in the form < net_address > / < prefix > .
        :param pulumi.Input[str] peer_ep_group_id: The ID for the endpoint group that contains private CIDRs in the form < net_address > / < prefix > for the peer side of the connection.
               You must specify this parameter with the local_ep_group_id parameter unless in backward-compatible mode
               where peer_cidrs is provided with a subnet_id for the VPN service.
        :param pulumi.Input[str] peer_id: The peer router identity for authentication. A valid value is an IPv4 address, IPv6 address, e-mail address, key ID, or FQDN.
               Typically, this value matches the peer_address value.
               Changing this updates the existing policy.
        :param pulumi.Input[str] psk: The pre-shared key. A valid value is any string.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create an IPSec site connection. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               site connection.
        :param pulumi.Input[str] tenant_id: The owner of the connection. Required if admin wants to
               create a connection for another project. Changing this creates a new connection.
        :param pulumi.Input[Mapping[str, Any]] value_specs: Map of additional options.
        :param pulumi.Input[str] vpnservice_id: The ID of the VPN service. Changing this creates a new connection.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["admin_state_up"] = admin_state_up
        __props__["description"] = description
        __props__["dpds"] = dpds
        __props__["ikepolicy_id"] = ikepolicy_id
        __props__["initiator"] = initiator
        __props__["ipsecpolicy_id"] = ipsecpolicy_id
        __props__["local_ep_group_id"] = local_ep_group_id
        __props__["local_id"] = local_id
        __props__["mtu"] = mtu
        __props__["name"] = name
        __props__["peer_address"] = peer_address
        __props__["peer_cidrs"] = peer_cidrs
        __props__["peer_ep_group_id"] = peer_ep_group_id
        __props__["peer_id"] = peer_id
        __props__["psk"] = psk
        __props__["region"] = region
        __props__["tenant_id"] = tenant_id
        __props__["value_specs"] = value_specs
        __props__["vpnservice_id"] = vpnservice_id
        return SiteConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="adminStateUp")
    def admin_state_up(self) -> Optional[bool]:
        """
        The administrative state of the resource. Can either be up(true) or down(false).
        Changing this updates the administrative state of the existing connection.
        """
        return pulumi.get(self, "admin_state_up")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The human-readable description for the connection.
        Changing this updates the description of the existing connection.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def dpds(self) -> List['outputs.SiteConnectionDpd']:
        """
        A dictionary with dead peer detection (DPD) protocol controls.
        """
        return pulumi.get(self, "dpds")

    @property
    @pulumi.getter(name="ikepolicyId")
    def ikepolicy_id(self) -> str:
        """
        The ID of the IKE policy. Changing this creates a new connection.
        """
        return pulumi.get(self, "ikepolicy_id")

    @property
    @pulumi.getter
    def initiator(self) -> str:
        """
        A valid value is response-only or bi-directional. Default is bi-directional.
        """
        return pulumi.get(self, "initiator")

    @property
    @pulumi.getter(name="ipsecpolicyId")
    def ipsecpolicy_id(self) -> str:
        """
        The ID of the IPsec policy. Changing this creates a new connection.
        """
        return pulumi.get(self, "ipsecpolicy_id")

    @property
    @pulumi.getter(name="localEpGroupId")
    def local_ep_group_id(self) -> Optional[str]:
        """
        The ID for the endpoint group that contains private subnets for the local side of the connection.
        You must specify this parameter with the peer_ep_group_id parameter unless
        in backward- compatible mode where peer_cidrs is provided with a subnet_id for the VPN service.
        Changing this updates the existing connection.
        """
        return pulumi.get(self, "local_ep_group_id")

    @property
    @pulumi.getter(name="localId")
    def local_id(self) -> Optional[str]:
        """
        An ID to be used instead of the external IP address for a virtual router used in traffic between instances on different networks in east-west traffic.
        Most often, local ID would be domain name, email address, etc.
        If this is not configured then the external IP address will be used as the ID.
        """
        return pulumi.get(self, "local_id")

    @property
    @pulumi.getter
    def mtu(self) -> float:
        """
        The maximum transmission unit (MTU) value to address fragmentation.
        Minimum value is 68 for IPv4, and 1280 for IPv6.
        """
        return pulumi.get(self, "mtu")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the connection. Changing this updates the name of
        the existing connection.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="peerAddress")
    def peer_address(self) -> str:
        """
        The peer gateway public IPv4 or IPv6 address or FQDN.
        """
        return pulumi.get(self, "peer_address")

    @property
    @pulumi.getter(name="peerCidrs")
    def peer_cidrs(self) -> Optional[List[str]]:
        """
        Unique list of valid peer private CIDRs in the form < net_address > / < prefix > .
        """
        return pulumi.get(self, "peer_cidrs")

    @property
    @pulumi.getter(name="peerEpGroupId")
    def peer_ep_group_id(self) -> Optional[str]:
        """
        The ID for the endpoint group that contains private CIDRs in the form < net_address > / < prefix > for the peer side of the connection.
        You must specify this parameter with the local_ep_group_id parameter unless in backward-compatible mode
        where peer_cidrs is provided with a subnet_id for the VPN service.
        """
        return pulumi.get(self, "peer_ep_group_id")

    @property
    @pulumi.getter(name="peerId")
    def peer_id(self) -> str:
        """
        The peer router identity for authentication. A valid value is an IPv4 address, IPv6 address, e-mail address, key ID, or FQDN.
        Typically, this value matches the peer_address value.
        Changing this updates the existing policy.
        """
        return pulumi.get(self, "peer_id")

    @property
    @pulumi.getter
    def psk(self) -> str:
        """
        The pre-shared key. A valid value is any string.
        """
        return pulumi.get(self, "psk")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        The region in which to obtain the V2 Networking client.
        A Networking client is needed to create an IPSec site connection. If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        site connection.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The owner of the connection. Required if admin wants to
        create a connection for another project. Changing this creates a new connection.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter(name="valueSpecs")
    def value_specs(self) -> Optional[Mapping[str, Any]]:
        """
        Map of additional options.
        """
        return pulumi.get(self, "value_specs")

    @property
    @pulumi.getter(name="vpnserviceId")
    def vpnservice_id(self) -> str:
        """
        The ID of the VPN service. Changing this creates a new connection.
        """
        return pulumi.get(self, "vpnservice_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

