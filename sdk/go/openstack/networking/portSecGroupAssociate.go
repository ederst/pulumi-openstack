// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package networking

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type PortSecGroupAssociate struct {
	pulumi.CustomResourceState

	// The collection of Security Group IDs on the port
	// which have been explicitly and implicitly added.
	AllSecurityGroupIds pulumi.StringArrayOutput `pulumi:"allSecurityGroupIds"`
	// Whether to replace or append the list of security
	// groups, specified in the `securityGroupIds`. Defaults to `false`.
	Enforce pulumi.BoolPtrOutput `pulumi:"enforce"`
	// An UUID of the port to apply security groups to.
	PortId pulumi.StringOutput `pulumi:"portId"`
	// The region in which to obtain the V2 networking client.
	// A networking client is needed to manage a port. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// resource.
	Region pulumi.StringOutput `pulumi:"region"`
	// A list of security group IDs to apply to
	// the port. The security groups must be specified by ID and not name (as
	// opposed to how they are configured with the Compute Instance).
	SecurityGroupIds pulumi.StringArrayOutput `pulumi:"securityGroupIds"`
}

// NewPortSecGroupAssociate registers a new resource with the given unique name, arguments, and options.
func NewPortSecGroupAssociate(ctx *pulumi.Context,
	name string, args *PortSecGroupAssociateArgs, opts ...pulumi.ResourceOption) (*PortSecGroupAssociate, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.PortId == nil {
		return nil, errors.New("invalid value for required argument 'PortId'")
	}
	if args.SecurityGroupIds == nil {
		return nil, errors.New("invalid value for required argument 'SecurityGroupIds'")
	}
	var resource PortSecGroupAssociate
	err := ctx.RegisterResource("openstack:networking/portSecGroupAssociate:PortSecGroupAssociate", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPortSecGroupAssociate gets an existing PortSecGroupAssociate resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPortSecGroupAssociate(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PortSecGroupAssociateState, opts ...pulumi.ResourceOption) (*PortSecGroupAssociate, error) {
	var resource PortSecGroupAssociate
	err := ctx.ReadResource("openstack:networking/portSecGroupAssociate:PortSecGroupAssociate", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering PortSecGroupAssociate resources.
type portSecGroupAssociateState struct {
	// The collection of Security Group IDs on the port
	// which have been explicitly and implicitly added.
	AllSecurityGroupIds []string `pulumi:"allSecurityGroupIds"`
	// Whether to replace or append the list of security
	// groups, specified in the `securityGroupIds`. Defaults to `false`.
	Enforce *bool `pulumi:"enforce"`
	// An UUID of the port to apply security groups to.
	PortId *string `pulumi:"portId"`
	// The region in which to obtain the V2 networking client.
	// A networking client is needed to manage a port. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// resource.
	Region *string `pulumi:"region"`
	// A list of security group IDs to apply to
	// the port. The security groups must be specified by ID and not name (as
	// opposed to how they are configured with the Compute Instance).
	SecurityGroupIds []string `pulumi:"securityGroupIds"`
}

type PortSecGroupAssociateState struct {
	// The collection of Security Group IDs on the port
	// which have been explicitly and implicitly added.
	AllSecurityGroupIds pulumi.StringArrayInput
	// Whether to replace or append the list of security
	// groups, specified in the `securityGroupIds`. Defaults to `false`.
	Enforce pulumi.BoolPtrInput
	// An UUID of the port to apply security groups to.
	PortId pulumi.StringPtrInput
	// The region in which to obtain the V2 networking client.
	// A networking client is needed to manage a port. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// resource.
	Region pulumi.StringPtrInput
	// A list of security group IDs to apply to
	// the port. The security groups must be specified by ID and not name (as
	// opposed to how they are configured with the Compute Instance).
	SecurityGroupIds pulumi.StringArrayInput
}

func (PortSecGroupAssociateState) ElementType() reflect.Type {
	return reflect.TypeOf((*portSecGroupAssociateState)(nil)).Elem()
}

type portSecGroupAssociateArgs struct {
	// Whether to replace or append the list of security
	// groups, specified in the `securityGroupIds`. Defaults to `false`.
	Enforce *bool `pulumi:"enforce"`
	// An UUID of the port to apply security groups to.
	PortId string `pulumi:"portId"`
	// The region in which to obtain the V2 networking client.
	// A networking client is needed to manage a port. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// resource.
	Region *string `pulumi:"region"`
	// A list of security group IDs to apply to
	// the port. The security groups must be specified by ID and not name (as
	// opposed to how they are configured with the Compute Instance).
	SecurityGroupIds []string `pulumi:"securityGroupIds"`
}

// The set of arguments for constructing a PortSecGroupAssociate resource.
type PortSecGroupAssociateArgs struct {
	// Whether to replace or append the list of security
	// groups, specified in the `securityGroupIds`. Defaults to `false`.
	Enforce pulumi.BoolPtrInput
	// An UUID of the port to apply security groups to.
	PortId pulumi.StringInput
	// The region in which to obtain the V2 networking client.
	// A networking client is needed to manage a port. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// resource.
	Region pulumi.StringPtrInput
	// A list of security group IDs to apply to
	// the port. The security groups must be specified by ID and not name (as
	// opposed to how they are configured with the Compute Instance).
	SecurityGroupIds pulumi.StringArrayInput
}

func (PortSecGroupAssociateArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*portSecGroupAssociateArgs)(nil)).Elem()
}

type PortSecGroupAssociateInput interface {
	pulumi.Input

	ToPortSecGroupAssociateOutput() PortSecGroupAssociateOutput
	ToPortSecGroupAssociateOutputWithContext(ctx context.Context) PortSecGroupAssociateOutput
}

func (*PortSecGroupAssociate) ElementType() reflect.Type {
	return reflect.TypeOf((*PortSecGroupAssociate)(nil))
}

func (i *PortSecGroupAssociate) ToPortSecGroupAssociateOutput() PortSecGroupAssociateOutput {
	return i.ToPortSecGroupAssociateOutputWithContext(context.Background())
}

func (i *PortSecGroupAssociate) ToPortSecGroupAssociateOutputWithContext(ctx context.Context) PortSecGroupAssociateOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PortSecGroupAssociateOutput)
}

