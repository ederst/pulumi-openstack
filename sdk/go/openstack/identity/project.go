// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package identity

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a V3 Project resource within OpenStack Keystone.
// 
// Note: You _must_ have admin privileges in your OpenStack cloud to use
// this resource.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_project_v3.html.markdown.
type Project struct {
	s *pulumi.ResourceState
}

// NewProject registers a new resource with the given unique name, arguments, and options.
func NewProject(ctx *pulumi.Context,
	name string, args *ProjectArgs, opts ...pulumi.ResourceOpt) (*Project, error) {
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["description"] = nil
		inputs["domainId"] = nil
		inputs["enabled"] = nil
		inputs["isDomain"] = nil
		inputs["name"] = nil
		inputs["parentId"] = nil
		inputs["region"] = nil
	} else {
		inputs["description"] = args.Description
		inputs["domainId"] = args.DomainId
		inputs["enabled"] = args.Enabled
		inputs["isDomain"] = args.IsDomain
		inputs["name"] = args.Name
		inputs["parentId"] = args.ParentId
		inputs["region"] = args.Region
	}
	s, err := ctx.RegisterResource("openstack:identity/project:Project", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Project{s: s}, nil
}

// GetProject gets an existing Project resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetProject(ctx *pulumi.Context,
	name string, id pulumi.ID, state *ProjectState, opts ...pulumi.ResourceOpt) (*Project, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["description"] = state.Description
		inputs["domainId"] = state.DomainId
		inputs["enabled"] = state.Enabled
		inputs["isDomain"] = state.IsDomain
		inputs["name"] = state.Name
		inputs["parentId"] = state.ParentId
		inputs["region"] = state.Region
	}
	s, err := ctx.ReadResource("openstack:identity/project:Project", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Project{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Project) URN() pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Project) ID() pulumi.IDOutput {
	return r.s.ID()
}

// A description of the project.
func (r *Project) Description() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["description"])
}

// The domain this project belongs to.
func (r *Project) DomainId() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["domainId"])
}

// Whether the project is enabled or disabled. Valid
// values are `true` and `false`.
func (r *Project) Enabled() pulumi.BoolOutput {
	return (pulumi.BoolOutput)(r.s.State["enabled"])
}

// Whether this project is a domain. Valid values
// are `true` and `false`.
func (r *Project) IsDomain() pulumi.BoolOutput {
	return (pulumi.BoolOutput)(r.s.State["isDomain"])
}

// The name of the project.
func (r *Project) Name() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["name"])
}

// The parent of this project.
func (r *Project) ParentId() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["parentId"])
}

// The region in which to obtain the V3 Keystone client.
// If omitted, the `region` argument of the provider is used. Changing this
// creates a new User.
func (r *Project) Region() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["region"])
}

// Input properties used for looking up and filtering Project resources.
type ProjectState struct {
	// A description of the project.
	Description interface{}
	// The domain this project belongs to.
	DomainId interface{}
	// Whether the project is enabled or disabled. Valid
	// values are `true` and `false`.
	Enabled interface{}
	// Whether this project is a domain. Valid values
	// are `true` and `false`.
	IsDomain interface{}
	// The name of the project.
	Name interface{}
	// The parent of this project.
	ParentId interface{}
	// The region in which to obtain the V3 Keystone client.
	// If omitted, the `region` argument of the provider is used. Changing this
	// creates a new User.
	Region interface{}
}

// The set of arguments for constructing a Project resource.
type ProjectArgs struct {
	// A description of the project.
	Description interface{}
	// The domain this project belongs to.
	DomainId interface{}
	// Whether the project is enabled or disabled. Valid
	// values are `true` and `false`.
	Enabled interface{}
	// Whether this project is a domain. Valid values
	// are `true` and `false`.
	IsDomain interface{}
	// The name of the project.
	Name interface{}
	// The parent of this project.
	ParentId interface{}
	// The region in which to obtain the V3 Keystone client.
	// If omitted, the `region` argument of the provider is used. Changing this
	// creates a new User.
	Region interface{}
}
