// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sharedfilesystem

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this data source to get the ID of an available Shared File System share.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack/sharedfilesystem"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		opt0 := "share_1"
// 		_, err := sharedfilesystem.LookupShare(ctx, &sharedfilesystem.LookupShareArgs{
// 			Name: &opt0,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupShare(ctx *pulumi.Context, args *LookupShareArgs, opts ...pulumi.InvokeOption) (*LookupShareResult, error) {
	var rv LookupShareResult
	err := ctx.Invoke("openstack:sharedfilesystem/getShare:getShare", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getShare.
type LookupShareArgs struct {
	// The human-readable description for the share.
	Description *string `pulumi:"description"`
	// The export location path of the share. Available
	// since Manila API version 2.35.
	ExportLocationPath *string `pulumi:"exportLocationPath"`
	// The level of visibility for the share.
	// length.
	IsPublic *bool `pulumi:"isPublic"`
	// One or more metadata key and value pairs as a dictionary of
	// strings.
	Metadata map[string]interface{} `pulumi:"metadata"`
	// The name of the share.
	Name *string `pulumi:"name"`
	// The region in which to obtain the V2 Shared File System client.
	Region *string `pulumi:"region"`
	// The UUID of the share's share network.
	ShareNetworkId *string `pulumi:"shareNetworkId"`
	// The UUID of the share's base snapshot.
	SnapshotId *string `pulumi:"snapshotId"`
	// A share status filter. A valid value is `creating`,
	// `error`, `available`, `deleting`, `errorDeleting`, `manageStarting`,
	// `manageError`, `unmanageStarting`, `unmanageError`, `unmanaged`,
	// `extending`, `extendingError`, `shrinking`, `shrinkingError`, or
	// `shrinkingPossibleDataLossError`.
	Status *string `pulumi:"status"`
}

// A collection of values returned by getShare.
type LookupShareResult struct {
	// The share availability zone.
	AvailabilityZone string `pulumi:"availabilityZone"`
	// See Argument Reference above.
	Description string `pulumi:"description"`
	// See Argument Reference above.
	ExportLocationPath *string `pulumi:"exportLocationPath"`
	// A list of export locations. For example, when a share
	// server has more than one network interface, it can have multiple export
	// locations.
	ExportLocations []GetShareExportLocation `pulumi:"exportLocations"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// See Argument Reference above.
	IsPublic bool `pulumi:"isPublic"`
	// See Argument Reference above.
	Metadata map[string]interface{} `pulumi:"metadata"`
	// See Argument Reference above.
	Name string `pulumi:"name"`
	// See Argument Reference above.
	ProjectId string `pulumi:"projectId"`
	// The region in which to obtain the V2 Shared File System client.
	Region string `pulumi:"region"`
	// See Argument Reference above.
	ShareNetworkId string `pulumi:"shareNetworkId"`
	// The share protocol.
	ShareProto string `pulumi:"shareProto"`
	// The share size, in GBs.
	Size int `pulumi:"size"`
	// See Argument Reference above.
	SnapshotId string `pulumi:"snapshotId"`
	// See Argument Reference above.
	Status string `pulumi:"status"`
}
