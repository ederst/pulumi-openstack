# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['ApplicationCredential']


class ApplicationCredential(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 access_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationCredentialAccessRuleArgs']]]]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expires_at: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 secret: Optional[pulumi.Input[str]] = None,
                 unrestricted: Optional[pulumi.Input[bool]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## Import

        Application Credentials can be imported using the `id`, e.g.

        ```sh
         $ pulumi import openstack:identity/applicationCredential:ApplicationCredential application_credential_1 c17304b7-0953-4738-abb0-67005882b0a0
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationCredentialAccessRuleArgs']]]] access_rules: A collection of one or more access rules, which
               this application credential allows to follow. The structure is described
               below. Changing this creates a new application credential.
        :param pulumi.Input[str] description: A description of the application credential.
               Changing this creates a new application credential.
        :param pulumi.Input[str] expires_at: The expiration time of the application credential
               in the RFC3339 timestamp format (e.g. `2019-03-09T12:58:49Z`). If omitted,
               an application credential will never expire. Changing this creates a new
               application credential.
        :param pulumi.Input[str] name: A name of the application credential. Changing this
               creates a new application credential.
        :param pulumi.Input[str] region: The region in which to obtain the V3 Keystone client.
               If omitted, the `region` argument of the provider is used. Changing this
               creates a new application credential.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] roles: A collection of one or more role names, which this
               application credential has to be associated with its project. If omitted,
               all the current user's roles within the scoped project will be inherited by
               a new application credential. Changing this creates a new application
               credential.
        :param pulumi.Input[str] secret: The secret for the application credential. If omitted,
               it will be generated by the server. Changing this creates a new application
               credential.
        :param pulumi.Input[bool] unrestricted: A flag indicating whether the application
               credential may be used for creation or destruction of other application
               credentials or trusts. Changing this creates a new application credential.
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

            __props__['access_rules'] = access_rules
            __props__['description'] = description
            __props__['expires_at'] = expires_at
            __props__['name'] = name
            __props__['region'] = region
            __props__['roles'] = roles
            __props__['secret'] = secret
            __props__['unrestricted'] = unrestricted
            __props__['project_id'] = None
        super(ApplicationCredential, __self__).__init__(
            'openstack:identity/applicationCredential:ApplicationCredential',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            access_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationCredentialAccessRuleArgs']]]]] = None,
            description: Optional[pulumi.Input[str]] = None,
            expires_at: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            roles: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            secret: Optional[pulumi.Input[str]] = None,
            unrestricted: Optional[pulumi.Input[bool]] = None) -> 'ApplicationCredential':
        """
        Get an existing ApplicationCredential resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationCredentialAccessRuleArgs']]]] access_rules: A collection of one or more access rules, which
               this application credential allows to follow. The structure is described
               below. Changing this creates a new application credential.
        :param pulumi.Input[str] description: A description of the application credential.
               Changing this creates a new application credential.
        :param pulumi.Input[str] expires_at: The expiration time of the application credential
               in the RFC3339 timestamp format (e.g. `2019-03-09T12:58:49Z`). If omitted,
               an application credential will never expire. Changing this creates a new
               application credential.
        :param pulumi.Input[str] name: A name of the application credential. Changing this
               creates a new application credential.
        :param pulumi.Input[str] project_id: The ID of the project the application credential was created
               for and that authentication requests using this application credential will
               be scoped to.
        :param pulumi.Input[str] region: The region in which to obtain the V3 Keystone client.
               If omitted, the `region` argument of the provider is used. Changing this
               creates a new application credential.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] roles: A collection of one or more role names, which this
               application credential has to be associated with its project. If omitted,
               all the current user's roles within the scoped project will be inherited by
               a new application credential. Changing this creates a new application
               credential.
        :param pulumi.Input[str] secret: The secret for the application credential. If omitted,
               it will be generated by the server. Changing this creates a new application
               credential.
        :param pulumi.Input[bool] unrestricted: A flag indicating whether the application
               credential may be used for creation or destruction of other application
               credentials or trusts. Changing this creates a new application credential.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["access_rules"] = access_rules
        __props__["description"] = description
        __props__["expires_at"] = expires_at
        __props__["name"] = name
        __props__["project_id"] = project_id
        __props__["region"] = region
        __props__["roles"] = roles
        __props__["secret"] = secret
        __props__["unrestricted"] = unrestricted
        return ApplicationCredential(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessRules")
    def access_rules(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationCredentialAccessRule']]]:
        """
        A collection of one or more access rules, which
        this application credential allows to follow. The structure is described
        below. Changing this creates a new application credential.
        """
        return pulumi.get(self, "access_rules")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description of the application credential.
        Changing this creates a new application credential.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> pulumi.Output[Optional[str]]:
        """
        The expiration time of the application credential
        in the RFC3339 timestamp format (e.g. `2019-03-09T12:58:49Z`). If omitted,
        an application credential will never expire. Changing this creates a new
        application credential.
        """
        return pulumi.get(self, "expires_at")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        A name of the application credential. Changing this
        creates a new application credential.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The ID of the project the application credential was created
        for and that authentication requests using this application credential will
        be scoped to.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V3 Keystone client.
        If omitted, the `region` argument of the provider is used. Changing this
        creates a new application credential.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def roles(self) -> pulumi.Output[Sequence[str]]:
        """
        A collection of one or more role names, which this
        application credential has to be associated with its project. If omitted,
        all the current user's roles within the scoped project will be inherited by
        a new application credential. Changing this creates a new application
        credential.
        """
        return pulumi.get(self, "roles")

    @property
    @pulumi.getter
    def secret(self) -> pulumi.Output[str]:
        """
        The secret for the application credential. If omitted,
        it will be generated by the server. Changing this creates a new application
        credential.
        """
        return pulumi.get(self, "secret")

    @property
    @pulumi.getter
    def unrestricted(self) -> pulumi.Output[Optional[bool]]:
        """
        A flag indicating whether the application
        credential may be used for creation or destruction of other application
        credentials or trusts. Changing this creates a new application credential.
        """
        return pulumi.get(self, "unrestricted")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

