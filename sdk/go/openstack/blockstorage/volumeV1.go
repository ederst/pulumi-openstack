// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package blockstorage

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a V1 volume resource within OpenStack.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/blockstorage"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := blockstorage.NewVolumeV1(ctx, "volume1", &blockstorage.VolumeV1Args{
// 			Description: pulumi.String("first test volume"),
// 			Region:      pulumi.String("RegionOne"),
// 			Size:        pulumi.Int(3),
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
// Volumes can be imported using the `id`, e.g.
//
// ```sh
//  $ pulumi import openstack:blockstorage/volumeV1:VolumeV1 volume_1 ea257959-eeb1-4c10-8d33-26f0409a755d
// ```
type VolumeV1 struct {
	pulumi.CustomResourceState

	// If a volume is attached to an instance, this attribute will
	// display the Attachment ID, Instance ID, and the Device as the Instance
	// sees it.
	Attachments VolumeV1AttachmentArrayOutput `pulumi:"attachments"`
	// The availability zone for the volume.
	// Changing this creates a new volume.
	AvailabilityZone pulumi.StringOutput `pulumi:"availabilityZone"`
	// A description of the volume. Changing this updates
	// the volume's description.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The image ID from which to create the volume.
	// Changing this creates a new volume.
	ImageId pulumi.StringPtrOutput `pulumi:"imageId"`
	// Metadata key/value pairs to associate with the volume.
	// Changing this updates the existing volume metadata.
	Metadata pulumi.MapOutput `pulumi:"metadata"`
	// A unique name for the volume. Changing this updates the
	// volume's name.
	Name pulumi.StringOutput `pulumi:"name"`
	// The region in which to create the volume. If
	// omitted, the `region` argument of the provider is used. Changing this
	// creates a new volume.
	Region pulumi.StringOutput `pulumi:"region"`
	// The size of the volume to create (in gigabytes). Changing
	// this creates a new volume.
	Size pulumi.IntOutput `pulumi:"size"`
	// The snapshot ID from which to create the volume.
	// Changing this creates a new volume.
	SnapshotId pulumi.StringPtrOutput `pulumi:"snapshotId"`
	// The volume ID from which to create the volume.
	// Changing this creates a new volume.
	SourceVolId pulumi.StringPtrOutput `pulumi:"sourceVolId"`
	// The type of volume to create.
	// Changing this creates a new volume.
	VolumeType pulumi.StringOutput `pulumi:"volumeType"`
}

