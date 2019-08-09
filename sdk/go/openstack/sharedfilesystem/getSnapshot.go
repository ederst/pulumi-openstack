// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sharedfilesystem

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to get the ID of an available Shared File System snapshot.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/sharedfilesystem_snapshot_v2.html.markdown.
func LookupSnapshot(ctx *pulumi.Context, args *GetSnapshotArgs) (*GetSnapshotResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["description"] = args.Description
		inputs["name"] = args.Name
		inputs["region"] = args.Region
		inputs["shareId"] = args.ShareId
		inputs["status"] = args.Status
	}
	outputs, err := ctx.Invoke("openstack:sharedfilesystem/getSnapshot:getSnapshot", inputs)
	if err != nil {
		return nil, err
	}
	return &GetSnapshotResult{
		Description: outputs["description"],
		Name: outputs["name"],
		ProjectId: outputs["projectId"],
		Region: outputs["region"],
		ShareId: outputs["shareId"],
		ShareProto: outputs["shareProto"],
		ShareSize: outputs["shareSize"],
		Size: outputs["size"],
		Status: outputs["status"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getSnapshot.
type GetSnapshotArgs struct {
	// The human-readable description of the snapshot.
	Description interface{}
	// The name of the snapshot.
	Name interface{}
	// The region in which to obtain the V2 Shared File System client.
	Region interface{}
	ShareId interface{}
	// A snapshot status filter. A valid value is `available`, `error`,
	// `creating`, `deleting`, `manageStarting`, `manageError`, `unmanageStarting`,
	// `unmanageError` or `errorDeleting`.
	Status interface{}
}

// A collection of values returned by getSnapshot.
type GetSnapshotResult struct {
	// See Argument Reference above.
	Description interface{}
	// See Argument Reference above.
	Name interface{}
	// See Argument Reference above.
	ProjectId interface{}
	Region interface{}
	// The UUID of the source share that was used to create the snapshot.
	ShareId interface{}
	// The file system protocol of a share snapshot.
	ShareProto interface{}
	// The share snapshot size, in GBs.
	ShareSize interface{}
	// The snapshot size, in GBs.
	Size interface{}
	// See Argument Reference above.
	Status interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
