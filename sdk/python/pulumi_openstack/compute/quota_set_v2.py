# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['QuotaSetV2']


class QuotaSetV2(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cores: Optional[pulumi.Input[int]] = None,
                 fixed_ips: Optional[pulumi.Input[int]] = None,
                 floating_ips: Optional[pulumi.Input[int]] = None,
                 injected_file_content_bytes: Optional[pulumi.Input[int]] = None,
                 injected_file_path_bytes: Optional[pulumi.Input[int]] = None,
                 injected_files: Optional[pulumi.Input[int]] = None,
                 instances: Optional[pulumi.Input[int]] = None,
                 key_pairs: Optional[pulumi.Input[int]] = None,
                 metadata_items: Optional[pulumi.Input[int]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 ram: Optional[pulumi.Input[int]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 security_group_rules: Optional[pulumi.Input[int]] = None,
                 security_groups: Optional[pulumi.Input[int]] = None,
                 server_group_members: Optional[pulumi.Input[int]] = None,
                 server_groups: Optional[pulumi.Input[int]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a V2 compute quotaset resource within OpenStack.

        > **Note:** This usually requires admin privileges.

        > **Note:** This resource has a no-op deletion so no actual actions will be done against the OpenStack API
            in case of delete call.

        > **Note:** This resource has all-in creation so all optional quota arguments that were not specified are
            created with zero value.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        project1 = openstack.identity.Project("project1")
        quotaset1 = openstack.compute.QuotaSetV2("quotaset1",
            project_id=project1.id,
            key_pairs=10,
            ram=40960,
            cores=32,
            instances=20,
            server_groups=4,
            server_group_members=8)
        ```

        ## Import

        Quotasets can be imported using the `project_id`, e.g.

        ```sh
         $ pulumi import openstack:compute/quotaSetV2:QuotaSetV2 quotaset_1 2a0f2240-c5e6-41de-896d-e80d97428d6b
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] cores: Quota value for cores.
               Changing this updates the existing quotaset.
        :param pulumi.Input[int] fixed_ips: Quota value for fixed IPs.
               Changing this updates the existing quotaset.
        :param pulumi.Input[int] floating_ips: Quota value for floating IPs.
               Changing this updates the existing quotaset.
        :param pulumi.Input[int] injected_file_content_bytes: Quota value for content bytes
               of injected files. Changing this updates the existing quotaset.
        :param pulumi.Input[int] injected_file_path_bytes: Quota value for path bytes of
               injected files. Changing this updates the existing quotaset.
        :param pulumi.Input[int] injected_files: Quota value for injected files.
               Changing this updates the existing quotaset.
        :param pulumi.Input[int] instances: Quota value for instances.
               Changing this updates the existing quotaset.
        :param pulumi.Input[int] key_pairs: Quota value for key pairs.
               Changing this updates the existing quotaset.
        :param pulumi.Input[int] metadata_items: Quota value for metadata items.
               Changing this updates the existing quotaset.
        :param pulumi.Input[str] project_id: ID of the project to manage quotas.
               Changing this creates a new quotaset.
        :param pulumi.Input[int] ram: Quota value for RAM.
               Changing this updates the existing quotaset.
        :param pulumi.Input[str] region: The region in which to create the volume. If
               omitted, the `region` argument of the provider is used. Changing this
               creates a new quotaset.
        :param pulumi.Input[int] security_group_rules: Quota value for security group rules.
               Changing this updates the existing quotaset.
        :param pulumi.Input[int] security_groups: Quota value for security groups.
               Changing this updates the existing quotaset.
        :param pulumi.Input[int] server_group_members: Quota value for server groups members.
               Changing this updates the existing quotaset.
        :param pulumi.Input[int] server_groups: Quota value for server groups.
               Changing this updates the existing quotaset.
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

            __props__['cores'] = cores
            __props__['fixed_ips'] = fixed_ips
            __props__['floating_ips'] = floating_ips
            __props__['injected_file_content_bytes'] = injected_file_content_bytes
            __props__['injected_file_path_bytes'] = injected_file_path_bytes
            __props__['injected_files'] = injected_files
            __props__['instances'] = instances
            __props__['key_pairs'] = key_pairs
            __props__['metadata_items'] = metadata_items
            if project_id is None and not opts.urn:
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
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cores: Optional[pulumi.Input[int]] = None,
            fixed_ips: Optional[pulumi.Input[int]] = None,
            floating_ips: Optional[pulumi.Input[int]] = None,
            injected_file_content_bytes: Optional[pulumi.Input[int]] = None,
            injected_file_path_bytes: Optional[pulumi.Input[int]] = None,
            injected_files: Optional[pulumi.Input[int]] = None,
            instances: Optional[pulumi.Input[int]] = None,
            key_pairs: Optional[pulumi.Input[int]] = None,
            metadata_items: Optional[pulumi.Input[int]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            ram: Optional[pulumi.Input[int]] = None,
            region: Optional[pulumi.Input[str]] = None,
            security_group_rules: Optional[pulumi.Input[int]] = None,
            security_groups: Optional[pulumi.Input[int]] = None,
            server_group_members: Optional[pulumi.Input[int]] = None,
            server_groups: Optional[pulumi.Input[int]] = None) -> 'QuotaSetV2':
        """
        Get an existing QuotaSetV2 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] cores: Quota value for cores.
               Changing this updates the existing quotaset.
        :param pulumi.Input[int] fixed_ips: Quota value for fixed IPs.
               Changing this updates the existing quotaset.
        :param pulumi.Input[int] floating_ips: Quota value for floating IPs.
               Changing this updates the existing quotaset.
        :param pulumi.Input[int] injected_file_content_bytes: Quota value for content bytes
               of injected files. Changing this updates the existing quotaset.
        :param pulumi.Input[int] injected_file_path_bytes: Quota value for path bytes of
               injected files. Changing this updates the existing quotaset.
        :param pulumi.Input[int] injected_files: Quota value for injected files.
               Changing this updates the existing quotaset.
        :param pulumi.Input[int] instances: Quota value for instances.
               Changing this updates the existing quotaset.
        :param pulumi.Input[int] key_pairs: Quota value for key pairs.
               Changing this updates the existing quotaset.
        :param pulumi.Input[int] metadata_items: Quota value for metadata items.
               Changing this updates the existing quotaset.
        :param pulumi.Input[str] project_id: ID of the project to manage quotas.
               Changing this creates a new quotaset.
        :param pulumi.Input[int] ram: Quota value for RAM.
               Changing this updates the existing quotaset.
        :param pulumi.Input[str] region: The region in which to create the volume. If
               omitted, the `region` argument of the provider is used. Changing this
               creates a new quotaset.
        :param pulumi.Input[int] security_group_rules: Quota value for security group rules.
               Changing this updates the existing quotaset.
        :param pulumi.Input[int] security_groups: Quota value for security groups.
               Changing this updates the existing quotaset.
        :param pulumi.Input[int] server_group_members: Quota value for server groups members.
               Changing this updates the existing quotaset.
        :param pulumi.Input[int] server_groups: Quota value for server groups.
               Changing this updates the existing quotaset.
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

    @property
    @pulumi.getter
    def cores(self) -> pulumi.Output[int]:
        """
        Quota value for cores.
        Changing this updates the existing quotaset.
        """
        return pulumi.get(self, "cores")

    @property
    @pulumi.getter(name="fixedIps")
    def fixed_ips(self) -> pulumi.Output[int]:
        """
        Quota value for fixed IPs.
        Changing this updates the existing quotaset.
        """
        return pulumi.get(self, "fixed_ips")

    @property
    @pulumi.getter(name="floatingIps")
    def floating_ips(self) -> pulumi.Output[int]:
        """
        Quota value for floating IPs.
        Changing this updates the existing quotaset.
        """
        return pulumi.get(self, "floating_ips")

    @property
    @pulumi.getter(name="injectedFileContentBytes")
    def injected_file_content_bytes(self) -> pulumi.Output[int]:
        """
        Quota value for content bytes
        of injected files. Changing this updates the existing quotaset.
        """
        return pulumi.get(self, "injected_file_content_bytes")

    @property
    @pulumi.getter(name="injectedFilePathBytes")
    def injected_file_path_bytes(self) -> pulumi.Output[int]:
        """
        Quota value for path bytes of
        injected files. Changing this updates the existing quotaset.
        """
        return pulumi.get(self, "injected_file_path_bytes")

    @property
    @pulumi.getter(name="injectedFiles")
    def injected_files(self) -> pulumi.Output[int]:
        """
        Quota value for injected files.
        Changing this updates the existing quotaset.
        """
        return pulumi.get(self, "injected_files")

    @property
    @pulumi.getter
    def instances(self) -> pulumi.Output[int]:
        """
        Quota value for instances.
        Changing this updates the existing quotaset.
        """
        return pulumi.get(self, "instances")

    @property
    @pulumi.getter(name="keyPairs")
    def key_pairs(self) -> pulumi.Output[int]:
        """
        Quota value for key pairs.
        Changing this updates the existing quotaset.
        """
        return pulumi.get(self, "key_pairs")

    @property
    @pulumi.getter(name="metadataItems")
    def metadata_items(self) -> pulumi.Output[int]:
        """
        Quota value for metadata items.
        Changing this updates the existing quotaset.
        """
        return pulumi.get(self, "metadata_items")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        ID of the project to manage quotas.
        Changing this creates a new quotaset.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def ram(self) -> pulumi.Output[int]:
        """
        Quota value for RAM.
        Changing this updates the existing quotaset.
        """
        return pulumi.get(self, "ram")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to create the volume. If
        omitted, the `region` argument of the provider is used. Changing this
        creates a new quotaset.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="securityGroupRules")
    def security_group_rules(self) -> pulumi.Output[int]:
        """
        Quota value for security group rules.
        Changing this updates the existing quotaset.
        """
        return pulumi.get(self, "security_group_rules")

    @property
    @pulumi.getter(name="securityGroups")
    def security_groups(self) -> pulumi.Output[int]:
        """
        Quota value for security groups.
        Changing this updates the existing quotaset.
        """
        return pulumi.get(self, "security_groups")

    @property
    @pulumi.getter(name="serverGroupMembers")
    def server_group_members(self) -> pulumi.Output[int]:
        """
        Quota value for server groups members.
        Changing this updates the existing quotaset.
        """
        return pulumi.get(self, "server_group_members")

    @property
    @pulumi.getter(name="serverGroups")
    def server_groups(self) -> pulumi.Output[int]:
        """
        Quota value for server groups.
        Changing this updates the existing quotaset.
        """
        return pulumi.get(self, "server_groups")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

