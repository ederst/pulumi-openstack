// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package dns

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Manages a DNS zone in the OpenStack DNS Service.
//
// ## Example Usage
// ### Automatically detect the correct network
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/dns"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := dns.NewZone(ctx, "example_com", &dns.ZoneArgs{
// 			Description: pulumi.String("An example zone"),
// 			Email:       pulumi.String("jdoe@example.com"),
// 			Ttl:         pulumi.Int(3000),
// 			Type:        pulumi.String("PRIMARY"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Zone struct {
	pulumi.CustomResourceState

	// Attributes for the DNS Service scheduler.
	// Changing this creates a new zone.
	Attributes pulumi.MapOutput `pulumi:"attributes"`
	// A description of the zone.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The email contact for the zone record.
	Email pulumi.StringPtrOutput `pulumi:"email"`
	// An array of master DNS servers. For when `type` is
	// `SECONDARY`.
	Masters pulumi.StringArrayOutput `pulumi:"masters"`
	// The name of the zone. Note the `.` at the end of the name.
	// Changing this creates a new DNS zone.
	Name pulumi.StringOutput `pulumi:"name"`
	// The region in which to obtain the V2 Compute client.
	// Keypairs are associated with accounts, but a Compute client is needed to
	// create one. If omitted, the `region` argument of the provider is used.
	// Changing this creates a new DNS zone.
	Region pulumi.StringOutput `pulumi:"region"`
	// The time to live (TTL) of the zone.
	Ttl pulumi.IntOutput `pulumi:"ttl"`
	// The type of zone. Can either be `PRIMARY` or `SECONDARY`.
	// Changing this creates a new zone.
	Type pulumi.StringOutput `pulumi:"type"`
	// Map of additional options. Changing this creates a
	// new zone.
	ValueSpecs pulumi.MapOutput `pulumi:"valueSpecs"`
}

// NewZone registers a new resource with the given unique name, arguments, and options.
func NewZone(ctx *pulumi.Context,
	name string, args *ZoneArgs, opts ...pulumi.ResourceOption) (*Zone, error) {
	if args == nil {
		args = &ZoneArgs{}
	}
	var resource Zone
	err := ctx.RegisterResource("openstack:dns/zone:Zone", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetZone gets an existing Zone resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetZone(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ZoneState, opts ...pulumi.ResourceOption) (*Zone, error) {
	var resource Zone
	err := ctx.ReadResource("openstack:dns/zone:Zone", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Zone resources.
type zoneState struct {
	// Attributes for the DNS Service scheduler.
	// Changing this creates a new zone.
	Attributes map[string]interface{} `pulumi:"attributes"`
	// A description of the zone.
	Description *string `pulumi:"description"`
	// The email contact for the zone record.
	Email *string `pulumi:"email"`
	// An array of master DNS servers. For when `type` is
	// `SECONDARY`.
	Masters []string `pulumi:"masters"`
	// The name of the zone. Note the `.` at the end of the name.
	// Changing this creates a new DNS zone.
	Name *string `pulumi:"name"`
	// The region in which to obtain the V2 Compute client.
	// Keypairs are associated with accounts, but a Compute client is needed to
	// create one. If omitted, the `region` argument of the provider is used.
	// Changing this creates a new DNS zone.
	Region *string `pulumi:"region"`
	// The time to live (TTL) of the zone.
	Ttl *int `pulumi:"ttl"`
	// The type of zone. Can either be `PRIMARY` or `SECONDARY`.
	// Changing this creates a new zone.
	Type *string `pulumi:"type"`
	// Map of additional options. Changing this creates a
	// new zone.
	ValueSpecs map[string]interface{} `pulumi:"valueSpecs"`
}

type ZoneState struct {
	// Attributes for the DNS Service scheduler.
	// Changing this creates a new zone.
	Attributes pulumi.MapInput
	// A description of the zone.
	Description pulumi.StringPtrInput
	// The email contact for the zone record.
	Email pulumi.StringPtrInput
	// An array of master DNS servers. For when `type` is
	// `SECONDARY`.
	Masters pulumi.StringArrayInput
	// The name of the zone. Note the `.` at the end of the name.
	// Changing this creates a new DNS zone.
	Name pulumi.StringPtrInput
	// The region in which to obtain the V2 Compute client.
	// Keypairs are associated with accounts, but a Compute client is needed to
	// create one. If omitted, the `region` argument of the provider is used.
	// Changing this creates a new DNS zone.
	Region pulumi.StringPtrInput
	// The time to live (TTL) of the zone.
	Ttl pulumi.IntPtrInput
	// The type of zone. Can either be `PRIMARY` or `SECONDARY`.
	// Changing this creates a new zone.
	Type pulumi.StringPtrInput
	// Map of additional options. Changing this creates a
	// new zone.
	ValueSpecs pulumi.MapInput
}

func (ZoneState) ElementType() reflect.Type {
	return reflect.TypeOf((*zoneState)(nil)).Elem()
}

type zoneArgs struct {
	// Attributes for the DNS Service scheduler.
	// Changing this creates a new zone.
	Attributes map[string]interface{} `pulumi:"attributes"`
	// A description of the zone.
	Description *string `pulumi:"description"`
	// The email contact for the zone record.
	Email *string `pulumi:"email"`
	// An array of master DNS servers. For when `type` is
	// `SECONDARY`.
	Masters []string `pulumi:"masters"`
	// The name of the zone. Note the `.` at the end of the name.
	// Changing this creates a new DNS zone.
	Name *string `pulumi:"name"`
	// The region in which to obtain the V2 Compute client.
	// Keypairs are associated with accounts, but a Compute client is needed to
	// create one. If omitted, the `region` argument of the provider is used.
	// Changing this creates a new DNS zone.
	Region *string `pulumi:"region"`
	// The time to live (TTL) of the zone.
	Ttl *int `pulumi:"ttl"`
	// The type of zone. Can either be `PRIMARY` or `SECONDARY`.
	// Changing this creates a new zone.
	Type *string `pulumi:"type"`
	// Map of additional options. Changing this creates a
	// new zone.
	ValueSpecs map[string]interface{} `pulumi:"valueSpecs"`
}

// The set of arguments for constructing a Zone resource.
type ZoneArgs struct {
	// Attributes for the DNS Service scheduler.
	// Changing this creates a new zone.
	Attributes pulumi.MapInput
	// A description of the zone.
	Description pulumi.StringPtrInput
	// The email contact for the zone record.
	Email pulumi.StringPtrInput
	// An array of master DNS servers. For when `type` is
	// `SECONDARY`.
	Masters pulumi.StringArrayInput
	// The name of the zone. Note the `.` at the end of the name.
	// Changing this creates a new DNS zone.
	Name pulumi.StringPtrInput
	// The region in which to obtain the V2 Compute client.
	// Keypairs are associated with accounts, but a Compute client is needed to
	// create one. If omitted, the `region` argument of the provider is used.
	// Changing this creates a new DNS zone.
	Region pulumi.StringPtrInput
	// The time to live (TTL) of the zone.
	Ttl pulumi.IntPtrInput
	// The type of zone. Can either be `PRIMARY` or `SECONDARY`.
	// Changing this creates a new zone.
	Type pulumi.StringPtrInput
	// Map of additional options. Changing this creates a
	// new zone.
	ValueSpecs pulumi.MapInput
}

func (ZoneArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*zoneArgs)(nil)).Elem()
}
