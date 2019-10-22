// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package loadbalancer

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a V2 loadbalancer resource within OpenStack.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/lb_loadbalancer_v2.html.markdown.
type LoadBalancer struct {
	s *pulumi.ResourceState
}

// NewLoadBalancer registers a new resource with the given unique name, arguments, and options.
func NewLoadBalancer(ctx *pulumi.Context,
	name string, args *LoadBalancerArgs, opts ...pulumi.ResourceOpt) (*LoadBalancer, error) {
	if args == nil || args.VipSubnetId == nil {
		return nil, errors.New("missing required argument 'VipSubnetId'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["adminStateUp"] = nil
		inputs["description"] = nil
		inputs["flavorId"] = nil
		inputs["loadbalancerProvider"] = nil
		inputs["name"] = nil
		inputs["region"] = nil
		inputs["securityGroupIds"] = nil
		inputs["tenantId"] = nil
		inputs["vipAddress"] = nil
		inputs["vipSubnetId"] = nil
	} else {
		inputs["adminStateUp"] = args.AdminStateUp
		inputs["description"] = args.Description
		inputs["flavorId"] = args.FlavorId
		inputs["loadbalancerProvider"] = args.LoadbalancerProvider
		inputs["name"] = args.Name
		inputs["region"] = args.Region
		inputs["securityGroupIds"] = args.SecurityGroupIds
		inputs["tenantId"] = args.TenantId
		inputs["vipAddress"] = args.VipAddress
		inputs["vipSubnetId"] = args.VipSubnetId
	}
	inputs["vipPortId"] = nil
	s, err := ctx.RegisterResource("openstack:loadbalancer/loadBalancer:LoadBalancer", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &LoadBalancer{s: s}, nil
}

// GetLoadBalancer gets an existing LoadBalancer resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLoadBalancer(ctx *pulumi.Context,
	name string, id pulumi.ID, state *LoadBalancerState, opts ...pulumi.ResourceOpt) (*LoadBalancer, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["adminStateUp"] = state.AdminStateUp
		inputs["description"] = state.Description
		inputs["flavorId"] = state.FlavorId
		inputs["loadbalancerProvider"] = state.LoadbalancerProvider
		inputs["name"] = state.Name
		inputs["region"] = state.Region
		inputs["securityGroupIds"] = state.SecurityGroupIds
		inputs["tenantId"] = state.TenantId
		inputs["vipAddress"] = state.VipAddress
		inputs["vipPortId"] = state.VipPortId
		inputs["vipSubnetId"] = state.VipSubnetId
	}
	s, err := ctx.ReadResource("openstack:loadbalancer/loadBalancer:LoadBalancer", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &LoadBalancer{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *LoadBalancer) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *LoadBalancer) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The administrative state of the Loadbalancer.
// A valid value is true (UP) or false (DOWN).
func (r *LoadBalancer) AdminStateUp() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["adminStateUp"])
}

// Human-readable description for the Loadbalancer.
func (r *LoadBalancer) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

// The UUID of a flavor. Changing this creates a new
// loadbalancer.
func (r *LoadBalancer) FlavorId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["flavorId"])
}

// The name of the provider. Changing this
// creates a new loadbalancer.
func (r *LoadBalancer) LoadbalancerProvider() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["loadbalancerProvider"])
}

// Human-readable name for the Loadbalancer. Does not have
// to be unique.
func (r *LoadBalancer) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The region in which to obtain the V2 Networking client.
// A Networking client is needed to create an LB member. If omitted, the
// `region` argument of the provider is used. Changing this creates a new
// LB member.
func (r *LoadBalancer) Region() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["region"])
}

// A list of security group IDs to apply to the
// loadbalancer. The security groups must be specified by ID and not name (as
// opposed to how they are configured with the Compute Instance).
func (r *LoadBalancer) SecurityGroupIds() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["securityGroupIds"])
}

// Required for admins. The UUID of the tenant who owns
// the Loadbalancer.  Only administrative users can specify a tenant UUID
// other than their own.  Changing this creates a new loadbalancer.
func (r *LoadBalancer) TenantId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["tenantId"])
}

// The ip address of the load balancer.
// Changing this creates a new loadbalancer.
func (r *LoadBalancer) VipAddress() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["vipAddress"])
}

// The Port ID of the Load Balancer IP.
func (r *LoadBalancer) VipPortId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["vipPortId"])
}

// The network on which to allocate the
// Loadbalancer's address. A tenant can only create Loadbalancers on networks
// authorized by policy (e.g. networks that belong to them or networks that
// are shared).  Changing this creates a new loadbalancer.
func (r *LoadBalancer) VipSubnetId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["vipSubnetId"])
}

// Input properties used for looking up and filtering LoadBalancer resources.
type LoadBalancerState struct {
	// The administrative state of the Loadbalancer.
	// A valid value is true (UP) or false (DOWN).
	AdminStateUp interface{}
	// Human-readable description for the Loadbalancer.
	Description interface{}
	// The UUID of a flavor. Changing this creates a new
	// loadbalancer.
	FlavorId interface{}
	// The name of the provider. Changing this
	// creates a new loadbalancer.
	LoadbalancerProvider interface{}
	// Human-readable name for the Loadbalancer. Does not have
	// to be unique.
	Name interface{}
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an LB member. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// LB member.
	Region interface{}
	// A list of security group IDs to apply to the
	// loadbalancer. The security groups must be specified by ID and not name (as
	// opposed to how they are configured with the Compute Instance).
	SecurityGroupIds interface{}
	// Required for admins. The UUID of the tenant who owns
	// the Loadbalancer.  Only administrative users can specify a tenant UUID
	// other than their own.  Changing this creates a new loadbalancer.
	TenantId interface{}
	// The ip address of the load balancer.
	// Changing this creates a new loadbalancer.
	VipAddress interface{}
	// The Port ID of the Load Balancer IP.
	VipPortId interface{}
	// The network on which to allocate the
	// Loadbalancer's address. A tenant can only create Loadbalancers on networks
	// authorized by policy (e.g. networks that belong to them or networks that
	// are shared).  Changing this creates a new loadbalancer.
	VipSubnetId interface{}
}

// The set of arguments for constructing a LoadBalancer resource.
type LoadBalancerArgs struct {
	// The administrative state of the Loadbalancer.
	// A valid value is true (UP) or false (DOWN).
	AdminStateUp interface{}
	// Human-readable description for the Loadbalancer.
	Description interface{}
	// The UUID of a flavor. Changing this creates a new
	// loadbalancer.
	FlavorId interface{}
	// The name of the provider. Changing this
	// creates a new loadbalancer.
	LoadbalancerProvider interface{}
	// Human-readable name for the Loadbalancer. Does not have
	// to be unique.
	Name interface{}
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an LB member. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// LB member.
	Region interface{}
	// A list of security group IDs to apply to the
	// loadbalancer. The security groups must be specified by ID and not name (as
	// opposed to how they are configured with the Compute Instance).
	SecurityGroupIds interface{}
	// Required for admins. The UUID of the tenant who owns
	// the Loadbalancer.  Only administrative users can specify a tenant UUID
	// other than their own.  Changing this creates a new loadbalancer.
	TenantId interface{}
	// The ip address of the load balancer.
	// Changing this creates a new loadbalancer.
	VipAddress interface{}
	// The network on which to allocate the
	// Loadbalancer's address. A tenant can only create Loadbalancers on networks
	// authorized by policy (e.g. networks that belong to them or networks that
	// are shared).  Changing this creates a new loadbalancer.
	VipSubnetId interface{}
}