func (i *PortSecGroupAssociate) ToPortSecGroupAssociatePtrOutput() PortSecGroupAssociatePtrOutput {
	return i.ToPortSecGroupAssociatePtrOutputWithContext(context.Background())
}

func (i *PortSecGroupAssociate) ToPortSecGroupAssociatePtrOutputWithContext(ctx context.Context) PortSecGroupAssociatePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PortSecGroupAssociatePtrOutput)
}

type PortSecGroupAssociatePtrInput interface {
	pulumi.Input

	ToPortSecGroupAssociatePtrOutput() PortSecGroupAssociatePtrOutput
	ToPortSecGroupAssociatePtrOutputWithContext(ctx context.Context) PortSecGroupAssociatePtrOutput
}

type portSecGroupAssociatePtrType PortSecGroupAssociateArgs

func (*portSecGroupAssociatePtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**PortSecGroupAssociate)(nil))
}

func (i *portSecGroupAssociatePtrType) ToPortSecGroupAssociatePtrOutput() PortSecGroupAssociatePtrOutput {
	return i.ToPortSecGroupAssociatePtrOutputWithContext(context.Background())
}

func (i *portSecGroupAssociatePtrType) ToPortSecGroupAssociatePtrOutputWithContext(ctx context.Context) PortSecGroupAssociatePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PortSecGroupAssociatePtrOutput)
}

// PortSecGroupAssociateArrayInput is an input type that accepts PortSecGroupAssociateArray and PortSecGroupAssociateArrayOutput values.
// You can construct a concrete instance of `PortSecGroupAssociateArrayInput` via:
//
//          PortSecGroupAssociateArray{ PortSecGroupAssociateArgs{...} }
type PortSecGroupAssociateArrayInput interface {
	pulumi.Input

	ToPortSecGroupAssociateArrayOutput() PortSecGroupAssociateArrayOutput
	ToPortSecGroupAssociateArrayOutputWithContext(context.Context) PortSecGroupAssociateArrayOutput
}

type PortSecGroupAssociateArray []PortSecGroupAssociateInput

func (PortSecGroupAssociateArray) ElementType() reflect.Type {
	return reflect.TypeOf(([]*PortSecGroupAssociate)(nil))
}

func (i PortSecGroupAssociateArray) ToPortSecGroupAssociateArrayOutput() PortSecGroupAssociateArrayOutput {
	return i.ToPortSecGroupAssociateArrayOutputWithContext(context.Background())
}

func (i PortSecGroupAssociateArray) ToPortSecGroupAssociateArrayOutputWithContext(ctx context.Context) PortSecGroupAssociateArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PortSecGroupAssociateArrayOutput)
}

