// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package identity

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a V3 Role assignment within OpenStack Keystone.
//
// Note: You _must_ have admin privileges in your OpenStack cloud to use
// this resource.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_role_assignment_v3.html.markdown.
type RoleAssignment struct {
	pulumi.CustomResourceState

	// The domain to assign the role in.
	DomainId pulumi.StringPtrOutput `pulumi:"domainId"`
	// The group to assign the role to.
	GroupId pulumi.StringPtrOutput `pulumi:"groupId"`
	// The project to assign the role in.
	ProjectId pulumi.StringPtrOutput `pulumi:"projectId"`
	Region pulumi.StringOutput `pulumi:"region"`
	// The role to assign.
	RoleId pulumi.StringOutput `pulumi:"roleId"`
	// The user to assign the role to.
	UserId pulumi.StringPtrOutput `pulumi:"userId"`
}

// NewRoleAssignment registers a new resource with the given unique name, arguments, and options.
func NewRoleAssignment(ctx *pulumi.Context,
	name string, args *RoleAssignmentArgs, opts ...pulumi.ResourceOption) (*RoleAssignment, error) {
	if args == nil || args.RoleId == nil {
		return nil, errors.New("missing required argument 'RoleId'")
	}
	if args == nil {
		args = &RoleAssignmentArgs{}
	}
	var resource RoleAssignment
	err := ctx.RegisterResource("openstack:identity/roleAssignment:RoleAssignment", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRoleAssignment gets an existing RoleAssignment resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRoleAssignment(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RoleAssignmentState, opts ...pulumi.ResourceOption) (*RoleAssignment, error) {
	var resource RoleAssignment
	err := ctx.ReadResource("openstack:identity/roleAssignment:RoleAssignment", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering RoleAssignment resources.
type roleAssignmentState struct {
	// The domain to assign the role in.
	DomainId *string `pulumi:"domainId"`
	// The group to assign the role to.
	GroupId *string `pulumi:"groupId"`
	// The project to assign the role in.
	ProjectId *string `pulumi:"projectId"`
	Region *string `pulumi:"region"`
	// The role to assign.
	RoleId *string `pulumi:"roleId"`
	// The user to assign the role to.
	UserId *string `pulumi:"userId"`
}

type RoleAssignmentState struct {
	// The domain to assign the role in.
	DomainId pulumi.StringPtrInput
	// The group to assign the role to.
	GroupId pulumi.StringPtrInput
	// The project to assign the role in.
	ProjectId pulumi.StringPtrInput
	Region pulumi.StringPtrInput
	// The role to assign.
	RoleId pulumi.StringPtrInput
	// The user to assign the role to.
	UserId pulumi.StringPtrInput
}

func (RoleAssignmentState) ElementType() reflect.Type {
	return reflect.TypeOf((*roleAssignmentState)(nil)).Elem()
}

type roleAssignmentArgs struct {
	// The domain to assign the role in.
	DomainId *string `pulumi:"domainId"`
	// The group to assign the role to.
	GroupId *string `pulumi:"groupId"`
	// The project to assign the role in.
	ProjectId *string `pulumi:"projectId"`
	Region *string `pulumi:"region"`
	// The role to assign.
	RoleId string `pulumi:"roleId"`
	// The user to assign the role to.
	UserId *string `pulumi:"userId"`
}

// The set of arguments for constructing a RoleAssignment resource.
type RoleAssignmentArgs struct {
	// The domain to assign the role in.
	DomainId pulumi.StringPtrInput
	// The group to assign the role to.
	GroupId pulumi.StringPtrInput
	// The project to assign the role in.
	ProjectId pulumi.StringPtrInput
	Region pulumi.StringPtrInput
	// The role to assign.
	RoleId pulumi.StringInput
	// The user to assign the role to.
	UserId pulumi.StringPtrInput
}

func (RoleAssignmentArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*roleAssignmentArgs)(nil)).Elem()
}

