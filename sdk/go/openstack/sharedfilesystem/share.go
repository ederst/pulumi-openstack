// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package sharedfilesystem

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this resource to configure a share.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/sharedfilesystem_share_v2.html.markdown.
type Share struct {
	s *pulumi.ResourceState
}

// NewShare registers a new resource with the given unique name, arguments, and options.
func NewShare(ctx *pulumi.Context,
	name string, args *ShareArgs, opts ...pulumi.ResourceOpt) (*Share, error) {
	if args == nil || args.ShareProto == nil {
		return nil, errors.New("missing required argument 'ShareProto'")
	}
	if args == nil || args.Size == nil {
		return nil, errors.New("missing required argument 'Size'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["availabilityZone"] = nil
		inputs["description"] = nil
		inputs["isPublic"] = nil
		inputs["metadata"] = nil
		inputs["name"] = nil
		inputs["region"] = nil
		inputs["shareNetworkId"] = nil
		inputs["shareProto"] = nil
		inputs["shareType"] = nil
		inputs["size"] = nil
		inputs["snapshotId"] = nil
	} else {
		inputs["availabilityZone"] = args.AvailabilityZone
		inputs["description"] = args.Description
		inputs["isPublic"] = args.IsPublic
		inputs["metadata"] = args.Metadata
		inputs["name"] = args.Name
		inputs["region"] = args.Region
		inputs["shareNetworkId"] = args.ShareNetworkId
		inputs["shareProto"] = args.ShareProto
		inputs["shareType"] = args.ShareType
		inputs["size"] = args.Size
		inputs["snapshotId"] = args.SnapshotId
	}
	inputs["allMetadata"] = nil
	inputs["exportLocations"] = nil
	inputs["hasReplicas"] = nil
	inputs["host"] = nil
	inputs["projectId"] = nil
	inputs["replicationType"] = nil
	inputs["shareServerId"] = nil
	s, err := ctx.RegisterResource("openstack:sharedfilesystem/share:Share", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Share{s: s}, nil
}

// GetShare gets an existing Share resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetShare(ctx *pulumi.Context,
	name string, id pulumi.ID, state *ShareState, opts ...pulumi.ResourceOpt) (*Share, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["allMetadata"] = state.AllMetadata
		inputs["availabilityZone"] = state.AvailabilityZone
		inputs["description"] = state.Description
		inputs["exportLocations"] = state.ExportLocations
		inputs["hasReplicas"] = state.HasReplicas
		inputs["host"] = state.Host
		inputs["isPublic"] = state.IsPublic
		inputs["metadata"] = state.Metadata
		inputs["name"] = state.Name
		inputs["projectId"] = state.ProjectId
		inputs["region"] = state.Region
		inputs["replicationType"] = state.ReplicationType
		inputs["shareNetworkId"] = state.ShareNetworkId
		inputs["shareProto"] = state.ShareProto
		inputs["shareServerId"] = state.ShareServerId
		inputs["shareType"] = state.ShareType
		inputs["size"] = state.Size
		inputs["snapshotId"] = state.SnapshotId
	}
	s, err := ctx.ReadResource("openstack:sharedfilesystem/share:Share", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Share{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Share) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Share) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The map of metadata, assigned on the share, which has been
// explicitly and implicitly added.
func (r *Share) AllMetadata() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["allMetadata"])
}

// The share availability zone. Changing this creates a
// new share.
func (r *Share) AvailabilityZone() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["availabilityZone"])
}

// The human-readable description for the share.
// Changing this updates the description of the existing share.
func (r *Share) Description() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["description"])
}

// A list of export locations. For example, when a share server
// has more than one network interface, it can have multiple export locations.
func (r *Share) ExportLocations() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["exportLocations"])
}

// Indicates whether a share has replicas or not.
func (r *Share) HasReplicas() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["hasReplicas"])
}

// The share host name.
func (r *Share) Host() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["host"])
}

// The level of visibility for the share. Set to true to make
// share public. Set to false to make it private. Default value is false. Changing this
// updates the existing share.
func (r *Share) IsPublic() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["isPublic"])
}

// One or more metadata key and value pairs as a dictionary of
// strings.
func (r *Share) Metadata() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["metadata"])
}

// The name of the share. Changing this updates the name
// of the existing share.
func (r *Share) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The owner of the Share.
func (r *Share) ProjectId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["projectId"])
}

// The region in which to obtain the V2 Shared File System client.
// A Shared File System client is needed to create a share. Changing this
// creates a new share.
func (r *Share) Region() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["region"])
}

// The share replication type.
func (r *Share) ReplicationType() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["replicationType"])
}

