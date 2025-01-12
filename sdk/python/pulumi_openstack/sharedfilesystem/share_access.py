# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['ShareAccess']


class ShareAccess(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_level: Optional[pulumi.Input[str]] = None,
                 access_to: Optional[pulumi.Input[str]] = None,
                 access_type: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 share_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## Import

        This resource can be imported by specifying the ID of the share and the ID of the share access, separated by a slash, e.g.

        ```sh
         $ pulumi import openstack:sharedfilesystem/shareAccess:ShareAccess share_access_1 <share id>/<share access id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_level: The access level to the share. Can either be `rw` or `ro`.
        :param pulumi.Input[str] access_to: The value that defines the access. Can either be an IP
               address or a username verified by configured Security Service of the Share Network.
        :param pulumi.Input[str] access_type: The access rule type. Can either be an ip, user,
               cert, or cephx. cephx support requires an OpenStack environment that supports
               Shared Filesystem microversion 2.13 (Mitaka) or later.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Shared File System client.
               A Shared File System client is needed to create a share access. Changing this
               creates a new share access.
        :param pulumi.Input[str] share_id: The UUID of the share to which you are granted access.
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

            if access_level is None and not opts.urn:
                raise TypeError("Missing required property 'access_level'")
            __props__['access_level'] = access_level
            if access_to is None and not opts.urn:
                raise TypeError("Missing required property 'access_to'")
            __props__['access_to'] = access_to
            if access_type is None and not opts.urn:
                raise TypeError("Missing required property 'access_type'")
            __props__['access_type'] = access_type
            __props__['region'] = region
            if share_id is None and not opts.urn:
                raise TypeError("Missing required property 'share_id'")
            __props__['share_id'] = share_id
            __props__['access_key'] = None
        super(ShareAccess, __self__).__init__(
            'openstack:sharedfilesystem/shareAccess:ShareAccess',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access_key: Optional[pulumi.Input[str]] = None,
            access_level: Optional[pulumi.Input[str]] = None,
            access_to: Optional[pulumi.Input[str]] = None,
            access_type: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            share_id: Optional[pulumi.Input[str]] = None) -> 'ShareAccess':
        """
        Get an existing ShareAccess resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] access_key: The access credential of the entity granted access.
        :param pulumi.Input[str] access_level: The access level to the share. Can either be `rw` or `ro`.
        :param pulumi.Input[str] access_to: The value that defines the access. Can either be an IP
               address or a username verified by configured Security Service of the Share Network.
        :param pulumi.Input[str] access_type: The access rule type. Can either be an ip, user,
               cert, or cephx. cephx support requires an OpenStack environment that supports
               Shared Filesystem microversion 2.13 (Mitaka) or later.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Shared File System client.
               A Shared File System client is needed to create a share access. Changing this
               creates a new share access.
        :param pulumi.Input[str] share_id: The UUID of the share to which you are granted access.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["access_key"] = access_key
        __props__["access_level"] = access_level
        __props__["access_to"] = access_to
        __props__["access_type"] = access_type
        __props__["region"] = region
        __props__["share_id"] = share_id
        return ShareAccess(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessKey")
    def access_key(self) -> pulumi.Output[str]:
        """
        The access credential of the entity granted access.
        """
        return pulumi.get(self, "access_key")

    @property
    @pulumi.getter(name="accessLevel")
    def access_level(self) -> pulumi.Output[str]:
        """
        The access level to the share. Can either be `rw` or `ro`.
        """
        return pulumi.get(self, "access_level")

    @property
    @pulumi.getter(name="accessTo")
    def access_to(self) -> pulumi.Output[str]:
        """
        The value that defines the access. Can either be an IP
        address or a username verified by configured Security Service of the Share Network.
        """
        return pulumi.get(self, "access_to")

    @property
    @pulumi.getter(name="accessType")
    def access_type(self) -> pulumi.Output[str]:
        """
        The access rule type. Can either be an ip, user,
        cert, or cephx. cephx support requires an OpenStack environment that supports
        Shared Filesystem microversion 2.13 (Mitaka) or later.
        """
        return pulumi.get(self, "access_type")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V2 Shared File System client.
        A Shared File System client is needed to create a share access. Changing this
        creates a new share access.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="shareId")
    def share_id(self) -> pulumi.Output[str]:
        """
        The UUID of the share to which you are granted access.
        """
        return pulumi.get(self, "share_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

