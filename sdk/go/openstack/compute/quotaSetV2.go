// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a V2 compute quotaset resource within OpenStack.
// 
// > **Note:** This usually requires admin privileges.
// 
// > **Note:** This resource has a no-op deletion so no actual actions will be done against the OpenStack API 
//     in case of delete call.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_quotaset_v2.html.markdown.
type QuotaSetV2 struct {
	s *pulumi.ResourceState
}

// NewQuotaSetV2 registers a new resource with the given unique name, arguments, and options.
func NewQuotaSetV2(ctx *pulumi.Context,
	name string, args *QuotaSetV2Args, opts ...pulumi.ResourceOpt) (*QuotaSetV2, error) {
	if args == nil || args.ProjectId == nil {
		return nil, errors.New("missing required argument 'ProjectId'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["cores"] = nil
		inputs["fixedIps"] = nil
		inputs["floatingIps"] = nil
		inputs["injectedFileContentBytes"] = nil
		inputs["injectedFilePathBytes"] = nil
		inputs["injectedFiles"] = nil
		inputs["instances"] = nil
		inputs["keyPairs"] = nil
		inputs["metadataItems"] = nil
		inputs["projectId"] = nil
		inputs["ram"] = nil
		inputs["region"] = nil
		inputs["securityGroupRules"] = nil
		inputs["securityGroups"] = nil
		inputs["serverGroupMembers"] = nil
		inputs["serverGroups"] = nil
	} else {
		inputs["cores"] = args.Cores
		inputs["fixedIps"] = args.FixedIps
		inputs["floatingIps"] = args.FloatingIps
		inputs["injectedFileContentBytes"] = args.InjectedFileContentBytes
		inputs["injectedFilePathBytes"] = args.InjectedFilePathBytes
		inputs["injectedFiles"] = args.InjectedFiles
		inputs["instances"] = args.Instances
		inputs["keyPairs"] = args.KeyPairs
		inputs["metadataItems"] = args.MetadataItems
		inputs["projectId"] = args.ProjectId
		inputs["ram"] = args.Ram
		inputs["region"] = args.Region
		inputs["securityGroupRules"] = args.SecurityGroupRules
		inputs["securityGroups"] = args.SecurityGroups
		inputs["serverGroupMembers"] = args.ServerGroupMembers
		inputs["serverGroups"] = args.ServerGroups
	}
	s, err := ctx.RegisterResource("openstack:compute/quotaSetV2:QuotaSetV2", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &QuotaSetV2{s: s}, nil
}

// GetQuotaSetV2 gets an existing QuotaSetV2 resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetQuotaSetV2(ctx *pulumi.Context,
	name string, id pulumi.ID, state *QuotaSetV2State, opts ...pulumi.ResourceOpt) (*QuotaSetV2, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["cores"] = state.Cores
		inputs["fixedIps"] = state.FixedIps
		inputs["floatingIps"] = state.FloatingIps
		inputs["injectedFileContentBytes"] = state.InjectedFileContentBytes
		inputs["injectedFilePathBytes"] = state.InjectedFilePathBytes
		inputs["injectedFiles"] = state.InjectedFiles
		inputs["instances"] = state.Instances
		inputs["keyPairs"] = state.KeyPairs
		inputs["metadataItems"] = state.MetadataItems
		inputs["projectId"] = state.ProjectId
		inputs["ram"] = state.Ram
		inputs["region"] = state.Region
		inputs["securityGroupRules"] = state.SecurityGroupRules
		inputs["securityGroups"] = state.SecurityGroups
		inputs["serverGroupMembers"] = state.ServerGroupMembers
		inputs["serverGroups"] = state.ServerGroups
	}
	s, err := ctx.ReadResource("openstack:compute/quotaSetV2:QuotaSetV2", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &QuotaSetV2{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *QuotaSetV2) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *QuotaSetV2) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// Quota value for cores.
// Changing this updates the existing quotaset.
func (r *QuotaSetV2) Cores() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["cores"])
}

// Quota value for fixed IPs.
// Changing this updates the existing quotaset.
func (r *QuotaSetV2) FixedIps() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["fixedIps"])
}

// Quota value for floating IPs.
// Changing this updates the existing quotaset.
func (r *QuotaSetV2) FloatingIps() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["floatingIps"])
}

// Quota value for content bytes
// of injected files. Changing this updates the existing quotaset.
func (r *QuotaSetV2) InjectedFileContentBytes() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["injectedFileContentBytes"])
}

// Quota value for path bytes of
// injected files. Changing this updates the existing quotaset.
func (r *QuotaSetV2) InjectedFilePathBytes() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["injectedFilePathBytes"])
}

// Quota value for injected files.
// Changing this updates the existing quotaset.
func (r *QuotaSetV2) InjectedFiles() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["injectedFiles"])
}

// Quota value for instances.
// Changing this updates the existing quotaset.
func (r *QuotaSetV2) Instances() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["instances"])
}

// Quota value for key pairs.
// Changing this updates the existing quotaset.
func (r *QuotaSetV2) KeyPairs() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["keyPairs"])
}

