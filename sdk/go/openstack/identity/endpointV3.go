// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package identity

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a V3 Endpoint resource within OpenStack Keystone.
//
// > **Note:** This usually requires admin privileges.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/identity_endpoint_v3.html.markdown.
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
	if args == nil || args.EndpointRegion == nil {
		return nil, errors.New("missing required argument 'EndpointRegion'")
	}
	if args == nil || args.ServiceId == nil {
		return nil, errors.New("missing required argument 'ServiceId'")
	}
	if args == nil || args.Url == nil {
		return nil, errors.New("missing required argument 'Url'")
	}
	if args == nil {
		args = &EndpointV3Args{}
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