// The UUID of a share network where the share server exists
// or will be created. If `share_network_id` is not set and you provide a `snapshot_id`,
// the share_network_id value from the snapshot is used. Changing this creates a new share.
func (r *Share) ShareNetworkId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["shareNetworkId"])
}

// The share protocol - can either be NFS, CIFS,
// CEPHFS, GLUSTERFS, HDFS or MAPRFS. Changing this creates a new share.
func (r *Share) ShareProto() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["shareProto"])
}

// The UUID of the share server.
func (r *Share) ShareServerId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["shareServerId"])
}

// The share type name. If you omit this parameter, the default
// share type is used.
func (r *Share) ShareType() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["shareType"])
}

// The share size, in GBs. The requested share size cannot be greater
// than the allowed GB quota. Changing this resizes the existing share.
func (r *Share) Size() *pulumi.IntOutput {
	return (*pulumi.IntOutput)(r.s.State["size"])
}

// The UUID of the share's base snapshot. Changing this creates
// a new share.
func (r *Share) SnapshotId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["snapshotId"])
}

// Input properties used for looking up and filtering Share resources.
type ShareState struct {
	// The map of metadata, assigned on the share, which has been
	// explicitly and implicitly added.
	AllMetadata interface{}
	// The share availability zone. Changing this creates a
	// new share.
	AvailabilityZone interface{}
	// The human-readable description for the share.
	// Changing this updates the description of the existing share.
	Description interface{}
	// A list of export locations. For example, when a share server
	// has more than one network interface, it can have multiple export locations.
	ExportLocations interface{}
	// Indicates whether a share has replicas or not.
	HasReplicas interface{}
	// The share host name.
	Host interface{}
	// The level of visibility for the share. Set to true to make
	// share public. Set to false to make it private. Default value is false. Changing this
	// updates the existing share.
	IsPublic interface{}
	// One or more metadata key and value pairs as a dictionary of
	// strings.
	Metadata interface{}
	// The name of the share. Changing this updates the name
	// of the existing share.
	Name interface{}
	// The owner of the Share.
	ProjectId interface{}
	// The region in which to obtain the V2 Shared File System client.
	// A Shared File System client is needed to create a share. Changing this
	// creates a new share.
	Region interface{}
	// The share replication type.
	ReplicationType interface{}
	// The UUID of a share network where the share server exists
	// or will be created. If `share_network_id` is not set and you provide a `snapshot_id`,
	// the share_network_id value from the snapshot is used. Changing this creates a new share.
	ShareNetworkId interface{}
	// The share protocol - can either be NFS, CIFS,
	// CEPHFS, GLUSTERFS, HDFS or MAPRFS. Changing this creates a new share.
	ShareProto interface{}
	// The UUID of the share server.
	ShareServerId interface{}
	// The share type name. If you omit this parameter, the default
	// share type is used.
	ShareType interface{}
	// The share size, in GBs. The requested share size cannot be greater
	// than the allowed GB quota. Changing this resizes the existing share.
	Size interface{}
	// The UUID of the share's base snapshot. Changing this creates
	// a new share.
	SnapshotId interface{}
}

// The set of arguments for constructing a Share resource.
type ShareArgs struct {
	// The share availability zone. Changing this creates a
	// new share.
	AvailabilityZone interface{}
	// The human-readable description for the share.
	// Changing this updates the description of the existing share.
	Description interface{}
	// The level of visibility for the share. Set to true to make
	// share public. Set to false to make it private. Default value is false. Changing this
	// updates the existing share.
	IsPublic interface{}
	// One or more metadata key and value pairs as a dictionary of
	// strings.
	Metadata interface{}
	// The name of the share. Changing this updates the name
	// of the existing share.
	Name interface{}
	// The region in which to obtain the V2 Shared File System client.
	// A Shared File System client is needed to create a share. Changing this
	// creates a new share.
	Region interface{}
	// The UUID of a share network where the share server exists
	// or will be created. If `share_network_id` is not set and you provide a `snapshot_id`,
	// the share_network_id value from the snapshot is used. Changing this creates a new share.
	ShareNetworkId interface{}
	// The share protocol - can either be NFS, CIFS,
	// CEPHFS, GLUSTERFS, HDFS or MAPRFS. Changing this creates a new share.
	ShareProto interface{}
	// The share type name. If you omit this parameter, the default
	// share type is used.
	ShareType interface{}
	// The share size, in GBs. The requested share size cannot be greater
	// than the allowed GB quota. Changing this resizes the existing share.
	Size interface{}
	// The UUID of the share's base snapshot. Changing this creates
	// a new share.
	SnapshotId interface{}
}
