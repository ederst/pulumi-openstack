// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package loadbalancer

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a V2 members resource within OpenStack (batch members update).
//
// > **Note:** This resource works only within Octavia API. For
// legacy Neutron LBaaS v2 extension please use
// loadbalancer.Member resource.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/loadbalancer"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := loadbalancer.NewMembers(ctx, "members1", &loadbalancer.MembersArgs{
// 			Members: loadbalancer.MembersMemberArray{
// 				&loadbalancer.MembersMemberArgs{
// 					Address:      pulumi.String("192.168.199.23"),
// 					ProtocolPort: pulumi.Int(8080),
// 				},
// 				&loadbalancer.MembersMemberArgs{
// 					Address:      pulumi.String("192.168.199.24"),
// 					ProtocolPort: pulumi.Int(8080),
// 				},
// 			},
// 			PoolId: pulumi.String("935685fb-a896-40f9-9ff4-ae531a3a00fe"),
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
// Load Balancer Pool Members can be imported using the Pool ID, e.g.
//
// ```sh
//  $ pulumi import openstack:loadbalancer/members:Members members_1 c22974d2-4c95-4bcb-9819-0afc5ed303d5
// ```
type Members struct {
	pulumi.CustomResourceState

	// A set of dictionaries containing member parameters. The
	// structure is described below.
	Members MembersMemberArrayOutput `pulumi:"members"`
	// The id of the pool that members will be assigned to.
	// Changing this creates a new members resource.
	PoolId pulumi.StringOutput `pulumi:"poolId"`
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create pool members. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// members resource.
	Region pulumi.StringOutput `pulumi:"region"`
}

// NewMembers registers a new resource with the given unique name, arguments, and options.
func NewMembers(ctx *pulumi.Context,
	name string, args *MembersArgs, opts ...pulumi.ResourceOption) (*Members, error) {
	if args == nil || args.PoolId == nil {
		return nil, errors.New("missing required argument 'PoolId'")
	}
	if args == nil {
		args = &MembersArgs{}
	}
	var resource Members
	err := ctx.RegisterResource("openstack:loadbalancer/members:Members", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetMembers gets an existing Members resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetMembers(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *MembersState, opts ...pulumi.ResourceOption) (*Members, error) {
	var resource Members
	err := ctx.ReadResource("openstack:loadbalancer/members:Members", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Members resources.
type membersState struct {
	// A set of dictionaries containing member parameters. The
	// structure is described below.
	Members []MembersMember `pulumi:"members"`
	// The id of the pool that members will be assigned to.
	// Changing this creates a new members resource.
	PoolId *string `pulumi:"poolId"`
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create pool members. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// members resource.
	Region *string `pulumi:"region"`
}

type MembersState struct {
	// A set of dictionaries containing member parameters. The
	// structure is described below.
	Members MembersMemberArrayInput
	// The id of the pool that members will be assigned to.
	// Changing this creates a new members resource.
	PoolId pulumi.StringPtrInput
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create pool members. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// members resource.
	Region pulumi.StringPtrInput
}

func (MembersState) ElementType() reflect.Type {
	return reflect.TypeOf((*membersState)(nil)).Elem()
}

type membersArgs struct {
	// A set of dictionaries containing member parameters. The
	// structure is described below.
	Members []MembersMember `pulumi:"members"`
	// The id of the pool that members will be assigned to.
	// Changing this creates a new members resource.
	PoolId string `pulumi:"poolId"`
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create pool members. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// members resource.
	Region *string `pulumi:"region"`
}

// The set of arguments for constructing a Members resource.
type MembersArgs struct {
	// A set of dictionaries containing member parameters. The
	// structure is described below.
	Members MembersMemberArrayInput
	// The id of the pool that members will be assigned to.
	// Changing this creates a new members resource.
	PoolId pulumi.StringInput
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create pool members. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// members resource.
	Region pulumi.StringPtrInput
}

func (MembersArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*membersArgs)(nil)).Elem()
}

type MembersInput interface {
	pulumi.Input

	ToMembersOutput() MembersOutput
	ToMembersOutputWithContext(ctx context.Context) MembersOutput
}

func (Members) ElementType() reflect.Type {
	return reflect.TypeOf((*Members)(nil)).Elem()
}

func (i Members) ToMembersOutput() MembersOutput {
	return i.ToMembersOutputWithContext(context.Background())
}

func (i Members) ToMembersOutputWithContext(ctx context.Context) MembersOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MembersOutput)
}

type MembersOutput struct {
	*pulumi.OutputState
}

func (MembersOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*MembersOutput)(nil)).Elem()
}

func (o MembersOutput) ToMembersOutput() MembersOutput {
	return o
}

func (o MembersOutput) ToMembersOutputWithContext(ctx context.Context) MembersOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(MembersOutput{})
}
