# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class User(pulumi.CustomResource):
    default_project_id: pulumi.Output[str]
    """
    The default project this user belongs to.
    """
    description: pulumi.Output[str]
    """
    A description of the user.
    """
    domain_id: pulumi.Output[str]
    """
    The domain this user belongs to.
    """
    enabled: pulumi.Output[bool]
    """
    Whether the user is enabled or disabled. Valid
    values are `true` and `false`.
    """
    extra: pulumi.Output[dict]
    """
    Free-form key/value pairs of extra information.
    """
    ignore_change_password_upon_first_use: pulumi.Output[bool]
    """
    User will not have to
    change their password upon first use. Valid values are `true` and `false`.
    """
    ignore_lockout_failure_attempts: pulumi.Output[bool]
    """
    User will not have a failure
    lockout placed on their account. Valid values are `true` and `false`.
    """
    ignore_password_expiry: pulumi.Output[bool]
    """
    User's password will not expire.
    Valid values are `true` and `false`.
    """
    multi_factor_auth_enabled: pulumi.Output[bool]
    """
    Whether to enable multi-factor
    authentication. Valid values are `true` and `false`.
    """
    multi_factor_auth_rules: pulumi.Output[list]
    """
    A multi-factor authentication rule.
    The structure is documented below. Please see the
    [Ocata release notes](https://docs.openstack.org/releasenotes/keystone/ocata.html)
    for more information on how to use mulit-factor rules.

      * `rules` (`list`) - A list of authentication plugins that the user must
        authenticate with.
    """
    name: pulumi.Output[str]
    """
    The name of the user.
    """
    password: pulumi.Output[str]
    """
    The password for the user.
    """
    region: pulumi.Output[str]
    """
    The region in which to obtain the V3 Keystone client.
    If omitted, the `region` argument of the provider is used. Changing this
    creates a new User.
    """
    def __init__(__self__, resource_name, opts=None, default_project_id=None, description=None, domain_id=None, enabled=None, extra=None, ignore_change_password_upon_first_use=None, ignore_lockout_failure_attempts=None, ignore_password_expiry=None, multi_factor_auth_enabled=None, multi_factor_auth_rules=None, name=None, password=None, region=None, __props__=None, __name__=None, __opts__=None):
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
                {
                    "rule": [
                        "password",
                        "totp",
                    ],
                },
                {
                    "rule": ["password"],
                },
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
        :param pulumi.Input[dict] extra: Free-form key/value pairs of extra information.
        :param pulumi.Input[bool] ignore_change_password_upon_first_use: User will not have to
               change their password upon first use. Valid values are `true` and `false`.
        :param pulumi.Input[bool] ignore_lockout_failure_attempts: User will not have a failure
               lockout placed on their account. Valid values are `true` and `false`.
        :param pulumi.Input[bool] ignore_password_expiry: User's password will not expire.
               Valid values are `true` and `false`.
        :param pulumi.Input[bool] multi_factor_auth_enabled: Whether to enable multi-factor
               authentication. Valid values are `true` and `false`.
        :param pulumi.Input[list] multi_factor_auth_rules: A multi-factor authentication rule.
               The structure is documented below. Please see the
               [Ocata release notes](https://docs.openstack.org/releasenotes/keystone/ocata.html)
               for more information on how to use mulit-factor rules.
        :param pulumi.Input[str] name: The name of the user.
        :param pulumi.Input[str] password: The password for the user.
        :param pulumi.Input[str] region: The region in which to obtain the V3 Keystone client.
               If omitted, the `region` argument of the provider is used. Changing this
               creates a new User.

        The **multi_factor_auth_rules** object supports the following:

          * `rules` (`pulumi.Input[list]`) - A list of authentication plugins that the user must
            authenticate with.
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
    def get(resource_name, id, opts=None, default_project_id=None, description=None, domain_id=None, enabled=None, extra=None, ignore_change_password_upon_first_use=None, ignore_lockout_failure_attempts=None, ignore_password_expiry=None, multi_factor_auth_enabled=None, multi_factor_auth_rules=None, name=None, password=None, region=None):
        """
        Get an existing User resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_project_id: The default project this user belongs to.
        :param pulumi.Input[str] description: A description of the user.
        :param pulumi.Input[str] domain_id: The domain this user belongs to.
        :param pulumi.Input[bool] enabled: Whether the user is enabled or disabled. Valid
               values are `true` and `false`.
        :param pulumi.Input[dict] extra: Free-form key/value pairs of extra information.
        :param pulumi.Input[bool] ignore_change_password_upon_first_use: User will not have to
               change their password upon first use. Valid values are `true` and `false`.
        :param pulumi.Input[bool] ignore_lockout_failure_attempts: User will not have a failure
               lockout placed on their account. Valid values are `true` and `false`.
        :param pulumi.Input[bool] ignore_password_expiry: User's password will not expire.
               Valid values are `true` and `false`.
        :param pulumi.Input[bool] multi_factor_auth_enabled: Whether to enable multi-factor
               authentication. Valid values are `true` and `false`.
        :param pulumi.Input[list] multi_factor_auth_rules: A multi-factor authentication rule.
               The structure is documented below. Please see the
               [Ocata release notes](https://docs.openstack.org/releasenotes/keystone/ocata.html)
               for more information on how to use mulit-factor rules.
        :param pulumi.Input[str] name: The name of the user.
        :param pulumi.Input[str] password: The password for the user.
        :param pulumi.Input[str] region: The region in which to obtain the V3 Keystone client.
               If omitted, the `region` argument of the provider is used. Changing this
               creates a new User.

        The **multi_factor_auth_rules** object supports the following:

          * `rules` (`pulumi.Input[list]`) - A list of authentication plugins that the user must
            authenticate with.
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
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

