// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package compute

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Associate a floating IP to an instance. This can be used instead of the
// `floatingIp` options in `compute.Instance`.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_floatingip_associate_v2.html.markdown.
type FloatingIpAssociate struct {
	pulumi.CustomResourceState

	// The specific IP address to direct traffic to.
	FixedIp pulumi.StringPtrOutput `pulumi:"fixedIp"`
	// The floating IP to associate.
	FloatingIp pulumi.StringOutput `pulumi:"floatingIp"`
	// The instance to associte the floating IP with.
	InstanceId pulumi.StringOutput `pulumi:"instanceId"`
	// The region in which to obtain the V2 Compute client.
	// Keypairs are associated with accounts, but a Compute client is needed to
	// create one. If omitted, the `region` argument of the provider is used.
	// Changing this creates a new floatingip_associate.
	Region              pulumi.StringOutput  `pulumi:"region"`
	WaitUntilAssociated pulumi.BoolPtrOutput `pulumi:"waitUntilAssociated"`
}

// NewFloatingIpAssociate registers a new resource with the given unique name, arguments, and options.
func NewFloatingIpAssociate(ctx *pulumi.Context,
	name string, args *FloatingIpAssociateArgs, opts ...pulumi.ResourceOption) (*FloatingIpAssociate, error) {
	if args == nil || args.FloatingIp == nil {
		return nil, errors.New("missing required argument 'FloatingIp'")
	}
	if args == nil || args.InstanceId == nil {
		return nil, errors.New("missing required argument 'InstanceId'")
	}
	if args == nil {
		args = &FloatingIpAssociateArgs{}
	}
	var resource FloatingIpAssociate
	err := ctx.RegisterResource("openstack:compute/floatingIpAssociate:FloatingIpAssociate", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFloatingIpAssociate gets an existing FloatingIpAssociate resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFloatingIpAssociate(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FloatingIpAssociateState, opts ...pulumi.ResourceOption) (*FloatingIpAssociate, error) {
	var resource FloatingIpAssociate
	err := ctx.ReadResource("openstack:compute/floatingIpAssociate:FloatingIpAssociate", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering FloatingIpAssociate resources.
type floatingIpAssociateState struct {
	// The specific IP address to direct traffic to.
	FixedIp *string `pulumi:"fixedIp"`
	// The floating IP to associate.
	FloatingIp *string `pulumi:"floatingIp"`
	// The instance to associte the floating IP with.
	InstanceId *string `pulumi:"instanceId"`
	// The region in which to obtain the V2 Compute client.
	// Keypairs are associated with accounts, but a Compute client is needed to
	// create one. If omitted, the `region` argument of the provider is used.
	// Changing this creates a new floatingip_associate.
	Region              *string `pulumi:"region"`
	WaitUntilAssociated *bool   `pulumi:"waitUntilAssociated"`
}

type FloatingIpAssociateState struct {
	// The specific IP address to direct traffic to.
	FixedIp pulumi.StringPtrInput
	// The floating IP to associate.
	FloatingIp pulumi.StringPtrInput
	// The instance to associte the floating IP with.
	InstanceId pulumi.StringPtrInput
	// The region in which to obtain the V2 Compute client.
	// Keypairs are associated with accounts, but a Compute client is needed to
	// create one. If omitted, the `region` argument of the provider is used.
	// Changing this creates a new floatingip_associate.
	Region              pulumi.StringPtrInput
	WaitUntilAssociated pulumi.BoolPtrInput
}

func (FloatingIpAssociateState) ElementType() reflect.Type {
	return reflect.TypeOf((*floatingIpAssociateState)(nil)).Elem()
}

type floatingIpAssociateArgs struct {
	// The specific IP address to direct traffic to.
	FixedIp *string `pulumi:"fixedIp"`
	// The floating IP to associate.
	FloatingIp string `pulumi:"floatingIp"`
	// The instance to associte the floating IP with.
	InstanceId string `pulumi:"instanceId"`
	// The region in which to obtain the V2 Compute client.
	// Keypairs are associated with accounts, but a Compute client is needed to
	// create one. If omitted, the `region` argument of the provider is used.
	// Changing this creates a new floatingip_associate.
	Region              *string `pulumi:"region"`
	WaitUntilAssociated *bool   `pulumi:"waitUntilAssociated"`
}

// The set of arguments for constructing a FloatingIpAssociate resource.
type FloatingIpAssociateArgs struct {
	// The specific IP address to direct traffic to.
	FixedIp pulumi.StringPtrInput
	// The floating IP to associate.
	FloatingIp pulumi.StringInput
	// The instance to associte the floating IP with.
	InstanceId pulumi.StringInput
	// The region in which to obtain the V2 Compute client.
	// Keypairs are associated with accounts, but a Compute client is needed to
	// create one. If omitted, the `region` argument of the provider is used.
	// Changing this creates a new floatingip_associate.
	Region              pulumi.StringPtrInput
	WaitUntilAssociated pulumi.BoolPtrInput
}

func (FloatingIpAssociateArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*floatingIpAssociateArgs)(nil)).Elem()
}
