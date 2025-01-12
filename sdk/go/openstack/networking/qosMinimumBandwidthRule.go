// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package networking

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a V2 Neutron QoS minimum bandwidth rule resource within OpenStack.
//
// ## Example Usage
// ### Create a QoS Policy with some minimum bandwidth rule
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/networking"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		qosPolicy1, err := networking.NewQosPolicy(ctx, "qosPolicy1", &networking.QosPolicyArgs{
// 			Description: pulumi.String("min_kbps"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = networking.NewQosMinimumBandwidthRule(ctx, "minimumBandwidthRule1", &networking.QosMinimumBandwidthRuleArgs{
// 			MinKbps:     pulumi.Int(200),
// 			QosPolicyId: qosPolicy1.ID(),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Import
//
// QoS minimum bandwidth rules can be imported using the `qos_policy_id/minimum_bandwidth_rule_id` format, e.g.
//
// ```sh
//  $ pulumi import openstack:networking/qosMinimumBandwidthRule:QosMinimumBandwidthRule minimum_bandwidth_rule_1 d6ae28ce-fcb5-4180-aa62-d260a27e09ae/46dfb556-b92f-48ce-94c5-9a9e2140de94
// ```
type QosMinimumBandwidthRule struct {
	pulumi.CustomResourceState

	// The direction of traffic. Defaults to "egress". Changing this updates the direction of the
	// existing QoS minimum bandwidth rule.
	Direction pulumi.StringPtrOutput `pulumi:"direction"`
	// The minimum kilobits per second. Changing this updates the min kbps value of the existing
	// QoS minimum bandwidth rule.
	MinKbps pulumi.IntOutput `pulumi:"minKbps"`
	// The QoS policy reference. Changing this creates a new QoS minimum bandwidth rule.
	QosPolicyId pulumi.StringOutput `pulumi:"qosPolicyId"`
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create a Neutron QoS minimum bandwidth rule. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new QoS minimum bandwidth rule.
	Region pulumi.StringOutput `pulumi:"region"`
}