// PortSecGroupAssociateMapInput is an input type that accepts PortSecGroupAssociateMap and PortSecGroupAssociateMapOutput values.
// You can construct a concrete instance of `PortSecGroupAssociateMapInput` via:
//
//          PortSecGroupAssociateMap{ "key": PortSecGroupAssociateArgs{...} }
type PortSecGroupAssociateMapInput interface {
	pulumi.Input

	ToPortSecGroupAssociateMapOutput() PortSecGroupAssociateMapOutput
	ToPortSecGroupAssociateMapOutputWithContext(context.Context) PortSecGroupAssociateMapOutput
}

type PortSecGroupAssociateMap map[string]PortSecGroupAssociateInput

func (PortSecGroupAssociateMap) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*PortSecGroupAssociate)(nil))
}

func (i PortSecGroupAssociateMap) ToPortSecGroupAssociateMapOutput() PortSecGroupAssociateMapOutput {
	return i.ToPortSecGroupAssociateMapOutputWithContext(context.Background())
}

func (i PortSecGroupAssociateMap) ToPortSecGroupAssociateMapOutputWithContext(ctx context.Context) PortSecGroupAssociateMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(PortSecGroupAssociateMapOutput)
}

type PortSecGroupAssociateOutput struct {
	*pulumi.OutputState
}

func (PortSecGroupAssociateOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*PortSecGroupAssociate)(nil))
}

func (o PortSecGroupAssociateOutput) ToPortSecGroupAssociateOutput() PortSecGroupAssociateOutput {
	return o
}

func (o PortSecGroupAssociateOutput) ToPortSecGroupAssociateOutputWithContext(ctx context.Context) PortSecGroupAssociateOutput {
	return o
}

func (o PortSecGroupAssociateOutput) ToPortSecGroupAssociatePtrOutput() PortSecGroupAssociatePtrOutput {
	return o.ToPortSecGroupAssociatePtrOutputWithContext(context.Background())
}

func (o PortSecGroupAssociateOutput) ToPortSecGroupAssociatePtrOutputWithContext(ctx context.Context) PortSecGroupAssociatePtrOutput {
	return o.ApplyT(func(v PortSecGroupAssociate) *PortSecGroupAssociate {
		return &v
	}).(PortSecGroupAssociatePtrOutput)
}

type PortSecGroupAssociatePtrOutput struct {
	*pulumi.OutputState
}

func (PortSecGroupAssociatePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**PortSecGroupAssociate)(nil))
}

func (o PortSecGroupAssociatePtrOutput) ToPortSecGroupAssociatePtrOutput() PortSecGroupAssociatePtrOutput {
	return o
}

func (o PortSecGroupAssociatePtrOutput) ToPortSecGroupAssociatePtrOutputWithContext(ctx context.Context) PortSecGroupAssociatePtrOutput {
	return o
}

type PortSecGroupAssociateArrayOutput struct{ *pulumi.OutputState }

func (PortSecGroupAssociateArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]PortSecGroupAssociate)(nil))
}

func (o PortSecGroupAssociateArrayOutput) ToPortSecGroupAssociateArrayOutput() PortSecGroupAssociateArrayOutput {
	return o
}

func (o PortSecGroupAssociateArrayOutput) ToPortSecGroupAssociateArrayOutputWithContext(ctx context.Context) PortSecGroupAssociateArrayOutput {
	return o
}

func (o PortSecGroupAssociateArrayOutput) Index(i pulumi.IntInput) PortSecGroupAssociateOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) PortSecGroupAssociate {
		return vs[0].([]PortSecGroupAssociate)[vs[1].(int)]
	}).(PortSecGroupAssociateOutput)
}

type PortSecGroupAssociateMapOutput struct{ *pulumi.OutputState }

func (PortSecGroupAssociateMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]PortSecGroupAssociate)(nil))
}

func (o PortSecGroupAssociateMapOutput) ToPortSecGroupAssociateMapOutput() PortSecGroupAssociateMapOutput {
	return o
}

func (o PortSecGroupAssociateMapOutput) ToPortSecGroupAssociateMapOutputWithContext(ctx context.Context) PortSecGroupAssociateMapOutput {
	return o
}

func (o PortSecGroupAssociateMapOutput) MapIndex(k pulumi.StringInput) PortSecGroupAssociateOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) PortSecGroupAssociate {
		return vs[0].(map[string]PortSecGroupAssociate)[vs[1].(string)]
	}).(PortSecGroupAssociateOutput)
}

func init() {
	pulumi.RegisterOutputType(PortSecGroupAssociateOutput{})
	pulumi.RegisterOutputType(PortSecGroupAssociatePtrOutput{})
	pulumi.RegisterOutputType(PortSecGroupAssociateArrayOutput{})
	pulumi.RegisterOutputType(PortSecGroupAssociateMapOutput{})
}
