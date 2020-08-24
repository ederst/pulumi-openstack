# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['AddressScope']


class AddressScope(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ip_version: Optional[pulumi.Input[float]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 shared: Optional[pulumi.Input[bool]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a V2 Neutron addressscope resource within OpenStack.

        ## Example Usage
        ### Create an Address-scope

        ```python
        import pulumi
        import pulumi_openstack as openstack

        addressscope1 = openstack.networking.AddressScope("addressscope1", ip_version=6)
        ```
        ### Create a Subnet Pool from an Address-scope

        ```python
        import pulumi
        import pulumi_openstack as openstack

        addressscope1 = openstack.networking.AddressScope("addressscope1", ip_version=6)
        subnetpool1 = openstack.networking.SubnetPool("subnetpool1",
            address_scope_id=addressscope1.id,
            prefixes=[
                "fdf7:b13d:dead:beef::/64",
                "fd65:86cc:a334:39b7::/64",
            ])
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] ip_version: IP version, either 4 (default) or 6. Changing this
               creates a new address-scope.
        :param pulumi.Input[str] name: The name of the address-scope. Changing this updates the
               name of the existing address-scope.
        :param pulumi.Input[str] project_id: The owner of the address-scope. Required if admin
               wants to create a address-scope for another project. Changing this creates a
               new address-scope.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create a Neutron address-scope. If omitted,
               the `region` argument of the provider is used. Changing this creates a new
               address-scope.
        :param pulumi.Input[bool] shared: Indicates whether this address-scope is shared across
               all projects. Changing this updates the shared status of the existing
               address-scope.
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

            __props__['ip_version'] = ip_version
            __props__['name'] = name
            __props__['project_id'] = project_id
            __props__['region'] = region
            __props__['shared'] = shared
        super(AddressScope, __self__).__init__(
            'openstack:networking/addressScope:AddressScope',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            ip_version: Optional[pulumi.Input[float]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            shared: Optional[pulumi.Input[bool]] = None) -> 'AddressScope':
        """
        Get an existing AddressScope resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] ip_version: IP version, either 4 (default) or 6. Changing this
               creates a new address-scope.
        :param pulumi.Input[str] name: The name of the address-scope. Changing this updates the
               name of the existing address-scope.
        :param pulumi.Input[str] project_id: The owner of the address-scope. Required if admin
               wants to create a address-scope for another project. Changing this creates a
               new address-scope.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create a Neutron address-scope. If omitted,
               the `region` argument of the provider is used. Changing this creates a new
               address-scope.
        :param pulumi.Input[bool] shared: Indicates whether this address-scope is shared across
               all projects. Changing this updates the shared status of the existing
               address-scope.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["ip_version"] = ip_version
        __props__["name"] = name
        __props__["project_id"] = project_id
        __props__["region"] = region
        __props__["shared"] = shared
        return AddressScope(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="ipVersion")
    def ip_version(self) -> Optional[float]:
        """
        IP version, either 4 (default) or 6. Changing this
        creates a new address-scope.
        """
        return pulumi.get(self, "ip_version")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the address-scope. Changing this updates the
        name of the existing address-scope.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        """
        The owner of the address-scope. Required if admin
        wants to create a address-scope for another project. Changing this creates a
        new address-scope.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        The region in which to obtain the V2 Networking client.
        A Networking client is needed to create a Neutron address-scope. If omitted,
        the `region` argument of the provider is used. Changing this creates a new
        address-scope.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def shared(self) -> bool:
        """
        Indicates whether this address-scope is shared across
        all projects. Changing this updates the shared status of the existing
        address-scope.
        """
        return pulumi.get(self, "shared")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

