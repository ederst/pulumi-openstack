// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package loadbalancer

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a V1 load balancer pool resource within OpenStack.
//
// ## Notes
//
// The `member` block is deprecated in favor of the `loadbalancer.MemberV1` resource.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/lb_pool_v1.html.markdown.
type PoolV1 struct {
	pulumi.CustomResourceState

	// The algorithm used to distribute load between the
	// members of the pool. The current specification supports 'ROUND_ROBIN' and
	// 'LEAST_CONNECTIONS' as valid values for this attribute.
	LbMethod pulumi.StringOutput `pulumi:"lbMethod"`
	// The backend load balancing provider. For example:
	// `haproxy`, `F5`, etc.
	LbProvider pulumi.StringOutput `pulumi:"lbProvider"`
	// A list of IDs of monitors to associate with the
	// pool.
	MonitorIds pulumi.StringArrayOutput `pulumi:"monitorIds"`
	// The name of the pool. Changing this updates the name of
	// the existing pool.
	Name pulumi.StringOutput `pulumi:"name"`
	// The protocol used by the pool members, you can use
	// either 'TCP, 'HTTP', or 'HTTPS'. Changing this creates a new pool.
	Protocol pulumi.StringOutput `pulumi:"protocol"`
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an LB pool. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// LB pool.
	Region pulumi.StringOutput `pulumi:"region"`
	// The network on which the members of the pool will be
	// located. Only members that are on this network can be added to the pool.
	// Changing this creates a new pool.
	SubnetId pulumi.StringOutput `pulumi:"subnetId"`
	// The owner of the member. Required if admin wants to
	// create a pool member for another tenant. Changing this creates a new member.
	TenantId pulumi.StringOutput `pulumi:"tenantId"`
}

