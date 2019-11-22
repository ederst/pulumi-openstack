// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Attaches a Network Interface (a Port) to an Instance using the OpenStack
// Compute (Nova) v2 API.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_interface_attach_v2.html.markdown.
type InterfaceAttach struct {
	s *pulumi.ResourceState
}

// NewInterfaceAttach registers a new resource with the given unique name, arguments, and options.
func NewInterfaceAttach(ctx *pulumi.Context,
	name string, args *InterfaceAttachArgs, opts ...pulumi.ResourceOpt) (*InterfaceAttach, error) {
	if args == nil || args.InstanceId == nil {
		return nil, errors.New("missing required argument 'InstanceId'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["fixedIp"] = nil
		inputs["instanceId"] = nil
		inputs["networkId"] = nil
		inputs["portId"] = nil
		inputs["region"] = nil
	} else {
		inputs["fixedIp"] = args.FixedIp
		inputs["instanceId"] = args.InstanceId
		inputs["networkId"] = args.NetworkId
		inputs["portId"] = args.PortId
		inputs["region"] = args.Region
	}
	s, err := ctx.RegisterResource("openstack:compute/interfaceAttach:InterfaceAttach", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &InterfaceAttach{s: s}, nil
}

// GetInterfaceAttach gets an existing InterfaceAttach resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetInterfaceAttach(ctx *pulumi.Context,
	name string, id pulumi.ID, state *InterfaceAttachState, opts ...pulumi.ResourceOpt) (*InterfaceAttach, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["fixedIp"] = state.FixedIp
		inputs["instanceId"] = state.InstanceId
		inputs["networkId"] = state.NetworkId
		inputs["portId"] = state.PortId
		inputs["region"] = state.Region
	}
	s, err := ctx.ReadResource("openstack:compute/interfaceAttach:InterfaceAttach", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &InterfaceAttach{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *InterfaceAttach) URN() pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *InterfaceAttach) ID() pulumi.IDOutput {
	return r.s.ID()
}

// An IP address to assosciate with the port.
// _NOTE_: This option cannot be used with port_id. You must specifiy a network_id. The IP address must lie in a range on the supplied network.
func (r *InterfaceAttach) FixedIp() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["fixedIp"])
}

// The ID of the Instance to attach the Port or Network to.
func (r *InterfaceAttach) InstanceId() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["instanceId"])
}

// The ID of the Network to attach to an Instance. A port will be created automatically.
// _NOTE_: This option and `portId` are mutually exclusive.
func (r *InterfaceAttach) NetworkId() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["networkId"])
}

// The ID of the Port to attach to an Instance.
// _NOTE_: This option and `networkId` are mutually exclusive.
func (r *InterfaceAttach) PortId() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["portId"])
}

// The region in which to create the interface attachment.
// If omitted, the `region` argument of the provider is used. Changing this
// creates a new attachment.
func (r *InterfaceAttach) Region() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["region"])
}

// Input properties used for looking up and filtering InterfaceAttach resources.
type InterfaceAttachState struct {
	// An IP address to assosciate with the port.
	// _NOTE_: This option cannot be used with port_id. You must specifiy a network_id. The IP address must lie in a range on the supplied network.
	FixedIp interface{}
	// The ID of the Instance to attach the Port or Network to.
	InstanceId interface{}
	// The ID of the Network to attach to an Instance. A port will be created automatically.
	// _NOTE_: This option and `portId` are mutually exclusive.
	NetworkId interface{}
	// The ID of the Port to attach to an Instance.
	// _NOTE_: This option and `networkId` are mutually exclusive.
	PortId interface{}
	// The region in which to create the interface attachment.
	// If omitted, the `region` argument of the provider is used. Changing this
	// creates a new attachment.
	Region interface{}
}

// The set of arguments for constructing a InterfaceAttach resource.
type InterfaceAttachArgs struct {
	// An IP address to assosciate with the port.
	// _NOTE_: This option cannot be used with port_id. You must specifiy a network_id. The IP address must lie in a range on the supplied network.
	FixedIp interface{}
	// The ID of the Instance to attach the Port or Network to.
	InstanceId interface{}
	// The ID of the Network to attach to an Instance. A port will be created automatically.
	// _NOTE_: This option and `portId` are mutually exclusive.
	NetworkId interface{}
	// The ID of the Port to attach to an Instance.
	// _NOTE_: This option and `networkId` are mutually exclusive.
	PortId interface{}
	// The region in which to create the interface attachment.
	// If omitted, the `region` argument of the provider is used. Changing this
	// creates a new attachment.
	Region interface{}
}
