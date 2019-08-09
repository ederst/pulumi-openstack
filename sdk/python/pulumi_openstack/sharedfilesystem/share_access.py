# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class ShareAccess(pulumi.CustomResource):
    access_key: pulumi.Output[str]
    """
    The access credential of the entity granted access.
    """
    access_level: pulumi.Output[str]
    """
    The access level to the share. Can either be `rw` or `ro`.
    """
    access_to: pulumi.Output[str]
    """
    The value that defines the access. Can either be an IP
    address or a username verified by configured Security Service of the Share Network.
    """
    access_type: pulumi.Output[str]
    """
    The access rule type. Can either be an ip, user,
    cert, or cephx. cephx support requires an OpenStack environment that supports
    Shared Filesystem microversion 2.13 (Mitaka) or later.
    """
    region: pulumi.Output[str]
    """
    The region in which to obtain the V2 Shared File System client.
    A Shared File System client is needed to create a share access. Changing this
    creates a new share access.
    """
    share_id: pulumi.Output[str]
    """
    The UUID of the share to which you are granted access.
    """
    def __init__(__self__, resource_name, opts=None, access_level=None, access_to=None, access_type=None, region=None, share_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Create a ShareAccess resource with the given unique name, props, and options.
        
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

        > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/sharedfilesystem_share_access_v2.html.markdown.
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
            opts.version = utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if access_level is None:
                raise TypeError("Missing required property 'access_level'")
            __props__['access_level'] = access_level
            if access_to is None:
                raise TypeError("Missing required property 'access_to'")
            __props__['access_to'] = access_to
            if access_type is None:
                raise TypeError("Missing required property 'access_type'")
            __props__['access_type'] = access_type
            __props__['region'] = region
            if share_id is None:
                raise TypeError("Missing required property 'share_id'")
            __props__['share_id'] = share_id
            __props__['access_key'] = None
        super(ShareAccess, __self__).__init__(
            'openstack:sharedfilesystem/shareAccess:ShareAccess',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, access_key=None, access_level=None, access_to=None, access_type=None, region=None, share_id=None):
        """
        Get an existing ShareAccess resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
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

        > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/sharedfilesystem_share_access_v2.html.markdown.
        """
        opts = pulumi.ResourceOptions(id=id) if opts is None else opts.merge(pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["access_key"] = access_key
        __props__["access_level"] = access_level
        __props__["access_to"] = access_to
        __props__["access_type"] = access_type
        __props__["region"] = region
        __props__["share_id"] = share_id
        return ShareAccess(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

