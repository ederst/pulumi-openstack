// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package networking

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a networking V2 trunk resource within OpenStack.
type Trunk struct {
	s *pulumi.ResourceState
}

// NewTrunk registers a new resource with the given unique name, arguments, and options.
func NewTrunk(ctx *pulumi.Context,
	name string, args *TrunkArgs, opts ...pulumi.ResourceOpt) (*Trunk, error) {
	if args == nil || args.PortId == nil {
		return nil, errors.New("missing required argument 'PortId'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["adminStateUp"] = nil
		inputs["name"] = nil
		inputs["portId"] = nil
		inputs["region"] = nil
		inputs["subPorts"] = nil
		inputs["tags"] = nil
		inputs["tenantId"] = nil
	} else {
		inputs["adminStateUp"] = args.AdminStateUp
		inputs["name"] = args.Name
		inputs["portId"] = args.PortId
		inputs["region"] = args.Region
		inputs["subPorts"] = args.SubPorts
		inputs["tags"] = args.Tags
		inputs["tenantId"] = args.TenantId
	}
	s, err := ctx.RegisterResource("openstack:networking/trunk:Trunk", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Trunk{s: s}, nil
}

// GetTrunk gets an existing Trunk resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetTrunk(ctx *pulumi.Context,
	name string, id pulumi.ID, state *TrunkState, opts ...pulumi.ResourceOpt) (*Trunk, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["adminStateUp"] = state.AdminStateUp
		inputs["name"] = state.Name
		inputs["portId"] = state.PortId
		inputs["region"] = state.Region
		inputs["subPorts"] = state.SubPorts
		inputs["tags"] = state.Tags
		inputs["tenantId"] = state.TenantId
	}
	s, err := ctx.ReadResource("openstack:networking/trunk:Trunk", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Trunk{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Trunk) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Trunk) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// Administrative up/down status for the trunk
// (must be "true" or "false" if provided). Changing this updates the
// `admin_state_up` of an existing trunk.
func (r *Trunk) AdminStateUp() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["adminStateUp"])
}

// A unique name for the port. Changing this
// updates the `name` of an existing port.
func (r *Trunk) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The ID of the port to be used as the parent port of the
// trunk. This is the port that should be used as the compute instance network
// port. Changing this creates a new trunk.
func (r *Trunk) PortId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["portId"])
}

// The region in which to obtain the V2 networking client.
// A networking client is needed to create a trunk. If omitted, the
// `region` argument of the provider is used. Changing this creates a new
// trunk.
func (r *Trunk) Region() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["region"])
}

// The set of ports that will be made subports of the trunk.
// The structure of each subport is described below.
func (r *Trunk) SubPorts() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["subPorts"])
}

func (r *Trunk) Tags() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["tags"])
}

// The owner of the Trunk. Required if admin wants
// to create a trunk on behalf of another tenant. Changing this creates a new trunk.
func (r *Trunk) TenantId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["tenantId"])
}

// Input properties used for looking up and filtering Trunk resources.
type TrunkState struct {
	// Administrative up/down status for the trunk
	// (must be "true" or "false" if provided). Changing this updates the
	// `admin_state_up` of an existing trunk.
	AdminStateUp interface{}
	// A unique name for the port. Changing this
	// updates the `name` of an existing port.
	Name interface{}
	// The ID of the port to be used as the parent port of the
	// trunk. This is the port that should be used as the compute instance network
	// port. Changing this creates a new trunk.
	PortId interface{}
	// The region in which to obtain the V2 networking client.
	// A networking client is needed to create a trunk. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// trunk.
	Region interface{}
	// The set of ports that will be made subports of the trunk.
	// The structure of each subport is described below.
	SubPorts interface{}
	Tags interface{}
	// The owner of the Trunk. Required if admin wants
	// to create a trunk on behalf of another tenant. Changing this creates a new trunk.
	TenantId interface{}
}

// The set of arguments for constructing a Trunk resource.
type TrunkArgs struct {
	// Administrative up/down status for the trunk
	// (must be "true" or "false" if provided). Changing this updates the
	// `admin_state_up` of an existing trunk.
	AdminStateUp interface{}
	// A unique name for the port. Changing this
	// updates the `name` of an existing port.
	Name interface{}
	// The ID of the port to be used as the parent port of the
	// trunk. This is the port that should be used as the compute instance network
	// port. Changing this creates a new trunk.
	PortId interface{}
	// The region in which to obtain the V2 networking client.
	// A networking client is needed to create a trunk. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// trunk.
	Region interface{}
	// The set of ports that will be made subports of the trunk.
	// The structure of each subport is described below.
	SubPorts interface{}
	Tags interface{}
	// The owner of the Trunk. Required if admin wants
	// to create a trunk on behalf of another tenant. Changing this creates a new trunk.
	TenantId interface{}
}
