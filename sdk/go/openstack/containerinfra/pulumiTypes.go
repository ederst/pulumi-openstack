// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package containerinfra

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type ClusterKubeconfig struct {
	ClientCertificate    *string `pulumi:"clientCertificate"`
	ClientKey            *string `pulumi:"clientKey"`
	ClusterCaCertificate *string `pulumi:"clusterCaCertificate"`
	Host                 *string `pulumi:"host"`
	RawConfig            *string `pulumi:"rawConfig"`
}

// ClusterKubeconfigInput is an input type that accepts ClusterKubeconfigArgs and ClusterKubeconfigOutput values.
// You can construct a concrete instance of `ClusterKubeconfigInput` via:
//
//          ClusterKubeconfigArgs{...}
type ClusterKubeconfigInput interface {
	pulumi.Input

	ToClusterKubeconfigOutput() ClusterKubeconfigOutput
	ToClusterKubeconfigOutputWithContext(context.Context) ClusterKubeconfigOutput
}

type ClusterKubeconfigArgs struct {
	ClientCertificate    pulumi.StringPtrInput `pulumi:"clientCertificate"`
	ClientKey            pulumi.StringPtrInput `pulumi:"clientKey"`
	ClusterCaCertificate pulumi.StringPtrInput `pulumi:"clusterCaCertificate"`
	Host                 pulumi.StringPtrInput `pulumi:"host"`
	RawConfig            pulumi.StringPtrInput `pulumi:"rawConfig"`
}

func (ClusterKubeconfigArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ClusterKubeconfig)(nil)).Elem()
}

func (i ClusterKubeconfigArgs) ToClusterKubeconfigOutput() ClusterKubeconfigOutput {
	return i.ToClusterKubeconfigOutputWithContext(context.Background())
}

func (i ClusterKubeconfigArgs) ToClusterKubeconfigOutputWithContext(ctx context.Context) ClusterKubeconfigOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClusterKubeconfigOutput)
}

func (i ClusterKubeconfigArgs) ToClusterKubeconfigPtrOutput() ClusterKubeconfigPtrOutput {
	return i.ToClusterKubeconfigPtrOutputWithContext(context.Background())
}

func (i ClusterKubeconfigArgs) ToClusterKubeconfigPtrOutputWithContext(ctx context.Context) ClusterKubeconfigPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClusterKubeconfigOutput).ToClusterKubeconfigPtrOutputWithContext(ctx)
}

// ClusterKubeconfigPtrInput is an input type that accepts ClusterKubeconfigArgs, ClusterKubeconfigPtr and ClusterKubeconfigPtrOutput values.
// You can construct a concrete instance of `ClusterKubeconfigPtrInput` via:
//
//          ClusterKubeconfigArgs{...}
//
//  or:
//
//          nil
type ClusterKubeconfigPtrInput interface {
	pulumi.Input

	ToClusterKubeconfigPtrOutput() ClusterKubeconfigPtrOutput
	ToClusterKubeconfigPtrOutputWithContext(context.Context) ClusterKubeconfigPtrOutput
}

type clusterKubeconfigPtrType ClusterKubeconfigArgs

func ClusterKubeconfigPtr(v *ClusterKubeconfigArgs) ClusterKubeconfigPtrInput {
	return (*clusterKubeconfigPtrType)(v)
}

func (*clusterKubeconfigPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**ClusterKubeconfig)(nil)).Elem()
}

func (i *clusterKubeconfigPtrType) ToClusterKubeconfigPtrOutput() ClusterKubeconfigPtrOutput {
	return i.ToClusterKubeconfigPtrOutputWithContext(context.Background())
}

func (i *clusterKubeconfigPtrType) ToClusterKubeconfigPtrOutputWithContext(ctx context.Context) ClusterKubeconfigPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClusterKubeconfigPtrOutput)
}

type ClusterKubeconfigOutput struct{ *pulumi.OutputState }

