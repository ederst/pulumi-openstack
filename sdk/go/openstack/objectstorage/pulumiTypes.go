// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package objectstorage

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type ContainerVersioning struct {
	// Container in which versions will be stored.
	Location string `pulumi:"location"`
	// Versioning type which can be `versions` or `history` according to [Openstack documentation](https://docs.openstack.org/swift/latest/overview_object_versioning.html).
	Type string `pulumi:"type"`
}

type ContainerVersioningInput interface {
	pulumi.Input

	ToContainerVersioningOutput() ContainerVersioningOutput
	ToContainerVersioningOutputWithContext(context.Context) ContainerVersioningOutput
}

type ContainerVersioningArgs struct {
	// Container in which versions will be stored.
	Location pulumi.StringInput `pulumi:"location"`
	// Versioning type which can be `versions` or `history` according to [Openstack documentation](https://docs.openstack.org/swift/latest/overview_object_versioning.html).
	Type pulumi.StringInput `pulumi:"type"`
}

func (ContainerVersioningArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ContainerVersioning)(nil)).Elem()
}

func (i ContainerVersioningArgs) ToContainerVersioningOutput() ContainerVersioningOutput {
	return i.ToContainerVersioningOutputWithContext(context.Background())
}

func (i ContainerVersioningArgs) ToContainerVersioningOutputWithContext(ctx context.Context) ContainerVersioningOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ContainerVersioningOutput)
}

func (i ContainerVersioningArgs) ToContainerVersioningPtrOutput() ContainerVersioningPtrOutput {
	return i.ToContainerVersioningPtrOutputWithContext(context.Background())
}

func (i ContainerVersioningArgs) ToContainerVersioningPtrOutputWithContext(ctx context.Context) ContainerVersioningPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ContainerVersioningOutput).ToContainerVersioningPtrOutputWithContext(ctx)
}

type ContainerVersioningPtrInput interface {
	pulumi.Input

	ToContainerVersioningPtrOutput() ContainerVersioningPtrOutput
	ToContainerVersioningPtrOutputWithContext(context.Context) ContainerVersioningPtrOutput
}

type containerVersioningPtrType ContainerVersioningArgs

func ContainerVersioningPtr(v *ContainerVersioningArgs) ContainerVersioningPtrInput {
	return (*containerVersioningPtrType)(v)
}

func (*containerVersioningPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**ContainerVersioning)(nil)).Elem()
}

func (i *containerVersioningPtrType) ToContainerVersioningPtrOutput() ContainerVersioningPtrOutput {
	return i.ToContainerVersioningPtrOutputWithContext(context.Background())
}

func (i *containerVersioningPtrType) ToContainerVersioningPtrOutputWithContext(ctx context.Context) ContainerVersioningPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ContainerVersioningPtrOutput)
}

type ContainerVersioningOutput struct{ *pulumi.OutputState }

func (ContainerVersioningOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ContainerVersioning)(nil)).Elem()
}

func (o ContainerVersioningOutput) ToContainerVersioningOutput() ContainerVersioningOutput {
	return o
}

func (o ContainerVersioningOutput) ToContainerVersioningOutputWithContext(ctx context.Context) ContainerVersioningOutput {
	return o
}

func (o ContainerVersioningOutput) ToContainerVersioningPtrOutput() ContainerVersioningPtrOutput {
	return o.ToContainerVersioningPtrOutputWithContext(context.Background())
}

func (o ContainerVersioningOutput) ToContainerVersioningPtrOutputWithContext(ctx context.Context) ContainerVersioningPtrOutput {
	return o.ApplyT(func(v ContainerVersioning) *ContainerVersioning {
		return &v
	}).(ContainerVersioningPtrOutput)
}

// Container in which versions will be stored.
func (o ContainerVersioningOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v ContainerVersioning) string { return v.Location }).(pulumi.StringOutput)
}

// Versioning type which can be `versions` or `history` according to [Openstack documentation](https://docs.openstack.org/swift/latest/overview_object_versioning.html).
func (o ContainerVersioningOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v ContainerVersioning) string { return v.Type }).(pulumi.StringOutput)
}

type ContainerVersioningPtrOutput struct{ *pulumi.OutputState }

func (ContainerVersioningPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ContainerVersioning)(nil)).Elem()
}

func (o ContainerVersioningPtrOutput) ToContainerVersioningPtrOutput() ContainerVersioningPtrOutput {
	return o
}

func (o ContainerVersioningPtrOutput) ToContainerVersioningPtrOutputWithContext(ctx context.Context) ContainerVersioningPtrOutput {
	return o
}

func (o ContainerVersioningPtrOutput) Elem() ContainerVersioningOutput {
	return o.ApplyT(func(v *ContainerVersioning) ContainerVersioning { return *v }).(ContainerVersioningOutput)
}

// Container in which versions will be stored.
func (o ContainerVersioningPtrOutput) Location() pulumi.StringOutput {
	return o.ApplyT(func(v ContainerVersioning) string { return v.Location }).(pulumi.StringOutput)
}

// Versioning type which can be `versions` or `history` according to [Openstack documentation](https://docs.openstack.org/swift/latest/overview_object_versioning.html).
func (o ContainerVersioningPtrOutput) Type() pulumi.StringOutput {
	return o.ApplyT(func(v ContainerVersioning) string { return v.Type }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(ContainerVersioningOutput{})
	pulumi.RegisterOutputType(ContainerVersioningPtrOutput{})
}
