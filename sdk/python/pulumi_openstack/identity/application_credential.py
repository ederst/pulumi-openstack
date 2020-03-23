# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class ApplicationCredential(pulumi.CustomResource):
    access_rules: pulumi.Output[list]
    """
    A collection of one or more access rules, which
    this application credential allows to follow. The structure is described
    below. Changing this creates a new application credential.

      * `id` (`str`)
      * `method` (`str`)
      * `path` (`str`)
      * `service` (`str`)
    """
    description: pulumi.Output[str]
    """
    A description of the application credential.
    Changing this creates a new application credential.
    """
    expires_at: pulumi.Output[str]
    """
    The expiration time of the application credential
    in the RFC3339 timestamp format (e.g. `2019-03-09T12:58:49Z`). If omitted,
    an application credential will never expire. Changing this creates a new
    application credential.
    """
    name: pulumi.Output[str]
    """
    A name of the application credential. Changing this
    creates a new application credential.
    """
    project_id: pulumi.Output[str]
    """
    The ID of the project the application credential was created
    for and that authentication requests using this application credential will
    be scoped to.
    """
    region: pulumi.Output[str]
    """
    The region in which to obtain the V3 Keystone client.
    If omitted, the `region` argument of the provider is used. Changing this
    creates a new application credential.
    """
    roles: pulumi.Output[list]
    """
    A collection of one or more role names, which this
    application credential has to be associated with its project. If omitted,
    all the current user's roles within the scoped project will be inherited by
    a new application credential. Changing this creates a new application
    credential.
    """
    secret: pulumi.Output[str]
    """
    The secret for the application credential. If omitted,
    it will be generated by the server. Changing this creates a new application
    credential.
    """
    unrestricted: pulumi.Output[bool]
    """
    A flag indicating whether the application
    credential may be used for creation or destruction of other application
    credentials or trusts. Changing this creates a new application credential.
    """
    def __init__(__self__, resource_name, opts=None, access_rules=None, description=None, expires_at=None, name=None, region=None, roles=None, secret=None, unrestricted=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a V3 Application Credential resource within OpenStack Keystone.

        > **Note:** All arguments including the application credential name and secret
        will be stored in the raw state as plain-text. [Read more about sensitive data
        in state](https://www.terraform.io/docs/state/sensitive-data.html).

        > **Note:** An Application Credential is created within the authenticated user
        project scope and is not visible by an admin or other accounts.
        The Application Credential visibility is similar to
        `compute.Keypair`.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_application_credential_v3.html.markdown.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] access_rules: A collection of one or more access rules, which
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
        :param pulumi.Input[list] roles: A collection of one or more role names, which this
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

        The **access_rules** object supports the following:

          * `id` (`pulumi.Input[str]`)
          * `method` (`pulumi.Input[str]`)
          * `path` (`pulumi.Input[str]`)
          * `service` (`pulumi.Input[str]`)
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
    def get(resource_name, id, opts=None, access_rules=None, description=None, expires_at=None, name=None, project_id=None, region=None, roles=None, secret=None, unrestricted=None):
        """
        Get an existing ApplicationCredential resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[list] access_rules: A collection of one or more access rules, which
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
        :param pulumi.Input[list] roles: A collection of one or more role names, which this
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

        The **access_rules** object supports the following:

          * `id` (`pulumi.Input[str]`)
          * `method` (`pulumi.Input[str]`)
          * `path` (`pulumi.Input[str]`)
          * `service` (`pulumi.Input[str]`)
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
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

