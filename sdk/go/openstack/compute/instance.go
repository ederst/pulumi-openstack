// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a V2 VM instance resource within OpenStack.
// 
// ## Importing instances
// 
// Importing instances can be tricky, since the nova api does not offer all
// information provided at creation time for later retrieval.
// Network interface attachment order, and number and sizes of ephemeral
// disks are examples of this.
// 
// ### Importing an instance with multiple emphemeral disks
// 
// The importer cannot read the emphemeral disk configuration
// of an instance, so just specify image_id as in the configuration 
// of the basic instance example.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_instance_v2.html.markdown.
type Instance struct {
	s *pulumi.ResourceState
}

// NewInstance registers a new resource with the given unique name, arguments, and options.
func NewInstance(ctx *pulumi.Context,
	name string, args *InstanceArgs, opts ...pulumi.ResourceOpt) (*Instance, error) {
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["accessIpV4"] = nil
		inputs["accessIpV6"] = nil
		inputs["adminPass"] = nil
		inputs["availabilityZone"] = nil
		inputs["blockDevices"] = nil
		inputs["configDrive"] = nil
		inputs["flavorId"] = nil
		inputs["flavorName"] = nil
		inputs["forceDelete"] = nil
		inputs["imageId"] = nil
		inputs["imageName"] = nil
		inputs["keyPair"] = nil
		inputs["metadata"] = nil
		inputs["name"] = nil
		inputs["networks"] = nil
		inputs["personalities"] = nil
		inputs["powerState"] = nil
		inputs["region"] = nil
		inputs["schedulerHints"] = nil
		inputs["securityGroups"] = nil
		inputs["stopBeforeDestroy"] = nil
		inputs["userData"] = nil
		inputs["vendorOptions"] = nil
	} else {
		inputs["accessIpV4"] = args.AccessIpV4
		inputs["accessIpV6"] = args.AccessIpV6
		inputs["adminPass"] = args.AdminPass
		inputs["availabilityZone"] = args.AvailabilityZone
		inputs["blockDevices"] = args.BlockDevices
		inputs["configDrive"] = args.ConfigDrive
		inputs["flavorId"] = args.FlavorId
		inputs["flavorName"] = args.FlavorName
		inputs["forceDelete"] = args.ForceDelete
		inputs["imageId"] = args.ImageId
		inputs["imageName"] = args.ImageName
		inputs["keyPair"] = args.KeyPair
		inputs["metadata"] = args.Metadata
		inputs["name"] = args.Name
		inputs["networks"] = args.Networks
		inputs["personalities"] = args.Personalities
		inputs["powerState"] = args.PowerState
		inputs["region"] = args.Region
		inputs["schedulerHints"] = args.SchedulerHints
		inputs["securityGroups"] = args.SecurityGroups
		inputs["stopBeforeDestroy"] = args.StopBeforeDestroy
		inputs["userData"] = args.UserData
		inputs["vendorOptions"] = args.VendorOptions
	}
	inputs["allMetadata"] = nil
	s, err := ctx.RegisterResource("openstack:compute/instance:Instance", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Instance{s: s}, nil
}

// GetInstance gets an existing Instance resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetInstance(ctx *pulumi.Context,
	name string, id pulumi.ID, state *InstanceState, opts ...pulumi.ResourceOpt) (*Instance, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["accessIpV4"] = state.AccessIpV4
		inputs["accessIpV6"] = state.AccessIpV6
		inputs["adminPass"] = state.AdminPass
		inputs["allMetadata"] = state.AllMetadata
		inputs["availabilityZone"] = state.AvailabilityZone
		inputs["blockDevices"] = state.BlockDevices
		inputs["configDrive"] = state.ConfigDrive
		inputs["flavorId"] = state.FlavorId
		inputs["flavorName"] = state.FlavorName
		inputs["forceDelete"] = state.ForceDelete
		inputs["imageId"] = state.ImageId
		inputs["imageName"] = state.ImageName
		inputs["keyPair"] = state.KeyPair
		inputs["metadata"] = state.Metadata
		inputs["name"] = state.Name
		inputs["networks"] = state.Networks
		inputs["personalities"] = state.Personalities
		inputs["powerState"] = state.PowerState
		inputs["region"] = state.Region
		inputs["schedulerHints"] = state.SchedulerHints
		inputs["securityGroups"] = state.SecurityGroups
		inputs["stopBeforeDestroy"] = state.StopBeforeDestroy
		inputs["userData"] = state.UserData
		inputs["vendorOptions"] = state.VendorOptions
	}
	s, err := ctx.ReadResource("openstack:compute/instance:Instance", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Instance{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Instance) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Instance) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The first detected Fixed IPv4 address.