// NewQosMinimumBandwidthRule registers a new resource with the given unique name, arguments, and options.
func NewQosMinimumBandwidthRule(ctx *pulumi.Context,
	name string, args *QosMinimumBandwidthRuleArgs, opts ...pulumi.ResourceOption) (*QosMinimumBandwidthRule, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.MinKbps == nil {
		return nil, errors.New("invalid value for required argument 'MinKbps'")
	}
	if args.QosPolicyId == nil {
		return nil, errors.New("invalid value for required argument 'QosPolicyId'")
	}
	var resource QosMinimumBandwidthRule
	err := ctx.RegisterResource("openstack:networking/qosMinimumBandwidthRule:QosMinimumBandwidthRule", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetQosMinimumBandwidthRule gets an existing QosMinimumBandwidthRule resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetQosMinimumBandwidthRule(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *QosMinimumBandwidthRuleState, opts ...pulumi.ResourceOption) (*QosMinimumBandwidthRule, error) {
	var resource QosMinimumBandwidthRule
	err := ctx.ReadResource("openstack:networking/qosMinimumBandwidthRule:QosMinimumBandwidthRule", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering QosMinimumBandwidthRule resources.
type qosMinimumBandwidthRuleState struct {
	// The direction of traffic. Defaults to "egress". Changing this updates the direction of the
	// existing QoS minimum bandwidth rule.
	Direction *string `pulumi:"direction"`
	// The minimum kilobits per second. Changing this updates the min kbps value of the existing
	// QoS minimum bandwidth rule.
	MinKbps *int `pulumi:"minKbps"`
	// The QoS policy reference. Changing this creates a new QoS minimum bandwidth rule.
	QosPolicyId *string `pulumi:"qosPolicyId"`
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create a Neutron QoS minimum bandwidth rule. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new QoS minimum bandwidth rule.
	Region *string `pulumi:"region"`
}

type QosMinimumBandwidthRuleState struct {
	// The direction of traffic. Defaults to "egress". Changing this updates the direction of the
	// existing QoS minimum bandwidth rule.
	Direction pulumi.StringPtrInput
	// The minimum kilobits per second. Changing this updates the min kbps value of the existing
	// QoS minimum bandwidth rule.
	MinKbps pulumi.IntPtrInput
	// The QoS policy reference. Changing this creates a new QoS minimum bandwidth rule.
	QosPolicyId pulumi.StringPtrInput
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create a Neutron QoS minimum bandwidth rule. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new QoS minimum bandwidth rule.
	Region pulumi.StringPtrInput
}

func (QosMinimumBandwidthRuleState) ElementType() reflect.Type {
	return reflect.TypeOf((*qosMinimumBandwidthRuleState)(nil)).Elem()
}

type qosMinimumBandwidthRuleArgs struct {
	// The direction of traffic. Defaults to "egress". Changing this updates the direction of the
	// existing QoS minimum bandwidth rule.
	Direction *string `pulumi:"direction"`
	// The minimum kilobits per second. Changing this updates the min kbps value of the existing
	// QoS minimum bandwidth rule.
	MinKbps int `pulumi:"minKbps"`
	// The QoS policy reference. Changing this creates a new QoS minimum bandwidth rule.
	QosPolicyId string `pulumi:"qosPolicyId"`
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create a Neutron QoS minimum bandwidth rule. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new QoS minimum bandwidth rule.
	Region *string `pulumi:"region"`
}

// The set of arguments for constructing a QosMinimumBandwidthRule resource.
type QosMinimumBandwidthRuleArgs struct {
	// The direction of traffic. Defaults to "egress". Changing this updates the direction of the
	// existing QoS minimum bandwidth rule.
	Direction pulumi.StringPtrInput
	// The minimum kilobits per second. Changing this updates the min kbps value of the existing
	// QoS minimum bandwidth rule.
	MinKbps pulumi.IntInput
	// The QoS policy reference. Changing this creates a new QoS minimum bandwidth rule.
	QosPolicyId pulumi.StringInput
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create a Neutron QoS minimum bandwidth rule. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new QoS minimum bandwidth rule.
	Region pulumi.StringPtrInput
}

func (QosMinimumBandwidthRuleArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*qosMinimumBandwidthRuleArgs)(nil)).Elem()
}

type QosMinimumBandwidthRuleInput interface {
	pulumi.Input

	ToQosMinimumBandwidthRuleOutput() QosMinimumBandwidthRuleOutput
	ToQosMinimumBandwidthRuleOutputWithContext(ctx context.Context) QosMinimumBandwidthRuleOutput
}

func (*QosMinimumBandwidthRule) ElementType() reflect.Type {
	return reflect.TypeOf((*QosMinimumBandwidthRule)(nil))
}

func (i *QosMinimumBandwidthRule) ToQosMinimumBandwidthRuleOutput() QosMinimumBandwidthRuleOutput {
	return i.ToQosMinimumBandwidthRuleOutputWithContext(context.Background())
}

func (i *QosMinimumBandwidthRule) ToQosMinimumBandwidthRuleOutputWithContext(ctx context.Context) QosMinimumBandwidthRuleOutput {
	return pulumi.ToOutputWithContext(ctx, i).(QosMinimumBandwidthRuleOutput)
}

func (i *QosMinimumBandwidthRule) ToQosMinimumBandwidthRulePtrOutput() QosMinimumBandwidthRulePtrOutput {
	return i.ToQosMinimumBandwidthRulePtrOutputWithContext(context.Background())
}

func (i *QosMinimumBandwidthRule) ToQosMinimumBandwidthRulePtrOutputWithContext(ctx context.Context) QosMinimumBandwidthRulePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(QosMinimumBandwidthRulePtrOutput)
}

type QosMinimumBandwidthRulePtrInput interface {
	pulumi.Input

	ToQosMinimumBandwidthRulePtrOutput() QosMinimumBandwidthRulePtrOutput
	ToQosMinimumBandwidthRulePtrOutputWithContext(ctx context.Context) QosMinimumBandwidthRulePtrOutput
}

type qosMinimumBandwidthRulePtrType QosMinimumBandwidthRuleArgs

func (*qosMinimumBandwidthRulePtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**QosMinimumBandwidthRule)(nil))
}

