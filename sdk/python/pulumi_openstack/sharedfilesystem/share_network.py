# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['ShareNetwork']


class ShareNetwork(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 neutron_net_id: Optional[pulumi.Input[str]] = None,
                 neutron_subnet_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 security_service_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Use this resource to configure a share network.

        A share network stores network information that share servers can use when
        shares are created.

        ## Example Usage
        ### Basic share network

        ```python
        import pulumi
        import pulumi_openstack as openstack

        network1 = openstack.networking.Network("network1", admin_state_up=True)
        subnet1 = openstack.networking.Subnet("subnet1",
            cidr="192.168.199.0/24",
            ip_version=4,
            network_id=network1.id)
        sharenetwork1 = openstack.sharedfilesystem.ShareNetwork("sharenetwork1",
            description="test share network",
            neutron_net_id=network1.id,
            neutron_subnet_id=subnet1.id)
        ```
        ### Share network with associated security services

        ```python
        import pulumi
        import pulumi_openstack as openstack

        network1 = openstack.networking.Network("network1", admin_state_up=True)
        subnet1 = openstack.networking.Subnet("subnet1",
            cidr="192.168.199.0/24",
            ip_version=4,
            network_id=network1.id)
        securityservice1 = openstack.sharedfilesystem.SecurityService("securityservice1",
            description="created by terraform",
            dns_ip="192.168.199.10",
            domain="example.com",
            ou="CN=Computers,DC=example,DC=com",
            password="s8cret",
            server="192.168.199.10",
            type="active_directory",
            user="joinDomainUser")
        sharenetwork1 = openstack.sharedfilesystem.ShareNetwork("sharenetwork1",
            description="test share network with security services",
            neutron_net_id=network1.id,
            neutron_subnet_id=subnet1.id,
            security_service_ids=[securityservice1.id])
        ```

        ## Import

        This resource can be imported by specifying the ID of the share network

        ```sh
         $ pulumi import openstack:sharedfilesystem/shareNetwork:ShareNetwork sharenetwork_1 <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: The human-readable description for the share network.
               Changing this updates the description of the existing share network.
        :param pulumi.Input[str] name: The name for the share network. Changing this updates the name
               of the existing share network.
        :param pulumi.Input[str] neutron_net_id: The UUID of a neutron network when setting up or updating
               a share network. Changing this updates the existing share network if it's not used by
               shares.
        :param pulumi.Input[str] neutron_subnet_id: The UUID of the neutron subnet when setting up or
               updating a share network. Changing this updates the existing share network if it's
               not used by shares.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Shared File System client.
               A Shared File System client is needed to create a share network. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               share network.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_service_ids: The list of security service IDs to associate with
               the share network. The security service must be specified by ID and not name.
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

            __props__['description'] = description
            __props__['name'] = name
            if neutron_net_id is None and not opts.urn:
                raise TypeError("Missing required property 'neutron_net_id'")
            __props__['neutron_net_id'] = neutron_net_id
            if neutron_subnet_id is None and not opts.urn:
                raise TypeError("Missing required property 'neutron_subnet_id'")
            __props__['neutron_subnet_id'] = neutron_subnet_id
            __props__['region'] = region
            __props__['security_service_ids'] = security_service_ids
            __props__['cidr'] = None
            __props__['ip_version'] = None
            __props__['network_type'] = None
            __props__['project_id'] = None
            __props__['segmentation_id'] = None
        super(ShareNetwork, __self__).__init__(
            'openstack:sharedfilesystem/shareNetwork:ShareNetwork',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cidr: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            ip_version: Optional[pulumi.Input[int]] = None,
            name: Optional[pulumi.Input[str]] = None,
            network_type: Optional[pulumi.Input[str]] = None,
            neutron_net_id: Optional[pulumi.Input[str]] = None,
            neutron_subnet_id: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            security_service_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            segmentation_id: Optional[pulumi.Input[int]] = None) -> 'ShareNetwork':
        """
        Get an existing ShareNetwork resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cidr: The share network CIDR.
        :param pulumi.Input[str] description: The human-readable description for the share network.
               Changing this updates the description of the existing share network.
        :param pulumi.Input[int] ip_version: The IP version of the share network. Can either be 4 or 6.
        :param pulumi.Input[str] name: The name for the share network. Changing this updates the name
               of the existing share network.
        :param pulumi.Input[str] network_type: The share network type. Can either be VLAN, VXLAN, GRE, or flat.
        :param pulumi.Input[str] neutron_net_id: The UUID of a neutron network when setting up or updating
               a share network. Changing this updates the existing share network if it's not used by
               shares.
        :param pulumi.Input[str] neutron_subnet_id: The UUID of the neutron subnet when setting up or
               updating a share network. Changing this updates the existing share network if it's
               not used by shares.
        :param pulumi.Input[str] project_id: The owner of the Share Network.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Shared File System client.
               A Shared File System client is needed to create a share network. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               share network.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] security_service_ids: The list of security service IDs to associate with
               the share network. The security service must be specified by ID and not name.
        :param pulumi.Input[int] segmentation_id: The share network segmentation ID.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["cidr"] = cidr
        __props__["description"] = description
        __props__["ip_version"] = ip_version
        __props__["name"] = name
        __props__["network_type"] = network_type
        __props__["neutron_net_id"] = neutron_net_id
        __props__["neutron_subnet_id"] = neutron_subnet_id
        __props__["project_id"] = project_id
        __props__["region"] = region
        __props__["security_service_ids"] = security_service_ids
        __props__["segmentation_id"] = segmentation_id
        return ShareNetwork(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def cidr(self) -> pulumi.Output[str]:
        """
        The share network CIDR.
        """
        return pulumi.get(self, "cidr")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The human-readable description for the share network.
        Changing this updates the description of the existing share network.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="ipVersion")
    def ip_version(self) -> pulumi.Output[int]:
        """
        The IP version of the share network. Can either be 4 or 6.
        """
        return pulumi.get(self, "ip_version")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name for the share network. Changing this updates the name
        of the existing share network.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkType")
    def network_type(self) -> pulumi.Output[str]:
        """
        The share network type. Can either be VLAN, VXLAN, GRE, or flat.
        """
        return pulumi.get(self, "network_type")

    @property
    @pulumi.getter(name="neutronNetId")
    def neutron_net_id(self) -> pulumi.Output[str]:
        """
        The UUID of a neutron network when setting up or updating
        a share network. Changing this updates the existing share network if it's not used by
        shares.
        """
        return pulumi.get(self, "neutron_net_id")

    @property
    @pulumi.getter(name="neutronSubnetId")
    def neutron_subnet_id(self) -> pulumi.Output[str]:
        """
        The UUID of the neutron subnet when setting up or
        updating a share network. Changing this updates the existing share network if it's
        not used by shares.
        """
        return pulumi.get(self, "neutron_subnet_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The owner of the Share Network.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V2 Shared File System client.
        A Shared File System client is needed to create a share network. If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        share network.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="securityServiceIds")
    def security_service_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The list of security service IDs to associate with
        the share network. The security service must be specified by ID and not name.
        """
        return pulumi.get(self, "security_service_ids")

    @property
    @pulumi.getter(name="segmentationId")
    def segmentation_id(self) -> pulumi.Output[int]:
        """
        The share network segmentation ID.
        """
        return pulumi.get(self, "segmentation_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

