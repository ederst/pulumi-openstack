// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package networking

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to get the ID of an available OpenStack trunk.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/networking_trunk_v2.html.markdown.
func LookupTrunk(ctx *pulumi.Context, args *LookupTrunkArgs, opts ...pulumi.InvokeOption) (*LookupTrunkResult, error) {
	var rv LookupTrunkResult
	err := ctx.Invoke("openstack:networking/getTrunk:getTrunk", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getTrunk.
type LookupTrunkArgs struct {
	// The administrative state of the trunk.
	AdminStateUp *bool `pulumi:"adminStateUp"`
	// Human-readable description of the trunk.
	Description *string `pulumi:"description"`
	// The name of the trunk.
	Name *string `pulumi:"name"`
	// The ID of the trunk parent port.
	PortId *string `pulumi:"portId"`
	// The owner of the trunk.
	ProjectId *string `pulumi:"projectId"`
	// The region in which to obtain the V2 Neutron client.
	// A Neutron client is needed to retrieve trunk ids. If omitted, the
	// `region` argument of the provider is used.
	Region *string `pulumi:"region"`
	// The status of the trunk.
	Status *string `pulumi:"status"`
	// The list of trunk tags to filter.
	Tags []string `pulumi:"tags"`
	// The ID of the trunk.
	TrunkId *string `pulumi:"trunkId"`
}

// A collection of values returned by getTrunk.
type LookupTrunkResult struct {
	AdminStateUp *bool `pulumi:"adminStateUp"`
	// The set of string tags applied on the trunk.
	AllTags     []string `pulumi:"allTags"`
	Description *string  `pulumi:"description"`
	// id is the provider-assigned unique ID for this managed resource.
	Id   string  `pulumi:"id"`
	Name *string `pulumi:"name"`
	// The ID of the trunk subport.
	PortId    *string `pulumi:"portId"`
	ProjectId string  `pulumi:"projectId"`
	Region    string  `pulumi:"region"`
	Status    *string `pulumi:"status"`
	// The set of the trunk subports. The structure of each subport is
	// described below.
	SubPorts []GetTrunkSubPort `pulumi:"subPorts"`
	Tags     []string          `pulumi:"tags"`
	TrunkId  *string           `pulumi:"trunkId"`
}
