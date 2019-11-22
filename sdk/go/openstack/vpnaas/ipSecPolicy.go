// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package vpnaas

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a V2 Neutron IPSec policy resource within OpenStack.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/vpnaas_ipsec_policy_v2.html.markdown.
type IpSecPolicy struct {
	s *pulumi.ResourceState
}

// NewIpSecPolicy registers a new resource with the given unique name, arguments, and options.
func NewIpSecPolicy(ctx *pulumi.Context,
	name string, args *IpSecPolicyArgs, opts ...pulumi.ResourceOpt) (*IpSecPolicy, error) {
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["authAlgorithm"] = nil
		inputs["description"] = nil
		inputs["encapsulationMode"] = nil
		inputs["encryptionAlgorithm"] = nil
		inputs["lifetimes"] = nil
		inputs["name"] = nil
		inputs["pfs"] = nil
		inputs["region"] = nil
		inputs["tenantId"] = nil
		inputs["transformProtocol"] = nil
		inputs["valueSpecs"] = nil
	} else {
		inputs["authAlgorithm"] = args.AuthAlgorithm
		inputs["description"] = args.Description
		inputs["encapsulationMode"] = args.EncapsulationMode
		inputs["encryptionAlgorithm"] = args.EncryptionAlgorithm
		inputs["lifetimes"] = args.Lifetimes
		inputs["name"] = args.Name
		inputs["pfs"] = args.Pfs
		inputs["region"] = args.Region
		inputs["tenantId"] = args.TenantId
		inputs["transformProtocol"] = args.TransformProtocol
		inputs["valueSpecs"] = args.ValueSpecs
	}
	s, err := ctx.RegisterResource("openstack:vpnaas/ipSecPolicy:IpSecPolicy", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &IpSecPolicy{s: s}, nil
}

// GetIpSecPolicy gets an existing IpSecPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetIpSecPolicy(ctx *pulumi.Context,
	name string, id pulumi.ID, state *IpSecPolicyState, opts ...pulumi.ResourceOpt) (*IpSecPolicy, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["authAlgorithm"] = state.AuthAlgorithm
		inputs["description"] = state.Description
		inputs["encapsulationMode"] = state.EncapsulationMode
		inputs["encryptionAlgorithm"] = state.EncryptionAlgorithm
		inputs["lifetimes"] = state.Lifetimes
		inputs["name"] = state.Name
		inputs["pfs"] = state.Pfs
		inputs["region"] = state.Region
		inputs["tenantId"] = state.TenantId
		inputs["transformProtocol"] = state.TransformProtocol
		inputs["valueSpecs"] = state.ValueSpecs
	}
	s, err := ctx.ReadResource("openstack:vpnaas/ipSecPolicy:IpSecPolicy", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &IpSecPolicy{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *IpSecPolicy) URN() pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *IpSecPolicy) ID() pulumi.IDOutput {
	return r.s.ID()
}

// The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
// Default is sha1. Changing this updates the algorithm of the existing policy.
func (r *IpSecPolicy) AuthAlgorithm() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["authAlgorithm"])
}

// The human-readable description for the policy.
// Changing this updates the description of the existing policy.
func (r *IpSecPolicy) Description() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["description"])
}

// The encapsulation mode. Valid values are tunnel and transport. Default is tunnel.
// Changing this updates the existing policy.
func (r *IpSecPolicy) EncapsulationMode() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["encapsulationMode"])
}

// The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
// The default value is aes-128. Changing this updates the existing policy.
func (r *IpSecPolicy) EncryptionAlgorithm() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["encryptionAlgorithm"])
}

// The lifetime of the security association. Consists of Unit and Value.
// - `unit` - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes.
// Default is seconds.
// - `value` - (Optional) The value for the lifetime of the security association. Must be a positive integer.
// Default is 3600.
func (r *IpSecPolicy) Lifetimes() pulumi.ArrayOutput {
	return (pulumi.ArrayOutput)(r.s.State["lifetimes"])
}

