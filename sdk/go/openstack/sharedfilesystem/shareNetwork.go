// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sharedfilesystem

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this resource to configure a share network.
// 
// A share network stores network information that share servers can use when
// shares are created.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/sharedfilesystem_sharenetwork_v2.html.markdown.
type ShareNetwork struct {
	s *pulumi.ResourceState
}

// NewShareNetwork registers a new resource with the given unique name, arguments, and options.
func NewShareNetwork(ctx *pulumi.Context,
	name string, args *ShareNetworkArgs, opts ...pulumi.ResourceOpt) (*ShareNetwork, error) {
	if args == nil || args.NeutronNetId == nil {
		return nil, errors.New("missing required argument 'NeutronNetId'")
	}
	if args == nil || args.NeutronSubnetId == nil {
		return nil, errors.New("missing required argument 'NeutronSubnetId'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["description"] = nil
		inputs["name"] = nil
		inputs["neutronNetId"] = nil
		inputs["neutronSubnetId"] = nil
		inputs["region"] = nil
		inputs["securityServiceIds"] = nil
	} else {
		inputs["description"] = args.Description
		inputs["name"] = args.Name
		inputs["neutronNetId"] = args.NeutronNetId
		inputs["neutronSubnetId"] = args.NeutronSubnetId
		inputs["region"] = args.Region
		inputs["securityServiceIds"] = args.SecurityServiceIds
	}
	inputs["cidr"] = nil
	inputs["ipVersion"] = nil
	inputs["networkType"] = nil
	inputs["projectId"] = nil
	inputs["segmentationId"] = nil
	s, err := ctx.RegisterResource("openstack:sharedfilesystem/shareNetwork:ShareNetwork", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ShareNetwork{s: s}, nil
}

// GetShareNetwork gets an existing ShareNetwork resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetShareNetwork(ctx *pulumi.Context,
	name string, id pulumi.ID, state *ShareNetworkState, opts ...pulumi.ResourceOpt) (*ShareNetwork, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["cidr"] = state.Cidr
		inputs["description"] = state.Description
		inputs["ipVersion"] = state.IpVersion
		inputs["name"] = state.Name
		inputs["networkType"] = state.NetworkType
		inputs["neutronNetId"] = state.NeutronNetId
		inputs["neutronSubnetId"] = state.NeutronSubnetId
		inputs["projectId"] = state.ProjectId
		inputs["region"] = state.Region
		inputs["securityServiceIds"] = state.SecurityServiceIds
		inputs["segmentationId"] = state.SegmentationId
	}
	s, err := ctx.ReadResource("openstack:sharedfilesystem/shareNetwork:ShareNetwork", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ShareNetwork{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *ShareNetwork) URN() pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *ShareNetwork) ID() pulumi.IDOutput {
	return r.s.ID()
}

// The share network CIDR.
func (r *ShareNetwork) Cidr() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["cidr"])
}

// The human-readable description for the share network.
// Changing this updates the description of the existing share network.
func (r *ShareNetwork) Description() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["description"])
}

// The IP version of the share network. Can either be 4 or 6.
func (r *ShareNetwork) IpVersion() pulumi.IntOutput {
	return (pulumi.IntOutput)(r.s.State["ipVersion"])
}

// The name for the share network. Changing this updates the name
// of the existing share network.
func (r *ShareNetwork) Name() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["name"])
}

// The share network type. Can either be VLAN, VXLAN, GRE, or flat.
func (r *ShareNetwork) NetworkType() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["networkType"])
}

// The UUID of a neutron network when setting up or updating
// a share network. Changing this updates the existing share network if it's not used by
// shares.
func (r *ShareNetwork) NeutronNetId() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["neutronNetId"])
}

// The UUID of the neutron subnet when setting up or
// updating a share network. Changing this updates the existing share network if it's
// not used by shares.
func (r *ShareNetwork) NeutronSubnetId() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["neutronSubnetId"])
}

// The owner of the Share Network.
func (r *ShareNetwork) ProjectId() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["projectId"])
}

// The region in which to obtain the V2 Shared File System client.
// A Shared File System client is needed to create a share network. If omitted, the
// `region` argument of the provider is used. Changing this creates a new
// share network.
func (r *ShareNetwork) Region() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["region"])
}

// The list of security service IDs to associate with
// the share network. The security service must be specified by ID and not name.
func (r *ShareNetwork) SecurityServiceIds() pulumi.ArrayOutput {
	return (pulumi.ArrayOutput)(r.s.State["securityServiceIds"])
}

// The share network segmentation ID.
func (r *ShareNetwork) SegmentationId() pulumi.IntOutput {
	return (pulumi.IntOutput)(r.s.State["segmentationId"])
}

// Input properties used for looking up and filtering ShareNetwork resources.
type ShareNetworkState struct {
	// The share network CIDR.
	Cidr interface{}
	// The human-readable description for the share network.
	// Changing this updates the description of the existing share network.
	Description interface{}
	// The IP version of the share network. Can either be 4 or 6.
	IpVersion interface{}
	// The name for the share network. Changing this updates the name
	// of the existing share network.
	Name interface{}
	// The share network type. Can either be VLAN, VXLAN, GRE, or flat.
	NetworkType interface{}
	// The UUID of a neutron network when setting up or updating
	// a share network. Changing this updates the existing share network if it's not used by
	// shares.
	NeutronNetId interface{}
	// The UUID of the neutron subnet when setting up or
	// updating a share network. Changing this updates the existing share network if it's
	// not used by shares.
	NeutronSubnetId interface{}
	// The owner of the Share Network.
	ProjectId interface{}
	// The region in which to obtain the V2 Shared File System client.
	// A Shared File System client is needed to create a share network. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// share network.
	Region interface{}
	// The list of security service IDs to associate with
	// the share network. The security service must be specified by ID and not name.
	SecurityServiceIds interface{}
	// The share network segmentation ID.
	SegmentationId interface{}
}

// The set of arguments for constructing a ShareNetwork resource.
type ShareNetworkArgs struct {
	// The human-readable description for the share network.
	// Changing this updates the description of the existing share network.
	Description interface{}
	// The name for the share network. Changing this updates the name
	// of the existing share network.
	Name interface{}
	// The UUID of a neutron network when setting up or updating
	// a share network. Changing this updates the existing share network if it's not used by
	// shares.
	NeutronNetId interface{}
	// The UUID of the neutron subnet when setting up or
	// updating a share network. Changing this updates the existing share network if it's
	// not used by shares.
	NeutronSubnetId interface{}
	// The region in which to obtain the V2 Shared File System client.
	// A Shared File System client is needed to create a share network. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// share network.
	Region interface{}
	// The list of security service IDs to associate with
	// the share network. The security service must be specified by ID and not name.
	SecurityServiceIds interface{}
}
