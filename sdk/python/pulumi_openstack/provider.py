# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class Provider(pulumi.ProviderResource):
    def __init__(__self__, resource_name, opts=None, application_credential_id=None, application_credential_name=None, application_credential_secret=None, auth_url=None, cacert_file=None, cert=None, cloud=None, default_domain=None, delayed_auth=None, disable_no_cache_header=None, domain_id=None, domain_name=None, endpoint_overrides=None, endpoint_type=None, insecure=None, key=None, max_retries=None, password=None, project_domain_id=None, project_domain_name=None, region=None, swauth=None, tenant_id=None, tenant_name=None, token=None, use_octavia=None, user_domain_id=None, user_domain_name=None, user_id=None, user_name=None, __props__=None, __name__=None, __opts__=None):
        """
        The provider type for the openstack package. By default, resources use package-wide configuration
        settings, however an explicit `Provider` instance may be created and passed during resource
        construction to achieve fine-grained programmatic control over provider settings. See the
        [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/index.html.markdown.
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

            __props__['application_credential_id'] = application_credential_id
            __props__['application_credential_name'] = application_credential_name
            __props__['application_credential_secret'] = application_credential_secret
            if auth_url is None:
                auth_url = utilities.get_env('OS_AUTH_URL')
            __props__['auth_url'] = auth_url
            if cacert_file is None:
                cacert_file = utilities.get_env('OS_CACERT')
            __props__['cacert_file'] = cacert_file
            if cert is None:
                cert = utilities.get_env('OS_CERT')
            __props__['cert'] = cert
            if cloud is None:
                cloud = utilities.get_env('OS_CLOUD')
            __props__['cloud'] = cloud
            if default_domain is None:
                default_domain = (utilities.get_env('OS_DEFAULT_DOMAIN') or 'default')
            __props__['default_domain'] = default_domain
            __props__['delayed_auth'] = pulumi.Output.from_input(delayed_auth).apply(json.dumps) if delayed_auth is not None else None
            __props__['disable_no_cache_header'] = pulumi.Output.from_input(disable_no_cache_header).apply(json.dumps) if disable_no_cache_header is not None else None
            if domain_id is None:
                domain_id = utilities.get_env('OS_DOMAIN_ID')
            __props__['domain_id'] = domain_id
            if domain_name is None:
                domain_name = utilities.get_env('OS_DOMAIN_NAME')
            __props__['domain_name'] = domain_name
            __props__['endpoint_overrides'] = pulumi.Output.from_input(endpoint_overrides).apply(json.dumps) if endpoint_overrides is not None else None
            if endpoint_type is None:
                endpoint_type = utilities.get_env('OS_ENDPOINT_TYPE')
            __props__['endpoint_type'] = endpoint_type
            if insecure is None:
                insecure = utilities.get_env_bool('OS_INSECURE')
            __props__['insecure'] = pulumi.Output.from_input(insecure).apply(json.dumps) if insecure is not None else None
            if key is None:
                key = utilities.get_env('OS_KEY')
            __props__['key'] = key
            __props__['max_retries'] = pulumi.Output.from_input(max_retries).apply(json.dumps) if max_retries is not None else None
            if password is None:
                password = utilities.get_env('OS_PASSWORD')
            __props__['password'] = password
            if project_domain_id is None:
                project_domain_id = utilities.get_env('OS_PROJECT_DOMAIN_ID')
            __props__['project_domain_id'] = project_domain_id
            if project_domain_name is None:
                project_domain_name = utilities.get_env('OS_PROJECT_DOMAIN_NAME')
            __props__['project_domain_name'] = project_domain_name
            if region is None:
                region = utilities.get_env('OS_REGION_NAME')
            __props__['region'] = region
            if swauth is None:
                swauth = utilities.get_env_bool('OS_SWAUTH')
            __props__['swauth'] = pulumi.Output.from_input(swauth).apply(json.dumps) if swauth is not None else None
            if tenant_id is None:
                tenant_id = utilities.get_env('OS_TENANT_ID', 'OS_PROJECT_ID')
            __props__['tenant_id'] = tenant_id
            if tenant_name is None:
                tenant_name = utilities.get_env('OS_TENANT_NAME', 'OS_PROJECT_NAME')
            __props__['tenant_name'] = tenant_name
            if token is None:
                token = utilities.get_env('OS_TOKEN', 'OS_AUTH_TOKEN')
            __props__['token'] = token
            if use_octavia is None:
                use_octavia = utilities.get_env_bool('OS_USE_OCTAVIA')
            __props__['use_octavia'] = pulumi.Output.from_input(use_octavia).apply(json.dumps) if use_octavia is not None else None
            if user_domain_id is None:
                user_domain_id = utilities.get_env('OS_USER_DOMAIN_ID')
            __props__['user_domain_id'] = user_domain_id
            if user_domain_name is None:
                user_domain_name = utilities.get_env('OS_USER_DOMAIN_NAME')
            __props__['user_domain_name'] = user_domain_name
            if user_id is None:
                user_id = utilities.get_env('OS_USER_ID')
            __props__['user_id'] = user_id
            if user_name is None:
                user_name = utilities.get_env('OS_USERNAME')
            __props__['user_name'] = user_name
        super(Provider, __self__).__init__(
            'openstack',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None):
        """
        Get an existing Provider resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/index.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        return Provider(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

