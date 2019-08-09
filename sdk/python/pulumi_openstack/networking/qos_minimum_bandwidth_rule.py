# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class QosMinimumBandwidthRule(pulumi.CustomResource):
    direction: pulumi.Output[str]
    """
    The direction of traffic. Defaults to "egress". Changing this updates the direction of the
    existing QoS minimum bandwidth rule.
    """
    min_kbps: pulumi.Output[float]
    """
    The minimum kilobits per second. Changing this updates the min kbps value of the existing
    QoS minimum bandwidth rule.
    """
    qos_policy_id: pulumi.Output[str]
    """
    The QoS policy reference. Changing this creates a new QoS minimum bandwidth rule.
    """
    region: pulumi.Output[str]
    """
    The region in which to obtain the V2 Networking client.
    A Networking client is needed to create a Neutron QoS minimum bandwidth rule. If omitted, the
    `region` argument of the provider is used. Changing this creates a new QoS minimum bandwidth rule.
    """
    def __init__(__self__, resource_name, opts=None, direction=None, min_kbps=None, qos_policy_id=None, region=None, __props__=None, __name__=None, __opts__=None):
        """
        Manages a V2 Neutron QoS minimum bandwidth rule resource within OpenStack.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] direction: The direction of traffic. Defaults to "egress". Changing this updates the direction of the
               existing QoS minimum bandwidth rule.
        :param pulumi.Input[float] min_kbps: The minimum kilobits per second. Changing this updates the min kbps value of the existing
               QoS minimum bandwidth rule.
        :param pulumi.Input[str] qos_policy_id: The QoS policy reference. Changing this creates a new QoS minimum bandwidth rule.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create a Neutron QoS minimum bandwidth rule. If omitted, the
               `region` argument of the provider is used. Changing this creates a new QoS minimum bandwidth rule.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/networking_qos_minimum_bandwidth_rule_v2.html.markdown.
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

            __props__['direction'] = direction
            if min_kbps is None:
                raise TypeError("Missing required property 'min_kbps'")
            __props__['min_kbps'] = min_kbps
            if qos_policy_id is None:
                raise TypeError("Missing required property 'qos_policy_id'")
            __props__['qos_policy_id'] = qos_policy_id
            __props__['region'] = region
        super(QosMinimumBandwidthRule, __self__).__init__(
            'openstack:networking/qosMinimumBandwidthRule:QosMinimumBandwidthRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, direction=None, min_kbps=None, qos_policy_id=None, region=None):
        """
        Get an existing QosMinimumBandwidthRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.
        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] direction: The direction of traffic. Defaults to "egress". Changing this updates the direction of the
               existing QoS minimum bandwidth rule.
        :param pulumi.Input[float] min_kbps: The minimum kilobits per second. Changing this updates the min kbps value of the existing
               QoS minimum bandwidth rule.
        :param pulumi.Input[str] qos_policy_id: The QoS policy reference. Changing this creates a new QoS minimum bandwidth rule.
        :param pulumi.Input[str] region: The region in which to obtain the V2 Networking client.
               A Networking client is needed to create a Neutron QoS minimum bandwidth rule. If omitted, the
               `region` argument of the provider is used. Changing this creates a new QoS minimum bandwidth rule.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/networking_qos_minimum_bandwidth_rule_v2.html.markdown.
        """
        opts = pulumi.ResourceOptions(id=id) if opts is None else opts.merge(pulumi.ResourceOptions(id=id))

        __props__ = dict()
        __props__["direction"] = direction
        __props__["min_kbps"] = min_kbps
        __props__["qos_policy_id"] = qos_policy_id
        __props__["region"] = region
        return QosMinimumBandwidthRule(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop
