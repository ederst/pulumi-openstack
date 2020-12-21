# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from .. import _utilities, _tables

__all__ = ['L7RuleV2']


class L7RuleV2(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 admin_state_up: Optional[pulumi.Input[bool]] = None,
                 compare_type: Optional[pulumi.Input[str]] = None,
                 invert: Optional[pulumi.Input[bool]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 l7policy_id: Optional[pulumi.Input[str]] = None,
                 region: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Manages a V2 L7 Rule resource within OpenStack.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_openstack as openstack

        network1 = openstack.networking.Network("network1", admin_state_up=True)
        subnet1 = openstack.networking.Subnet("subnet1",
            cidr="192.168.199.0/24",
            ip_version=4,
            network_id=network1.id)
        loadbalancer1 = openstack.loadbalancer.LoadBalancer("loadbalancer1", vip_subnet_id=subnet1.id)
        listener1 = openstack.loadbalancer.Listener("listener1",
            loadbalancer_id=loadbalancer1.id,
            protocol="HTTP",
            protocol_port=8080)
        pool1 = openstack.loadbalancer.Pool("pool1",
            lb_method="ROUND_ROBIN",
            loadbalancer_id=loadbalancer1.id,
            protocol="HTTP")
        l7policy1 = openstack.loadbalancer.L7PolicyV2("l7policy1",
            action="REDIRECT_TO_URL",
            description="test description",
            listener_id=listener1.id,
            position=1,
            redirect_url="http://www.example.com")
        l7rule1 = openstack.loadbalancer.L7RuleV2("l7rule1",
            compare_type="EQUAL_TO",
            l7policy_id=l7policy1.id,
            type="PATH",
            value="/api")
        ```

        ## Import

        Load Balancer L7 Rule can be imported using the L7 Policy ID and L7 Rule ID separated by a slash, e.g.

        ```sh
         $ pulumi import openstack:loadbalancer/l7RuleV2:L7RuleV2 l7rule_1 e0bd694a-abbe-450e-b329-0931fd1cc5eb/4086b0c9-b18c-4d1c-b6b8-4c56c3ad2a9e
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] admin_state_up: The administrative state of the L7 Rule.
               A valid value is true (UP) or false (DOWN).
        :param pulumi.Input[str] compare_type: The comparison type for the L7 rule - can either be
               CONTAINS, STARTS\_WITH, ENDS_WITH, EQUAL_TO or REGEX
        :param pulumi.Input[bool] invert: When true the logic of the rule is inverted. For example, with invert
               true, equal to would become not equal to. Default is false.
        :param pulumi.Input[str] key: The key to use for the comparison. For example, the name of the cookie to
               evaluate. Valid when `type` is set to COOKIE or HEADER.
        :param pulumi.Input[str] l7policy_id: The ID of the L7 Policy to query. Changing this creates a new
               L7 Rule.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create an . If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               L7 Rule.
        :param pulumi.Input[str] tenant_id: Required for admins. The UUID of the tenant who owns
               the L7 Rule.  Only administrative users can specify a tenant UUID
               other than their own. Changing this creates a new L7 Rule.
        :param pulumi.Input[str] type: The L7 Rule type - can either be COOKIE, FILE\_TYPE, HEADER,
               HOST\_NAME or PATH.
        :param pulumi.Input[str] value: The value to use for the comparison. For example, the file type to
               compare.
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

            __props__['admin_state_up'] = admin_state_up
            if compare_type is None and not opts.urn:
                raise TypeError("Missing required property 'compare_type'")
            __props__['compare_type'] = compare_type
            __props__['invert'] = invert
            __props__['key'] = key
            if l7policy_id is None and not opts.urn:
                raise TypeError("Missing required property 'l7policy_id'")
            __props__['l7policy_id'] = l7policy_id
            __props__['region'] = region
            __props__['tenant_id'] = tenant_id
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
            if value is None and not opts.urn:
                raise TypeError("Missing required property 'value'")
            __props__['value'] = value
            __props__['listener_id'] = None
        super(L7RuleV2, __self__).__init__(
            'openstack:loadbalancer/l7RuleV2:L7RuleV2',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            admin_state_up: Optional[pulumi.Input[bool]] = None,
            compare_type: Optional[pulumi.Input[str]] = None,
            invert: Optional[pulumi.Input[bool]] = None,
            key: Optional[pulumi.Input[str]] = None,
            l7policy_id: Optional[pulumi.Input[str]] = None,
            listener_id: Optional[pulumi.Input[str]] = None,
            region: Optional[pulumi.Input[str]] = None,
            tenant_id: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            value: Optional[pulumi.Input[str]] = None) -> 'L7RuleV2':
        """
        Get an existing L7RuleV2 resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] admin_state_up: The administrative state of the L7 Rule.
               A valid value is true (UP) or false (DOWN).
        :param pulumi.Input[str] compare_type: The comparison type for the L7 rule - can either be
               CONTAINS, STARTS\_WITH, ENDS_WITH, EQUAL_TO or REGEX
        :param pulumi.Input[bool] invert: When true the logic of the rule is inverted. For example, with invert
               true, equal to would become not equal to. Default is false.
        :param pulumi.Input[str] key: The key to use for the comparison. For example, the name of the cookie to
               evaluate. Valid when `type` is set to COOKIE or HEADER.
        :param pulumi.Input[str] l7policy_id: The ID of the L7 Policy to query. Changing this creates a new
               L7 Rule.
        :param pulumi.Input[str] listener_id: The ID of the Listener owning this resource.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create an . If omitted, the
               `region` argument of the provider is used. Changing this creates a new
               L7 Rule.
        :param pulumi.Input[str] tenant_id: Required for admins. The UUID of the tenant who owns
               the L7 Rule.  Only administrative users can specify a tenant UUID
               other than their own. Changing this creates a new L7 Rule.
        :param pulumi.Input[str] type: The L7 Rule type - can either be COOKIE, FILE\_TYPE, HEADER,
               HOST\_NAME or PATH.
        :param pulumi.Input[str] value: The value to use for the comparison. For example, the file type to
               compare.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["admin_state_up"] = admin_state_up
        __props__["compare_type"] = compare_type
        __props__["invert"] = invert
        __props__["key"] = key
        __props__["l7policy_id"] = l7policy_id
        __props__["listener_id"] = listener_id
        __props__["region"] = region
        __props__["tenant_id"] = tenant_id
        __props__["type"] = type
        __props__["value"] = value
        return L7RuleV2(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="adminStateUp")
    def admin_state_up(self) -> pulumi.Output[Optional[bool]]:
        """
        The administrative state of the L7 Rule.
        A valid value is true (UP) or false (DOWN).
        """
        return pulumi.get(self, "admin_state_up")

    @property
    @pulumi.getter(name="compareType")
    def compare_type(self) -> pulumi.Output[str]:
        """
        The comparison type for the L7 rule - can either be
        CONTAINS, STARTS\_WITH, ENDS_WITH, EQUAL_TO or REGEX
        """
        return pulumi.get(self, "compare_type")

    @property
    @pulumi.getter
    def invert(self) -> pulumi.Output[Optional[bool]]:
        """
        When true the logic of the rule is inverted. For example, with invert
        true, equal to would become not equal to. Default is false.
        """
        return pulumi.get(self, "invert")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[Optional[str]]:
        """
        The key to use for the comparison. For example, the name of the cookie to
        evaluate. Valid when `type` is set to COOKIE or HEADER.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="l7policyId")
    def l7policy_id(self) -> pulumi.Output[str]:
        """
        The ID of the L7 Policy to query. Changing this creates a new
        L7 Rule.
        """
        return pulumi.get(self, "l7policy_id")

    @property
    @pulumi.getter(name="listenerId")
    def listener_id(self) -> pulumi.Output[str]:
        """
        The ID of the Listener owning this resource.
        """
        return pulumi.get(self, "listener_id")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        The region in which to obtain the V2 Networking client.
        A Networking client is needed to create an . If omitted, the
        `region` argument of the provider is used. Changing this creates a new
        L7 Rule.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[str]:
        """
        Required for admins. The UUID of the tenant who owns
        the L7 Rule.  Only administrative users can specify a tenant UUID
        other than their own. Changing this creates a new L7 Rule.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The L7 Rule type - can either be COOKIE, FILE\_TYPE, HEADER,
        HOST\_NAME or PATH.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        """
        The value to use for the comparison. For example, the file type to
        compare.
        """
        return pulumi.get(self, "value")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