func (ClusterKubeconfigOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ClusterKubeconfig)(nil)).Elem()
}

func (o ClusterKubeconfigOutput) ToClusterKubeconfigOutput() ClusterKubeconfigOutput {
	return o
}

func (o ClusterKubeconfigOutput) ToClusterKubeconfigOutputWithContext(ctx context.Context) ClusterKubeconfigOutput {
	return o
}

func (o ClusterKubeconfigOutput) ToClusterKubeconfigPtrOutput() ClusterKubeconfigPtrOutput {
	return o.ToClusterKubeconfigPtrOutputWithContext(context.Background())
}

func (o ClusterKubeconfigOutput) ToClusterKubeconfigPtrOutputWithContext(ctx context.Context) ClusterKubeconfigPtrOutput {
	return o.ApplyT(func(v ClusterKubeconfig) *ClusterKubeconfig {
		return &v
	}).(ClusterKubeconfigPtrOutput)
}
func (o ClusterKubeconfigOutput) ClientCertificate() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ClusterKubeconfig) *string { return v.ClientCertificate }).(pulumi.StringPtrOutput)
}

func (o ClusterKubeconfigOutput) ClientKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ClusterKubeconfig) *string { return v.ClientKey }).(pulumi.StringPtrOutput)
}

func (o ClusterKubeconfigOutput) ClusterCaCertificate() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ClusterKubeconfig) *string { return v.ClusterCaCertificate }).(pulumi.StringPtrOutput)
}

func (o ClusterKubeconfigOutput) Host() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ClusterKubeconfig) *string { return v.Host }).(pulumi.StringPtrOutput)
}

func (o ClusterKubeconfigOutput) RawConfig() pulumi.StringPtrOutput {
	return o.ApplyT(func(v ClusterKubeconfig) *string { return v.RawConfig }).(pulumi.StringPtrOutput)
}

type ClusterKubeconfigPtrOutput struct{ *pulumi.OutputState }

func (ClusterKubeconfigPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ClusterKubeconfig)(nil)).Elem()
}

func (o ClusterKubeconfigPtrOutput) ToClusterKubeconfigPtrOutput() ClusterKubeconfigPtrOutput {
	return o
}

func (o ClusterKubeconfigPtrOutput) ToClusterKubeconfigPtrOutputWithContext(ctx context.Context) ClusterKubeconfigPtrOutput {
	return o
}

func (o ClusterKubeconfigPtrOutput) Elem() ClusterKubeconfigOutput {
	return o.ApplyT(func(v *ClusterKubeconfig) ClusterKubeconfig { return *v }).(ClusterKubeconfigOutput)
}

func (o ClusterKubeconfigPtrOutput) ClientCertificate() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ClusterKubeconfig) *string {
		if v == nil {
			return nil
		}
		return v.ClientCertificate
	}).(pulumi.StringPtrOutput)
}

func (o ClusterKubeconfigPtrOutput) ClientKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ClusterKubeconfig) *string {
		if v == nil {
			return nil
		}
		return v.ClientKey
	}).(pulumi.StringPtrOutput)
}

func (o ClusterKubeconfigPtrOutput) ClusterCaCertificate() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ClusterKubeconfig) *string {
		if v == nil {
			return nil
		}
		return v.ClusterCaCertificate
	}).(pulumi.StringPtrOutput)
}

func (o ClusterKubeconfigPtrOutput) Host() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ClusterKubeconfig) *string {
		if v == nil {
			return nil
		}
		return v.Host
	}).(pulumi.StringPtrOutput)
}

func (o ClusterKubeconfigPtrOutput) RawConfig() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *ClusterKubeconfig) *string {
		if v == nil {
			return nil
		}
		return v.RawConfig
	}).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(ClusterKubeconfigOutput{})
	pulumi.RegisterOutputType(ClusterKubeconfigPtrOutput{})
}
