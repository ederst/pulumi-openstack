// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this data source to get information about host aggregates
// by name.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/compute"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := compute.LookupAggregateV2(ctx, &compute.LookupAggregateV2Args{
// 			Name: "test",
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupAggregateV2(ctx *pulumi.Context, args *LookupAggregateV2Args, opts ...pulumi.InvokeOption) (*LookupAggregateV2Result, error) {
	var rv LookupAggregateV2Result
	err := ctx.Invoke("openstack:compute/getAggregateV2:getAggregateV2", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getAggregateV2.
type LookupAggregateV2Args struct {
	// List of Hypervisors contained in the Host Aggregate
	Hosts []string `pulumi:"hosts"`
	// Metadata of the Host Aggregate
	Metadata map[string]string `pulumi:"metadata"`
	// The name of the host aggregate
	Name string `pulumi:"name"`
}

// A collection of values returned by getAggregateV2.
type LookupAggregateV2Result struct {
	// List of Hypervisors contained in the Host Aggregate
	Hosts []string `pulumi:"hosts"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// Metadata of the Host Aggregate
	Metadata map[string]string `pulumi:"metadata"`
	// See Argument Reference above.
	Name string `pulumi:"name"`
	// Availability zone of the Host Aggregate
	Zone string `pulumi:"zone"`
}
