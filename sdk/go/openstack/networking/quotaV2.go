// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package networking

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a V2 networking quota resource within OpenStack.
//
// > **Note:** This usually requires admin privileges.
//
// > **Note:** This resource has a no-op deletion so no actual actions will be done against the OpenStack API 
//     in case of delete call.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/networking_quota_v2.html.markdown.
type QuotaV2 struct {
	pulumi.CustomResourceState

	// Quota value for floating IPs. Changing this updates the
	// existing quota.
	Floatingip pulumi.IntOutput `pulumi:"floatingip"`
	// Quota value for networks. Changing this updates the
	// existing quota.
	Network pulumi.IntOutput `pulumi:"network"`
	// Quota value for ports. Changing this updates the
	// existing quota.
	Port pulumi.IntOutput `pulumi:"port"`
	// ID of the project to manage quota. Changing this
	// creates new quota.
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
	// Quota value for RBAC policies.
	// Changing this updates the existing quota.
	RbacPolicy pulumi.IntOutput `pulumi:"rbacPolicy"`
	// The region in which to create the quota. If
	// omitted, the `region` argument of the provider is used. Changing this
	// creates new quota.
	Region pulumi.StringOutput `pulumi:"region"`
	// Quota value for routers. Changing this updates the
	// existing quota.
	Router pulumi.IntOutput `pulumi:"router"`
	// Quota value for security groups. Changing
	// this updates the existing quota.
	SecurityGroup pulumi.IntOutput `pulumi:"securityGroup"`
	// Quota value for security group rules.
	// Changing this updates the existing quota.
	SecurityGroupRule pulumi.IntOutput `pulumi:"securityGroupRule"`
	// Quota value for subnets. Changing
	// this updates the existing quota.
	Subnet pulumi.IntOutput `pulumi:"subnet"`
	// Quota value for subnetpools.
	// Changing this updates the existing quota.
	Subnetpool pulumi.IntOutput `pulumi:"subnetpool"`
}

