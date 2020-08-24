# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['User']


class User(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 databases: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
                 host: Optional[pulumi.Input[str]] = None,
                 instance_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a V1 DB user resource within OpenStack.

        ## Example Usage

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[List[pulumi.Input[str]]] databases: A list of database user should have access to.
        :param pulumi.Input[str] name: A unique name for the resource.
        :param pulumi.Input[str] password: User's password.
        :param pulumi.Input[str] region: Openstack region resource is created in.
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

            __props__['databases'] = databases
            __props__['host'] = host
            if instance_id is None:
                raise TypeError("Missing required property 'instance_id'")
            __props__['instance_id'] = instance_id
            __props__['name'] = name
            if password is None:
                raise TypeError("Missing required property 'password'")
            __props__['password'] = password
            __props__['region'] = region
        super(User, __self__).__init__(
            'openstack:database/user:User',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            databases: Optional[pulumi.Input[List[pulumi.Input[str]]]] = None,
            host: Optional[pulumi.Input[str]] = None,
            instance_id: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            password: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None) -> 'User':
        """
        Get an existing User resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[List[pulumi.Input[str]]] databases: A list of database user should have access to.
        :param pulumi.Input[str] name: A unique name for the resource.
        :param pulumi.Input[str] password: User's password.
        :param pulumi.Input[str] region: Openstack region resource is created in.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["databases"] = databases
        __props__["host"] = host
        __props__["instance_id"] = instance_id
        __props__["name"] = name
        __props__["password"] = password
        __props__["region"] = region
        return User(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def databases(self) -> List[str]:
        """
        A list of database user should have access to.
        """
        return pulumi.get(self, "databases")

    @property
    @pulumi.getter
    def host(self) -> Optional[str]:
        return pulumi.get(self, "host")

    @property
    @pulumi.getter(name="instanceId")
    def instance_id(self) -> str:
        return pulumi.get(self, "instance_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        A unique name for the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def password(self) -> str:
        """
        User's password.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        Openstack region resource is created in.
        """
        return pulumi.get(self, "region")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