func (r *Instance) AccessIpV4() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["accessIpV4"])
}

// The first detected Fixed IPv6 address.
func (r *Instance) AccessIpV6() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["accessIpV6"])
}

// The administrative password to assign to the server.
// Changing this changes the root password on the existing server.
func (r *Instance) AdminPass() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["adminPass"])
}

func (r *Instance) AllMetadata() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["allMetadata"])
}

// The availability zone in which to create
// the server. Changing this creates a new server.
func (r *Instance) AvailabilityZone() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["availabilityZone"])
}

// Configuration of block devices. The block_device
// structure is documented below. Changing this creates a new server.
// You can specify multiple block devices which will create an instance with
// multiple disks. This configuration is very flexible, so please see the
// following [reference](https://docs.openstack.org/nova/latest/user/block-device-mapping.html)
// for more information.
func (r *Instance) BlockDevices() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["blockDevices"])
}

// Whether to use the config_drive feature to
// configure the instance. Changing this creates a new server.
func (r *Instance) ConfigDrive() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["configDrive"])
}

// The flavor ID of
// the desired flavor for the server. Changing this resizes the existing server.
func (r *Instance) FlavorId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["flavorId"])
}

// The name of the
// desired flavor for the server. Changing this resizes the existing server.
func (r *Instance) FlavorName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["flavorName"])
}

// Whether to force the OpenStack instance to be
// forcefully deleted. This is useful for environments that have reclaim / soft
// deletion enabled.
func (r *Instance) ForceDelete() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["forceDelete"])
}

// (Optional; Required if `image_name` is empty and not booting
// from a volume. Do not specify if booting from a volume.) The image ID of
// the desired image for the server. Changing this creates a new server.
func (r *Instance) ImageId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["imageId"])
}

// (Optional; Required if `image_id` is empty and not booting
// from a volume. Do not specify if booting from a volume.) The name of the
// desired image for the server. Changing this creates a new server.
func (r *Instance) ImageName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["imageName"])
}

// The name of a key pair to put on the server. The key
// pair must already be created and associated with the tenant's account.
// Changing this creates a new server.
func (r *Instance) KeyPair() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["keyPair"])
}

// Metadata key/value pairs to make available from
// within the instance. Changing this updates the existing server metadata.
func (r *Instance) Metadata() *pulumi.MapOutput {
	return (*pulumi.MapOutput)(r.s.State["metadata"])
}

// A unique name for the resource.
func (r *Instance) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// An array of one or more networks to attach to the
// instance. The network object structure is documented below. Changing this
// creates a new server.
func (r *Instance) Networks() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["networks"])
}

// Customize the personality of an instance by
// defining one or more files and their contents. The personality structure
// is described below.
func (r *Instance) Personalities() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["personalities"])
}

// Provide the VM state. Only 'active' and 'shutoff'
// are supported values. *Note*: If the initial power_state is the shutoff
// the VM will be stopped immediately after build and the provisioners like
// remote-exec or files are not supported.
func (r *Instance) PowerState() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["powerState"])
}

// The region in which to create the server instance. If
// omitted, the `region` argument of the provider is used. Changing this
// creates a new server.
func (r *Instance) Region() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["region"])
}

// Provide the Nova scheduler with hints on how
// the instance should be launched. The available hints are described below.
func (r *Instance) SchedulerHints() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["schedulerHints"])
}