// The name of the policy. Changing this updates the name of
// the existing policy.
func (r *IpSecPolicy) Name() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["name"])
}

// The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
// Changing this updates the existing policy.
func (r *IpSecPolicy) Pfs() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["pfs"])
}

// The region in which to obtain the V2 Networking client.
// A Networking client is needed to create an IPSec policy. If omitted, the
// `region` argument of the provider is used. Changing this creates a new
// policy.
func (r *IpSecPolicy) Region() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["region"])
}

// The owner of the policy. Required if admin wants to
// create a policy for another project. Changing this creates a new policy.
func (r *IpSecPolicy) TenantId() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["tenantId"])
}

// The transform protocol. Valid values are ESP, AH and AH-ESP.
// Changing this updates the existing policy. Default is ESP.
func (r *IpSecPolicy) TransformProtocol() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["transformProtocol"])
}

// Map of additional options.
func (r *IpSecPolicy) ValueSpecs() pulumi.MapOutput {
	return (pulumi.MapOutput)(r.s.State["valueSpecs"])
}

// Input properties used for looking up and filtering IpSecPolicy resources.
type IpSecPolicyState struct {
	// The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
	// Default is sha1. Changing this updates the algorithm of the existing policy.
	AuthAlgorithm interface{}
	// The human-readable description for the policy.
	// Changing this updates the description of the existing policy.
	Description interface{}
	// The encapsulation mode. Valid values are tunnel and transport. Default is tunnel.
	// Changing this updates the existing policy.
	EncapsulationMode interface{}
	// The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
	// The default value is aes-128. Changing this updates the existing policy.
	EncryptionAlgorithm interface{}
	// The lifetime of the security association. Consists of Unit and Value.
	// - `unit` - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes.
	// Default is seconds.
	// - `value` - (Optional) The value for the lifetime of the security association. Must be a positive integer.
	// Default is 3600.
	Lifetimes interface{}
	// The name of the policy. Changing this updates the name of
	// the existing policy.
	Name interface{}
	// The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
	// Changing this updates the existing policy.
	Pfs interface{}
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an IPSec policy. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// policy.
	Region interface{}
	// The owner of the policy. Required if admin wants to
	// create a policy for another project. Changing this creates a new policy.
	TenantId interface{}
	// The transform protocol. Valid values are ESP, AH and AH-ESP.
	// Changing this updates the existing policy. Default is ESP.
	TransformProtocol interface{}
	// Map of additional options.
	ValueSpecs interface{}
}

// The set of arguments for constructing a IpSecPolicy resource.
type IpSecPolicyArgs struct {
	// The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
	// Default is sha1. Changing this updates the algorithm of the existing policy.
	AuthAlgorithm interface{}
	// The human-readable description for the policy.
	// Changing this updates the description of the existing policy.
	Description interface{}
	// The encapsulation mode. Valid values are tunnel and transport. Default is tunnel.
	// Changing this updates the existing policy.
	EncapsulationMode interface{}
	// The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
	// The default value is aes-128. Changing this updates the existing policy.
	EncryptionAlgorithm interface{}
	// The lifetime of the security association. Consists of Unit and Value.
	// - `unit` - (Optional) The units for the lifetime of the security association. Can be either seconds or kilobytes.
	// Default is seconds.
	// - `value` - (Optional) The value for the lifetime of the security association. Must be a positive integer.
	// Default is 3600.
	Lifetimes interface{}
	// The name of the policy. Changing this updates the name of
	// the existing policy.
	Name interface{}
	// The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
	// Changing this updates the existing policy.
	Pfs interface{}
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an IPSec policy. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// policy.
	Region interface{}
	// The owner of the policy. Required if admin wants to
	// create a policy for another project. Changing this creates a new policy.
	TenantId interface{}
	// The transform protocol. Valid values are ESP, AH and AH-ESP.
	// Changing this updates the existing policy. Default is ESP.
	TransformProtocol interface{}
	// Map of additional options.
	ValueSpecs interface{}
}
