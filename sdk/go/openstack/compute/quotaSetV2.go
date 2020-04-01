// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package compute

import (
	"reflect"

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
	pulumi.CustomResourceState

	// Quota value for cores.
	// Changing this updates the existing quotaset.
	Cores pulumi.IntOutput `pulumi:"cores"`
	// Quota value for fixed IPs.
	// Changing this updates the existing quotaset.
	FixedIps pulumi.IntOutput `pulumi:"fixedIps"`
	// Quota value for floating IPs.
	// Changing this updates the existing quotaset.
	FloatingIps pulumi.IntOutput `pulumi:"floatingIps"`
	// Quota value for content bytes
	// of injected files. Changing this updates the existing quotaset.
	InjectedFileContentBytes pulumi.IntOutput `pulumi:"injectedFileContentBytes"`
	// Quota value for path bytes of
	// injected files. Changing this updates the existing quotaset.
	InjectedFilePathBytes pulumi.IntOutput `pulumi:"injectedFilePathBytes"`
	// Quota value for injected files.
	// Changing this updates the existing quotaset.
	InjectedFiles pulumi.IntOutput `pulumi:"injectedFiles"`
	// Quota value for instances.
	// Changing this updates the existing quotaset.
	Instances pulumi.IntOutput `pulumi:"instances"`
	// Quota value for key pairs.
	// Changing this updates the existing quotaset.
	KeyPairs pulumi.IntOutput `pulumi:"keyPairs"`
	// Quota value for metadata items.
	// Changing this updates the existing quotaset.
	MetadataItems pulumi.IntOutput `pulumi:"metadataItems"`
	// ID of the project to manage quotas.
	// Changing this creates a new quotaset.
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
	// Quota value for RAM.
	// Changing this updates the existing quotaset.
	Ram pulumi.IntOutput `pulumi:"ram"`
	// The region in which to create the volume. If
	// omitted, the `region` argument of the provider is used. Changing this
	// creates a new quotaset.
	Region pulumi.StringOutput `pulumi:"region"`
	// Quota value for security group rules.
	// Changing this updates the existing quotaset.
	SecurityGroupRules pulumi.IntOutput `pulumi:"securityGroupRules"`
	// Quota value for security groups.
	// Changing this updates the existing quotaset.
	SecurityGroups pulumi.IntOutput `pulumi:"securityGroups"`
	// Quota value for server groups members.
	// Changing this updates the existing quotaset.
	ServerGroupMembers pulumi.IntOutput `pulumi:"serverGroupMembers"`
	// Quota value for server groups.
	// Changing this updates the existing quotaset.
	ServerGroups pulumi.IntOutput `pulumi:"serverGroups"`
}

