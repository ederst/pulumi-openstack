// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a V2 floating IP resource within OpenStack Nova (compute)
// that can be used for compute instances.
// 
// Please note that managing floating IPs through the OpenStack Compute API has
// been deprecated. Unless you are using an older OpenStack environment, it is
// recommended to use the [`openstack_networking_floatingip_v2`](networking_floatingip_v2.html)
// resource instead, which uses the OpenStack Networking API.
type FloatingIP struct {
	s *pulumi.ResourceState
}

// NewFloatingIP registers a new resource with the given unique name, arguments, and options.
func NewFloatingIP(ctx *pulumi.Context,
	name string, args *FloatingIPArgs, opts ...pulumi.ResourceOpt) (*FloatingIP, error) {
	if args == nil || args.Pool == nil {
		return nil, errors.New("missing required argument 'Pool'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["pool"] = nil
		inputs["region"] = nil
	} else {
		inputs["pool"] = args.Pool
		inputs["region"] = args.Region
	}
	inputs["address"] = nil
	inputs["fixedIp"] = nil
	inputs["instanceId"] = nil
	s, err := ctx.RegisterResource("openstack:compute/floatingIP:FloatingIP", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &FloatingIP{s: s}, nil
}

// GetFloatingIP gets an existing FloatingIP resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFloatingIP(ctx *pulumi.Context,
	name string, id pulumi.ID, state *FloatingIPState, opts ...pulumi.ResourceOpt) (*FloatingIP, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["address"] = state.Address
		inputs["fixedIp"] = state.FixedIp
		inputs["instanceId"] = state.InstanceId
		inputs["pool"] = state.Pool
		inputs["region"] = state.Region
	}
	s, err := ctx.ReadResource("openstack:compute/floatingIP:FloatingIP", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &FloatingIP{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *FloatingIP) URN() *pulumi.URNOutput {
	return r.s.URN
}

// ID is this resource's unique identifier assigned by its provider.
func (r *FloatingIP) ID() *pulumi.IDOutput {
	return r.s.ID
}

// The actual floating IP address itself.
func (r *FloatingIP) Address() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["address"])
}

// The fixed IP address corresponding to the floating IP.
func (r *FloatingIP) FixedIp() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["fixedIp"])
}

// UUID of the compute instance associated with the floating IP.
func (r *FloatingIP) InstanceId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["instanceId"])
}

// The name of the pool from which to obtain the floating
// IP. Changing this creates a new floating IP.
func (r *FloatingIP) Pool() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["pool"])
}

// The region in which to obtain the V2 Compute client.
// A Compute client is needed to create a floating IP that can be used with
// a compute instance. If omitted, the `region` argument of the provider
// is used. Changing this creates a new floating IP (which may or may not
// have a different address).
func (r *FloatingIP) Region() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["region"])
}

// Input properties used for looking up and filtering FloatingIP resources.
type FloatingIPState struct {
	// The actual floating IP address itself.
	Address interface{}
	// The fixed IP address corresponding to the floating IP.
	FixedIp interface{}
	// UUID of the compute instance associated with the floating IP.
	InstanceId interface{}
	// The name of the pool from which to obtain the floating
	// IP. Changing this creates a new floating IP.
	Pool interface{}
	// The region in which to obtain the V2 Compute client.
	// A Compute client is needed to create a floating IP that can be used with
	// a compute instance. If omitted, the `region` argument of the provider
	// is used. Changing this creates a new floating IP (which may or may not
	// have a different address).
	Region interface{}
}

// The set of arguments for constructing a FloatingIP resource.
type FloatingIPArgs struct {
	// The name of the pool from which to obtain the floating
	// IP. Changing this creates a new floating IP.
	Pool interface{}
	// The region in which to obtain the V2 Compute client.
	// A Compute client is needed to create a floating IP that can be used with
	// a compute instance. If omitted, the `region` argument of the provider
	// is used. Changing this creates a new floating IP (which may or may not
	// have a different address).
	Region interface{}
}