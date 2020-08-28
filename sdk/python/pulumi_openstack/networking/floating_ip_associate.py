# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['FloatingIpAssociate']


class FloatingIpAssociate(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fixed_ip: Optional[pulumi.Input[str]] = None,
                 floating_ip: Optional[pulumi.Input[str]] = None,
                 port_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Associates a floating IP to a port. This is useful for situations
        where you have a pre-allocated floating IP or are unable to use the
        `networking.FloatingIp` resource to create a floating IP.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        port1 = openstack.networking.Port("port1", network_id="a5bbd213-e1d3-49b6-aed1-9df60ea94b9a")
        fip1 = openstack.networking.FloatingIpAssociate("fip1",
            floating_ip="1.2.3.4",
            port_id=port1.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] floating_ip: IP Address of an existing floating IP.
        :param pulumi.Input[str] port_id: ID of an existing port with at least one IP address to
               associate with this floating IP.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create a floating IP that can be used with
               another networking resource, such as a load balancer. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               floating IP (which may or may not have a different address).
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

            __props__['fixed_ip'] = fixed_ip
            if floating_ip is None:
                raise TypeError("Missing required property 'floating_ip'")
            __props__['floating_ip'] = floating_ip
            if port_id is None:
                raise TypeError("Missing required property 'port_id'")
            __props__['port_id'] = port_id
            __props__['region'] = region
        super(FloatingIpAssociate, __self__).__init__(
            'openstack:networking/floatingIpAssociate:FloatingIpAssociate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            fixed_ip: Optional[pulumi.Input[str]] = None,
            floating_ip: Optional[pulumi.Input[str]] = None,
            port_id: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None) -> 'FloatingIpAssociate':
        """
        Get an existing FloatingIpAssociate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] floating_ip: IP Address of an existing floating IP.
        :param pulumi.Input[str] port_id: ID of an existing port with at least one IP address to
               associate with this floating IP.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create a floating IP that can be used with
               another networking resource, such as a load balancer. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               floating IP (which may or may not have a different address).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["fixed_ip"] = fixed_ip
        __props__["floating_ip"] = floating_ip
        __props__["port_id"] = port_id
        __props__["region"] = region
        return FloatingIpAssociate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="fixedIp")
    def fixed_ip(self) -> pulumi.Output[str]:
        return pulumi.get(self, "fixed_ip")

    @property
    @pulumi.getter(name="floatingIp")
    def floating_ip(self) -> pulumi.Output[str]:
        """
        IP Address of an existing floating IP.
        """
        return pulumi.get(self, "floating_ip")

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

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