// An array of one or more security group names
// or ids to associate with the server. Changing this results in adding/removing
// security groups from the existing server. *Note*: When attaching the
// instance to networks using Ports, place the security groups on the Port
// and not the instance.
func (r *Instance) SecurityGroups() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["securityGroups"])
}

// Whether to try stop instance gracefully
// before destroying it, thus giving chance for guest OS daemons to stop correctly.
// If instance doesn't stop within timeout, it will be destroyed anyway.
func (r *Instance) StopBeforeDestroy() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["stopBeforeDestroy"])
}

// The user data to provide when launching the instance.
// Changing this creates a new server.
func (r *Instance) UserData() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["userData"])
}

// Map of additional vendor-specific options.
// Supported options are described below.
func (r *Instance) VendorOptions() *pulumi.Output {
	return r.s.State["vendorOptions"]
}

// Input properties used for looking up and filtering Instance resources.
type InstanceState struct {
	// The first detected Fixed IPv4 address.
	AccessIpV4 interface{}
	// The first detected Fixed IPv6 address.
	AccessIpV6 interface{}
	// The administrative password to assign to the server.
	// Changing this changes the root password on the existing server.
	AdminPass interface{}
	AllMetadata interface{}
	// The availability zone in which to create
	// the server. Changing this creates a new server.
	AvailabilityZone interface{}
	// Configuration of block devices. The block_device
	// structure is documented below. Changing this creates a new server.
	// You can specify multiple block devices which will create an instance with
	// multiple disks. This configuration is very flexible, so please see the
	// following [reference](https://docs.openstack.org/nova/latest/user/block-device-mapping.html)
	// for more information.
	BlockDevices interface{}
	// Whether to use the config_drive feature to
	// configure the instance. Changing this creates a new server.
	ConfigDrive interface{}
	// The flavor ID of
	// the desired flavor for the server. Changing this resizes the existing server.
	FlavorId interface{}
	// The name of the
	// desired flavor for the server. Changing this resizes the existing server.
	FlavorName interface{}
	// Whether to force the OpenStack instance to be
	// forcefully deleted. This is useful for environments that have reclaim / soft
	// deletion enabled.
	ForceDelete interface{}
	// (Optional; Required if `image_name` is empty and not booting
	// from a volume. Do not specify if booting from a volume.) The image ID of
	// the desired image for the server. Changing this creates a new server.
	ImageId interface{}
	// (Optional; Required if `image_id` is empty and not booting
	// from a volume. Do not specify if booting from a volume.) The name of the
	// desired image for the server. Changing this creates a new server.
	ImageName interface{}
	// The name of a key pair to put on the server. The key
	// pair must already be created and associated with the tenant's account.
	// Changing this creates a new server.
	KeyPair interface{}
	// Metadata key/value pairs to make available from
	// within the instance. Changing this updates the existing server metadata.
	Metadata interface{}
	// A unique name for the resource.
	Name interface{}
	// An array of one or more networks to attach to the
	// instance. The network object structure is documented below. Changing this
	// creates a new server.
	Networks interface{}
	// Customize the personality of an instance by
	// defining one or more files and their contents. The personality structure
	// is described below.
	Personalities interface{}
	// Provide the VM state. Only 'active' and 'shutoff'
	// are supported values. *Note*: If the initial power_state is the shutoff
	// the VM will be stopped immediately after build and the provisioners like
	// remote-exec or files are not supported.
	PowerState interface{}
	// The region in which to create the server instance. If
	// omitted, the `region` argument of the provider is used. Changing this
	// creates a new server.
	Region interface{}
	// Provide the Nova scheduler with hints on how
	// the instance should be launched. The available hints are described below.
	SchedulerHints interface{}
	// An array of one or more security group names
	// or ids to associate with the server. Changing this results in adding/removing
	// security groups from the existing server. *Note*: When attaching the
	// instance to networks using Ports, place the security groups on the Port
	// and not the instance.
	SecurityGroups interface{}
	// Whether to try stop instance gracefully
	// before destroying it, thus giving chance for guest OS daemons to stop correctly.
	// If instance doesn't stop within timeout, it will be destroyed anyway.
	StopBeforeDestroy interface{}
	// The user data to provide when launching the instance.
	// Changing this creates a new server.
	UserData interface{}
	// Map of additional vendor-specific options.
	// Supported options are described below.
	VendorOptions interface{}
}