// NewQuotaSetV2 registers a new resource with the given unique name, arguments, and options.
func NewQuotaSetV2(ctx *pulumi.Context,
	name string, args *QuotaSetV2Args, opts ...pulumi.ResourceOption) (*QuotaSetV2, error) {
	if args == nil || args.ProjectId == nil {
		return nil, errors.New("missing required argument 'ProjectId'")
	}
	if args == nil {
		args = &QuotaSetV2Args{}
	}
	var resource QuotaSetV2
	err := ctx.RegisterResource("openstack:compute/quotaSetV2:QuotaSetV2", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetQuotaSetV2 gets an existing QuotaSetV2 resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetQuotaSetV2(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *QuotaSetV2State, opts ...pulumi.ResourceOption) (*QuotaSetV2, error) {
	var resource QuotaSetV2
	err := ctx.ReadResource("openstack:compute/quotaSetV2:QuotaSetV2", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering QuotaSetV2 resources.
type quotaSetV2State struct {
	// Quota value for cores.
	// Changing this updates the existing quotaset.
	Cores *int `pulumi:"cores"`
	// Quota value for fixed IPs.
	// Changing this updates the existing quotaset.
	FixedIps *int `pulumi:"fixedIps"`
	// Quota value for floating IPs.
	// Changing this updates the existing quotaset.
	FloatingIps *int `pulumi:"floatingIps"`
	// Quota value for content bytes
	// of injected files. Changing this updates the existing quotaset.
	InjectedFileContentBytes *int `pulumi:"injectedFileContentBytes"`
	// Quota value for path bytes of
	// injected files. Changing this updates the existing quotaset.
	InjectedFilePathBytes *int `pulumi:"injectedFilePathBytes"`
	// Quota value for injected files.
	// Changing this updates the existing quotaset.
	InjectedFiles *int `pulumi:"injectedFiles"`
	// Quota value for instances.
	// Changing this updates the existing quotaset.
	Instances *int `pulumi:"instances"`
	// Quota value for key pairs.
	// Changing this updates the existing quotaset.
	KeyPairs *int `pulumi:"keyPairs"`
	// Quota value for metadata items.
	// Changing this updates the existing quotaset.
	MetadataItems *int `pulumi:"metadataItems"`
	// ID of the project to manage quotas.
	// Changing this creates a new quotaset.
	ProjectId *string `pulumi:"projectId"`
	// Quota value for RAM.
	// Changing this updates the existing quotaset.
	Ram *int `pulumi:"ram"`
	// The region in which to create the volume. If
	// omitted, the `region` argument of the provider is used. Changing this
	// creates a new quotaset.
	Region *string `pulumi:"region"`
	// Quota value for security group rules.
	// Changing this updates the existing quotaset.
	SecurityGroupRules *int `pulumi:"securityGroupRules"`
	// Quota value for security groups.
	// Changing this updates the existing quotaset.
	SecurityGroups *int `pulumi:"securityGroups"`
	// Quota value for server groups members.
	// Changing this updates the existing quotaset.
	ServerGroupMembers *int `pulumi:"serverGroupMembers"`
	// Quota value for server groups.
	// Changing this updates the existing quotaset.
	ServerGroups *int `pulumi:"serverGroups"`
}

type QuotaSetV2State struct {
	// Quota value for cores.
	// Changing this updates the existing quotaset.
	Cores pulumi.IntPtrInput
	// Quota value for fixed IPs.
	// Changing this updates the existing quotaset.
	FixedIps pulumi.IntPtrInput
	// Quota value for floating IPs.
	// Changing this updates the existing quotaset.
	FloatingIps pulumi.IntPtrInput
	// Quota value for content bytes
	// of injected files. Changing this updates the existing quotaset.
	InjectedFileContentBytes pulumi.IntPtrInput
	// Quota value for path bytes of
	// injected files. Changing this updates the existing quotaset.
	InjectedFilePathBytes pulumi.IntPtrInput
	// Quota value for injected files.
	// Changing this updates the existing quotaset.
	InjectedFiles pulumi.IntPtrInput
	// Quota value for instances.
	// Changing this updates the existing quotaset.
	Instances pulumi.IntPtrInput
	// Quota value for key pairs.
	// Changing this updates the existing quotaset.
	KeyPairs pulumi.IntPtrInput
	// Quota value for metadata items.
	// Changing this updates the existing quotaset.
	MetadataItems pulumi.IntPtrInput
	// ID of the project to manage quotas.
	// Changing this creates a new quotaset.
	ProjectId pulumi.StringPtrInput
	// Quota value for RAM.
	// Changing this updates the existing quotaset.
	Ram pulumi.IntPtrInput
	// The region in which to create the volume. If
	// omitted, the `region` argument of the provider is used. Changing this
	// creates a new quotaset.
	Region pulumi.StringPtrInput
	// Quota value for security group rules.
	// Changing this updates the existing quotaset.
	SecurityGroupRules pulumi.IntPtrInput
	// Quota value for security groups.
	// Changing this updates the existing quotaset.
	SecurityGroups pulumi.IntPtrInput
	// Quota value for server groups members.
	// Changing this updates the existing quotaset.
	ServerGroupMembers pulumi.IntPtrInput
	// Quota value for server groups.
	// Changing this updates the existing quotaset.
	ServerGroups pulumi.IntPtrInput
}

func (QuotaSetV2State) ElementType() reflect.Type {
	return reflect.TypeOf((*quotaSetV2State)(nil)).Elem()
}

type quotaSetV2Args struct {
	// Quota value for cores.
	// Changing this updates the existing quotaset.
	Cores *int `pulumi:"cores"`
	// Quota value for fixed IPs.
	// Changing this updates the existing quotaset.
	FixedIps *int `pulumi:"fixedIps"`
	// Quota value for floating IPs.
	// Changing this updates the existing quotaset.
	FloatingIps *int `pulumi:"floatingIps"`
	// Quota value for content bytes
	// of injected files. Changing this updates the existing quotaset.
	InjectedFileContentBytes *int `pulumi:"injectedFileContentBytes"`
	// Quota value for path bytes of
	// injected files. Changing this updates the existing quotaset.
	InjectedFilePathBytes *int `pulumi:"injectedFilePathBytes"`
	// Quota value for injected files.
	// Changing this updates the existing quotaset.
	InjectedFiles *int `pulumi:"injectedFiles"`
	// Quota value for instances.
	// Changing this updates the existing quotaset.
	Instances *int `pulumi:"instances"`
	// Quota value for key pairs.
	// Changing this updates the existing quotaset.
	KeyPairs *int `pulumi:"keyPairs"`
	// Quota value for metadata items.
	// Changing this updates the existing quotaset.
	MetadataItems *int `pulumi:"metadataItems"`
	// ID of the project to manage quotas.
	// Changing this creates a new quotaset.
	ProjectId string `pulumi:"projectId"`
	// Quota value for RAM.
	// Changing this updates the existing quotaset.
	Ram *int `pulumi:"ram"`
	// The region in which to create the volume. If
	// omitted, the `region` argument of the provider is used. Changing this
	// creates a new quotaset.
	Region *string `pulumi:"region"`
	// Quota value for security group rules.
	// Changing this updates the existing quotaset.
	SecurityGroupRules *int `pulumi:"securityGroupRules"`
	// Quota value for security groups.
	// Changing this updates the existing quotaset.
	SecurityGroups *int `pulumi:"securityGroups"`
	// Quota value for server groups members.
	// Changing this updates the existing quotaset.
	ServerGroupMembers *int `pulumi:"serverGroupMembers"`
	// Quota value for server groups.
	// Changing this updates the existing quotaset.
	ServerGroups *int `pulumi:"serverGroups"`
}

// The set of arguments for constructing a QuotaSetV2 resource.
type QuotaSetV2Args struct {
	// Quota value for cores.
	// Changing this updates the existing quotaset.
	Cores pulumi.IntPtrInput
	// Quota value for fixed IPs.
	// Changing this updates the existing quotaset.
	FixedIps pulumi.IntPtrInput
	// Quota value for floating IPs.
	// Changing this updates the existing quotaset.
	FloatingIps pulumi.IntPtrInput
	// Quota value for content bytes
	// of injected files. Changing this updates the existing quotaset.
	InjectedFileContentBytes pulumi.IntPtrInput
	// Quota value for path bytes of
	// injected files. Changing this updates the existing quotaset.
	InjectedFilePathBytes pulumi.IntPtrInput
	// Quota value for injected files.
	// Changing this updates the existing quotaset.
	InjectedFiles pulumi.IntPtrInput
	// Quota value for instances.
	// Changing this updates the existing quotaset.
	Instances pulumi.IntPtrInput
	// Quota value for key pairs.
	// Changing this updates the existing quotaset.
	KeyPairs pulumi.IntPtrInput
	// Quota value for metadata items.
	// Changing this updates the existing quotaset.
	MetadataItems pulumi.IntPtrInput
	// ID of the project to manage quotas.
	// Changing this creates a new quotaset.
	ProjectId pulumi.StringInput
	// Quota value for RAM.
	// Changing this updates the existing quotaset.
	Ram pulumi.IntPtrInput
	// The region in which to create the volume. If
	// omitted, the `region` argument of the provider is used. Changing this
	// creates a new quotaset.
	Region pulumi.StringPtrInput
	// Quota value for security group rules.
	// Changing this updates the existing quotaset.
	SecurityGroupRules pulumi.IntPtrInput
	// Quota value for security groups.
	// Changing this updates the existing quotaset.
	SecurityGroups pulumi.IntPtrInput
	// Quota value for server groups members.
	// Changing this updates the existing quotaset.
	ServerGroupMembers pulumi.IntPtrInput
	// Quota value for server groups.
	// Changing this updates the existing quotaset.
	ServerGroups pulumi.IntPtrInput
}

func (QuotaSetV2Args) ElementType() reflect.Type {
	return reflect.TypeOf((*quotaSetV2Args)(nil)).Elem()
}