func (i *qosMinimumBandwidthRulePtrType) ToQosMinimumBandwidthRulePtrOutput() QosMinimumBandwidthRulePtrOutput {
	return i.ToQosMinimumBandwidthRulePtrOutputWithContext(context.Background())
}

func (i *qosMinimumBandwidthRulePtrType) ToQosMinimumBandwidthRulePtrOutputWithContext(ctx context.Context) QosMinimumBandwidthRulePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(QosMinimumBandwidthRulePtrOutput)
}

// QosMinimumBandwidthRuleArrayInput is an input type that accepts QosMinimumBandwidthRuleArray and QosMinimumBandwidthRuleArrayOutput values.
// You can construct a concrete instance of `QosMinimumBandwidthRuleArrayInput` via:
//
//          QosMinimumBandwidthRuleArray{ QosMinimumBandwidthRuleArgs{...} }
type QosMinimumBandwidthRuleArrayInput interface {
	pulumi.Input

	ToQosMinimumBandwidthRuleArrayOutput() QosMinimumBandwidthRuleArrayOutput
	ToQosMinimumBandwidthRuleArrayOutputWithContext(context.Context) QosMinimumBandwidthRuleArrayOutput
}

type QosMinimumBandwidthRuleArray []QosMinimumBandwidthRuleInput

func (QosMinimumBandwidthRuleArray) ElementType() reflect.Type {
	return reflect.TypeOf(([]*QosMinimumBandwidthRule)(nil))
}

func (i QosMinimumBandwidthRuleArray) ToQosMinimumBandwidthRuleArrayOutput() QosMinimumBandwidthRuleArrayOutput {
	return i.ToQosMinimumBandwidthRuleArrayOutputWithContext(context.Background())
}

func (i QosMinimumBandwidthRuleArray) ToQosMinimumBandwidthRuleArrayOutputWithContext(ctx context.Context) QosMinimumBandwidthRuleArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(QosMinimumBandwidthRuleArrayOutput)
}

// QosMinimumBandwidthRuleMapInput is an input type that accepts QosMinimumBandwidthRuleMap and QosMinimumBandwidthRuleMapOutput values.
// You can construct a concrete instance of `QosMinimumBandwidthRuleMapInput` via:
//
//          QosMinimumBandwidthRuleMap{ "key": QosMinimumBandwidthRuleArgs{...} }
type QosMinimumBandwidthRuleMapInput interface {
	pulumi.Input

	ToQosMinimumBandwidthRuleMapOutput() QosMinimumBandwidthRuleMapOutput
	ToQosMinimumBandwidthRuleMapOutputWithContext(context.Context) QosMinimumBandwidthRuleMapOutput
}

type QosMinimumBandwidthRuleMap map[string]QosMinimumBandwidthRuleInput

func (QosMinimumBandwidthRuleMap) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*QosMinimumBandwidthRule)(nil))
}

func (i QosMinimumBandwidthRuleMap) ToQosMinimumBandwidthRuleMapOutput() QosMinimumBandwidthRuleMapOutput {
	return i.ToQosMinimumBandwidthRuleMapOutputWithContext(context.Background())
}

func (i QosMinimumBandwidthRuleMap) ToQosMinimumBandwidthRuleMapOutputWithContext(ctx context.Context) QosMinimumBandwidthRuleMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(QosMinimumBandwidthRuleMapOutput)
}

type QosMinimumBandwidthRuleOutput struct {
	*pulumi.OutputState
}

func (QosMinimumBandwidthRuleOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*QosMinimumBandwidthRule)(nil))
}

func (o QosMinimumBandwidthRuleOutput) ToQosMinimumBandwidthRuleOutput() QosMinimumBandwidthRuleOutput {
	return o
}

func (o QosMinimumBandwidthRuleOutput) ToQosMinimumBandwidthRuleOutputWithContext(ctx context.Context) QosMinimumBandwidthRuleOutput {
	return o
}

func (o QosMinimumBandwidthRuleOutput) ToQosMinimumBandwidthRulePtrOutput() QosMinimumBandwidthRulePtrOutput {
	return o.ToQosMinimumBandwidthRulePtrOutputWithContext(context.Background())
}

func (o QosMinimumBandwidthRuleOutput) ToQosMinimumBandwidthRulePtrOutputWithContext(ctx context.Context) QosMinimumBandwidthRulePtrOutput {
	return o.ApplyT(func(v QosMinimumBandwidthRule) *QosMinimumBandwidthRule {
		return &v
	}).(QosMinimumBandwidthRulePtrOutput)
}

type QosMinimumBandwidthRulePtrOutput struct {
	*pulumi.OutputState
}

func (QosMinimumBandwidthRulePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**QosMinimumBandwidthRule)(nil))
}

func (o QosMinimumBandwidthRulePtrOutput) ToQosMinimumBandwidthRulePtrOutput() QosMinimumBandwidthRulePtrOutput {
	return o
}

func (o QosMinimumBandwidthRulePtrOutput) ToQosMinimumBandwidthRulePtrOutputWithContext(ctx context.Context) QosMinimumBandwidthRulePtrOutput {
	return o
}

type QosMinimumBandwidthRuleArrayOutput struct{ *pulumi.OutputState }

func (QosMinimumBandwidthRuleArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]QosMinimumBandwidthRule)(nil))
}

func (o QosMinimumBandwidthRuleArrayOutput) ToQosMinimumBandwidthRuleArrayOutput() QosMinimumBandwidthRuleArrayOutput {
	return o
}

func (o QosMinimumBandwidthRuleArrayOutput) ToQosMinimumBandwidthRuleArrayOutputWithContext(ctx context.Context) QosMinimumBandwidthRuleArrayOutput {
	return o
}

func (o QosMinimumBandwidthRuleArrayOutput) Index(i pulumi.IntInput) QosMinimumBandwidthRuleOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) QosMinimumBandwidthRule {
		return vs[0].([]QosMinimumBandwidthRule)[vs[1].(int)]
	}).(QosMinimumBandwidthRuleOutput)
}

type QosMinimumBandwidthRuleMapOutput struct{ *pulumi.OutputState }

func (QosMinimumBandwidthRuleMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]QosMinimumBandwidthRule)(nil))
}

func (o QosMinimumBandwidthRuleMapOutput) ToQosMinimumBandwidthRuleMapOutput() QosMinimumBandwidthRuleMapOutput {
	return o
}

func (o QosMinimumBandwidthRuleMapOutput) ToQosMinimumBandwidthRuleMapOutputWithContext(ctx context.Context) QosMinimumBandwidthRuleMapOutput {
	return o
}

func (o QosMinimumBandwidthRuleMapOutput) MapIndex(k pulumi.StringInput) QosMinimumBandwidthRuleOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) QosMinimumBandwidthRule {
		return vs[0].(map[string]QosMinimumBandwidthRule)[vs[1].(string)]
	}).(QosMinimumBandwidthRuleOutput)
}

func init() {
	pulumi.RegisterOutputType(QosMinimumBandwidthRuleOutput{})
	pulumi.RegisterOutputType(QosMinimumBandwidthRulePtrOutput{})
	pulumi.RegisterOutputType(QosMinimumBandwidthRuleArrayOutput{})
	pulumi.RegisterOutputType(QosMinimumBandwidthRuleMapOutput{})
}