// NewVolumeV1 registers a new resource with the given unique name, arguments, and options.
func NewVolumeV1(ctx *pulumi.Context,
	name string, args *VolumeV1Args, opts ...pulumi.ResourceOption) (*VolumeV1, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Size == nil {
		return nil, errors.New("invalid value for required argument 'Size'")
	}
	var resource VolumeV1
	err := ctx.RegisterResource("openstack:blockstorage/volumeV1:VolumeV1", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetVolumeV1 gets an existing VolumeV1 resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVolumeV1(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *VolumeV1State, opts ...pulumi.ResourceOption) (*VolumeV1, error) {
	var resource VolumeV1
	err := ctx.ReadResource("openstack:blockstorage/volumeV1:VolumeV1", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering VolumeV1 resources.
type volumeV1State struct {
	// If a volume is attached to an instance, this attribute will
	// display the Attachment ID, Instance ID, and the Device as the Instance
	// sees it.
	Attachments []VolumeV1Attachment `pulumi:"attachments"`
	// The availability zone for the volume.
	// Changing this creates a new volume.
	AvailabilityZone *string `pulumi:"availabilityZone"`
	// A description of the volume. Changing this updates
	// the volume's description.
	Description *string `pulumi:"description"`
	// The image ID from which to create the volume.
	// Changing this creates a new volume.
	ImageId *string `pulumi:"imageId"`
	// Metadata key/value pairs to associate with the volume.
	// Changing this updates the existing volume metadata.
	Metadata map[string]interface{} `pulumi:"metadata"`
	// A unique name for the volume. Changing this updates the
	// volume's name.
	Name *string `pulumi:"name"`
	// The region in which to create the volume. If
	// omitted, the `region` argument of the provider is used. Changing this
	// creates a new volume.
	Region *string `pulumi:"region"`
	// The size of the volume to create (in gigabytes). Changing
	// this creates a new volume.
	Size *int `pulumi:"size"`
	// The snapshot ID from which to create the volume.
	// Changing this creates a new volume.
	SnapshotId *string `pulumi:"snapshotId"`
	// The volume ID from which to create the volume.
	// Changing this creates a new volume.
	SourceVolId *string `pulumi:"sourceVolId"`
	// The type of volume to create.
	// Changing this creates a new volume.
	VolumeType *string `pulumi:"volumeType"`
}

type VolumeV1State struct {
	// If a volume is attached to an instance, this attribute will
	// display the Attachment ID, Instance ID, and the Device as the Instance
	// sees it.
	Attachments VolumeV1AttachmentArrayInput
	// The availability zone for the volume.
	// Changing this creates a new volume.
	AvailabilityZone pulumi.StringPtrInput
	// A description of the volume. Changing this updates
	// the volume's description.
	Description pulumi.StringPtrInput
	// The image ID from which to create the volume.
	// Changing this creates a new volume.
	ImageId pulumi.StringPtrInput
	// Metadata key/value pairs to associate with the volume.
	// Changing this updates the existing volume metadata.
	Metadata pulumi.MapInput
	// A unique name for the volume. Changing this updates the
	// volume's name.
	Name pulumi.StringPtrInput
	// The region in which to create the volume. If
	// omitted, the `region` argument of the provider is used. Changing this
	// creates a new volume.
	Region pulumi.StringPtrInput
	// The size of the volume to create (in gigabytes). Changing
	// this creates a new volume.
	Size pulumi.IntPtrInput
	// The snapshot ID from which to create the volume.
	// Changing this creates a new volume.
	SnapshotId pulumi.StringPtrInput
	// The volume ID from which to create the volume.
	// Changing this creates a new volume.
	SourceVolId pulumi.StringPtrInput
	// The type of volume to create.
	// Changing this creates a new volume.
	VolumeType pulumi.StringPtrInput
}

func (VolumeV1State) ElementType() reflect.Type {
	return reflect.TypeOf((*volumeV1State)(nil)).Elem()
}

type volumeV1Args struct {
	// The availability zone for the volume.
	// Changing this creates a new volume.
	AvailabilityZone *string `pulumi:"availabilityZone"`
	// A description of the volume. Changing this updates
	// the volume's description.
	Description *string `pulumi:"description"`
	// The image ID from which to create the volume.
	// Changing this creates a new volume.
	ImageId *string `pulumi:"imageId"`
	// Metadata key/value pairs to associate with the volume.
	// Changing this updates the existing volume metadata.
	Metadata map[string]interface{} `pulumi:"metadata"`
	// A unique name for the volume. Changing this updates the
	// volume's name.
	Name *string `pulumi:"name"`
	// The region in which to create the volume. If
	// omitted, the `region` argument of the provider is used. Changing this
	// creates a new volume.
	Region *string `pulumi:"region"`
	// The size of the volume to create (in gigabytes). Changing
	// this creates a new volume.
	Size int `pulumi:"size"`
	// The snapshot ID from which to create the volume.
	// Changing this creates a new volume.
	SnapshotId *string `pulumi:"snapshotId"`
	// The volume ID from which to create the volume.
	// Changing this creates a new volume.
	SourceVolId *string `pulumi:"sourceVolId"`
	// The type of volume to create.
	// Changing this creates a new volume.
	VolumeType *string `pulumi:"volumeType"`
}

// The set of arguments for constructing a VolumeV1 resource.
type VolumeV1Args struct {
	// The availability zone for the volume.
	// Changing this creates a new volume.
	AvailabilityZone pulumi.StringPtrInput
	// A description of the volume. Changing this updates
	// the volume's description.
	Description pulumi.StringPtrInput
	// The image ID from which to create the volume.
	// Changing this creates a new volume.
	ImageId pulumi.StringPtrInput
	// Metadata key/value pairs to associate with the volume.
	// Changing this updates the existing volume metadata.
	Metadata pulumi.MapInput
	// A unique name for the volume. Changing this updates the
	// volume's name.
	Name pulumi.StringPtrInput
	// The region in which to create the volume. If
	// omitted, the `region` argument of the provider is used. Changing this
	// creates a new volume.
	Region pulumi.StringPtrInput
	// The size of the volume to create (in gigabytes). Changing
	// this creates a new volume.
	Size pulumi.IntInput
	// The snapshot ID from which to create the volume.
	// Changing this creates a new volume.
	SnapshotId pulumi.StringPtrInput
	// The volume ID from which to create the volume.
	// Changing this creates a new volume.
	SourceVolId pulumi.StringPtrInput
	// The type of volume to create.
	// Changing this creates a new volume.
	VolumeType pulumi.StringPtrInput
}

func (VolumeV1Args) ElementType() reflect.Type {
	return reflect.TypeOf((*volumeV1Args)(nil)).Elem()
}

type VolumeV1Input interface {
	pulumi.Input

	ToVolumeV1Output() VolumeV1Output
	ToVolumeV1OutputWithContext(ctx context.Context) VolumeV1Output
}

func (*VolumeV1) ElementType() reflect.Type {
	return reflect.TypeOf((*VolumeV1)(nil))
}

func (i *VolumeV1) ToVolumeV1Output() VolumeV1Output {
	return i.ToVolumeV1OutputWithContext(context.Background())
}

func (i *VolumeV1) ToVolumeV1OutputWithContext(ctx context.Context) VolumeV1Output {
	return pulumi.ToOutputWithContext(ctx, i).(VolumeV1Output)
}

func (i *VolumeV1) ToVolumeV1PtrOutput() VolumeV1PtrOutput {
	return i.ToVolumeV1PtrOutputWithContext(context.Background())
}

func (i *VolumeV1) ToVolumeV1PtrOutputWithContext(ctx context.Context) VolumeV1PtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VolumeV1PtrOutput)
}

type VolumeV1PtrInput interface {
	pulumi.Input

	ToVolumeV1PtrOutput() VolumeV1PtrOutput
	ToVolumeV1PtrOutputWithContext(ctx context.Context) VolumeV1PtrOutput
}

type volumeV1PtrType VolumeV1Args

func (*volumeV1PtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**VolumeV1)(nil))
}

