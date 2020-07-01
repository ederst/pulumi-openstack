// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package loadbalancer

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a V1 load balancer monitor resource within OpenStack.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/loadbalancer"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := loadbalancer.NewMonitorV1(ctx, "monitor1", &loadbalancer.MonitorV1Args{
// 			AdminStateUp: pulumi.String("true"),
// 			Delay:        pulumi.Int(30),
// 			MaxRetries:   pulumi.Int(3),
// 			Timeout:      pulumi.Int(5),
// 			Type:         pulumi.String("PING"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type MonitorV1 struct {
	pulumi.CustomResourceState

	// The administrative state of the monitor.
	// Acceptable values are "true" and "false". Changing this value updates the
	// state of the existing monitor.
	AdminStateUp pulumi.StringOutput `pulumi:"adminStateUp"`
	// The time, in seconds, between sending probes to members.
	// Changing this creates a new monitor.
	Delay pulumi.IntOutput `pulumi:"delay"`
	// Required for HTTP(S) types. Expected HTTP codes
	// for a passing HTTP(S) monitor. You can either specify a single status like
	// "200", or a range like "200-202". Changing this updates the expectedCodes
	// of the existing monitor.
	ExpectedCodes pulumi.StringPtrOutput `pulumi:"expectedCodes"`
	// Required for HTTP(S) types. The HTTP method used
	// for requests by the monitor. If this attribute is not specified, it defaults
	// to "GET". Changing this updates the httpMethod of the existing monitor.
	HttpMethod pulumi.StringPtrOutput `pulumi:"httpMethod"`
	// Number of permissible ping failures before changing
	// the member's status to INACTIVE. Must be a number between 1 and 10. Changing
	// this updates the maxRetries of the existing monitor.
	MaxRetries pulumi.IntOutput `pulumi:"maxRetries"`
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an LB monitor. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// LB monitor.
	Region pulumi.StringOutput `pulumi:"region"`
	// The owner of the monitor. Required if admin wants to
	// create a monitor for another tenant. Changing this creates a new monitor.
	TenantId pulumi.StringOutput `pulumi:"tenantId"`
	// Maximum number of seconds for a monitor to wait for a
	// ping reply before it times out. The value must be less than the delay value.
	// Changing this updates the timeout of the existing monitor.
	Timeout pulumi.IntOutput `pulumi:"timeout"`
	// The type of probe, which is PING, TCP, HTTP, or HTTPS,
	// that is sent by the monitor to verify the member state. Changing this
	// creates a new monitor.
	Type pulumi.StringOutput `pulumi:"type"`
	// Required for HTTP(S) types. URI path that will be
	// accessed if monitor type is HTTP or HTTPS. Changing this updates the
	// urlPath of the existing monitor.
	UrlPath pulumi.StringPtrOutput `pulumi:"urlPath"`
}

