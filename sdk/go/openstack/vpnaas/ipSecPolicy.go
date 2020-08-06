// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package vpnaas

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a V2 Neutron IPSec policy resource within OpenStack.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/vpnaas"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := vpnaas.NewIpSecPolicy(ctx, "policy1", nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type IpSecPolicy struct {
	pulumi.CustomResourceState

	// The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
	// Default is sha1. Changing this updates the algorithm of the existing policy.
	AuthAlgorithm pulumi.StringOutput `pulumi:"authAlgorithm"`
	// The human-readable description for the policy.
	// Changing this updates the description of the existing policy.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The encapsulation mode. Valid values are tunnel and transport. Default is tunnel.
	// Changing this updates the existing policy.
	EncapsulationMode pulumi.StringOutput `pulumi:"encapsulationMode"`
	// The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
	// The default value is aes-128. Changing this updates the existing policy.
	EncryptionAlgorithm pulumi.StringOutput `pulumi:"encryptionAlgorithm"`
	// The lifetime of the security association. Consists of Unit and Value.
	Lifetimes IpSecPolicyLifetimeArrayOutput `pulumi:"lifetimes"`
	// The name of the policy. Changing this updates the name of
	// the existing policy.
	Name pulumi.StringOutput `pulumi:"name"`
	// The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
	// Changing this updates the existing policy.
	Pfs pulumi.StringOutput `pulumi:"pfs"`
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an IPSec policy. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// policy.
	Region pulumi.StringOutput `pulumi:"region"`
	// The owner of the policy. Required if admin wants to
	// create a policy for another project. Changing this creates a new policy.
	TenantId pulumi.StringOutput `pulumi:"tenantId"`
	// The transform protocol. Valid values are ESP, AH and AH-ESP.
	// Changing this updates the existing policy. Default is ESP.
	TransformProtocol pulumi.StringOutput `pulumi:"transformProtocol"`
	// Map of additional options.
	ValueSpecs pulumi.MapOutput `pulumi:"valueSpecs"`
}

