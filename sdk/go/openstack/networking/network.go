// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package networking

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a V2 Neutron network resource within OpenStack.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/networking_network_v2.html.markdown.
type Network struct {
	s *pulumi.ResourceState
}

// NewNetwork registers a new resource with the given unique name, arguments, and options.
func NewNetwork(ctx *pulumi.Context,
	name string, args *NetworkArgs, opts ...pulumi.ResourceOpt) (*Network, error) {
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["adminStateUp"] = nil
		inputs["availabilityZoneHints"] = nil
		inputs["description"] = nil
		inputs["dnsDomain"] = nil
		inputs["external"] = nil
		inputs["mtu"] = nil
		inputs["name"] = nil
		inputs["portSecurityEnabled"] = nil
		inputs["qosPolicyId"] = nil
		inputs["region"] = nil
		inputs["segments"] = nil
		inputs["shared"] = nil
		inputs["tags"] = nil
		inputs["tenantId"] = nil
		inputs["transparentVlan"] = nil
		inputs["valueSpecs"] = nil
	} else {
		inputs["adminStateUp"] = args.AdminStateUp
		inputs["availabilityZoneHints"] = args.AvailabilityZoneHints
		inputs["description"] = args.Description
		inputs["dnsDomain"] = args.DnsDomain
		inputs["external"] = args.External
		inputs["mtu"] = args.Mtu
		inputs["name"] = args.Name
		inputs["portSecurityEnabled"] = args.PortSecurityEnabled
		inputs["qosPolicyId"] = args.QosPolicyId
		inputs["region"] = args.Region
		inputs["segments"] = args.Segments
		inputs["shared"] = args.Shared
		inputs["tags"] = args.Tags
		inputs["tenantId"] = args.TenantId
		inputs["transparentVlan"] = args.TransparentVlan
		inputs["valueSpecs"] = args.ValueSpecs
	}
	inputs["allTags"] = nil
	s, err := ctx.RegisterResource("openstack:networking/network:Network", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Network{s: s}, nil
}

// GetNetwork gets an existing Network resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNetwork(ctx *pulumi.Context,
	name string, id pulumi.ID, state *NetworkState, opts ...pulumi.ResourceOpt) (*Network, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["adminStateUp"] = state.AdminStateUp
		inputs["allTags"] = state.AllTags
		inputs["availabilityZoneHints"] = state.AvailabilityZoneHints
		inputs["description"] = state.Description
		inputs["dnsDomain"] = state.DnsDomain
		inputs["external"] = state.External
		inputs["mtu"] = state.Mtu
		inputs["name"] = state.Name
		inputs["portSecurityEnabled"] = state.PortSecurityEnabled
		inputs["qosPolicyId"] = state.QosPolicyId
		inputs["region"] = state.Region
		inputs["segments"] = state.Segments
		inputs["shared"] = state.Shared
		inputs["tags"] = state.Tags
		inputs["tenantId"] = state.TenantId
		inputs["transparentVlan"] = state.TransparentVlan
		inputs["valueSpecs"] = state.ValueSpecs
	}
	s, err := ctx.ReadResource("openstack:networking/network:Network", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Network{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Network) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Network) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The administrative state of the network.
// Acceptable values are "true" and "false". Changing this value updates the
// state of the existing network.
func (r *Network) AdminStateUp() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["adminStateUp"])
}

// The collection of tags assigned on the network, which have been
// explicitly and implicitly added.
func (r *Network) AllTags() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["allTags"])
}

// An availability zone is used to make
// network resources highly available. Used for resources with high availability
// so that they are scheduled on different availability zones. Changing this
// creates a new network.
func (r *Network) AvailabilityZoneHints() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["availabilityZoneHints"])
}

// Human-readable description of the network. Changing this
// updates the name of the existing network.
func (r *Network) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

// The network DNS domain. Available, when Neutron DNS
// extension is enabled. The `dns_domain` of a network in conjunction with the
// `dns_name` attribute of its ports will be published in an external DNS
// service when Neutron is configured to integrate with such a service.
func (r *Network) DnsDomain() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["dnsDomain"])
}

// Specifies whether the network resource has the
// external routing facility. Valid values are true and false. Defaults to
// false. Changing this updates the external attribute of the existing network.
func (r *Network) External() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["external"])
}

// The network MTU. Available for read-only, when Neutron
// `net-mtu` extension is enabled. Available for the modification, when
// Neutron `net-mtu-writable` extension is enabled.
func (r *Network) Mtu() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["mtu"])
}

// The name of the network. Changing this updates the name of
// the existing network.
func (r *Network) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// Whether to explicitly enable or disable
// port security on the network. Port Security is usually enabled by default, so
// omitting this argument will usually result in a value of "true". Setting this
// explicitly to `false` will disable port security. Valid values are `true` and
// `false`.
func (r *Network) PortSecurityEnabled() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["portSecurityEnabled"])
}

// Reference to the associated QoS policy.
func (r *Network) QosPolicyId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["qosPolicyId"])
}

// The region in which to obtain the V2 Networking client.
// A Networking client is needed to create a Neutron network. If omitted, the
// `region` argument of the provider is used. Changing this creates a new
// network.
func (r *Network) Region() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["region"])
}

// An array of one or more provider segment objects.
func (r *Network) Segments() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["segments"])
}

// Specifies whether the network resource can be accessed
// by any tenant or not. Changing this updates the sharing capabilities of the
// existing network.
func (r *Network) Shared() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["shared"])
}

