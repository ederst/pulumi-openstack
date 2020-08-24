# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['RbacPolicyV2']


class RbacPolicyV2(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[str]] = None,
                 object_id: Optional[pulumi.Input[str]] = None,
                 object_type: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 target_tenant: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The RBAC policy resource contains functionality for working with Neutron RBAC
        Policies. Role-Based Access Control (RBAC) policy framework enables both
        operators and users to grant access to resources for specific projects.

        Sharing an object with a specific project is accomplished by creating a
        policy entry that permits the target project the `access_as_shared` action
        on that object.

        To make a network available as an external network for specific projects
        rather than all projects, use the `access_as_external` action.
        If a network is marked as external during creation, it now implicitly creates
        a wildcard RBAC policy granting everyone access to preserve previous behavior
        before this feature was added.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        network1 = openstack.networking.Network("network1", admin_state_up=True)
        rbac_policy1 = openstack.networking.RbacPolicyV2("rbacPolicy1",
            action="access_as_shared",
            object_id=network1.id,
            object_type="network",
            target_tenant="20415a973c9e45d3917f078950644697")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action: Action for the RBAC policy. Can either be
               `access_as_external` or `access_as_shared`.
        :param pulumi.Input[str] object_id: The ID of the `object_type` resource. An
               `object_type` of `network` returns a network ID and an `object_type` of
               `qos_policy` returns a QoS ID.
        :param pulumi.Input[str] object_type: The type of the object that the RBAC policy
               affects. Can either be `qos-policy` or `network`.
        :param pulumi.Input[str] region: The region in which to obtain the V2 networking client.
               A networking client is needed to configure a routing entry on a subnet. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               routing entry.
        :param pulumi.Input[str] target_tenant: The ID of the tenant to which the RBAC policy
               will be enforced.
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

            if action is None:
                raise TypeError("Missing required property 'action'")
            __props__['action'] = action
            if object_id is None:
                raise TypeError("Missing required property 'object_id'")
            __props__['object_id'] = object_id
            if object_type is None:
                raise TypeError("Missing required property 'object_type'")
            __props__['object_type'] = object_type
            __props__['region'] = region
            if target_tenant is None:
                raise TypeError("Missing required property 'target_tenant'")
            __props__['target_tenant'] = target_tenant
            __props__['project_id'] = None
        super(RbacPolicyV2, __self__).__init__(
            'openstack:networking/rbacPolicyV2:RbacPolicyV2',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            action: Optional[pulumi.Input[str]] = None,
            object_id: Optional[pulumi.Input[str]] = None,
            object_type: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            target_tenant: Optional[pulumi.Input[str]] = None) -> 'RbacPolicyV2':
        """
        Get an existing RbacPolicyV2 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action: Action for the RBAC policy. Can either be
               `access_as_external` or `access_as_shared`.
        :param pulumi.Input[str] object_id: The ID of the `object_type` resource. An
               `object_type` of `network` returns a network ID and an `object_type` of
               `qos_policy` returns a QoS ID.
        :param pulumi.Input[str] object_type: The type of the object that the RBAC policy
               affects. Can either be `qos-policy` or `network`.
        :param pulumi.Input[str] region: The region in which to obtain the V2 networking client.
               A networking client is needed to configure a routing entry on a subnet. If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               routing entry.
        :param pulumi.Input[str] target_tenant: The ID of the tenant to which the RBAC policy
               will be enforced.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["action"] = action
        __props__["object_id"] = object_id
        __props__["object_type"] = object_type
        __props__["project_id"] = project_id
        __props__["region"] = region
        __props__["target_tenant"] = target_tenant
        return RbacPolicyV2(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def action(self) -> str:
        """
        Action for the RBAC policy. Can either be
        `access_as_external` or `access_as_shared`.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> str:
        """
        The ID of the `object_type` resource. An
        `object_type` of `network` returns a network ID and an `object_type` of
        `qos_policy` returns a QoS ID.
        """
        return pulumi.get(self, "object_id")

    @property
    @pulumi.getter(name="objectType")
    def object_type(self) -> str:
        """
        The type of the object that the RBAC policy
        affects. Can either be `qos-policy` or `network`.
        """
        return pulumi.get(self, "object_type")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter
    def region(self) -> str:
        """
        The region in which to obtain the V2 networking client.
        A networking client is needed to configure a routing entry on a subnet. If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        routing entry.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="targetTenant")
    def target_tenant(self) -> str:
        """
        The ID of the tenant to which the RBAC policy
        will be enforced.
        """
        return pulumi.get(self, "target_tenant")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