func (i *volumeV1PtrType) ToVolumeV1PtrOutput() VolumeV1PtrOutput {
	return i.ToVolumeV1PtrOutputWithContext(context.Background())
}

func (i *volumeV1PtrType) ToVolumeV1PtrOutputWithContext(ctx context.Context) VolumeV1PtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VolumeV1PtrOutput)
}

// VolumeV1ArrayInput is an input type that accepts VolumeV1Array and VolumeV1ArrayOutput values.
// You can construct a concrete instance of `VolumeV1ArrayInput` via:
//
//          VolumeV1Array{ VolumeV1Args{...} }
type VolumeV1ArrayInput interface {
	pulumi.Input

	ToVolumeV1ArrayOutput() VolumeV1ArrayOutput
	ToVolumeV1ArrayOutputWithContext(context.Context) VolumeV1ArrayOutput
}

type VolumeV1Array []VolumeV1Input

func (VolumeV1Array) ElementType() reflect.Type {
	return reflect.TypeOf(([]*VolumeV1)(nil))
}

func (i VolumeV1Array) ToVolumeV1ArrayOutput() VolumeV1ArrayOutput {
	return i.ToVolumeV1ArrayOutputWithContext(context.Background())
}

func (i VolumeV1Array) ToVolumeV1ArrayOutputWithContext(ctx context.Context) VolumeV1ArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VolumeV1ArrayOutput)
}

