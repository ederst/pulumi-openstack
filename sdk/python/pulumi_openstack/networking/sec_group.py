# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['SecGroup']


class SecGroup(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delete_default_rules: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Create a SecGroup resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] delete_default_rules: Whether or not to delete the default
               egress security rules. This is `false` by default. See the below note
               for more information.
        :param pulumi.Input[str] description: A unique name for the security group.
        :param pulumi.Input[str] name: A unique name for the security group.
        :param pulumi.Input[str] region: The region in which to obtain the V2 networking client.
               A networking client is needed to create a port. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               security group.
        :param pulumi.Input[List[pulumi.Input[str]]] tags: A set of string tags for the security group.
        :param pulumi.Input[str] tenant_id: The owner of the security group. Required if admin
               wants to create a port for another tenant. Changing this creates a new
               security group.
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

            __props__['delete_default_rules'] = delete_default_rules
            __props__['description'] = description
            __props__['name'] = name
            __props__['region'] = region
            __props__['tags'] = tags
            __props__['tenant_id'] = tenant_id
            __props__['all_tags'] = None
        super(SecGroup, __self__).__init__(
            'openstack:networking/secGroup:SecGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            all_tags: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            delete_default_rules: Optional[pulumi.Input[bool]] = None,
            description: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            tags: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            tenant_id: Optional[pulumi.Input[str]] = None) -> 'SecGroup':
        """
        Get an existing SecGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[List[pulumi.Input[str]]] all_tags: The collection of tags assigned on the security group, which have
               been explicitly and implicitly added.
        :param pulumi.Input[bool] delete_default_rules: Whether or not to delete the default
               egress security rules. This is `false` by default. See the below note
               for more information.
        :param pulumi.Input[str] description: A unique name for the security group.
        :param pulumi.Input[str] name: A unique name for the security group.
        :param pulumi.Input[str] region: The region in which to obtain the V2 networking client.
               A networking client is needed to create a port. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               security group.
        :param pulumi.Input[List[pulumi.Input[str]]] tags: A set of string tags for the security group.
        :param pulumi.Input[str] tenant_id: The owner of the security group. Required if admin
               wants to create a port for another tenant. Changing this creates a new
               security group.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["all_tags"] = all_tags
        __props__["delete_default_rules"] = delete_default_rules
        __props__["description"] = description
        __props__["name"] = name
        __props__["region"] = region
        __props__["tags"] = tags
        __props__["tenant_id"] = tenant_id
        return SecGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="allTags")
    def all_tags(self) -> pulumi.Output[List[str]]:
        """
        The collection of tags assigned on the security group, which have
        been explicitly and implicitly added.
        """
        return pulumi.get(self, "all_tags")

    @property
    @pulumi.getter(name="deleteDefaultRules")
    def delete_default_rules(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether or not to delete the default
        egress security rules. This is `false` by default. See the below note
        for more information.
        """
        return pulumi.get(self, "delete_default_rules")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        A unique name for the security group.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A unique name for the security group.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V2 networking client.
        A networking client is needed to create a port. If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        security group.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[List[str]]]:
        """
        A set of string tags for the security group.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        """
        The owner of the security group. Required if admin
        wants to create a port for another tenant. Changing this creates a new
        security group.
        """
        return pulumi.get(self, "tenant_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

