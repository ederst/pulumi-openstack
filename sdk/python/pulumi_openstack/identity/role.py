# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['Role']


class Role(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 domain_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a V3 Role resource within OpenStack Keystone.

        Note: You _must_ have admin privileges in your OpenStack cloud to use
        this resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        role1 = openstack.identity.Role("role1")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_id: The domain the role belongs to.
        :param pulumi.Input[str] name: The name of the role.
        :param pulumi.Input[str] region: The region in which to obtain the V3 Keystone client.
               If omitted, the `region` argument of the provider is used. Changing this
               creates a new Role.
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

            __props__['domain_id'] = domain_id
            __props__['name'] = name
            __props__['region'] = region
        super(Role, __self__).__init__(
            'openstack:identity/role:Role',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            domain_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None) -> 'Role':
        """
        Get an existing Role resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] domain_id: The domain the role belongs to.
        :param pulumi.Input[str] name: The name of the role.
        :param pulumi.Input[str] region: The region in which to obtain the V3 Keystone client.
               If omitted, the `region` argument of the provider is used. Changing this
               creates a new Role.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["domain_id"] = domain_id
        __props__["name"] = name
        __props__["region"] = region
        return Role(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> str:
        """
        The domain the role belongs to.
        """
        return pulumi.get(self, "domain_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the role.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        The region in which to obtain the V3 Keystone client.
        If omitted, the `region` argument of the provider is used. Changing this
        creates a new Role.
        """
        return pulumi.get(self, "region")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

