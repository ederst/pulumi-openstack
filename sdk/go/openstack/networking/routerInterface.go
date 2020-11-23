// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package networking

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a V2 router interface resource within OpenStack.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/networking"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		network1, err := networking.NewNetwork(ctx, "network1", &networking.NetworkArgs{
// 			AdminStateUp: pulumi.Bool(true),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		subnet1, err := networking.NewSubnet(ctx, "subnet1", &networking.SubnetArgs{
// 			Cidr:      pulumi.String("192.168.199.0/24"),
// 			IpVersion: pulumi.Int(4),
// 			NetworkId: network1.ID(),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		router1, err := networking.NewRouter(ctx, "router1", &networking.RouterArgs{
// 			ExternalNetworkId: pulumi.String("f67f0d72-0ddf-11e4-9d95-e1f29f417e2f"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = networking.NewRouterInterface(ctx, "routerInterface1", &networking.RouterInterfaceArgs{
// 			RouterId: router1.ID(),
// 			SubnetId: subnet1.ID(),
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
// Router Interfaces can be imported using the port `id`, e.g. $ openstack port list --router <router name or id>
//
// ```sh
//  $ pulumi import openstack:networking/routerInterface:RouterInterface int_1 <port id from above output>
// ```
type RouterInterface struct {
	pulumi.CustomResourceState

	// ID of the port this interface connects to. Changing
	// this creates a new router interface.
	PortId pulumi.StringOutput `pulumi:"portId"`
	// The region in which to obtain the V2 networking client.
	// A networking client is needed to create a router. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// router interface.
	Region pulumi.StringOutput `pulumi:"region"`
	// ID of the router this interface belongs to. Changing
	// this creates a new router interface.
	RouterId pulumi.StringOutput `pulumi:"routerId"`
	// ID of the subnet this interface connects to. Changing
	// this creates a new router interface.
	SubnetId pulumi.StringOutput `pulumi:"subnetId"`
}

// NewRouterInterface registers a new resource with the given unique name, arguments, and options.
func NewRouterInterface(ctx *pulumi.Context,
	name string, args *RouterInterfaceArgs, opts ...pulumi.ResourceOption) (*RouterInterface, error) {
	if args == nil || args.RouterId == nil {
		return nil, errors.New("missing required argument 'RouterId'")
	}
	if args == nil {
		args = &RouterInterfaceArgs{}
	}
	var resource RouterInterface
	err := ctx.RegisterResource("openstack:networking/routerInterface:RouterInterface", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRouterInterface gets an existing RouterInterface resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRouterInterface(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RouterInterfaceState, opts ...pulumi.ResourceOption) (*RouterInterface, error) {
	var resource RouterInterface
	err := ctx.ReadResource("openstack:networking/routerInterface:RouterInterface", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering RouterInterface resources.
type routerInterfaceState struct {
	// ID of the port this interface connects to. Changing
	// this creates a new router interface.
	PortId *string `pulumi:"portId"`
	// The region in which to obtain the V2 networking client.
	// A networking client is needed to create a router. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// router interface.
	Region *string `pulumi:"region"`
	// ID of the router this interface belongs to. Changing
	// this creates a new router interface.
	RouterId *string `pulumi:"routerId"`
	// ID of the subnet this interface connects to. Changing
	// this creates a new router interface.
	SubnetId *string `pulumi:"subnetId"`
}

type RouterInterfaceState struct {
	// ID of the port this interface connects to. Changing
	// this creates a new router interface.
	PortId pulumi.StringPtrInput
	// The region in which to obtain the V2 networking client.
	// A networking client is needed to create a router. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// router interface.
	Region pulumi.StringPtrInput
	// ID of the router this interface belongs to. Changing
	// this creates a new router interface.
	RouterId pulumi.StringPtrInput
	// ID of the subnet this interface connects to. Changing
	// this creates a new router interface.
	SubnetId pulumi.StringPtrInput
}

func (RouterInterfaceState) ElementType() reflect.Type {
	return reflect.TypeOf((*routerInterfaceState)(nil)).Elem()
}

type routerInterfaceArgs struct {
	// ID of the port this interface connects to. Changing
	// this creates a new router interface.
	PortId *string `pulumi:"portId"`
	// The region in which to obtain the V2 networking client.
	// A networking client is needed to create a router. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// router interface.
	Region *string `pulumi:"region"`
	// ID of the router this interface belongs to. Changing
	// this creates a new router interface.
	RouterId string `pulumi:"routerId"`
	// ID of the subnet this interface connects to. Changing
	// this creates a new router interface.
	SubnetId *string `pulumi:"subnetId"`
}

// The set of arguments for constructing a RouterInterface resource.
type RouterInterfaceArgs struct {
	// ID of the port this interface connects to. Changing
	// this creates a new router interface.
	PortId pulumi.StringPtrInput
	// The region in which to obtain the V2 networking client.
	// A networking client is needed to create a router. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// router interface.
	Region pulumi.StringPtrInput
	// ID of the router this interface belongs to. Changing
	// this creates a new router interface.
	RouterId pulumi.StringInput
	// ID of the subnet this interface connects to. Changing
	// this creates a new router interface.
	SubnetId pulumi.StringPtrInput
}

func (RouterInterfaceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*routerInterfaceArgs)(nil)).Elem()
}

type RouterInterfaceInput interface {
	pulumi.Input

	ToRouterInterfaceOutput() RouterInterfaceOutput
	ToRouterInterfaceOutputWithContext(ctx context.Context) RouterInterfaceOutput
}

func (RouterInterface) ElementType() reflect.Type {
	return reflect.TypeOf((*RouterInterface)(nil)).Elem()
}

func (i RouterInterface) ToRouterInterfaceOutput() RouterInterfaceOutput {
	return i.ToRouterInterfaceOutputWithContext(context.Background())
}

func (i RouterInterface) ToRouterInterfaceOutputWithContext(ctx context.Context) RouterInterfaceOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RouterInterfaceOutput)
}

type RouterInterfaceOutput struct {
	*pulumi.OutputState
}

func (RouterInterfaceOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*RouterInterfaceOutput)(nil)).Elem()
}

func (o RouterInterfaceOutput) ToRouterInterfaceOutput() RouterInterfaceOutput {
	return o
}

func (o RouterInterfaceOutput) ToRouterInterfaceOutputWithContext(ctx context.Context) RouterInterfaceOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(RouterInterfaceOutput{})
}
