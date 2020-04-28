// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package networking

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this data source to get the ID of an available OpenStack QoS bandwidth limit rule.
func LookupQosBandwidthLimitRule(ctx *pulumi.Context, args *LookupQosBandwidthLimitRuleArgs, opts ...pulumi.InvokeOption) (*LookupQosBandwidthLimitRuleResult, error) {
	var rv LookupQosBandwidthLimitRuleResult
	err := ctx.Invoke("openstack:networking/getQosBandwidthLimitRule:getQosBandwidthLimitRule", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getQosBandwidthLimitRule.
type LookupQosBandwidthLimitRuleArgs struct {
	// The maximum burst size in kilobits of a QoS bandwidth limit rule.
	MaxBurstKbps *int `pulumi:"maxBurstKbps"`
	// The maximum kilobits per second of a QoS bandwidth limit rule.
	MaxKbps *int `pulumi:"maxKbps"`
	// The QoS policy reference.
	QosPolicyId string `pulumi:"qosPolicyId"`
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create a Neutron QoS bandwidth limit rule. If omitted, the
	// `region` argument of the provider is used.
	Region *string `pulumi:"region"`
}

// A collection of values returned by getQosBandwidthLimitRule.
type LookupQosBandwidthLimitRuleResult struct {
	// See Argument Reference above.
	Direction string `pulumi:"direction"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// See Argument Reference above.
	MaxBurstKbps int `pulumi:"maxBurstKbps"`
	// See Argument Reference above.
	MaxKbps int `pulumi:"maxKbps"`
	// See Argument Reference above.
	QosPolicyId string `pulumi:"qosPolicyId"`
	// See Argument Reference above.
	Region string `pulumi:"region"`
}
