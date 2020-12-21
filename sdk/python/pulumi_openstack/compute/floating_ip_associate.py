# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['FloatingIpAssociate']


class FloatingIpAssociate(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fixed_ip: Optional[pulumi.Input[str]] = None,
                 floating_ip: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 wait_until_associated: Optional[pulumi.Input[bool]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Associate a floating IP to an instance.

        ## Example Usage
        ### Automatically detect the correct network

        ```python
        import pulumi
        import pulumi_openstack as openstack

        instance1 = openstack.compute.Instance("instance1",
            flavor_id="3",
            image_id="ad091b52-742f-469e-8f3c-fd81cadf0743",
            key_pair="my_key_pair_name",
            security_groups=["default"])
        fip1_floating_ip = openstack.networking.FloatingIp("fip1FloatingIp", pool="my_pool")
        fip1_floating_ip_associate = openstack.compute.FloatingIpAssociate("fip1FloatingIpAssociate",
            floating_ip=fip1_floating_ip.address,
            instance_id=instance1.id)
        ```
        ### Explicitly set the network to attach to

        ```python
        import pulumi
        import pulumi_openstack as openstack

        instance1 = openstack.compute.Instance("instance1",
            flavor_id="3",
            image_id="ad091b52-742f-469e-8f3c-fd81cadf0743",
            key_pair="my_key_pair_name",
            networks=[
                openstack.compute.InstanceNetworkArgs(
                    name="my_network",
                ),
                openstack.compute.InstanceNetworkArgs(
                    name="default",
                ),
            ],
            security_groups=["default"])
        fip1_floating_ip = openstack.networking.FloatingIp("fip1FloatingIp", pool="my_pool")
        fip1_floating_ip_associate = openstack.compute.FloatingIpAssociate("fip1FloatingIpAssociate",
            fixed_ip=instance1.networks[1].fixed_ip_v4,
            floating_ip=fip1_floating_ip.address,
            instance_id=instance1.id)
        ```

        ## Import

        This resource can be imported by specifying all three arguments, separated by a forward slash

        ```sh
         $ pulumi import openstack:compute/floatingIpAssociate:FloatingIpAssociate fip_1 <floating_ip>/<instance_id>/<fixed_ip>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] fixed_ip: The specific IP address to direct traffic to.
        :param pulumi.Input[str] floating_ip: The floating IP to associate.
        :param pulumi.Input[str] instance_id: The instance to associte the floating IP with.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Compute client.
               Keypairs are associated with accounts, but a Compute client is needed to
               create one. If omitted, the `region` argument of the provider is used.
               Changing this creates a new floatingip_associate.
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
            if floating_ip is None and not opts.urn:
                raise TypeError("Missing required property 'floating_ip'")
            __props__['floating_ip'] = floating_ip
            if instance_id is None and not opts.urn:
                raise TypeError("Missing required property 'instance_id'")
            __props__['instance_id'] = instance_id
            __props__['region'] = region
            __props__['wait_until_associated'] = wait_until_associated
        super(FloatingIpAssociate, __self__).__init__(
            'openstack:compute/floatingIpAssociate:FloatingIpAssociate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            fixed_ip: Optional[pulumi.Input[str]] = None,
            floating_ip: Optional[pulumi.Input[str]] = None,
            instance_id: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            wait_until_associated: Optional[pulumi.Input[bool]] = None) -> 'FloatingIpAssociate':
        """
        Get an existing FloatingIpAssociate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] fixed_ip: The specific IP address to direct traffic to.
        :param pulumi.Input[str] floating_ip: The floating IP to associate.
        :param pulumi.Input[str] instance_id: The instance to associte the floating IP with.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Compute client.
               Keypairs are associated with accounts, but a Compute client is needed to
               create one. If omitted, the `region` argument of the provider is used.
               Changing this creates a new floatingip_associate.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["fixed_ip"] = fixed_ip
        __props__["floating_ip"] = floating_ip
        __props__["instance_id"] = instance_id
        __props__["region"] = region
        __props__["wait_until_associated"] = wait_until_associated
        return FloatingIpAssociate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="fixedIp")
    def fixed_ip(self) -> pulumi.Output[Optional[str]]:
        """
        The specific IP address to direct traffic to.
        """
        return pulumi.get(self, "fixed_ip")

    @property
    @pulumi.getter(name="floatingIp")
    def floating_ip(self) -> pulumi.Output[str]:
        """
        The floating IP to associate.
        """
        return pulumi.get(self, "floating_ip")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> pulumi.Output[str]:
        """
        The instance to associte the floating IP with.
        """
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V2 Compute client.
        Keypairs are associated with accounts, but a Compute client is needed to
        create one. If omitted, the `region` argument of the provider is used.
        Changing this creates a new floatingip_associate.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="waitUntilAssociated")
    def wait_until_associated(self) -> pulumi.Output[Optional[bool]]:
        return pulumi.get(self, "wait_until_associated")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