// VolumeV1MapInput is an input type that accepts VolumeV1Map and VolumeV1MapOutput values.
// You can construct a concrete instance of `VolumeV1MapInput` via:
//
//          VolumeV1Map{ "key": VolumeV1Args{...} }
type VolumeV1MapInput interface {
	pulumi.Input

	ToVolumeV1MapOutput() VolumeV1MapOutput
	ToVolumeV1MapOutputWithContext(context.Context) VolumeV1MapOutput
}

type VolumeV1Map map[string]VolumeV1Input

func (VolumeV1Map) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*VolumeV1)(nil))
}

func (i VolumeV1Map) ToVolumeV1MapOutput() VolumeV1MapOutput {
	return i.ToVolumeV1MapOutputWithContext(context.Background())
}

func (i VolumeV1Map) ToVolumeV1MapOutputWithContext(ctx context.Context) VolumeV1MapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(VolumeV1MapOutput)
}

type VolumeV1Output struct {
	*pulumi.OutputState
}

func (VolumeV1Output) ElementType() reflect.Type {
	return reflect.TypeOf((*VolumeV1)(nil))
}

func (o VolumeV1Output) ToVolumeV1Output() VolumeV1Output {
	return o
}

func (o VolumeV1Output) ToVolumeV1OutputWithContext(ctx context.Context) VolumeV1Output {
	return o
}

func (o VolumeV1Output) ToVolumeV1PtrOutput() VolumeV1PtrOutput {
	return o.ToVolumeV1PtrOutputWithContext(context.Background())
}

func (o VolumeV1Output) ToVolumeV1PtrOutputWithContext(ctx context.Context) VolumeV1PtrOutput {
	return o.ApplyT(func(v VolumeV1) *VolumeV1 {
		return &v
	}).(VolumeV1PtrOutput)
}

type VolumeV1PtrOutput struct {
	*pulumi.OutputState
}

func (VolumeV1PtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**VolumeV1)(nil))
}

func (o VolumeV1PtrOutput) ToVolumeV1PtrOutput() VolumeV1PtrOutput {
	return o
}

func (o VolumeV1PtrOutput) ToVolumeV1PtrOutputWithContext(ctx context.Context) VolumeV1PtrOutput {
	return o
}

type VolumeV1ArrayOutput struct{ *pulumi.OutputState }

func (VolumeV1ArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]VolumeV1)(nil))
}

func (o VolumeV1ArrayOutput) ToVolumeV1ArrayOutput() VolumeV1ArrayOutput {
	return o
}

func (o VolumeV1ArrayOutput) ToVolumeV1ArrayOutputWithContext(ctx context.Context) VolumeV1ArrayOutput {
	return o
}

func (o VolumeV1ArrayOutput) Index(i pulumi.IntInput) VolumeV1Output {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) VolumeV1 {
		return vs[0].([]VolumeV1)[vs[1].(int)]
	}).(VolumeV1Output)
}

type VolumeV1MapOutput struct{ *pulumi.OutputState }

func (VolumeV1MapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]VolumeV1)(nil))
}

func (o VolumeV1MapOutput) ToVolumeV1MapOutput() VolumeV1MapOutput {
	return o
}

func (o VolumeV1MapOutput) ToVolumeV1MapOutputWithContext(ctx context.Context) VolumeV1MapOutput {
	return o
}

func (o VolumeV1MapOutput) MapIndex(k pulumi.StringInput) VolumeV1Output {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) VolumeV1 {
		return vs[0].(map[string]VolumeV1)[vs[1].(string)]
	}).(VolumeV1Output)
}

func init() {
	pulumi.RegisterOutputType(VolumeV1Output{})
	pulumi.RegisterOutputType(VolumeV1PtrOutput{})
	pulumi.RegisterOutputType(VolumeV1ArrayOutput{})
	pulumi.RegisterOutputType(VolumeV1MapOutput{})
}
