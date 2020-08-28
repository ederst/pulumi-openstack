# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['User']


class User(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_project_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 domain_id: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 extra: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 ignore_change_password_upon_first_use: Optional[pulumi.Input[bool]] = None,
                 ignore_lockout_failure_attempts: Optional[pulumi.Input[bool]] = None,
                 ignore_password_expiry: Optional[pulumi.Input[bool]] = None,
                 multi_factor_auth_enabled: Optional[pulumi.Input[bool]] = None,
                 multi_factor_auth_rules: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['UserMultiFactorAuthRuleArgs']]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a V3 User resource within OpenStack Keystone.

        Note: You _must_ have admin privileges in your OpenStack cloud to use
        this resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        project1 = openstack.identity.Project("project1")
        user1 = openstack.identity.User("user1",
            default_project_id=project1.id,
            description="A user",
            extra={
                "email": "user_1@foobar.com",
            },
            ignore_change_password_upon_first_use=True,
            multi_factor_auth_enabled=True,
            multi_factor_auth_rules=[
                openstack.identity.UserMultiFactorAuthRuleArgs(
                    rules=[
                        "password",
                        "totp",
                    ],
                ),
                openstack.identity.UserMultiFactorAuthRuleArgs(
                    rules=["password"],
                ),
            ],
            password="password123")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_project_id: The default project this user belongs to.
        :param pulumi.Input[str] description: A description of the user.
        :param pulumi.Input[str] domain_id: The domain this user belongs to.
        :param pulumi.Input[bool] enabled: Whether the user is enabled or disabled. Valid
               values are `true` and `false`.
        :param pulumi.Input[Mapping[str, Any]] extra: Free-form key/value pairs of extra information.
        :param pulumi.Input[bool] ignore_change_password_upon_first_use: User will not have to
               change their password upon first use. Valid values are `true` and `false`.
        :param pulumi.Input[bool] ignore_lockout_failure_attempts: User will not have a failure
               lockout placed on their account. Valid values are `true` and `false`.
        :param pulumi.Input[bool] ignore_password_expiry: User's password will not expire.
               Valid values are `true` and `false`.
        :param pulumi.Input[bool] multi_factor_auth_enabled: Whether to enable multi-factor
               authentication. Valid values are `true` and `false`.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['UserMultiFactorAuthRuleArgs']]]] multi_factor_auth_rules: A multi-factor authentication rule.
               The structure is documented below. Please see the
               [Ocata release notes](https://docs.openstack.org/releasenotes/keystone/ocata.html)
               for more information on how to use mulit-factor rules.
        :param pulumi.Input[str] name: The name of the user.
        :param pulumi.Input[str] password: The password for the user.
        :param pulumi.Input[str] region: The region in which to obtain the V3 Keystone client.
               If omitted, the `region` argument of the provider is used. Changing this
               creates a new User.
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

            __props__['default_project_id'] = default_project_id
            __props__['description'] = description
            __props__['domain_id'] = domain_id
            __props__['enabled'] = enabled
            __props__['extra'] = extra
            __props__['ignore_change_password_upon_first_use'] = ignore_change_password_upon_first_use
            __props__['ignore_lockout_failure_attempts'] = ignore_lockout_failure_attempts
            __props__['ignore_password_expiry'] = ignore_password_expiry
            __props__['multi_factor_auth_enabled'] = multi_factor_auth_enabled
            __props__['multi_factor_auth_rules'] = multi_factor_auth_rules
            __props__['name'] = name
            __props__['password'] = password
            __props__['region'] = region
        super(User, __self__).__init__(
            'openstack:identity/user:User',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            default_project_id: Optional[pulumi.Input[str]] = None,
            description: Optional[pulumi.Input[str]] = None,
            domain_id: Optional[pulumi.Input[str]] = None,
            enabled: Optional[pulumi.Input[bool]] = None,
            extra: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            ignore_change_password_upon_first_use: Optional[pulumi.Input[bool]] = None,
            ignore_lockout_failure_attempts: Optional[pulumi.Input[bool]] = None,
            ignore_password_expiry: Optional[pulumi.Input[bool]] = None,
            multi_factor_auth_enabled: Optional[pulumi.Input[bool]] = None,
            multi_factor_auth_rules: Optional[pulumi.Input[List[pulumi.Input[pulumi.InputType['UserMultiFactorAuthRuleArgs']]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            password: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None) -> 'User':
        """
        Get an existing User resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_project_id: The default project this user belongs to.
        :param pulumi.Input[str] description: A description of the user.
        :param pulumi.Input[str] domain_id: The domain this user belongs to.
        :param pulumi.Input[bool] enabled: Whether the user is enabled or disabled. Valid
               values are `true` and `false`.
        :param pulumi.Input[Mapping[str, Any]] extra: Free-form key/value pairs of extra information.
        :param pulumi.Input[bool] ignore_change_password_upon_first_use: User will not have to
               change their password upon first use. Valid values are `true` and `false`.
        :param pulumi.Input[bool] ignore_lockout_failure_attempts: User will not have a failure
               lockout placed on their account. Valid values are `true` and `false`.
        :param pulumi.Input[bool] ignore_password_expiry: User's password will not expire.
               Valid values are `true` and `false`.
        :param pulumi.Input[bool] multi_factor_auth_enabled: Whether to enable multi-factor
               authentication. Valid values are `true` and `false`.
        :param pulumi.Input[List[pulumi.Input[pulumi.InputType['UserMultiFactorAuthRuleArgs']]]] multi_factor_auth_rules: A multi-factor authentication rule.
               The structure is documented below. Please see the
               [Ocata release notes](https://docs.openstack.org/releasenotes/keystone/ocata.html)
               for more information on how to use mulit-factor rules.
        :param pulumi.Input[str] name: The name of the user.
        :param pulumi.Input[str] password: The password for the user.
        :param pulumi.Input[str] region: The region in which to obtain the V3 Keystone client.
               If omitted, the `region` argument of the provider is used. Changing this
               creates a new User.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["default_project_id"] = default_project_id
        __props__["description"] = description
        __props__["domain_id"] = domain_id
        __props__["enabled"] = enabled
        __props__["extra"] = extra
        __props__["ignore_change_password_upon_first_use"] = ignore_change_password_upon_first_use
        __props__["ignore_lockout_failure_attempts"] = ignore_lockout_failure_attempts
        __props__["ignore_password_expiry"] = ignore_password_expiry
        __props__["multi_factor_auth_enabled"] = multi_factor_auth_enabled
        __props__["multi_factor_auth_rules"] = multi_factor_auth_rules
        __props__["name"] = name
        __props__["password"] = password
        __props__["region"] = region
        return User(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="defaultProjectId")
    def default_project_id(self) -> pulumi.Output[str]:
        """
        The default project this user belongs to.
        """
        return pulumi.get(self, "default_project_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the user.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="domainId")
    def domain_id(self) -> pulumi.Output[str]:
        """
        The domain this user belongs to.
        """
        return pulumi.get(self, "domain_id")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether the user is enabled or disabled. Valid
        values are `true` and `false`.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def extra(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        Free-form key/value pairs of extra information.
        """
        return pulumi.get(self, "extra")

    @property
    @pulumi.getter(name="ignoreChangePasswordUponFirstUse")
    def ignore_change_password_upon_first_use(self) -> pulumi.Output[Optional[bool]]:
        """
        User will not have to
        change their password upon first use. Valid values are `true` and `false`.
        """
        return pulumi.get(self, "ignore_change_password_upon_first_use")

    @property
    @pulumi.getter(name="ignoreLockoutFailureAttempts")
    def ignore_lockout_failure_attempts(self) -> pulumi.Output[Optional[bool]]:
        """
        User will not have a failure
        lockout placed on their account. Valid values are `true` and `false`.
        """
        return pulumi.get(self, "ignore_lockout_failure_attempts")

    @property
    @pulumi.getter(name="ignorePasswordExpiry")
    def ignore_password_expiry(self) -> pulumi.Output[Optional[bool]]:
        """
        User's password will not expire.
        Valid values are `true` and `false`.
        """
        return pulumi.get(self, "ignore_password_expiry")

    @property
    @pulumi.getter(name="multiFactorAuthEnabled")
    def multi_factor_auth_enabled(self) -> pulumi.Output[Optional[bool]]:
        """
        Whether to enable multi-factor
        authentication. Valid values are `true` and `false`.
        """
        return pulumi.get(self, "multi_factor_auth_enabled")

    @property
    @pulumi.getter(name="multiFactorAuthRules")
    def multi_factor_auth_rules(self) -> pulumi.Output[Optional[List['outputs.UserMultiFactorAuthRule']]]:
        """
        A multi-factor authentication rule.
        The structure is documented below. Please see the
        [Ocata release notes](https://docs.openstack.org/releasenotes/keystone/ocata.html)
        for more information on how to use mulit-factor rules.
        """
        return pulumi.get(self, "multi_factor_auth_rules")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the user.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[str]]:
        """
        The password for the user.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V3 Keystone client.
        If omitted, the `region` argument of the provider is used. Changing this
        creates a new User.
        """
        return pulumi.get(self, "region")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