// A set of string tags for the network.
func (r *Network) Tags() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["tags"])
}

// The owner of the network. Required if admin wants to
// create a network for another tenant. Changing this creates a new network.
func (r *Network) TenantId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["tenantId"])
}

// Specifies whether the network resource has the
// VLAN transparent attribute set. Valid values are true and false. Defaults to
// false. Changing this updates the `transparent_vlan` attribute of the existing
// network.
func (r *Network) TransparentVlan() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["transparentVlan"])
}

// Map of additional options.
func (r *Network) ValueSpecs() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["valueSpecs"])
}

// Input properties used for looking up and filtering Network resources.
type NetworkState struct {
	// The administrative state of the network.
	// Acceptable values are "true" and "false". Changing this value updates the
	// state of the existing network.
	AdminStateUp interface{}
	// The collection of tags assigned on the network, which have been
	// explicitly and implicitly added.
	AllTags interface{}
	// An availability zone is used to make
	// network resources highly available. Used for resources with high availability
	// so that they are scheduled on different availability zones. Changing this
	// creates a new network.
	AvailabilityZoneHints interface{}
	// Human-readable description of the network. Changing this
	// updates the name of the existing network.
	Description interface{}
	// The network DNS domain. Available, when Neutron DNS
	// extension is enabled. The `dns_domain` of a network in conjunction with the
	// `dns_name` attribute of its ports will be published in an external DNS
	// service when Neutron is configured to integrate with such a service.
	DnsDomain interface{}
	// Specifies whether the network resource has the
	// external routing facility. Valid values are true and false. Defaults to
	// false. Changing this updates the external attribute of the existing network.
	External interface{}
	// The network MTU. Available for read-only, when Neutron
	// `net-mtu` extension is enabled. Available for the modification, when
	// Neutron `net-mtu-writable` extension is enabled.
	Mtu interface{}
	// The name of the network. Changing this updates the name of
	// the existing network.
	Name interface{}
	// Whether to explicitly enable or disable
	// port security on the network. Port Security is usually enabled by default, so
	// omitting this argument will usually result in a value of "true". Setting this
	// explicitly to `false` will disable port security. Valid values are `true` and
	// `false`.
	PortSecurityEnabled interface{}
	// Reference to the associated QoS policy.
	QosPolicyId interface{}
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create a Neutron network. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// network.
	Region interface{}
	// An array of one or more provider segment objects.
	Segments interface{}
	// Specifies whether the network resource can be accessed
	// by any tenant or not. Changing this updates the sharing capabilities of the
	// existing network.
	Shared interface{}
	// A set of string tags for the network.
	Tags interface{}
	// The owner of the network. Required if admin wants to
	// create a network for another tenant. Changing this creates a new network.
	TenantId interface{}
	// Specifies whether the network resource has the
	// VLAN transparent attribute set. Valid values are true and false. Defaults to
	// false. Changing this updates the `transparent_vlan` attribute of the existing
	// network.
	TransparentVlan interface{}
	// Map of additional options.
	ValueSpecs interface{}
}

// The set of arguments for constructing a Network resource.
type NetworkArgs struct {
	// The administrative state of the network.
	// Acceptable values are "true" and "false". Changing this value updates the
	// state of the existing network.
	AdminStateUp interface{}
	// An availability zone is used to make
	// network resources highly available. Used for resources with high availability
	// so that they are scheduled on different availability zones. Changing this
	// creates a new network.
	AvailabilityZoneHints interface{}
	// Human-readable description of the network. Changing this
	// updates the name of the existing network.
	Description interface{}
	// The network DNS domain. Available, when Neutron DNS
	// extension is enabled. The `dns_domain` of a network in conjunction with the
	// `dns_name` attribute of its ports will be published in an external DNS
	// service when Neutron is configured to integrate with such a service.
	DnsDomain interface{}
	// Specifies whether the network resource has the
	// external routing facility. Valid values are true and false. Defaults to
	// false. Changing this updates the external attribute of the existing network.
	External interface{}
	// The network MTU. Available for read-only, when Neutron
	// `net-mtu` extension is enabled. Available for the modification, when
	// Neutron `net-mtu-writable` extension is enabled.
	Mtu interface{}
	// The name of the network. Changing this updates the name of
	// the existing network.
	Name interface{}
	// Whether to explicitly enable or disable
	// port security on the network. Port Security is usually enabled by default, so
	// omitting this argument will usually result in a value of "true". Setting this
	// explicitly to `false` will disable port security. Valid values are `true` and
	// `false`.
	PortSecurityEnabled interface{}
	// Reference to the associated QoS policy.
	QosPolicyId interface{}
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create a Neutron network. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// network.
	Region interface{}
	// An array of one or more provider segment objects.
	Segments interface{}
	// Specifies whether the network resource can be accessed
	// by any tenant or not. Changing this updates the sharing capabilities of the
	// existing network.
	Shared interface{}
	// A set of string tags for the network.
	Tags interface{}
	// The owner of the network. Required if admin wants to
	// create a network for another tenant. Changing this creates a new network.
	TenantId interface{}
	// Specifies whether the network resource has the
	// VLAN transparent attribute set. Valid values are true and false. Defaults to
	// false. Changing this updates the `transparent_vlan` attribute of the existing
	// network.
	TransparentVlan interface{}
	// Map of additional options.
	ValueSpecs interface{}
}
