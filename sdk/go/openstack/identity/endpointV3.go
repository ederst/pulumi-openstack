// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package identity

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a V3 Endpoint resource within OpenStack Keystone.
//
// > **Note:** This usually requires admin privileges.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/identity"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		service1, err := identity.NewServiceV3(ctx, "service1", &identity.ServiceV3Args{
// 			Type: pulumi.String("my-service-type"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = identity.NewEndpointV3(ctx, "endpoint1", &identity.EndpointV3Args{
// 			EndpointRegion: service1.Region,
// 			ServiceId:      service1.ID(),
// 			Url:            pulumi.String("http://my-endpoint"),
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
// Endpoints can be imported using the `id`, e.g.
//
// ```sh
//  $ pulumi import openstack:identity/endpointV3:EndpointV3 endpoint_1 5392472b-106a-4845-90c6-7c8445f18770
// ```
type EndpointV3 struct {
	pulumi.CustomResourceState

	// The endpoint region. The `region` and
	// `endpointRegion` can be different.
	EndpointRegion pulumi.StringOutput `pulumi:"endpointRegion"`
	// The endpoint interface. Valid values are `public`,
	// `internal` and `admin`. Default value is `public`
	Interface pulumi.StringPtrOutput `pulumi:"interface"`
	// The endpoint name.
	Name pulumi.StringOutput `pulumi:"name"`
	// The region in which to obtain the V3 Keystone client.
	// If omitted, the `region` argument of the provider is used.
	Region pulumi.StringOutput `pulumi:"region"`
	// The endpoint service ID.
	ServiceId pulumi.StringOutput `pulumi:"serviceId"`
	// The service name of the endpoint.
	ServiceName pulumi.StringOutput `pulumi:"serviceName"`
	// The service type of the endpoint.
	ServiceType pulumi.StringOutput `pulumi:"serviceType"`
	// The endpoint url.
	Url pulumi.StringOutput `pulumi:"url"`
}

