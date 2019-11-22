// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package blockstorage

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a V3 volume resource within OpenStack.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/blockstorage_volume_v3.html.markdown.
type Volume struct {
	s *pulumi.ResourceState
}

// NewVolume registers a new resource with the given unique name, arguments, and options.
func NewVolume(ctx *pulumi.Context,
	name string, args *VolumeArgs, opts ...pulumi.ResourceOpt) (*Volume, error) {
	if args == nil || args.Size == nil {
		return nil, errors.New("missing required argument 'Size'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["availabilityZone"] = nil
		inputs["consistencyGroupId"] = nil
		inputs["description"] = nil
		inputs["enableOnlineResize"] = nil
		inputs["imageId"] = nil
		inputs["metadata"] = nil
		inputs["multiattach"] = nil
		inputs["name"] = nil
		inputs["region"] = nil
		inputs["size"] = nil
		inputs["snapshotId"] = nil
		inputs["sourceReplica"] = nil
		inputs["sourceVolId"] = nil
		inputs["volumeType"] = nil
	} else {
		inputs["availabilityZone"] = args.AvailabilityZone
		inputs["consistencyGroupId"] = args.ConsistencyGroupId
		inputs["description"] = args.Description
		inputs["enableOnlineResize"] = args.EnableOnlineResize
		inputs["imageId"] = args.ImageId
		inputs["metadata"] = args.Metadata
		inputs["multiattach"] = args.Multiattach
		inputs["name"] = args.Name
		inputs["region"] = args.Region
		inputs["size"] = args.Size
		inputs["snapshotId"] = args.SnapshotId
		inputs["sourceReplica"] = args.SourceReplica
		inputs["sourceVolId"] = args.SourceVolId
		inputs["volumeType"] = args.VolumeType
	}
	inputs["attachments"] = nil
	s, err := ctx.RegisterResource("openstack:blockstorage/volume:Volume", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Volume{s: s}, nil
}

// GetVolume gets an existing Volume resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetVolume(ctx *pulumi.Context,
	name string, id pulumi.ID, state *VolumeState, opts ...pulumi.ResourceOpt) (*Volume, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["attachments"] = state.Attachments
		inputs["availabilityZone"] = state.AvailabilityZone
		inputs["consistencyGroupId"] = state.ConsistencyGroupId
		inputs["description"] = state.Description
		inputs["enableOnlineResize"] = state.EnableOnlineResize
		inputs["imageId"] = state.ImageId
		inputs["metadata"] = state.Metadata
		inputs["multiattach"] = state.Multiattach
		inputs["name"] = state.Name
		inputs["region"] = state.Region
		inputs["size"] = state.Size
		inputs["snapshotId"] = state.SnapshotId
		inputs["sourceReplica"] = state.SourceReplica
		inputs["sourceVolId"] = state.SourceVolId
		inputs["volumeType"] = state.VolumeType
	}
	s, err := ctx.ReadResource("openstack:blockstorage/volume:Volume", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Volume{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Volume) URN() pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Volume) ID() pulumi.IDOutput {
	return r.s.ID()
}

// If a volume is attached to an instance, this attribute will
// display the Attachment ID, Instance ID, and the Device as the Instance
// sees it.
func (r *Volume) Attachments() pulumi.ArrayOutput {
	return (pulumi.ArrayOutput)(r.s.State["attachments"])
}

// The availability zone for the volume.
// Changing this creates a new volume.
func (r *Volume) AvailabilityZone() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["availabilityZone"])
}

// The consistency group to place the volume
// in.
func (r *Volume) ConsistencyGroupId() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["consistencyGroupId"])
}

// A description of the volume. Changing this updates
// the volume's description.
func (r *Volume) Description() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["description"])
}

// When this option is set it allows extending
// attached volumes. Note: updating size of an attached volume requires Cinder
// support for version 3.42 and a compatible storage driver.
func (r *Volume) EnableOnlineResize() pulumi.BoolOutput {
	return (pulumi.BoolOutput)(r.s.State["enableOnlineResize"])
}

// The image ID from which to create the volume.
// Changing this creates a new volume.
func (r *Volume) ImageId() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["imageId"])
}

// Metadata key/value pairs to associate with the volume.
// Changing this updates the existing volume metadata.
func (r *Volume) Metadata() pulumi.MapOutput {
	return (pulumi.MapOutput)(r.s.State["metadata"])
}

