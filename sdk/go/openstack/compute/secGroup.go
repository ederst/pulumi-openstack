// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a V2 security group resource within OpenStack.
//
// Please note that managing security groups through the OpenStack Compute API
// has been deprecated. Unless you are using an older OpenStack environment, it is
// recommended to use the `networking.SecGroup`
// and `networking.SecGroupRule`
// resources instead, which uses the OpenStack Networking API.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/compute"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := compute.NewSecGroup(ctx, "secgroup1", &compute.SecGroupArgs{
// 			Description: pulumi.String("my security group"),
// 			Rules: compute.SecGroupRuleArray{
// 				&compute.SecGroupRuleArgs{
// 					Cidr:       pulumi.String("0.0.0.0/0"),
// 					FromPort:   pulumi.Int(22),
// 					IpProtocol: pulumi.String("tcp"),
// 					ToPort:     pulumi.Int(22),
// 				},
// 				&compute.SecGroupRuleArgs{
// 					Cidr:       pulumi.String("0.0.0.0/0"),
// 					FromPort:   pulumi.Int(80),
// 					IpProtocol: pulumi.String("tcp"),
// 					ToPort:     pulumi.Int(80),
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ## Notes
//
// ### ICMP Rules
//
// When using ICMP as the `ipProtocol`, the `fromPort` sets the ICMP _type_ and the `toPort` sets the ICMP _code_. To allow all ICMP types, set each value to `-1`, like so:
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		return nil
// 	})
// }
// ```
//
// A list of ICMP types and codes can be found [here](https://en.wikipedia.org/wiki/Internet_Control_Message_Protocol#Control_messages).
//
// ## Import
//
// Security Groups can be imported using the `id`, e.g.
//
// ```sh
//  $ pulumi import openstack:compute/secGroup:SecGroup my_secgroup 1bc30ee9-9d5b-4c30-bdd5-7f1e663f5edf
// ```
type SecGroup struct {
	pulumi.CustomResourceState

	// A description for the security group. Changing this
	// updates the `description` of an existing security group.
	Description pulumi.StringOutput `pulumi:"description"`
	// A unique name for the security group. Changing this
	// updates the `name` of an existing security group.
	Name pulumi.StringOutput `pulumi:"name"`
	// The region in which to obtain the V2 Compute client.
	// A Compute client is needed to create a security group. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// security group.
	Region pulumi.StringOutput `pulumi:"region"`
	// A rule describing how the security group operates. The
	// rule object structure is documented below. Changing this updates the
	// security group rules. As shown in the example above, multiple rule blocks
	// may be used.
	Rules SecGroupRuleArrayOutput `pulumi:"rules"`
}

// NewSecGroup registers a new resource with the given unique name, arguments, and options.
func NewSecGroup(ctx *pulumi.Context,
	name string, args *SecGroupArgs, opts ...pulumi.ResourceOption) (*SecGroup, error) {
	if args == nil || args.Description == nil {
		return nil, errors.New("missing required argument 'Description'")
	}
	if args == nil {
		args = &SecGroupArgs{}
	}
	var resource SecGroup
	err := ctx.RegisterResource("openstack:compute/secGroup:SecGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSecGroup gets an existing SecGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSecGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SecGroupState, opts ...pulumi.ResourceOption) (*SecGroup, error) {
	var resource SecGroup
	err := ctx.ReadResource("openstack:compute/secGroup:SecGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SecGroup resources.
type secGroupState struct {
	// A description for the security group. Changing this
	// updates the `description` of an existing security group.
	Description *string `pulumi:"description"`
	// A unique name for the security group. Changing this
	// updates the `name` of an existing security group.
	Name *string `pulumi:"name"`
	// The region in which to obtain the V2 Compute client.
	// A Compute client is needed to create a security group. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// security group.
	Region *string `pulumi:"region"`
	// A rule describing how the security group operates. The
	// rule object structure is documented below. Changing this updates the
	// security group rules. As shown in the example above, multiple rule blocks
	// may be used.
	Rules []SecGroupRule `pulumi:"rules"`
}

type SecGroupState struct {
	// A description for the security group. Changing this
	// updates the `description` of an existing security group.
	Description pulumi.StringPtrInput
	// A unique name for the security group. Changing this
	// updates the `name` of an existing security group.
	Name pulumi.StringPtrInput
	// The region in which to obtain the V2 Compute client.
	// A Compute client is needed to create a security group. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// security group.
	Region pulumi.StringPtrInput
	// A rule describing how the security group operates. The
	// rule object structure is documented below. Changing this updates the
	// security group rules. As shown in the example above, multiple rule blocks
	// may be used.
	Rules SecGroupRuleArrayInput
}

func (SecGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*secGroupState)(nil)).Elem()
}

type secGroupArgs struct {
	// A description for the security group. Changing this
	// updates the `description` of an existing security group.
	Description string `pulumi:"description"`
	// A unique name for the security group. Changing this
	// updates the `name` of an existing security group.
	Name *string `pulumi:"name"`
	// The region in which to obtain the V2 Compute client.
	// A Compute client is needed to create a security group. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// security group.
	Region *string `pulumi:"region"`
	// A rule describing how the security group operates. The
	// rule object structure is documented below. Changing this updates the
	// security group rules. As shown in the example above, multiple rule blocks
	// may be used.
	Rules []SecGroupRule `pulumi:"rules"`
}

// The set of arguments for constructing a SecGroup resource.
type SecGroupArgs struct {
	// A description for the security group. Changing this
	// updates the `description` of an existing security group.
	Description pulumi.StringInput
	// A unique name for the security group. Changing this
	// updates the `name` of an existing security group.
	Name pulumi.StringPtrInput
	// The region in which to obtain the V2 Compute client.
	// A Compute client is needed to create a security group. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// security group.
	Region pulumi.StringPtrInput
	// A rule describing how the security group operates. The
	// rule object structure is documented below. Changing this updates the
	// security group rules. As shown in the example above, multiple rule blocks
	// may be used.
	Rules SecGroupRuleArrayInput
}

func (SecGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*secGroupArgs)(nil)).Elem()
}

type SecGroupInput interface {
	pulumi.Input

	ToSecGroupOutput() SecGroupOutput
	ToSecGroupOutputWithContext(ctx context.Context) SecGroupOutput
}

func (SecGroup) ElementType() reflect.Type {
	return reflect.TypeOf((*SecGroup)(nil)).Elem()
}

func (i SecGroup) ToSecGroupOutput() SecGroupOutput {
	return i.ToSecGroupOutputWithContext(context.Background())
}

func (i SecGroup) ToSecGroupOutputWithContext(ctx context.Context) SecGroupOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SecGroupOutput)
}

type SecGroupOutput struct {
	*pulumi.OutputState
}

func (SecGroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SecGroupOutput)(nil)).Elem()
}

func (o SecGroupOutput) ToSecGroupOutput() SecGroupOutput {
	return o
}

func (o SecGroupOutput) ToSecGroupOutputWithContext(ctx context.Context) SecGroupOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(SecGroupOutput{})
}
