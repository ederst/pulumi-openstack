// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package blockstorage

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a V2 block storage quotaset resource within OpenStack.
// 
// > **Note:** This usually requires admin privileges.
// 
// > **Note:** This resource has a no-op deletion so no actual actions will be done against the OpenStack API 
//     in case of delete call.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/blockstorage_quotaset_v2.html.markdown.
type QuoteSetV2 struct {
	s *pulumi.ResourceState
}

// NewQuoteSetV2 registers a new resource with the given unique name, arguments, and options.
func NewQuoteSetV2(ctx *pulumi.Context,
	name string, args *QuoteSetV2Args, opts ...pulumi.ResourceOpt) (*QuoteSetV2, error) {
	if args == nil || args.ProjectId == nil {
		return nil, errors.New("missing required argument 'ProjectId'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["backupGigabytes"] = nil
		inputs["backups"] = nil
		inputs["gigabytes"] = nil
		inputs["groups"] = nil
		inputs["perVolumeGigabytes"] = nil
		inputs["projectId"] = nil
		inputs["region"] = nil
		inputs["snapshots"] = nil
		inputs["volumes"] = nil
	} else {
		inputs["backupGigabytes"] = args.BackupGigabytes
		inputs["backups"] = args.Backups
		inputs["gigabytes"] = args.Gigabytes
		inputs["groups"] = args.Groups
		inputs["perVolumeGigabytes"] = args.PerVolumeGigabytes
		inputs["projectId"] = args.ProjectId
		inputs["region"] = args.Region
		inputs["snapshots"] = args.Snapshots
		inputs["volumes"] = args.Volumes
	}
	s, err := ctx.RegisterResource("openstack:blockstorage/quoteSetV2:QuoteSetV2", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &QuoteSetV2{s: s}, nil
}

// GetQuoteSetV2 gets an existing QuoteSetV2 resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetQuoteSetV2(ctx *pulumi.Context,
	name string, id pulumi.ID, state *QuoteSetV2State, opts ...pulumi.ResourceOpt) (*QuoteSetV2, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["backupGigabytes"] = state.BackupGigabytes
		inputs["backups"] = state.Backups
		inputs["gigabytes"] = state.Gigabytes
		inputs["groups"] = state.Groups
		inputs["perVolumeGigabytes"] = state.PerVolumeGigabytes
		inputs["projectId"] = state.ProjectId
		inputs["region"] = state.Region
		inputs["snapshots"] = state.Snapshots
		inputs["volumes"] = state.Volumes
	}
	s, err := ctx.ReadResource("openstack:blockstorage/quoteSetV2:QuoteSetV2", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &QuoteSetV2{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *QuoteSetV2) URN() pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *QuoteSetV2) ID() pulumi.IDOutput {
	return r.s.ID()
}

// Quota value for backup gigabytes. Changing
// this updates the existing quotaset.
func (r *QuoteSetV2) BackupGigabytes() pulumi.IntOutput {
	return (pulumi.IntOutput)(r.s.State["backupGigabytes"])
}

// Quota value for backups. Changing this updates the
// existing quotaset.
func (r *QuoteSetV2) Backups() pulumi.IntOutput {
	return (pulumi.IntOutput)(r.s.State["backups"])
}

// Quota value for gigabytes. Changing this updates the
// existing quotaset.
func (r *QuoteSetV2) Gigabytes() pulumi.IntOutput {
	return (pulumi.IntOutput)(r.s.State["gigabytes"])
}

// Quota value for groups. Changing this updates the
// existing quotaset.
func (r *QuoteSetV2) Groups() pulumi.IntOutput {
	return (pulumi.IntOutput)(r.s.State["groups"])
}

// Quota value for gigabytes per volume .
// Changing this updates the existing quotaset.
func (r *QuoteSetV2) PerVolumeGigabytes() pulumi.IntOutput {
	return (pulumi.IntOutput)(r.s.State["perVolumeGigabytes"])
}

// ID of the project to manage quotas. Changing this
// creates a new quotaset.
func (r *QuoteSetV2) ProjectId() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["projectId"])
}

// The region in which to create the volume. If
// omitted, the `region` argument of the provider is used. Changing this
// creates a new quotaset.
func (r *QuoteSetV2) Region() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["region"])
}

// Quota value for snapshots. Changing this updates the
// existing quotaset.
func (r *QuoteSetV2) Snapshots() pulumi.IntOutput {
	return (pulumi.IntOutput)(r.s.State["snapshots"])
}

// Quota value for volumes. Changing this updates the
// existing quotaset.
func (r *QuoteSetV2) Volumes() pulumi.IntOutput {
	return (pulumi.IntOutput)(r.s.State["volumes"])
}

// Input properties used for looking up and filtering QuoteSetV2 resources.
type QuoteSetV2State struct {
	// Quota value for backup gigabytes. Changing
	// this updates the existing quotaset.
	BackupGigabytes interface{}
	// Quota value for backups. Changing this updates the
	// existing quotaset.
	Backups interface{}
	// Quota value for gigabytes. Changing this updates the
	// existing quotaset.
	Gigabytes interface{}
	// Quota value for groups. Changing this updates the
	// existing quotaset.
	Groups interface{}
	// Quota value for gigabytes per volume .
	// Changing this updates the existing quotaset.
	PerVolumeGigabytes interface{}
	// ID of the project to manage quotas. Changing this
	// creates a new quotaset.
	ProjectId interface{}
	// The region in which to create the volume. If
	// omitted, the `region` argument of the provider is used. Changing this
	// creates a new quotaset.
	Region interface{}
	// Quota value for snapshots. Changing this updates the
	// existing quotaset.
	Snapshots interface{}
	// Quota value for volumes. Changing this updates the
	// existing quotaset.
	Volumes interface{}
}

// The set of arguments for constructing a QuoteSetV2 resource.
type QuoteSetV2Args struct {
	// Quota value for backup gigabytes. Changing
	// this updates the existing quotaset.
	BackupGigabytes interface{}
	// Quota value for backups. Changing this updates the
	// existing quotaset.
	Backups interface{}
	// Quota value for gigabytes. Changing this updates the
	// existing quotaset.
	Gigabytes interface{}
	// Quota value for groups. Changing this updates the
	// existing quotaset.
	Groups interface{}
	// Quota value for gigabytes per volume .
	// Changing this updates the existing quotaset.
	PerVolumeGigabytes interface{}
	// ID of the project to manage quotas. Changing this
	// creates a new quotaset.
	ProjectId interface{}
	// The region in which to create the volume. If
	// omitted, the `region` argument of the provider is used. Changing this
	// creates a new quotaset.
	Region interface{}
	// Quota value for snapshots. Changing this updates the
	// existing quotaset.
	Snapshots interface{}
	// Quota value for volumes. Changing this updates the
	// existing quotaset.
	Volumes interface{}
}