// NewQuotaV2 registers a new resource with the given unique name, arguments, and options.
func NewQuotaV2(ctx *pulumi.Context,
	name string, args *QuotaV2Args, opts ...pulumi.ResourceOption) (*QuotaV2, error) {
	if args == nil || args.ProjectId == nil {
		return nil, errors.New("missing required argument 'ProjectId'")
	}
	if args == nil {
		args = &QuotaV2Args{}
	}
	var resource QuotaV2
	err := ctx.RegisterResource("openstack:networking/quotaV2:QuotaV2", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetQuotaV2 gets an existing QuotaV2 resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetQuotaV2(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *QuotaV2State, opts ...pulumi.ResourceOption) (*QuotaV2, error) {
	var resource QuotaV2
	err := ctx.ReadResource("openstack:networking/quotaV2:QuotaV2", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering QuotaV2 resources.
type quotaV2State struct {
	// Quota value for floating IPs. Changing this updates the
	// existing quota.
	Floatingip *int `pulumi:"floatingip"`
	// Quota value for networks. Changing this updates the
	// existing quota.
	Network *int `pulumi:"network"`
	// Quota value for ports. Changing this updates the
	// existing quota.
	Port *int `pulumi:"port"`
	// ID of the project to manage quota. Changing this
	// creates new quota.
	ProjectId *string `pulumi:"projectId"`
	// Quota value for RBAC policies.
	// Changing this updates the existing quota.
	RbacPolicy *int `pulumi:"rbacPolicy"`
	// The region in which to create the quota. If
	// omitted, the `region` argument of the provider is used. Changing this
	// creates new quota.
	Region *string `pulumi:"region"`
	// Quota value for routers. Changing this updates the
	// existing quota.
	Router *int `pulumi:"router"`
	// Quota value for security groups. Changing
	// this updates the existing quota.
	SecurityGroup *int `pulumi:"securityGroup"`
	// Quota value for security group rules.
	// Changing this updates the existing quota.
	SecurityGroupRule *int `pulumi:"securityGroupRule"`
	// Quota value for subnets. Changing
	// this updates the existing quota.
	Subnet *int `pulumi:"subnet"`
	// Quota value for subnetpools.
	// Changing this updates the existing quota.
	Subnetpool *int `pulumi:"subnetpool"`
}

type QuotaV2State struct {
	// Quota value for floating IPs. Changing this updates the
	// existing quota.
	Floatingip pulumi.IntPtrInput
	// Quota value for networks. Changing this updates the
	// existing quota.
	Network pulumi.IntPtrInput
	// Quota value for ports. Changing this updates the
	// existing quota.
	Port pulumi.IntPtrInput
	// ID of the project to manage quota. Changing this
	// creates new quota.
	ProjectId pulumi.StringPtrInput
	// Quota value for RBAC policies.
	// Changing this updates the existing quota.
	RbacPolicy pulumi.IntPtrInput
	// The region in which to create the quota. If
	// omitted, the `region` argument of the provider is used. Changing this
	// creates new quota.
	Region pulumi.StringPtrInput
	// Quota value for routers. Changing this updates the
	// existing quota.
	Router pulumi.IntPtrInput
	// Quota value for security groups. Changing
	// this updates the existing quota.
	SecurityGroup pulumi.IntPtrInput
	// Quota value for security group rules.
	// Changing this updates the existing quota.
	SecurityGroupRule pulumi.IntPtrInput
	// Quota value for subnets. Changing
	// this updates the existing quota.
	Subnet pulumi.IntPtrInput
	// Quota value for subnetpools.
	// Changing this updates the existing quota.
	Subnetpool pulumi.IntPtrInput
}

func (QuotaV2State) ElementType() reflect.Type {
	return reflect.TypeOf((*quotaV2State)(nil)).Elem()
}

type quotaV2Args struct {
	// Quota value for floating IPs. Changing this updates the
	// existing quota.
	Floatingip *int `pulumi:"floatingip"`
	// Quota value for networks. Changing this updates the
	// existing quota.
	Network *int `pulumi:"network"`
	// Quota value for ports. Changing this updates the
	// existing quota.
	Port *int `pulumi:"port"`
	// ID of the project to manage quota. Changing this
	// creates new quota.
	ProjectId string `pulumi:"projectId"`
	// Quota value for RBAC policies.
	// Changing this updates the existing quota.
	RbacPolicy *int `pulumi:"rbacPolicy"`
	// The region in which to create the quota. If
	// omitted, the `region` argument of the provider is used. Changing this
	// creates new quota.
	Region *string `pulumi:"region"`
	// Quota value for routers. Changing this updates the
	// existing quota.
	Router *int `pulumi:"router"`
	// Quota value for security groups. Changing
	// this updates the existing quota.
	SecurityGroup *int `pulumi:"securityGroup"`
	// Quota value for security group rules.
	// Changing this updates the existing quota.
	SecurityGroupRule *int `pulumi:"securityGroupRule"`
	// Quota value for subnets. Changing
	// this updates the existing quota.
	Subnet *int `pulumi:"subnet"`
	// Quota value for subnetpools.
	// Changing this updates the existing quota.
	Subnetpool *int `pulumi:"subnetpool"`
}

// The set of arguments for constructing a QuotaV2 resource.
type QuotaV2Args struct {
	// Quota value for floating IPs. Changing this updates the
	// existing quota.
	Floatingip pulumi.IntPtrInput
	// Quota value for networks. Changing this updates the
	// existing quota.
	Network pulumi.IntPtrInput
	// Quota value for ports. Changing this updates the
	// existing quota.
	Port pulumi.IntPtrInput
	// ID of the project to manage quota. Changing this
	// creates new quota.
	ProjectId pulumi.StringInput
	// Quota value for RBAC policies.
	// Changing this updates the existing quota.
	RbacPolicy pulumi.IntPtrInput
	// The region in which to create the quota. If
	// omitted, the `region` argument of the provider is used. Changing this
	// creates new quota.
	Region pulumi.StringPtrInput
	// Quota value for routers. Changing this updates the
	// existing quota.
	Router pulumi.IntPtrInput
	// Quota value for security groups. Changing
	// this updates the existing quota.
	SecurityGroup pulumi.IntPtrInput
	// Quota value for security group rules.
	// Changing this updates the existing quota.
	SecurityGroupRule pulumi.IntPtrInput
	// Quota value for subnets. Changing
	// this updates the existing quota.
	Subnet pulumi.IntPtrInput
	// Quota value for subnetpools.
	// Changing this updates the existing quota.
	Subnetpool pulumi.IntPtrInput
}

func (QuotaV2Args) ElementType() reflect.Type {
	return reflect.TypeOf((*quotaV2Args)(nil)).Elem()
}

