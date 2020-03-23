// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package compute

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a V2 floating IP resource within OpenStack Nova (compute)
// that can be used for compute instances.
//
// Please note that managing floating IPs through the OpenStack Compute API has
// been deprecated. Unless you are using an older OpenStack environment, it is
// recommended to use the `networking.FloatingIp`
// resource instead, which uses the OpenStack Networking API.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_floatingip_v2.html.markdown.
type FloatingIp struct {
	pulumi.CustomResourceState

	// The actual floating IP address itself.
	Address pulumi.StringOutput `pulumi:"address"`
	// The fixed IP address corresponding to the floating IP.
	FixedIp pulumi.StringOutput `pulumi:"fixedIp"`
	// UUID of the compute instance associated with the floating IP.
	InstanceId pulumi.StringOutput `pulumi:"instanceId"`
	// The name of the pool from which to obtain the floating
	// IP. Changing this creates a new floating IP.
	Pool pulumi.StringOutput `pulumi:"pool"`
	// The region in which to obtain the V2 Compute client.
	// A Compute client is needed to create a floating IP that can be used with
	// a compute instance. If omitted, the `region` argument of the provider
	// is used. Changing this creates a new floating IP (which may or may not
	// have a different address).
	Region pulumi.StringOutput `pulumi:"region"`
}

// NewFloatingIp registers a new resource with the given unique name, arguments, and options.
func NewFloatingIp(ctx *pulumi.Context,
	name string, args *FloatingIpArgs, opts ...pulumi.ResourceOption) (*FloatingIp, error) {
	if args == nil || args.Pool == nil {
		return nil, errors.New("missing required argument 'Pool'")
	}
	if args == nil {
		args = &FloatingIpArgs{}
	}
	var resource FloatingIp
	err := ctx.RegisterResource("openstack:compute/floatingIp:FloatingIp", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFloatingIp gets an existing FloatingIp resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFloatingIp(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FloatingIpState, opts ...pulumi.ResourceOption) (*FloatingIp, error) {
	var resource FloatingIp
	err := ctx.ReadResource("openstack:compute/floatingIp:FloatingIp", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering FloatingIp resources.
type floatingIpState struct {
	// The actual floating IP address itself.
	Address *string `pulumi:"address"`
	// The fixed IP address corresponding to the floating IP.
	FixedIp *string `pulumi:"fixedIp"`
	// UUID of the compute instance associated with the floating IP.
	InstanceId *string `pulumi:"instanceId"`
	// The name of the pool from which to obtain the floating
	// IP. Changing this creates a new floating IP.
	Pool *string `pulumi:"pool"`
	// The region in which to obtain the V2 Compute client.
	// A Compute client is needed to create a floating IP that can be used with
	// a compute instance. If omitted, the `region` argument of the provider
	// is used. Changing this creates a new floating IP (which may or may not
	// have a different address).
	Region *string `pulumi:"region"`
}

type FloatingIpState struct {
	// The actual floating IP address itself.
	Address pulumi.StringPtrInput
	// The fixed IP address corresponding to the floating IP.
	FixedIp pulumi.StringPtrInput
	// UUID of the compute instance associated with the floating IP.
	InstanceId pulumi.StringPtrInput
	// The name of the pool from which to obtain the floating
	// IP. Changing this creates a new floating IP.
	Pool pulumi.StringPtrInput
	// The region in which to obtain the V2 Compute client.
	// A Compute client is needed to create a floating IP that can be used with
	// a compute instance. If omitted, the `region` argument of the provider
	// is used. Changing this creates a new floating IP (which may or may not
	// have a different address).
	Region pulumi.StringPtrInput
}

func (FloatingIpState) ElementType() reflect.Type {
	return reflect.TypeOf((*floatingIpState)(nil)).Elem()
}

type floatingIpArgs struct {
	// The name of the pool from which to obtain the floating
	// IP. Changing this creates a new floating IP.
	Pool string `pulumi:"pool"`
	// The region in which to obtain the V2 Compute client.
	// A Compute client is needed to create a floating IP that can be used with
	// a compute instance. If omitted, the `region` argument of the provider
	// is used. Changing this creates a new floating IP (which may or may not
	// have a different address).
	Region *string `pulumi:"region"`
}

// The set of arguments for constructing a FloatingIp resource.
type FloatingIpArgs struct {
	// The name of the pool from which to obtain the floating
	// IP. Changing this creates a new floating IP.
	Pool pulumi.StringInput
	// The region in which to obtain the V2 Compute client.
	// A Compute client is needed to create a floating IP that can be used with
	// a compute instance. If omitted, the `region` argument of the provider
	// is used. Changing this creates a new floating IP (which may or may not
	// have a different address).
	Region pulumi.StringPtrInput
}

func (FloatingIpArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*floatingIpArgs)(nil)).Elem()
}