// NewMonitorV1 registers a new resource with the given unique name, arguments, and options.
func NewMonitorV1(ctx *pulumi.Context,
	name string, args *MonitorV1Args, opts ...pulumi.ResourceOption) (*MonitorV1, error) {
	if args == nil || args.Delay == nil {
		return nil, errors.New("missing required argument 'Delay'")
	}
	if args == nil || args.MaxRetries == nil {
		return nil, errors.New("missing required argument 'MaxRetries'")
	}
	if args == nil || args.Timeout == nil {
		return nil, errors.New("missing required argument 'Timeout'")
	}
	if args == nil || args.Type == nil {
		return nil, errors.New("missing required argument 'Type'")
	}
	if args == nil {
		args = &MonitorV1Args{}
	}
	var resource MonitorV1
	err := ctx.RegisterResource("openstack:loadbalancer/monitorV1:MonitorV1", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetMonitorV1 gets an existing MonitorV1 resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetMonitorV1(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *MonitorV1State, opts ...pulumi.ResourceOption) (*MonitorV1, error) {
	var resource MonitorV1
	err := ctx.ReadResource("openstack:loadbalancer/monitorV1:MonitorV1", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering MonitorV1 resources.
type monitorV1State struct {
	// The administrative state of the monitor.
	// Acceptable values are "true" and "false". Changing this value updates the
	// state of the existing monitor.
	AdminStateUp *string `pulumi:"adminStateUp"`
	// The time, in seconds, between sending probes to members.
	// Changing this creates a new monitor.
	Delay *int `pulumi:"delay"`
	// Required for HTTP(S) types. Expected HTTP codes
	// for a passing HTTP(S) monitor. You can either specify a single status like
	// "200", or a range like "200-202". Changing this updates the expectedCodes
	// of the existing monitor.
	ExpectedCodes *string `pulumi:"expectedCodes"`
	// Required for HTTP(S) types. The HTTP method used
	// for requests by the monitor. If this attribute is not specified, it defaults
	// to "GET". Changing this updates the httpMethod of the existing monitor.
	HttpMethod *string `pulumi:"httpMethod"`
	// Number of permissible ping failures before changing
	// the member's status to INACTIVE. Must be a number between 1 and 10. Changing
	// this updates the maxRetries of the existing monitor.
	MaxRetries *int `pulumi:"maxRetries"`
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an LB monitor. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// LB monitor.
	Region *string `pulumi:"region"`
	// The owner of the monitor. Required if admin wants to
	// create a monitor for another tenant. Changing this creates a new monitor.
	TenantId *string `pulumi:"tenantId"`
	// Maximum number of seconds for a monitor to wait for a
	// ping reply before it times out. The value must be less than the delay value.
	// Changing this updates the timeout of the existing monitor.
	Timeout *int `pulumi:"timeout"`
	// The type of probe, which is PING, TCP, HTTP, or HTTPS,
	// that is sent by the monitor to verify the member state. Changing this
	// creates a new monitor.
	Type *string `pulumi:"type"`
	// Required for HTTP(S) types. URI path that will be
	// accessed if monitor type is HTTP or HTTPS. Changing this updates the
	// urlPath of the existing monitor.
	UrlPath *string `pulumi:"urlPath"`
}

type MonitorV1State struct {
	// The administrative state of the monitor.
	// Acceptable values are "true" and "false". Changing this value updates the
	// state of the existing monitor.
	AdminStateUp pulumi.StringPtrInput
	// The time, in seconds, between sending probes to members.
	// Changing this creates a new monitor.
	Delay pulumi.IntPtrInput
	// Required for HTTP(S) types. Expected HTTP codes
	// for a passing HTTP(S) monitor. You can either specify a single status like
	// "200", or a range like "200-202". Changing this updates the expectedCodes
	// of the existing monitor.
	ExpectedCodes pulumi.StringPtrInput
	// Required for HTTP(S) types. The HTTP method used
	// for requests by the monitor. If this attribute is not specified, it defaults
	// to "GET". Changing this updates the httpMethod of the existing monitor.
	HttpMethod pulumi.StringPtrInput
	// Number of permissible ping failures before changing
	// the member's status to INACTIVE. Must be a number between 1 and 10. Changing
	// this updates the maxRetries of the existing monitor.
	MaxRetries pulumi.IntPtrInput
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an LB monitor. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// LB monitor.
	Region pulumi.StringPtrInput
	// The owner of the monitor. Required if admin wants to
	// create a monitor for another tenant. Changing this creates a new monitor.
	TenantId pulumi.StringPtrInput
	// Maximum number of seconds for a monitor to wait for a
	// ping reply before it times out. The value must be less than the delay value.
	// Changing this updates the timeout of the existing monitor.
	Timeout pulumi.IntPtrInput
	// The type of probe, which is PING, TCP, HTTP, or HTTPS,
	// that is sent by the monitor to verify the member state. Changing this
	// creates a new monitor.
	Type pulumi.StringPtrInput
	// Required for HTTP(S) types. URI path that will be
	// accessed if monitor type is HTTP or HTTPS. Changing this updates the
	// urlPath of the existing monitor.
	UrlPath pulumi.StringPtrInput
}

func (MonitorV1State) ElementType() reflect.Type {
	return reflect.TypeOf((*monitorV1State)(nil)).Elem()
}

type monitorV1Args struct {
	// The administrative state of the monitor.
	// Acceptable values are "true" and "false". Changing this value updates the
	// state of the existing monitor.
	AdminStateUp *string `pulumi:"adminStateUp"`
	// The time, in seconds, between sending probes to members.
	// Changing this creates a new monitor.
	Delay int `pulumi:"delay"`
	// Required for HTTP(S) types. Expected HTTP codes
	// for a passing HTTP(S) monitor. You can either specify a single status like
	// "200", or a range like "200-202". Changing this updates the expectedCodes
	// of the existing monitor.
	ExpectedCodes *string `pulumi:"expectedCodes"`
	// Required for HTTP(S) types. The HTTP method used
	// for requests by the monitor. If this attribute is not specified, it defaults
	// to "GET". Changing this updates the httpMethod of the existing monitor.
	HttpMethod *string `pulumi:"httpMethod"`
	// Number of permissible ping failures before changing
	// the member's status to INACTIVE. Must be a number between 1 and 10. Changing
	// this updates the maxRetries of the existing monitor.
	MaxRetries int `pulumi:"maxRetries"`
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an LB monitor. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// LB monitor.
	Region *string `pulumi:"region"`
	// The owner of the monitor. Required if admin wants to
	// create a monitor for another tenant. Changing this creates a new monitor.
	TenantId *string `pulumi:"tenantId"`
	// Maximum number of seconds for a monitor to wait for a
	// ping reply before it times out. The value must be less than the delay value.
	// Changing this updates the timeout of the existing monitor.
	Timeout int `pulumi:"timeout"`
	// The type of probe, which is PING, TCP, HTTP, or HTTPS,
	// that is sent by the monitor to verify the member state. Changing this
	// creates a new monitor.
	Type string `pulumi:"type"`
	// Required for HTTP(S) types. URI path that will be
	// accessed if monitor type is HTTP or HTTPS. Changing this updates the
	// urlPath of the existing monitor.
	UrlPath *string `pulumi:"urlPath"`
}

// The set of arguments for constructing a MonitorV1 resource.
type MonitorV1Args struct {
	// The administrative state of the monitor.
	// Acceptable values are "true" and "false". Changing this value updates the
	// state of the existing monitor.
	AdminStateUp pulumi.StringPtrInput
	// The time, in seconds, between sending probes to members.
	// Changing this creates a new monitor.
	Delay pulumi.IntInput
	// Required for HTTP(S) types. Expected HTTP codes
	// for a passing HTTP(S) monitor. You can either specify a single status like
	// "200", or a range like "200-202". Changing this updates the expectedCodes
	// of the existing monitor.
	ExpectedCodes pulumi.StringPtrInput
	// Required for HTTP(S) types. The HTTP method used
	// for requests by the monitor. If this attribute is not specified, it defaults
	// to "GET". Changing this updates the httpMethod of the existing monitor.
	HttpMethod pulumi.StringPtrInput
	// Number of permissible ping failures before changing
	// the member's status to INACTIVE. Must be a number between 1 and 10. Changing
	// this updates the maxRetries of the existing monitor.
	MaxRetries pulumi.IntInput
	// The region in which to obtain the V2 Networking client.
	// A Networking client is needed to create an LB monitor. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// LB monitor.
	Region pulumi.StringPtrInput
	// The owner of the monitor. Required if admin wants to
	// create a monitor for another tenant. Changing this creates a new monitor.
	TenantId pulumi.StringPtrInput
	// Maximum number of seconds for a monitor to wait for a
	// ping reply before it times out. The value must be less than the delay value.
	// Changing this updates the timeout of the existing monitor.
	Timeout pulumi.IntInput
	// The type of probe, which is PING, TCP, HTTP, or HTTPS,
	// that is sent by the monitor to verify the member state. Changing this
	// creates a new monitor.
	Type pulumi.StringInput
	// Required for HTTP(S) types. URI path that will be
	// accessed if monitor type is HTTP or HTTPS. Changing this updates the
	// urlPath of the existing monitor.
	UrlPath pulumi.StringPtrInput
}

func (MonitorV1Args) ElementType() reflect.Type {
	return reflect.TypeOf((*monitorV1Args)(nil)).Elem()
}