// NewEndpointV3 registers a new resource with the given unique name, arguments, and options.
func NewEndpointV3(ctx *pulumi.Context,
	name string, args *EndpointV3Args, opts ...pulumi.ResourceOption) (*EndpointV3, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.EndpointRegion == nil {
		return nil, errors.New("invalid value for required argument 'EndpointRegion'")
	}
	if args.ServiceId == nil {
		return nil, errors.New("invalid value for required argument 'ServiceId'")
	}
	if args.Url == nil {
		return nil, errors.New("invalid value for required argument 'Url'")
	}
	var resource EndpointV3
	err := ctx.RegisterResource("openstack:identity/endpointV3:EndpointV3", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEndpointV3 gets an existing EndpointV3 resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEndpointV3(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EndpointV3State, opts ...pulumi.ResourceOption) (*EndpointV3, error) {
	var resource EndpointV3
	err := ctx.ReadResource("openstack:identity/endpointV3:EndpointV3", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering EndpointV3 resources.
type endpointV3State struct {
	// The endpoint region. The `region` and
	// `endpointRegion` can be different.
	EndpointRegion *string `pulumi:"endpointRegion"`
	// The endpoint interface. Valid values are `public`,
	// `internal` and `admin`. Default value is `public`
	Interface *string `pulumi:"interface"`
	// The endpoint name.
	Name *string `pulumi:"name"`
	// The region in which to obtain the V3 Keystone client.
	// If omitted, the `region` argument of the provider is used.
	Region *string `pulumi:"region"`
	// The endpoint service ID.
	ServiceId *string `pulumi:"serviceId"`
	// The service name of the endpoint.
	ServiceName *string `pulumi:"serviceName"`
	// The service type of the endpoint.
	ServiceType *string `pulumi:"serviceType"`
	// The endpoint url.
	Url *string `pulumi:"url"`
}

type EndpointV3State struct {
	// The endpoint region. The `region` and
	// `endpointRegion` can be different.
	EndpointRegion pulumi.StringPtrInput
	// The endpoint interface. Valid values are `public`,
	// `internal` and `admin`. Default value is `public`
	Interface pulumi.StringPtrInput
	// The endpoint name.
	Name pulumi.StringPtrInput
	// The region in which to obtain the V3 Keystone client.
	// If omitted, the `region` argument of the provider is used.
	Region pulumi.StringPtrInput
	// The endpoint service ID.
	ServiceId pulumi.StringPtrInput
	// The service name of the endpoint.
	ServiceName pulumi.StringPtrInput
	// The service type of the endpoint.
	ServiceType pulumi.StringPtrInput
	// The endpoint url.
	Url pulumi.StringPtrInput
}

func (EndpointV3State) ElementType() reflect.Type {
	return reflect.TypeOf((*endpointV3State)(nil)).Elem()
}

type endpointV3Args struct {
	// The endpoint region. The `region` and
	// `endpointRegion` can be different.
	EndpointRegion string `pulumi:"endpointRegion"`
	// The endpoint interface. Valid values are `public`,
	// `internal` and `admin`. Default value is `public`
	Interface *string `pulumi:"interface"`
	// The endpoint name.
	Name *string `pulumi:"name"`
	// The region in which to obtain the V3 Keystone client.
	// If omitted, the `region` argument of the provider is used.
	Region *string `pulumi:"region"`
	// The endpoint service ID.
	ServiceId string `pulumi:"serviceId"`
	// The endpoint url.
	Url string `pulumi:"url"`
}

// The set of arguments for constructing a EndpointV3 resource.
type EndpointV3Args struct {
	// The endpoint region. The `region` and
	// `endpointRegion` can be different.
	EndpointRegion pulumi.StringInput
	// The endpoint interface. Valid values are `public`,
	// `internal` and `admin`. Default value is `public`
	Interface pulumi.StringPtrInput
	// The endpoint name.
	Name pulumi.StringPtrInput
	// The region in which to obtain the V3 Keystone client.
	// If omitted, the `region` argument of the provider is used.
	Region pulumi.StringPtrInput
	// The endpoint service ID.
	ServiceId pulumi.StringInput
	// The endpoint url.
	Url pulumi.StringInput
}

func (EndpointV3Args) ElementType() reflect.Type {
	return reflect.TypeOf((*endpointV3Args)(nil)).Elem()
}

type EndpointV3Input interface {
	pulumi.Input

	ToEndpointV3Output() EndpointV3Output
	ToEndpointV3OutputWithContext(ctx context.Context) EndpointV3Output
}

func (*EndpointV3) ElementType() reflect.Type {
	return reflect.TypeOf((*EndpointV3)(nil))
}

func (i *EndpointV3) ToEndpointV3Output() EndpointV3Output {
	return i.ToEndpointV3OutputWithContext(context.Background())
}

func (i *EndpointV3) ToEndpointV3OutputWithContext(ctx context.Context) EndpointV3Output {
	return pulumi.ToOutputWithContext(ctx, i).(EndpointV3Output)
}

func (i *EndpointV3) ToEndpointV3PtrOutput() EndpointV3PtrOutput {
	return i.ToEndpointV3PtrOutputWithContext(context.Background())
}

func (i *EndpointV3) ToEndpointV3PtrOutputWithContext(ctx context.Context) EndpointV3PtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EndpointV3PtrOutput)
}

type EndpointV3PtrInput interface {
	pulumi.Input

	ToEndpointV3PtrOutput() EndpointV3PtrOutput
	ToEndpointV3PtrOutputWithContext(ctx context.Context) EndpointV3PtrOutput
}

type endpointV3PtrType EndpointV3Args

func (*endpointV3PtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**EndpointV3)(nil))
}

func (i *endpointV3PtrType) ToEndpointV3PtrOutput() EndpointV3PtrOutput {
	return i.ToEndpointV3PtrOutputWithContext(context.Background())
}

func (i *endpointV3PtrType) ToEndpointV3PtrOutputWithContext(ctx context.Context) EndpointV3PtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EndpointV3PtrOutput)
}

// EndpointV3ArrayInput is an input type that accepts EndpointV3Array and EndpointV3ArrayOutput values.
// You can construct a concrete instance of `EndpointV3ArrayInput` via:
//
//          EndpointV3Array{ EndpointV3Args{...} }
type EndpointV3ArrayInput interface {
	pulumi.Input

	ToEndpointV3ArrayOutput() EndpointV3ArrayOutput
	ToEndpointV3ArrayOutputWithContext(context.Context) EndpointV3ArrayOutput
}

type EndpointV3Array []EndpointV3Input