// Allow the volume to be attached to more than one Compute instance.
func (r *Volume) Multiattach() pulumi.BoolOutput {
	return (pulumi.BoolOutput)(r.s.State["multiattach"])
}

// A unique name for the volume. Changing this updates the
// volume's name.
func (r *Volume) Name() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["name"])
}

// The region in which to create the volume. If
// omitted, the `region` argument of the provider is used. Changing this
// creates a new volume.
func (r *Volume) Region() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["region"])
}

// The size of the volume to create (in gigabytes).
func (r *Volume) Size() pulumi.IntOutput {
	return (pulumi.IntOutput)(r.s.State["size"])
}

// The snapshot ID from which to create the volume.
// Changing this creates a new volume.
func (r *Volume) SnapshotId() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["snapshotId"])
}

// The volume ID to replicate with.
func (r *Volume) SourceReplica() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["sourceReplica"])
}

// The volume ID from which to create the volume.
// Changing this creates a new volume.
func (r *Volume) SourceVolId() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["sourceVolId"])
}

// The type of volume to create.
// Changing this creates a new volume.
func (r *Volume) VolumeType() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["volumeType"])
}

// Input properties used for looking up and filtering Volume resources.
type VolumeState struct {
	// If a volume is attached to an instance, this attribute will
	// display the Attachment ID, Instance ID, and the Device as the Instance
	// sees it.
	Attachments interface{}
	// The availability zone for the volume.
	// Changing this creates a new volume.
	AvailabilityZone interface{}
	// The consistency group to place the volume
	// in.
	ConsistencyGroupId interface{}
	// A description of the volume. Changing this updates
	// the volume's description.
	Description interface{}
	// When this option is set it allows extending
	// attached volumes. Note: updating size of an attached volume requires Cinder
	// support for version 3.42 and a compatible storage driver.
	EnableOnlineResize interface{}
	// The image ID from which to create the volume.
	// Changing this creates a new volume.
	ImageId interface{}
	// Metadata key/value pairs to associate with the volume.
	// Changing this updates the existing volume metadata.
	Metadata interface{}
	// Allow the volume to be attached to more than one Compute instance.
	Multiattach interface{}
	// A unique name for the volume. Changing this updates the
	// volume's name.
	Name interface{}
	// The region in which to create the volume. If
	// omitted, the `region` argument of the provider is used. Changing this
	// creates a new volume.
	Region interface{}
	// The size of the volume to create (in gigabytes).
	Size interface{}
	// The snapshot ID from which to create the volume.
	// Changing this creates a new volume.
	SnapshotId interface{}
	// The volume ID to replicate with.
	SourceReplica interface{}
	// The volume ID from which to create the volume.
	// Changing this creates a new volume.
	SourceVolId interface{}
	// The type of volume to create.
	// Changing this creates a new volume.
	VolumeType interface{}
}

// The set of arguments for constructing a Volume resource.
type VolumeArgs struct {
	// The availability zone for the volume.
	// Changing this creates a new volume.
	AvailabilityZone interface{}
	// The consistency group to place the volume
	// in.
	ConsistencyGroupId interface{}
	// A description of the volume. Changing this updates
	// the volume's description.
	Description interface{}
	// When this option is set it allows extending
	// attached volumes. Note: updating size of an attached volume requires Cinder
	// support for version 3.42 and a compatible storage driver.
	EnableOnlineResize interface{}
	// The image ID from which to create the volume.
	// Changing this creates a new volume.
	ImageId interface{}
	// Metadata key/value pairs to associate with the volume.
	// Changing this updates the existing volume metadata.
	Metadata interface{}
	// Allow the volume to be attached to more than one Compute instance.
	Multiattach interface{}
	// A unique name for the volume. Changing this updates the
	// volume's name.
	Name interface{}
	// The region in which to create the volume. If
	// omitted, the `region` argument of the provider is used. Changing this
	// creates a new volume.
	Region interface{}
	// The size of the volume to create (in gigabytes).
	Size interface{}
	// The snapshot ID from which to create the volume.
	// Changing this creates a new volume.
	SnapshotId interface{}
	// The volume ID to replicate with.
	SourceReplica interface{}
	// The volume ID from which to create the volume.
	// Changing this creates a new volume.
	SourceVolId interface{}
	// The type of volume to create.
	// Changing this creates a new volume.
	VolumeType interface{}
}
