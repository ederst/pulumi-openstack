// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package loadbalancer

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a V1 load balancer member resource within OpenStack.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/lb_member_v1.html.markdown.
type MemberV1 struct {
	pulumi.CustomResourceState

	// The IP address of the member. Changing this creates a
	// new member.
	Address pulumi.StringOutput `pulumi:"address"`
	// The administrative state of the member.
	// Acceptable values are 'true' and 'false'. Changing this value updates the
	// state of the existing member.
	AdminStateUp pulumi.BoolOutput `pulumi:"adminStateUp"`
	// The ID of the LB pool. Changing this creates a new
	// member.
	PoolId pulumi.StringOutput `pulumi:"poolId"`
	// An integer representing the port on which the member is
	// hosted. Changing this creates a new member.
	Port pulumi.IntOutput `pulumi:"port"`
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an LB member. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// LB member.
	Region pulumi.StringOutput `pulumi:"region"`
	// The owner of the member. Required if admin wants to
	// create a member for another tenant. Changing this creates a new member.
	TenantId pulumi.StringPtrOutput `pulumi:"tenantId"`
	Weight pulumi.IntOutput `pulumi:"weight"`
}

// NewMemberV1 registers a new resource with the given unique name, arguments, and options.
func NewMemberV1(ctx *pulumi.Context,
	name string, args *MemberV1Args, opts ...pulumi.ResourceOption) (*MemberV1, error) {
	if args == nil || args.Address == nil {
		return nil, errors.New("missing required argument 'Address'")
	}
	if args == nil || args.PoolId == nil {
		return nil, errors.New("missing required argument 'PoolId'")
	}
	if args == nil || args.Port == nil {
		return nil, errors.New("missing required argument 'Port'")
	}
	if args == nil {
		args = &MemberV1Args{}
	}
	var resource MemberV1
	err := ctx.RegisterResource("openstack:loadbalancer/memberV1:MemberV1", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetMemberV1 gets an existing MemberV1 resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetMemberV1(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *MemberV1State, opts ...pulumi.ResourceOption) (*MemberV1, error) {
	var resource MemberV1
	err := ctx.ReadResource("openstack:loadbalancer/memberV1:MemberV1", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering MemberV1 resources.
type memberV1State struct {
	// The IP address of the member. Changing this creates a
	// new member.
	Address *string `pulumi:"address"`
	// The administrative state of the member.
	// Acceptable values are 'true' and 'false'. Changing this value updates the
	// state of the existing member.
	AdminStateUp *bool `pulumi:"adminStateUp"`
	// The ID of the LB pool. Changing this creates a new
	// member.
	PoolId *string `pulumi:"poolId"`
	// An integer representing the port on which the member is
	// hosted. Changing this creates a new member.
	Port *int `pulumi:"port"`
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an LB member. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// LB member.
	Region *string `pulumi:"region"`
	// The owner of the member. Required if admin wants to
	// create a member for another tenant. Changing this creates a new member.
	TenantId *string `pulumi:"tenantId"`
	Weight *int `pulumi:"weight"`
}

type MemberV1State struct {
	// The IP address of the member. Changing this creates a
	// new member.
	Address pulumi.StringPtrInput
	// The administrative state of the member.
	// Acceptable values are 'true' and 'false'. Changing this value updates the
	// state of the existing member.
	AdminStateUp pulumi.BoolPtrInput
	// The ID of the LB pool. Changing this creates a new
	// member.
	PoolId pulumi.StringPtrInput
	// An integer representing the port on which the member is
	// hosted. Changing this creates a new member.
	Port pulumi.IntPtrInput
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an LB member. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// LB member.
	Region pulumi.StringPtrInput
	// The owner of the member. Required if admin wants to
	// create a member for another tenant. Changing this creates a new member.
	TenantId pulumi.StringPtrInput
	Weight pulumi.IntPtrInput
}

func (MemberV1State) ElementType() reflect.Type {
	return reflect.TypeOf((*memberV1State)(nil)).Elem()
}

type memberV1Args struct {
	// The IP address of the member. Changing this creates a
	// new member.
	Address string `pulumi:"address"`
	// The administrative state of the member.
	// Acceptable values are 'true' and 'false'. Changing this value updates the
	// state of the existing member.
	AdminStateUp *bool `pulumi:"adminStateUp"`
	// The ID of the LB pool. Changing this creates a new
	// member.
	PoolId string `pulumi:"poolId"`
	// An integer representing the port on which the member is
	// hosted. Changing this creates a new member.
	Port int `pulumi:"port"`
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an LB member. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// LB member.
	Region *string `pulumi:"region"`
	// The owner of the member. Required if admin wants to
	// create a member for another tenant. Changing this creates a new member.
	TenantId *string `pulumi:"tenantId"`
	Weight *int `pulumi:"weight"`
}

// The set of arguments for constructing a MemberV1 resource.
type MemberV1Args struct {
	// The IP address of the member. Changing this creates a
	// new member.
	Address pulumi.StringInput
	// The administrative state of the member.
	// Acceptable values are 'true' and 'false'. Changing this value updates the
	// state of the existing member.
	AdminStateUp pulumi.BoolPtrInput
	// The ID of the LB pool. Changing this creates a new
	// member.
	PoolId pulumi.StringInput
	// An integer representing the port on which the member is
	// hosted. Changing this creates a new member.
	Port pulumi.IntInput
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an LB member. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// LB member.
	Region pulumi.StringPtrInput
	// The owner of the member. Required if admin wants to
	// create a member for another tenant. Changing this creates a new member.
	TenantId pulumi.StringPtrInput
	Weight pulumi.IntPtrInput
}

func (MemberV1Args) ElementType() reflect.Type {
	return reflect.TypeOf((*memberV1Args)(nil)).Elem()
}

