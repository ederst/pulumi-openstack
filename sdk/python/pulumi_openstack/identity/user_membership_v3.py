# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['UserMembershipV3']


class UserMembershipV3(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a user membership to group V3 resource within OpenStack.

        > **Note:** You _must_ have admin privileges in your OpenStack cloud to use
        this resource.

        ***

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        project1 = openstack.identity.Project("project1")
        user1 = openstack.identity.User("user1", default_project_id=project1.id)
        group1 = openstack.identity.GroupV3("group1", description="group 1")
        role1 = openstack.identity.Role("role1")
        user_membership1 = openstack.identity.UserMembershipV3("userMembership1",
            group_id=group1.id,
            user_id=user1.id)
        role_assignment1 = openstack.identity.RoleAssignment("roleAssignment1",
            group_id=group1.id,
            project_id=project1.id,
            role_id=role1.id)
        ```

        ## Import

        This resource can be imported by specifying all two arguments, separated by a forward slash

        ```sh
         $ pulumi import openstack:identity/userMembershipV3:UserMembershipV3 user_membership_1 <user_id>/<group_id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group_id: The UUID of group to which the user will be added.
               Changing this creates a new user membership.
        :param pulumi.Input[str] region: The region in which to obtain the V3 Identity client.
               If omitted, the `region` argument of the provider is used.
               Changing this creates a new user membership.
        :param pulumi.Input[str] user_id: The UUID of user to use. Changing this creates a new user membership.
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

            if group_id is None and not opts.urn:
                raise TypeError("Missing required property 'group_id'")
            __props__['group_id'] = group_id
            __props__['region'] = region
            if user_id is None and not opts.urn:
                raise TypeError("Missing required property 'user_id'")
            __props__['user_id'] = user_id
        super(UserMembershipV3, __self__).__init__(
            'openstack:identity/userMembershipV3:UserMembershipV3',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            group_id: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            user_id: Optional[pulumi.Input[str]] = None) -> 'UserMembershipV3':
        """
        Get an existing UserMembershipV3 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] group_id: The UUID of group to which the user will be added.
               Changing this creates a new user membership.
        :param pulumi.Input[str] region: The region in which to obtain the V3 Identity client.
               If omitted, the `region` argument of the provider is used.
               Changing this creates a new user membership.
        :param pulumi.Input[str] user_id: The UUID of user to use. Changing this creates a new user membership.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["group_id"] = group_id
        __props__["region"] = region
        __props__["user_id"] = user_id
        return UserMembershipV3(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> pulumi.Output[str]:
        """
        The UUID of group to which the user will be added.
        Changing this creates a new user membership.
        """
        return pulumi.get(self, "group_id")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V3 Identity client.
        If omitted, the `region` argument of the provider is used.
        Changing this creates a new user membership.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[str]:
        """
        The UUID of user to use. Changing this creates a new user membership.
        """
        return pulumi.get(self, "user_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