// NewPoolV1 registers a new resource with the given unique name, arguments, and options.
func NewPoolV1(ctx *pulumi.Context,
	name string, args *PoolV1Args, opts ...pulumi.ResourceOption) (*PoolV1, error) {
	if args == nil || args.LbMethod == nil {
		return nil, errors.New("missing required argument 'LbMethod'")
	}
	if args == nil || args.Protocol == nil {
		return nil, errors.New("missing required argument 'Protocol'")
	}
	if args == nil || args.SubnetId == nil {
		return nil, errors.New("missing required argument 'SubnetId'")
	}
	if args == nil {
		args = &PoolV1Args{}
	}
	var resource PoolV1
	err := ctx.RegisterResource("openstack:loadbalancer/poolV1:PoolV1", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetPoolV1 gets an existing PoolV1 resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetPoolV1(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *PoolV1State, opts ...pulumi.ResourceOption) (*PoolV1, error) {
	var resource PoolV1
	err := ctx.ReadResource("openstack:loadbalancer/poolV1:PoolV1", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering PoolV1 resources.
type poolV1State struct {
	// The algorithm used to distribute load between the
	// members of the pool. The current specification supports 'ROUND_ROBIN' and
	// 'LEAST_CONNECTIONS' as valid values for this attribute.
	LbMethod *string `pulumi:"lbMethod"`
	// The backend load balancing provider. For example:
	// `haproxy`, `F5`, etc.
	LbProvider *string `pulumi:"lbProvider"`
	// A list of IDs of monitors to associate with the
	// pool.
	MonitorIds []string `pulumi:"monitorIds"`
	// The name of the pool. Changing this updates the name of
	// the existing pool.
	Name *string `pulumi:"name"`
	// The protocol used by the pool members, you can use
	// either 'TCP, 'HTTP', or 'HTTPS'. Changing this creates a new pool.
	Protocol *string `pulumi:"protocol"`
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an LB pool. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// LB pool.
	Region *string `pulumi:"region"`
	// The network on which the members of the pool will be
	// located. Only members that are on this network can be added to the pool.
	// Changing this creates a new pool.
	SubnetId *string `pulumi:"subnetId"`
	// The owner of the member. Required if admin wants to
	// create a pool member for another tenant. Changing this creates a new member.
	TenantId *string `pulumi:"tenantId"`
}

type PoolV1State struct {
	// The algorithm used to distribute load between the
	// members of the pool. The current specification supports 'ROUND_ROBIN' and
	// 'LEAST_CONNECTIONS' as valid values for this attribute.
	LbMethod pulumi.StringPtrInput
	// The backend load balancing provider. For example:
	// `haproxy`, `F5`, etc.
	LbProvider pulumi.StringPtrInput
	// A list of IDs of monitors to associate with the
	// pool.
	MonitorIds pulumi.StringArrayInput
	// The name of the pool. Changing this updates the name of
	// the existing pool.
	Name pulumi.StringPtrInput
	// The protocol used by the pool members, you can use
	// either 'TCP, 'HTTP', or 'HTTPS'. Changing this creates a new pool.
	Protocol pulumi.StringPtrInput
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an LB pool. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// LB pool.
	Region pulumi.StringPtrInput
	// The network on which the members of the pool will be
	// located. Only members that are on this network can be added to the pool.
	// Changing this creates a new pool.
	SubnetId pulumi.StringPtrInput
	// The owner of the member. Required if admin wants to
	// create a pool member for another tenant. Changing this creates a new member.
	TenantId pulumi.StringPtrInput
}

func (PoolV1State) ElementType() reflect.Type {
	return reflect.TypeOf((*poolV1State)(nil)).Elem()
}

type poolV1Args struct {
	// The algorithm used to distribute load between the
	// members of the pool. The current specification supports 'ROUND_ROBIN' and
	// 'LEAST_CONNECTIONS' as valid values for this attribute.
	LbMethod string `pulumi:"lbMethod"`
	// The backend load balancing provider. For example:
	// `haproxy`, `F5`, etc.
	LbProvider *string `pulumi:"lbProvider"`
	// A list of IDs of monitors to associate with the
	// pool.
	MonitorIds []string `pulumi:"monitorIds"`
	// The name of the pool. Changing this updates the name of
	// the existing pool.
	Name *string `pulumi:"name"`
	// The protocol used by the pool members, you can use
	// either 'TCP, 'HTTP', or 'HTTPS'. Changing this creates a new pool.
	Protocol string `pulumi:"protocol"`
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an LB pool. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// LB pool.
	Region *string `pulumi:"region"`
	// The network on which the members of the pool will be
	// located. Only members that are on this network can be added to the pool.
	// Changing this creates a new pool.
	SubnetId string `pulumi:"subnetId"`
	// The owner of the member. Required if admin wants to
	// create a pool member for another tenant. Changing this creates a new member.
	TenantId *string `pulumi:"tenantId"`
}

// The set of arguments for constructing a PoolV1 resource.
type PoolV1Args struct {
	// The algorithm used to distribute load between the
	// members of the pool. The current specification supports 'ROUND_ROBIN' and
	// 'LEAST_CONNECTIONS' as valid values for this attribute.
	LbMethod pulumi.StringInput
	// The backend load balancing provider. For example:
	// `haproxy`, `F5`, etc.
	LbProvider pulumi.StringPtrInput
	// A list of IDs of monitors to associate with the
	// pool.
	MonitorIds pulumi.StringArrayInput
	// The name of the pool. Changing this updates the name of
	// the existing pool.
	Name pulumi.StringPtrInput
	// The protocol used by the pool members, you can use
	// either 'TCP, 'HTTP', or 'HTTPS'. Changing this creates a new pool.
	Protocol pulumi.StringInput
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an LB pool. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// LB pool.
	Region pulumi.StringPtrInput
	// The network on which the members of the pool will be
	// located. Only members that are on this network can be added to the pool.
	// Changing this creates a new pool.
	SubnetId pulumi.StringInput
	// The owner of the member. Required if admin wants to
	// create a pool member for another tenant. Changing this creates a new member.
	TenantId pulumi.StringPtrInput
}

func (PoolV1Args) ElementType() reflect.Type {
	return reflect.TypeOf((*poolV1Args)(nil)).Elem()
}
