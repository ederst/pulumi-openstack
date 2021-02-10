// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a project access for flavor V2 resource within OpenStack.
//
// > **Note:** You _must_ have admin privileges in your OpenStack cloud to use
// this resource.
//
// ***
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/compute"
// 	"github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/identity"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		project1, err := identity.NewProject(ctx, "project1", nil)
// 		if err != nil {
// 			return err
// 		}
// 		flavor1, err := compute.NewFlavor(ctx, "flavor1", &compute.FlavorArgs{
// 			Disk:     pulumi.Int(20),
// 			IsPublic: pulumi.Bool(false),
// 			Ram:      pulumi.Int(8096),
// 			Vcpus:    pulumi.Int(2),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = compute.NewFlavorAccess(ctx, "access1", &compute.FlavorAccessArgs{
// 			FlavorId: flavor1.ID(),
// 			TenantId: project1.ID(),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Import
//
// This resource can be imported by specifying all two arguments, separated by a forward slash
//
// ```sh
//  $ pulumi import openstack:compute/flavorAccess:FlavorAccess access_1 <flavor_id>/<tenant_id>
// ```
type FlavorAccess struct {
	pulumi.CustomResourceState

	// The UUID of flavor to use. Changing this creates a new flavor access.
	FlavorId pulumi.StringOutput `pulumi:"flavorId"`
	// The region in which to obtain the V2 Compute client.
	// If omitted, the `region` argument of the provider is used.
	// Changing this creates a new flavor access.
	Region pulumi.StringOutput `pulumi:"region"`
	// The UUID of tenant which is allowed to use the flavor.
	// Changing this creates a new flavor access.
	TenantId pulumi.StringOutput `pulumi:"tenantId"`
}

// NewFlavorAccess registers a new resource with the given unique name, arguments, and options.
func NewFlavorAccess(ctx *pulumi.Context,
	name string, args *FlavorAccessArgs, opts ...pulumi.ResourceOption) (*FlavorAccess, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.FlavorId == nil {
		return nil, errors.New("invalid value for required argument 'FlavorId'")
	}
	if args.TenantId == nil {
		return nil, errors.New("invalid value for required argument 'TenantId'")
	}
	var resource FlavorAccess
	err := ctx.RegisterResource("openstack:compute/flavorAccess:FlavorAccess", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetFlavorAccess gets an existing FlavorAccess resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetFlavorAccess(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *FlavorAccessState, opts ...pulumi.ResourceOption) (*FlavorAccess, error) {
	var resource FlavorAccess
	err := ctx.ReadResource("openstack:compute/flavorAccess:FlavorAccess", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering FlavorAccess resources.
type flavorAccessState struct {
	// The UUID of flavor to use. Changing this creates a new flavor access.
	FlavorId *string `pulumi:"flavorId"`
	// The region in which to obtain the V2 Compute client.
	// If omitted, the `region` argument of the provider is used.
	// Changing this creates a new flavor access.
	Region *string `pulumi:"region"`
	// The UUID of tenant which is allowed to use the flavor.
	// Changing this creates a new flavor access.
	TenantId *string `pulumi:"tenantId"`
}

type FlavorAccessState struct {
	// The UUID of flavor to use. Changing this creates a new flavor access.
	FlavorId pulumi.StringPtrInput
	// The region in which to obtain the V2 Compute client.
	// If omitted, the `region` argument of the provider is used.
	// Changing this creates a new flavor access.
	Region pulumi.StringPtrInput
	// The UUID of tenant which is allowed to use the flavor.
	// Changing this creates a new flavor access.
	TenantId pulumi.StringPtrInput
}

func (FlavorAccessState) ElementType() reflect.Type {
	return reflect.TypeOf((*flavorAccessState)(nil)).Elem()
}

type flavorAccessArgs struct {
	// The UUID of flavor to use. Changing this creates a new flavor access.
	FlavorId string `pulumi:"flavorId"`
	// The region in which to obtain the V2 Compute client.
	// If omitted, the `region` argument of the provider is used.
	// Changing this creates a new flavor access.
	Region *string `pulumi:"region"`
	// The UUID of tenant which is allowed to use the flavor.
	// Changing this creates a new flavor access.
	TenantId string `pulumi:"tenantId"`
}

// The set of arguments for constructing a FlavorAccess resource.
type FlavorAccessArgs struct {
	// The UUID of flavor to use. Changing this creates a new flavor access.
	FlavorId pulumi.StringInput
	// The region in which to obtain the V2 Compute client.
	// If omitted, the `region` argument of the provider is used.
	// Changing this creates a new flavor access.
	Region pulumi.StringPtrInput
	// The UUID of tenant which is allowed to use the flavor.
	// Changing this creates a new flavor access.
	TenantId pulumi.StringInput
}

func (FlavorAccessArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*flavorAccessArgs)(nil)).Elem()
}

type FlavorAccessInput interface {
	pulumi.Input

	ToFlavorAccessOutput() FlavorAccessOutput
	ToFlavorAccessOutputWithContext(ctx context.Context) FlavorAccessOutput
}

func (*FlavorAccess) ElementType() reflect.Type {
	return reflect.TypeOf((*FlavorAccess)(nil))
}

func (i *FlavorAccess) ToFlavorAccessOutput() FlavorAccessOutput {
	return i.ToFlavorAccessOutputWithContext(context.Background())
}

func (i *FlavorAccess) ToFlavorAccessOutputWithContext(ctx context.Context) FlavorAccessOutput {
	return pulumi.ToOutputWithContext(ctx, i).(FlavorAccessOutput)
}

type FlavorAccessOutput struct {
	*pulumi.OutputState
}

func (FlavorAccessOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*FlavorAccess)(nil))
}

func (o FlavorAccessOutput) ToFlavorAccessOutput() FlavorAccessOutput {
	return o
}

func (o FlavorAccessOutput) ToFlavorAccessOutputWithContext(ctx context.Context) FlavorAccessOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(FlavorAccessOutput{})
}