// Quota value for metadata items.
// Changing this updates the existing quotaset.
func (r *QuotaSetV2) MetadataItems() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["metadataItems"])
}

// ID of the project to manage quotas.
// Changing this creates a new quotaset.
func (r *QuotaSetV2) ProjectId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["projectId"])
}

// Quota value for RAM.
// Changing this updates the existing quotaset.
func (r *QuotaSetV2) Ram() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["ram"])
}

// The region in which to create the volume. If
// omitted, the `region` argument of the provider is used. Changing this
// creates a new quotaset.
func (r *QuotaSetV2) Region() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["region"])
}

// Quota value for security group rules.
// Changing this updates the existing quotaset.
func (r *QuotaSetV2) SecurityGroupRules() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["securityGroupRules"])
}

// Quota value for security groups.
// Changing this updates the existing quotaset.
func (r *QuotaSetV2) SecurityGroups() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["securityGroups"])
}

// Quota value for server groups members.
// Changing this updates the existing quotaset.
func (r *QuotaSetV2) ServerGroupMembers() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["serverGroupMembers"])
}

// Quota value for server groups.
// Changing this updates the existing quotaset.
func (r *QuotaSetV2) ServerGroups() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["serverGroups"])
}

// Input properties used for looking up and filtering QuotaSetV2 resources.
type QuotaSetV2State struct {
	// Quota value for cores.
	// Changing this updates the existing quotaset.
	Cores interface{}
	// Quota value for fixed IPs.
	// Changing this updates the existing quotaset.
	FixedIps interface{}
	// Quota value for floating IPs.
	// Changing this updates the existing quotaset.
	FloatingIps interface{}
	// Quota value for content bytes
	// of injected files. Changing this updates the existing quotaset.
	InjectedFileContentBytes interface{}
	// Quota value for path bytes of
	// injected files. Changing this updates the existing quotaset.
	InjectedFilePathBytes interface{}
	// Quota value for injected files.
	// Changing this updates the existing quotaset.
	InjectedFiles interface{}
	// Quota value for instances.
	// Changing this updates the existing quotaset.
	Instances interface{}
	// Quota value for key pairs.
	// Changing this updates the existing quotaset.
	KeyPairs interface{}
	// Quota value for metadata items.
	// Changing this updates the existing quotaset.
	MetadataItems interface{}
	// ID of the project to manage quotas.
	// Changing this creates a new quotaset.
	ProjectId interface{}
	// Quota value for RAM.
	// Changing this updates the existing quotaset.
	Ram interface{}
	// The region in which to create the volume. If
	// omitted, the `region` argument of the provider is used. Changing this
	// creates a new quotaset.
	Region interface{}
	// Quota value for security group rules.
	// Changing this updates the existing quotaset.
	SecurityGroupRules interface{}
	// Quota value for security groups.
	// Changing this updates the existing quotaset.
	SecurityGroups interface{}
	// Quota value for server groups members.
	// Changing this updates the existing quotaset.
	ServerGroupMembers interface{}
	// Quota value for server groups.
	// Changing this updates the existing quotaset.
	ServerGroups interface{}
}

// The set of arguments for constructing a QuotaSetV2 resource.
type QuotaSetV2Args struct {
	// Quota value for cores.
	// Changing this updates the existing quotaset.
	Cores interface{}
	// Quota value for fixed IPs.
	// Changing this updates the existing quotaset.
	FixedIps interface{}
	// Quota value for floating IPs.
	// Changing this updates the existing quotaset.
	FloatingIps interface{}
	// Quota value for content bytes
	// of injected files. Changing this updates the existing quotaset.
	InjectedFileContentBytes interface{}
	// Quota value for path bytes of
	// injected files. Changing this updates the existing quotaset.
	InjectedFilePathBytes interface{}
	// Quota value for injected files.
	// Changing this updates the existing quotaset.
	InjectedFiles interface{}
	// Quota value for instances.
	// Changing this updates the existing quotaset.
	Instances interface{}
	// Quota value for key pairs.
	// Changing this updates the existing quotaset.
	KeyPairs interface{}
	// Quota value for metadata items.
	// Changing this updates the existing quotaset.
	MetadataItems interface{}
	// ID of the project to manage quotas.
	// Changing this creates a new quotaset.
	ProjectId interface{}
	// Quota value for RAM.
	// Changing this updates the existing quotaset.
	Ram interface{}
	// The region in which to create the volume. If
	// omitted, the `region` argument of the provider is used. Changing this
	// creates a new quotaset.
	Region interface{}
	// Quota value for security group rules.
	// Changing this updates the existing quotaset.
	SecurityGroupRules interface{}
	// Quota value for security groups.
	// Changing this updates the existing quotaset.
	SecurityGroups interface{}
	// Quota value for server groups members.
	// Changing this updates the existing quotaset.
	ServerGroupMembers interface{}
	// Quota value for server groups.
	// Changing this updates the existing quotaset.
	ServerGroups interface{}
}
