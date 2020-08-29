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

__all__ = ['Trunk']


class Trunk(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admin_state_up: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 sub_ports: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['TrunkSubPortArgs']]]]] = None,
                 tags: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a networking V2 trunk resource within OpenStack.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        network1 = openstack.networking.Network("network1", admin_state_up=True)
        subnet1 = openstack.networking.Subnet("subnet1",
            cidr="192.168.1.0/24",
            enable_dhcp=True,
            ip_version=4,
            network_id=network1.id,
            no_gateway=True)
        parent_port1 = openstack.networking.Port("parentPort1",
            admin_state_up=True,
            network_id=network1.id,
            opts=ResourceOptions(depends_on=["openstack_networking_subnet_v2.subnet_1"]))
        subport1 = openstack.networking.Port("subport1",
            admin_state_up=True,
            network_id=network1.id,
            opts=ResourceOptions(depends_on=["openstack_networking_subnet_v2.subnet_1"]))
        trunk1 = openstack.networking.Trunk("trunk1",
            admin_state_up=True,
            port_id=parent_port1.id,
            sub_ports=[openstack.networking.TrunkSubPortArgs(
                port_id=subport1.id,
                segmentation_id=1,
                segmentation_type="vlan",
            )])
        instance1 = openstack.compute.Instance("instance1",
            networks=[openstack.compute.InstanceNetworkArgs(
                port=trunk1.port_id,
            )],
            security_groups=["default"])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] admin_state_up: Administrative up/down status for the trunk
               (must be "true" or "false" if provided). Changing this updates the
               `admin_state_up` of an existing trunk.
        :param pulumi.Input[str] description: Human-readable description of the trunk. Changing this
               updates the name of the existing trunk.
        :param pulumi.Input[str] name: A unique name for the trunk. Changing this
               updates the `name` of an existing trunk.
        :param pulumi.Input[str] port_id: The ID of the port to be made a subport of the trunk.
        :param pulumi.Input[str] region: The region in which to obtain the V2 networking client.
               A networking client is needed to create a trunk. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               trunk.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['TrunkSubPortArgs']]]] sub_ports: The set of ports that will be made subports of the trunk.
               The structure of each subport is described below.
        :param pulumi.Input[List[pulumi.Input[str]]] tags: A set of string tags for the port.
        :param pulumi.Input[str] tenant_id: The owner of the Trunk. Required if admin wants
               to create a trunk on behalf of another tenant. Changing this creates a new trunk.
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

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            admin_state_up: Optional[pulumi.Input[bool]] = None,
            all_tags: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            port_id: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            sub_ports: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['TrunkSubPortArgs']]]]] = None,
            tags: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            tenant_id: Optional[pulumi.Input[str]] = None) -> 'Trunk':
        """
        Get an existing Trunk resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] admin_state_up: Administrative up/down status for the trunk
               (must be "true" or "false" if provided). Changing this updates the
               `admin_state_up` of an existing trunk.
        :param pulumi.Input[List[pulumi.Input[str]]] all_tags: The collection of tags assigned on the trunk, which have been
               explicitly and implicitly added.
        :param pulumi.Input[str] description: Human-readable description of the trunk. Changing this
               updates the name of the existing trunk.
        :param pulumi.Input[str] name: A unique name for the trunk. Changing this
               updates the `name` of an existing trunk.
        :param pulumi.Input[str] port_id: The ID of the port to be made a subport of the trunk.
        :param pulumi.Input[str] region: The region in which to obtain the V2 networking client.
               A networking client is needed to create a trunk. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               trunk.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['TrunkSubPortArgs']]]] sub_ports: The set of ports that will be made subports of the trunk.
               The structure of each subport is described below.
        :param pulumi.Input[List[pulumi.Input[str]]] tags: A set of string tags for the port.
        :param pulumi.Input[str] tenant_id: The owner of the Trunk. Required if admin wants
               to create a trunk on behalf of another tenant. Changing this creates a new trunk.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["admin_state_up"] = admin_state_up
        __props__["all_tags"] = all_tags
        __props__["description"] = description
        __props__["name"] = name
        __props__["port_id"] = port_id
        __props__["region"] = region
        __props__["sub_ports"] = sub_ports
        __props__["tags"] = tags
        __props__["tenant_id"] = tenant_id
        return Trunk(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="adminStateUp")
    def admin_state_up(self) -> pulumi.Output[Optional[bool]]:
        """
        Administrative up/down status for the trunk
        (must be "true" or "false" if provided). Changing this updates the
        `admin_state_up` of an existing trunk.
        """
        return pulumi.get(self, "admin_state_up")

    @property
    @pulumi.getter(name="allTags")
    def all_tags(self) -> pulumi.Output[List[str]]:
        """
        The collection of tags assigned on the trunk, which have been
        explicitly and implicitly added.
        """
        return pulumi.get(self, "all_tags")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Human-readable description of the trunk. Changing this
        updates the name of the existing trunk.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A unique name for the trunk. Changing this
        updates the `name` of an existing trunk.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="portId")
    def port_id(self) -> pulumi.Output[str]:
        """
        The ID of the port to be made a subport of the trunk.
        """
        return pulumi.get(self, "port_id")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V2 networking client.
        A networking client is needed to create a trunk. If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        trunk.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="subPorts")
    def sub_ports(self) -> pulumi.Output[Optional[List['outputs.TrunkSubPort']]]:
        """
        The set of ports that will be made subports of the trunk.
        The structure of each subport is described below.
        """
        return pulumi.get(self, "sub_ports")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[List[str]]]:
        """
        A set of string tags for the port.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        """
        The owner of the Trunk. Required if admin wants
        to create a trunk on behalf of another tenant. Changing this creates a new trunk.
        """
        return pulumi.get(self, "tenant_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