func (EndpointV3Array) ElementType() reflect.Type {
	return reflect.TypeOf(([]*EndpointV3)(nil))
}

func (i EndpointV3Array) ToEndpointV3ArrayOutput() EndpointV3ArrayOutput {
	return i.ToEndpointV3ArrayOutputWithContext(context.Background())
}

func (i EndpointV3Array) ToEndpointV3ArrayOutputWithContext(ctx context.Context) EndpointV3ArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EndpointV3ArrayOutput)
}

// EndpointV3MapInput is an input type that accepts EndpointV3Map and EndpointV3MapOutput values.
// You can construct a concrete instance of `EndpointV3MapInput` via:
//
//          EndpointV3Map{ "key": EndpointV3Args{...} }
type EndpointV3MapInput interface {
	pulumi.Input

	ToEndpointV3MapOutput() EndpointV3MapOutput
	ToEndpointV3MapOutputWithContext(context.Context) EndpointV3MapOutput
}

type EndpointV3Map map[string]EndpointV3Input

func (EndpointV3Map) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*EndpointV3)(nil))
}

func (i EndpointV3Map) ToEndpointV3MapOutput() EndpointV3MapOutput {
	return i.ToEndpointV3MapOutputWithContext(context.Background())
}

func (i EndpointV3Map) ToEndpointV3MapOutputWithContext(ctx context.Context) EndpointV3MapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EndpointV3MapOutput)
}

type EndpointV3Output struct {
	*pulumi.OutputState
}

func (EndpointV3Output) ElementType() reflect.Type {
	return reflect.TypeOf((*EndpointV3)(nil))
}

func (o EndpointV3Output) ToEndpointV3Output() EndpointV3Output {
	return o
}

func (o EndpointV3Output) ToEndpointV3OutputWithContext(ctx context.Context) EndpointV3Output {
	return o
}

func (o EndpointV3Output) ToEndpointV3PtrOutput() EndpointV3PtrOutput {
	return o.ToEndpointV3PtrOutputWithContext(context.Background())
}

func (o EndpointV3Output) ToEndpointV3PtrOutputWithContext(ctx context.Context) EndpointV3PtrOutput {
	return o.ApplyT(func(v EndpointV3) *EndpointV3 {
		return &v
	}).(EndpointV3PtrOutput)
}

type EndpointV3PtrOutput struct {
	*pulumi.OutputState
}

func (EndpointV3PtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**EndpointV3)(nil))
}

func (o EndpointV3PtrOutput) ToEndpointV3PtrOutput() EndpointV3PtrOutput {
	return o
}

func (o EndpointV3PtrOutput) ToEndpointV3PtrOutputWithContext(ctx context.Context) EndpointV3PtrOutput {
	return o
}

type EndpointV3ArrayOutput struct{ *pulumi.OutputState }

func (EndpointV3ArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]EndpointV3)(nil))
}

func (o EndpointV3ArrayOutput) ToEndpointV3ArrayOutput() EndpointV3ArrayOutput {
	return o
}

func (o EndpointV3ArrayOutput) ToEndpointV3ArrayOutputWithContext(ctx context.Context) EndpointV3ArrayOutput {
	return o
}

func (o EndpointV3ArrayOutput) Index(i pulumi.IntInput) EndpointV3Output {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) EndpointV3 {
		return vs[0].([]EndpointV3)[vs[1].(int)]
	}).(EndpointV3Output)
}

type EndpointV3MapOutput struct{ *pulumi.OutputState }

func (EndpointV3MapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]EndpointV3)(nil))
}

func (o EndpointV3MapOutput) ToEndpointV3MapOutput() EndpointV3MapOutput {
	return o
}

func (o EndpointV3MapOutput) ToEndpointV3MapOutputWithContext(ctx context.Context) EndpointV3MapOutput {
	return o
}

func (o EndpointV3MapOutput) MapIndex(k pulumi.StringInput) EndpointV3Output {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) EndpointV3 {
		return vs[0].(map[string]EndpointV3)[vs[1].(string)]
	}).(EndpointV3Output)
}

func init() {
	pulumi.RegisterOutputType(EndpointV3Output{})
	pulumi.RegisterOutputType(EndpointV3PtrOutput{})
	pulumi.RegisterOutputType(EndpointV3ArrayOutput{})
	pulumi.RegisterOutputType(EndpointV3MapOutput{})
}