// NewIpSecPolicy registers a new resource with the given unique name, arguments, and options.
func NewIpSecPolicy(ctx *pulumi.Context,
	name string, args *IpSecPolicyArgs, opts ...pulumi.ResourceOption) (*IpSecPolicy, error) {
	if args == nil {
		args = &IpSecPolicyArgs{}
	}
	var resource IpSecPolicy
	err := ctx.RegisterResource("openstack:vpnaas/ipSecPolicy:IpSecPolicy", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetIpSecPolicy gets an existing IpSecPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetIpSecPolicy(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *IpSecPolicyState, opts ...pulumi.ResourceOption) (*IpSecPolicy, error) {
	var resource IpSecPolicy
	err := ctx.ReadResource("openstack:vpnaas/ipSecPolicy:IpSecPolicy", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering IpSecPolicy resources.
type ipSecPolicyState struct {
	// The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
	// Default is sha1. Changing this updates the algorithm of the existing policy.
	AuthAlgorithm *string `pulumi:"authAlgorithm"`
	// The human-readable description for the policy.
	// Changing this updates the description of the existing policy.
	Description *string `pulumi:"description"`
	// The encapsulation mode. Valid values are tunnel and transport. Default is tunnel.
	// Changing this updates the existing policy.
	EncapsulationMode *string `pulumi:"encapsulationMode"`
	// The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
	// The default value is aes-128. Changing this updates the existing policy.
	EncryptionAlgorithm *string `pulumi:"encryptionAlgorithm"`
	// The lifetime of the security association. Consists of Unit and Value.
	Lifetimes []IpSecPolicyLifetime `pulumi:"lifetimes"`
	// The name of the policy. Changing this updates the name of
	// the existing policy.
	Name *string `pulumi:"name"`
	// The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
	// Changing this updates the existing policy.
	Pfs *string `pulumi:"pfs"`
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an IPSec policy. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// policy.
	Region *string `pulumi:"region"`
	// The owner of the policy. Required if admin wants to
	// create a policy for another project. Changing this creates a new policy.
	TenantId *string `pulumi:"tenantId"`
	// The transform protocol. Valid values are ESP, AH and AH-ESP.
	// Changing this updates the existing policy. Default is ESP.
	TransformProtocol *string `pulumi:"transformProtocol"`
	// Map of additional options.
	ValueSpecs map[string]interface{} `pulumi:"valueSpecs"`
}

type IpSecPolicyState struct {
	// The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
	// Default is sha1. Changing this updates the algorithm of the existing policy.
	AuthAlgorithm pulumi.StringPtrInput
	// The human-readable description for the policy.
	// Changing this updates the description of the existing policy.
	Description pulumi.StringPtrInput
	// The encapsulation mode. Valid values are tunnel and transport. Default is tunnel.
	// Changing this updates the existing policy.
	EncapsulationMode pulumi.StringPtrInput
	// The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
	// The default value is aes-128. Changing this updates the existing policy.
	EncryptionAlgorithm pulumi.StringPtrInput
	// The lifetime of the security association. Consists of Unit and Value.
	Lifetimes IpSecPolicyLifetimeArrayInput
	// The name of the policy. Changing this updates the name of
	// the existing policy.
	Name pulumi.StringPtrInput
	// The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
	// Changing this updates the existing policy.
	Pfs pulumi.StringPtrInput
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an IPSec policy. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// policy.
	Region pulumi.StringPtrInput
	// The owner of the policy. Required if admin wants to
	// create a policy for another project. Changing this creates a new policy.
	TenantId pulumi.StringPtrInput
	// The transform protocol. Valid values are ESP, AH and AH-ESP.
	// Changing this updates the existing policy. Default is ESP.
	TransformProtocol pulumi.StringPtrInput
	// Map of additional options.
	ValueSpecs pulumi.MapInput
}

func (IpSecPolicyState) ElementType() reflect.Type {
	return reflect.TypeOf((*ipSecPolicyState)(nil)).Elem()
}

type ipSecPolicyArgs struct {
	// The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
	// Default is sha1. Changing this updates the algorithm of the existing policy.
	AuthAlgorithm *string `pulumi:"authAlgorithm"`
	// The human-readable description for the policy.
	// Changing this updates the description of the existing policy.
	Description *string `pulumi:"description"`
	// The encapsulation mode. Valid values are tunnel and transport. Default is tunnel.
	// Changing this updates the existing policy.
	EncapsulationMode *string `pulumi:"encapsulationMode"`
	// The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
	// The default value is aes-128. Changing this updates the existing policy.
	EncryptionAlgorithm *string `pulumi:"encryptionAlgorithm"`
	// The lifetime of the security association. Consists of Unit and Value.
	Lifetimes []IpSecPolicyLifetime `pulumi:"lifetimes"`
	// The name of the policy. Changing this updates the name of
	// the existing policy.
	Name *string `pulumi:"name"`
	// The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
	// Changing this updates the existing policy.
	Pfs *string `pulumi:"pfs"`
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an IPSec policy. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// policy.
	Region *string `pulumi:"region"`
	// The owner of the policy. Required if admin wants to
	// create a policy for another project. Changing this creates a new policy.
	TenantId *string `pulumi:"tenantId"`
	// The transform protocol. Valid values are ESP, AH and AH-ESP.
	// Changing this updates the existing policy. Default is ESP.
	TransformProtocol *string `pulumi:"transformProtocol"`
	// Map of additional options.
	ValueSpecs map[string]interface{} `pulumi:"valueSpecs"`
}

// The set of arguments for constructing a IpSecPolicy resource.
type IpSecPolicyArgs struct {
	// The authentication hash algorithm. Valid values are sha1, sha256, sha384, sha512.
	// Default is sha1. Changing this updates the algorithm of the existing policy.
	AuthAlgorithm pulumi.StringPtrInput
	// The human-readable description for the policy.
	// Changing this updates the description of the existing policy.
	Description pulumi.StringPtrInput
	// The encapsulation mode. Valid values are tunnel and transport. Default is tunnel.
	// Changing this updates the existing policy.
	EncapsulationMode pulumi.StringPtrInput
	// The encryption algorithm. Valid values are 3des, aes-128, aes-192 and so on.
	// The default value is aes-128. Changing this updates the existing policy.
	EncryptionAlgorithm pulumi.StringPtrInput
	// The lifetime of the security association. Consists of Unit and Value.
	Lifetimes IpSecPolicyLifetimeArrayInput
	// The name of the policy. Changing this updates the name of
	// the existing policy.
	Name pulumi.StringPtrInput
	// The perfect forward secrecy mode. Valid values are Group2, Group5 and Group14. Default is Group5.
	// Changing this updates the existing policy.
	Pfs pulumi.StringPtrInput
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an IPSec policy. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// policy.
	Region pulumi.StringPtrInput
	// The owner of the policy. Required if admin wants to
	// create a policy for another project. Changing this creates a new policy.
	TenantId pulumi.StringPtrInput
	// The transform protocol. Valid values are ESP, AH and AH-ESP.
	// Changing this updates the existing policy. Default is ESP.
	TransformProtocol pulumi.StringPtrInput
	// Map of additional options.
	ValueSpecs pulumi.MapInput
}

func (IpSecPolicyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ipSecPolicyArgs)(nil)).Elem()
}
