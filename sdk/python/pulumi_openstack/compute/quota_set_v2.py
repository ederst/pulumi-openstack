# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from .. import utilities, tables

class QuotaSetV2(pulumi.CustomResource):
    cores: pulumi.Output[float]
    """
    Quota value for cores.
    Changing this updates the existing quotaset.
    """
    fixed_ips: pulumi.Output[float]
    """
    Quota value for fixed IPs.
    Changing this updates the existing quotaset.
    """
    floating_ips: pulumi.Output[float]
    """
    Quota value for floating IPs.
    Changing this updates the existing quotaset.
    """
    injected_file_content_bytes: pulumi.Output[float]
    """
    Quota value for content bytes
    of injected files. Changing this updates the existing quotaset.
    """
    injected_file_path_bytes: pulumi.Output[float]
    """
    Quota value for path bytes of
    injected files. Changing this updates the existing quotaset.
    """
    injected_files: pulumi.Output[float]
    """
    Quota value for injected files.
    Changing this updates the existing quotaset.
    """
    instances: pulumi.Output[float]
    """
    Quota value for instances.
    Changing this updates the existing quotaset.
    """
    key_pairs: pulumi.Output[float]
    """
    Quota value for key pairs.
    Changing this updates the existing quotaset.
    """
    metadata_items: pulumi.Output[float]
    """
    Quota value for metadata items.
    Changing this updates the existing quotaset.
    """
    project_id: pulumi.Output[str]
    """
    ID of the project to manage quotas.
    Changing this creates a new quotaset.
    """
    ram: pulumi.Output[float]
    """
    Quota value for RAM.
    Changing this updates the existing quotaset.
    """
    region: pulumi.Output[str]
    """
    The region in which to create the volume. If
    omitted, the `region` argument of the provider is used. Changing this
    creates a new quotaset.
    """
    security_group_rules: pulumi.Output[float]
    """
    Quota value for security group rules.
    Changing this updates the existing quotaset.
    """
    security_groups: pulumi.Output[float]
    """
    Quota value for security groups.
    Changing this updates the existing quotaset.
    """
    server_group_members: pulumi.Output[float]
    """
    Quota value for server groups members.
    Changing this updates the existing quotaset.
    """
    server_groups: pulumi.Output[float]
    """
    Quota value for server groups.
    Changing this updates the existing quotaset.
    """
    def __init__(__self__, resource_name, opts=None, cores=None, fixed_ips=None, floating_ips=None, injected_file_content_bytes=None, injected_file_path_bytes=None, injected_files=None, instances=None, key_pairs=None, metadata_items=None, project_id=None, ram=None, region=None, security_group_rules=None, security_groups=None, server_group_members=None, server_groups=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a V2 compute quotaset resource within OpenStack.
        
        > **Note:** This usually requires admin privileges.
        
        > **Note:** This resource has a no-op deletion so no actual actions will be done against the OpenStack API 
            in case of delete call.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] cores: Quota value for cores.
               Changing this updates the existing quotaset.
        :param pulumi.Input[float] fixed_ips: Quota value for fixed IPs.
               Changing this updates the existing quotaset.
        :param pulumi.Input[float] floating_ips: Quota value for floating IPs.
               Changing this updates the existing quotaset.
        :param pulumi.Input[float] injected_file_content_bytes: Quota value for content bytes
               of injected files. Changing this updates the existing quotaset.
        :param pulumi.Input[float] injected_file_path_bytes: Quota value for path bytes of
               injected files. Changing this updates the existing quotaset.
        :param pulumi.Input[float] injected_files: Quota value for injected files.
               Changing this updates the existing quotaset.
        :param pulumi.Input[float] instances: Quota value for instances.
               Changing this updates the existing quotaset.
        :param pulumi.Input[float] key_pairs: Quota value for key pairs.
               Changing this updates the existing quotaset.
        :param pulumi.Input[float] metadata_items: Quota value for metadata items.
               Changing this updates the existing quotaset.
        :param pulumi.Input[str] project_id: ID of the project to manage quotas.
               Changing this creates a new quotaset.
        :param pulumi.Input[float] ram: Quota value for RAM.
               Changing this updates the existing quotaset.
        :param pulumi.Input[str] region: The region in which to create the volume. If
               omitted, the `region` argument of the provider is used. Changing this
               creates a new quotaset.
        :param pulumi.Input[float] security_group_rules: Quota value for security group rules.
               Changing this updates the existing quotaset.
        :param pulumi.Input[float] security_groups: Quota value for security groups.
               Changing this updates the existing quotaset.
        :param pulumi.Input[float] server_group_members: Quota value for server groups members.
               Changing this updates the existing quotaset.
        :param pulumi.Input[float] server_groups: Quota value for server groups.
               Changing this updates the existing quotaset.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_quotaset_v2.html.markdown.
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

            __props__['cores'] = cores
            __props__['fixed_ips'] = fixed_ips
            __props__['floating_ips'] = floating_ips
            __props__['injected_file_content_bytes'] = injected_file_content_bytes
            __props__['injected_file_path_bytes'] = injected_file_path_bytes
            __props__['injected_files'] = injected_files
            __props__['instances'] = instances
            __props__['key_pairs'] = key_pairs
            __props__['metadata_items'] = metadata_items
            if project_id is None:
                raise TypeError("Missing required property 'project_id'")
            __props__['project_id'] = project_id
            __props__['ram'] = ram
            __props__['region'] = region
            __props__['security_group_rules'] = security_group_rules
            __props__['security_groups'] = security_groups
            __props__['server_group_members'] = server_group_members
            __props__['server_groups'] = server_groups
        super(QuotaSetV2, __self__).__init__(
            'openstack:compute/quotaSetV2:QuotaSetV2',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, cores=None, fixed_ips=None, floating_ips=None, injected_file_content_bytes=None, injected_file_path_bytes=None, injected_files=None, instances=None, key_pairs=None, metadata_items=None, project_id=None, ram=None, region=None, security_group_rules=None, security_groups=None, server_group_members=None, server_groups=None):
        """
        Get an existing QuotaSetV2 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] cores: Quota value for cores.
               Changing this updates the existing quotaset.
        :param pulumi.Input[float] fixed_ips: Quota value for fixed IPs.
               Changing this updates the existing quotaset.
        :param pulumi.Input[float] floating_ips: Quota value for floating IPs.
               Changing this updates the existing quotaset.
        :param pulumi.Input[float] injected_file_content_bytes: Quota value for content bytes
               of injected files. Changing this updates the existing quotaset.
        :param pulumi.Input[float] injected_file_path_bytes: Quota value for path bytes of
               injected files. Changing this updates the existing quotaset.
        :param pulumi.Input[float] injected_files: Quota value for injected files.
               Changing this updates the existing quotaset.
        :param pulumi.Input[float] instances: Quota value for instances.
               Changing this updates the existing quotaset.
        :param pulumi.Input[float] key_pairs: Quota value for key pairs.
               Changing this updates the existing quotaset.
        :param pulumi.Input[float] metadata_items: Quota value for metadata items.
               Changing this updates the existing quotaset.
        :param pulumi.Input[str] project_id: ID of the project to manage quotas.
               Changing this creates a new quotaset.
        :param pulumi.Input[float] ram: Quota value for RAM.
               Changing this updates the existing quotaset.
        :param pulumi.Input[str] region: The region in which to create the volume. If
               omitted, the `region` argument of the provider is used. Changing this
               creates a new quotaset.
        :param pulumi.Input[float] security_group_rules: Quota value for security group rules.
               Changing this updates the existing quotaset.
        :param pulumi.Input[float] security_groups: Quota value for security groups.
               Changing this updates the existing quotaset.
        :param pulumi.Input[float] server_group_members: Quota value for server groups members.
               Changing this updates the existing quotaset.
        :param pulumi.Input[float] server_groups: Quota value for server groups.
               Changing this updates the existing quotaset.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_quotaset_v2.html.markdown.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["cores"] = cores
        __props__["fixed_ips"] = fixed_ips
        __props__["floating_ips"] = floating_ips
        __props__["injected_file_content_bytes"] = injected_file_content_bytes
        __props__["injected_file_path_bytes"] = injected_file_path_bytes
        __props__["injected_files"] = injected_files
        __props__["instances"] = instances
        __props__["key_pairs"] = key_pairs
        __props__["metadata_items"] = metadata_items
        __props__["project_id"] = project_id
        __props__["ram"] = ram
        __props__["region"] = region
        __props__["security_group_rules"] = security_group_rules
        __props__["security_groups"] = security_groups
        __props__["server_group_members"] = server_group_members
        __props__["server_groups"] = server_groups
        return QuotaSetV2(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