// The set of arguments for constructing a Instance resource.
type InstanceArgs struct {
	// The first detected Fixed IPv4 address.
	AccessIpV4 interface{}
	// The first detected Fixed IPv6 address.
	AccessIpV6 interface{}
	// The administrative password to assign to the server.
	// Changing this changes the root password on the existing server.
	AdminPass interface{}
	// The availability zone in which to create
	// the server. Changing this creates a new server.
	AvailabilityZone interface{}
	// Configuration of block devices. The block_device
	// structure is documented below. Changing this creates a new server.
	// You can specify multiple block devices which will create an instance with
	// multiple disks. This configuration is very flexible, so please see the
	// following [reference](https://docs.openstack.org/nova/latest/user/block-device-mapping.html)
	// for more information.
	BlockDevices interface{}
	// Whether to use the config_drive feature to
	// configure the instance. Changing this creates a new server.
	ConfigDrive interface{}
	// The flavor ID of
	// the desired flavor for the server. Changing this resizes the existing server.
	FlavorId interface{}
	// The name of the
	// desired flavor for the server. Changing this resizes the existing server.
	FlavorName interface{}
	// Whether to force the OpenStack instance to be
	// forcefully deleted. This is useful for environments that have reclaim / soft
	// deletion enabled.
	ForceDelete interface{}
	// (Optional; Required if `image_name` is empty and not booting
	// from a volume. Do not specify if booting from a volume.) The image ID of
	// the desired image for the server. Changing this creates a new server.
	ImageId interface{}
	// (Optional; Required if `image_id` is empty and not booting
	// from a volume. Do not specify if booting from a volume.) The name of the
	// desired image for the server. Changing this creates a new server.
	ImageName interface{}
	// The name of a key pair to put on the server. The key
	// pair must already be created and associated with the tenant's account.
	// Changing this creates a new server.
	KeyPair interface{}
	// Metadata key/value pairs to make available from
	// within the instance. Changing this updates the existing server metadata.
	Metadata interface{}
	// A unique name for the resource.
	Name interface{}
	// An array of one or more networks to attach to the
	// instance. The network object structure is documented below. Changing this
	// creates a new server.
	Networks interface{}
	// Customize the personality of an instance by
	// defining one or more files and their contents. The personality structure
	// is described below.
	Personalities interface{}
	// Provide the VM state. Only 'active' and 'shutoff'
	// are supported values. *Note*: If the initial power_state is the shutoff
	// the VM will be stopped immediately after build and the provisioners like
	// remote-exec or files are not supported.
	PowerState interface{}
	// The region in which to create the server instance. If
	// omitted, the `region` argument of the provider is used. Changing this
	// creates a new server.
	Region interface{}
	// Provide the Nova scheduler with hints on how
	// the instance should be launched. The available hints are described below.
	SchedulerHints interface{}
	// An array of one or more security group names
	// or ids to associate with the server. Changing this results in adding/removing
	// security groups from the existing server. *Note*: When attaching the
	// instance to networks using Ports, place the security groups on the Port
	// and not the instance.
	SecurityGroups interface{}
	// Whether to try stop instance gracefully
	// before destroying it, thus giving chance for guest OS daemons to stop correctly.
	// If instance doesn't stop within timeout, it will be destroyed anyway.
	StopBeforeDestroy interface{}
	// The user data to provide when launching the instance.
	// Changing this creates a new server.
	UserData interface{}
	// Map of additional vendor-specific options.
	// Supported options are described below.
	VendorOptions interface{}
}
