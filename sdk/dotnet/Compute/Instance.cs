// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OpenStack.Compute
{
    /// <summary>
    /// Manages a V2 VM instance resource within OpenStack.
    /// 
    /// 
    /// ## Importing instances
    /// 
    /// Importing instances can be tricky, since the nova api does not offer all
    /// information provided at creation time for later retrieval.
    /// Network interface attachment order, and number and sizes of ephemeral
    /// disks are examples of this.
    /// 
    /// ### Importing an instance with multiple emphemeral disks
    /// 
    /// The importer cannot read the emphemeral disk configuration
    /// of an instance, so just specify image_id as in the configuration
    /// of the basic instance example.
    /// </summary>
    public partial class Instance : Pulumi.CustomResource
    {
        /// <summary>
        /// The first detected Fixed IPv4 address.
        /// </summary>
        [Output("accessIpV4")]
        public Output<string> AccessIpV4 { get; private set; } = null!;

        /// <summary>
        /// The first detected Fixed IPv6 address.
        /// </summary>
        [Output("accessIpV6")]
        public Output<string> AccessIpV6 { get; private set; } = null!;

        /// <summary>
        /// The administrative password to assign to the server.
        /// Changing this changes the root password on the existing server.
        /// </summary>
        [Output("adminPass")]
        public Output<string?> AdminPass { get; private set; } = null!;

        [Output("allMetadata")]
        public Output<ImmutableDictionary<string, object>> AllMetadata { get; private set; } = null!;

        /// <summary>
        /// The collection of tags assigned on the instance, which have
        /// been explicitly and implicitly added.
        /// </summary>
        [Output("allTags")]
        public Output<ImmutableArray<string>> AllTags { get; private set; } = null!;

        /// <summary>
        /// The availability zone in which to create
        /// the server. Conflicts with `availability_zone_hints`. Changing this creates
        /// a new server.
        /// </summary>
        [Output("availabilityZone")]
        public Output<string> AvailabilityZone { get; private set; } = null!;

        /// <summary>
        /// The availability zone in which to
        /// create the server. This argument is preferred to `availability_zone`, when
        /// scheduling the server on a
        /// [particular](https://docs.openstack.org/nova/latest/admin/availability-zones.html)
        /// host or node. Conflicts with `availability_zone`. Changing this creates a
        /// new server.
        /// </summary>
        [Output("availabilityZoneHints")]
        public Output<string?> AvailabilityZoneHints { get; private set; } = null!;

        /// <summary>
        /// Configuration of block devices. The block_device
        /// structure is documented below. Changing this creates a new server.
        /// You can specify multiple block devices which will create an instance with
        /// multiple disks. This configuration is very flexible, so please see the
        /// following [reference](https://docs.openstack.org/nova/latest/user/block-device-mapping.html)
        /// for more information.
        /// </summary>
        [Output("blockDevices")]
        public Output<ImmutableArray<Outputs.InstanceBlockDevice>> BlockDevices { get; private set; } = null!;

        /// <summary>
        /// Whether to use the config_drive feature to
        /// configure the instance. Changing this creates a new server.
        /// </summary>
        [Output("configDrive")]
        public Output<bool?> ConfigDrive { get; private set; } = null!;

        /// <summary>
        /// The flavor ID of
        /// the desired flavor for the server. Changing this resizes the existing server.
        /// </summary>
        [Output("flavorId")]
        public Output<string> FlavorId { get; private set; } = null!;

        /// <summary>
        /// The name of the
        /// desired flavor for the server. Changing this resizes the existing server.
        /// </summary>
        [Output("flavorName")]
        public Output<string> FlavorName { get; private set; } = null!;

        /// <summary>
        /// Whether to force the OpenStack instance to be
        /// forcefully deleted. This is useful for environments that have reclaim / soft
        /// deletion enabled.
        /// </summary>
        [Output("forceDelete")]
        public Output<bool?> ForceDelete { get; private set; } = null!;

        /// <summary>
        /// (Optional; Required if `image_name` is empty and not booting
        /// from a volume. Do not specify if booting from a volume.) The image ID of
        /// the desired image for the server. Changing this creates a new server.
        /// </summary>
        [Output("imageId")]
        public Output<string> ImageId { get; private set; } = null!;

        /// <summary>
        /// (Optional; Required if `image_id` is empty and not booting
        /// from a volume. Do not specify if booting from a volume.) The name of the
        /// desired image for the server. Changing this creates a new server.
        /// </summary>
        [Output("imageName")]
        public Output<string> ImageName { get; private set; } = null!;

        /// <summary>
        /// The name of a key pair to put on the server. The key
        /// pair must already be created and associated with the tenant's account.
        /// Changing this creates a new server.
        /// </summary>
        [Output("keyPair")]
        public Output<string?> KeyPair { get; private set; } = null!;

        /// <summary>
        /// Metadata key/value pairs to make available from
        /// within the instance. Changing this updates the existing server metadata.
        /// </summary>
        [Output("metadata")]
        public Output<ImmutableDictionary<string, object>?> Metadata { get; private set; } = null!;

        /// <summary>
        /// The human-readable
        /// name of the network. Changing this creates a new server.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// An array of one or more networks to attach to the
        /// instance. The network object structure is documented below. Changing this
        /// creates a new server.
        /// </summary>
        [Output("networks")]
        public Output<ImmutableArray<Outputs.InstanceNetwork>> Networks { get; private set; } = null!;

        /// <summary>
        /// Customize the personality of an instance by
        /// defining one or more files and their contents. The personality structure
        /// is described below.
        /// </summary>
        [Output("personalities")]
        public Output<ImmutableArray<Outputs.InstancePersonality>> Personalities { get; private set; } = null!;

        /// <summary>
        /// Provide the VM state. Only 'active' and 'shutoff'
        /// are supported values. *Note*: If the initial power_state is the shutoff
        /// the VM will be stopped immediately after build and the provisioners like
        /// remote-exec or files are not supported.
        /// </summary>
        [Output("powerState")]
        public Output<string?> PowerState { get; private set; } = null!;

        /// <summary>
        /// The region in which to create the server instance. If
        /// omitted, the `region` argument of the provider is used. Changing this
        /// creates a new server.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// Provide the Nova scheduler with hints on how
        /// the instance should be launched. The available hints are described below.
        /// </summary>
        [Output("schedulerHints")]
        public Output<ImmutableArray<Outputs.InstanceSchedulerHint>> SchedulerHints { get; private set; } = null!;

        /// <summary>
        /// An array of one or more security group names
        /// or ids to associate with the server. Changing this results in adding/removing
        /// security groups from the existing server. *Note*: When attaching the
        /// instance to networks using Ports, place the security groups on the Port
        /// and not the instance.
        /// </summary>
        [Output("securityGroups")]
        public Output<ImmutableArray<string>> SecurityGroups { get; private set; } = null!;

        /// <summary>
        /// Whether to try stop instance gracefully
        /// before destroying it, thus giving chance for guest OS daemons to stop correctly.
        /// If instance doesn't stop within timeout, it will be destroyed anyway.
        /// </summary>
        [Output("stopBeforeDestroy")]
        public Output<bool?> StopBeforeDestroy { get; private set; } = null!;

        /// <summary>
        /// A set of string tags for the instance. Changing this
        /// updates the existing instance tags.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<string>> Tags { get; private set; } = null!;

        /// <summary>
        /// The user data to provide when launching the instance.
        /// Changing this creates a new server.
        /// </summary>
        [Output("userData")]
        public Output<string?> UserData { get; private set; } = null!;

        /// <summary>
        /// Map of additional vendor-specific options.
        /// Supported options are described below.
        /// </summary>
        [Output("vendorOptions")]
        public Output<Outputs.InstanceVendorOptions?> VendorOptions { get; private set; } = null!;


        /// <summary>
        /// Create a Instance resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Instance(string name, InstanceArgs? args = null, CustomResourceOptions? options = null)
            : base("openstack:compute/instance:Instance", name, args ?? new InstanceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Instance(string name, Input<string> id, InstanceState? state = null, CustomResourceOptions? options = null)
            : base("openstack:compute/instance:Instance", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Instance resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Instance Get(string name, Input<string> id, InstanceState? state = null, CustomResourceOptions? options = null)
        {
            return new Instance(name, id, state, options);
        }
    }

    public sealed class InstanceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The first detected Fixed IPv4 address.
        /// </summary>
        [Input("accessIpV4")]
        public Input<string>? AccessIpV4 { get; set; }

        /// <summary>
        /// The first detected Fixed IPv6 address.
        /// </summary>
        [Input("accessIpV6")]
        public Input<string>? AccessIpV6 { get; set; }

        /// <summary>
        /// The administrative password to assign to the server.
        /// Changing this changes the root password on the existing server.
        /// </summary>
        [Input("adminPass")]
        public Input<string>? AdminPass { get; set; }

        /// <summary>
        /// The availability zone in which to create
        /// the server. Conflicts with `availability_zone_hints`. Changing this creates
        /// a new server.
        /// </summary>
        [Input("availabilityZone")]
        public Input<string>? AvailabilityZone { get; set; }

        /// <summary>
        /// The availability zone in which to
        /// create the server. This argument is preferred to `availability_zone`, when
        /// scheduling the server on a
        /// [particular](https://docs.openstack.org/nova/latest/admin/availability-zones.html)
        /// host or node. Conflicts with `availability_zone`. Changing this creates a
        /// new server.
        /// </summary>
        [Input("availabilityZoneHints")]
        public Input<string>? AvailabilityZoneHints { get; set; }

        [Input("blockDevices")]
        private InputList<Inputs.InstanceBlockDeviceArgs>? _blockDevices;

        /// <summary>
        /// Configuration of block devices. The block_device
        /// structure is documented below. Changing this creates a new server.
        /// You can specify multiple block devices which will create an instance with
        /// multiple disks. This configuration is very flexible, so please see the
        /// following [reference](https://docs.openstack.org/nova/latest/user/block-device-mapping.html)
        /// for more information.
        /// </summary>
        public InputList<Inputs.InstanceBlockDeviceArgs> BlockDevices
        {
            get => _blockDevices ?? (_blockDevices = new InputList<Inputs.InstanceBlockDeviceArgs>());
            set => _blockDevices = value;
        }

        /// <summary>
        /// Whether to use the config_drive feature to
        /// configure the instance. Changing this creates a new server.
        /// </summary>
        [Input("configDrive")]
        public Input<bool>? ConfigDrive { get; set; }

        /// <summary>
        /// The flavor ID of
        /// the desired flavor for the server. Changing this resizes the existing server.
        /// </summary>
        [Input("flavorId")]
        public Input<string>? FlavorId { get; set; }

        /// <summary>
        /// The name of the
        /// desired flavor for the server. Changing this resizes the existing server.
        /// </summary>
        [Input("flavorName")]
        public Input<string>? FlavorName { get; set; }

        /// <summary>
        /// Whether to force the OpenStack instance to be
        /// forcefully deleted. This is useful for environments that have reclaim / soft
        /// deletion enabled.
        /// </summary>
        [Input("forceDelete")]
        public Input<bool>? ForceDelete { get; set; }

        /// <summary>
        /// (Optional; Required if `image_name` is empty and not booting
        /// from a volume. Do not specify if booting from a volume.) The image ID of
        /// the desired image for the server. Changing this creates a new server.
        /// </summary>
        [Input("imageId")]
        public Input<string>? ImageId { get; set; }

        /// <summary>
        /// (Optional; Required if `image_id` is empty and not booting
        /// from a volume. Do not specify if booting from a volume.) The name of the
        /// desired image for the server. Changing this creates a new server.
        /// </summary>
        [Input("imageName")]
        public Input<string>? ImageName { get; set; }

        /// <summary>
        /// The name of a key pair to put on the server. The key
        /// pair must already be created and associated with the tenant's account.
        /// Changing this creates a new server.
        /// </summary>
        [Input("keyPair")]
        public Input<string>? KeyPair { get; set; }

        [Input("metadata")]
        private InputMap<object>? _metadata;

        /// <summary>
        /// Metadata key/value pairs to make available from
        /// within the instance. Changing this updates the existing server metadata.
        /// </summary>
        public InputMap<object> Metadata
        {
            get => _metadata ?? (_metadata = new InputMap<object>());
            set => _metadata = value;
        }

        /// <summary>
        /// The human-readable
        /// name of the network. Changing this creates a new server.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("networks")]
        private InputList<Inputs.InstanceNetworkArgs>? _networks;

        /// <summary>
        /// An array of one or more networks to attach to the
        /// instance. The network object structure is documented below. Changing this
        /// creates a new server.
        /// </summary>
        public InputList<Inputs.InstanceNetworkArgs> Networks
        {
            get => _networks ?? (_networks = new InputList<Inputs.InstanceNetworkArgs>());
            set => _networks = value;
        }

        [Input("personalities")]
        private InputList<Inputs.InstancePersonalityArgs>? _personalities;

        /// <summary>
        /// Customize the personality of an instance by
        /// defining one or more files and their contents. The personality structure
        /// is described below.
        /// </summary>
        public InputList<Inputs.InstancePersonalityArgs> Personalities
        {
            get => _personalities ?? (_personalities = new InputList<Inputs.InstancePersonalityArgs>());
            set => _personalities = value;
        }

        /// <summary>
        /// Provide the VM state. Only 'active' and 'shutoff'
        /// are supported values. *Note*: If the initial power_state is the shutoff
        /// the VM will be stopped immediately after build and the provisioners like
        /// remote-exec or files are not supported.
        /// </summary>
        [Input("powerState")]
        public Input<string>? PowerState { get; set; }

        /// <summary>
        /// The region in which to create the server instance. If
        /// omitted, the `region` argument of the provider is used. Changing this
        /// creates a new server.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("schedulerHints")]
        private InputList<Inputs.InstanceSchedulerHintArgs>? _schedulerHints;

        /// <summary>
        /// Provide the Nova scheduler with hints on how
        /// the instance should be launched. The available hints are described below.
        /// </summary>
        public InputList<Inputs.InstanceSchedulerHintArgs> SchedulerHints
        {
            get => _schedulerHints ?? (_schedulerHints = new InputList<Inputs.InstanceSchedulerHintArgs>());
            set => _schedulerHints = value;
        }

        [Input("securityGroups")]
        private InputList<string>? _securityGroups;

        /// <summary>
        /// An array of one or more security group names
        /// or ids to associate with the server. Changing this results in adding/removing
        /// security groups from the existing server. *Note*: When attaching the
        /// instance to networks using Ports, place the security groups on the Port
        /// and not the instance.
        /// </summary>
        public InputList<string> SecurityGroups
        {
            get => _securityGroups ?? (_securityGroups = new InputList<string>());
            set => _securityGroups = value;
        }

        /// <summary>
        /// Whether to try stop instance gracefully
        /// before destroying it, thus giving chance for guest OS daemons to stop correctly.
        /// If instance doesn't stop within timeout, it will be destroyed anyway.
        /// </summary>
        [Input("stopBeforeDestroy")]
        public Input<bool>? StopBeforeDestroy { get; set; }

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// A set of string tags for the instance. Changing this
        /// updates the existing instance tags.
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The user data to provide when launching the instance.
        /// Changing this creates a new server.
        /// </summary>
        [Input("userData")]
        public Input<string>? UserData { get; set; }

        /// <summary>
        /// Map of additional vendor-specific options.
        /// Supported options are described below.
        /// </summary>
        [Input("vendorOptions")]
        public Input<Inputs.InstanceVendorOptionsArgs>? VendorOptions { get; set; }

        public InstanceArgs()
        {
        }
    }

    public sealed class InstanceState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The first detected Fixed IPv4 address.
        /// </summary>
        [Input("accessIpV4")]
        public Input<string>? AccessIpV4 { get; set; }

        /// <summary>
        /// The first detected Fixed IPv6 address.
        /// </summary>
        [Input("accessIpV6")]
        public Input<string>? AccessIpV6 { get; set; }

        /// <summary>
        /// The administrative password to assign to the server.
        /// Changing this changes the root password on the existing server.
        /// </summary>
        [Input("adminPass")]
        public Input<string>? AdminPass { get; set; }

        [Input("allMetadata")]
        private InputMap<object>? _allMetadata;
        public InputMap<object> AllMetadata
        {
            get => _allMetadata ?? (_allMetadata = new InputMap<object>());
            set => _allMetadata = value;
        }

        [Input("allTags")]
        private InputList<string>? _allTags;

        /// <summary>
        /// The collection of tags assigned on the instance, which have
        /// been explicitly and implicitly added.
        /// </summary>
        public InputList<string> AllTags
        {
            get => _allTags ?? (_allTags = new InputList<string>());
            set => _allTags = value;
        }

        /// <summary>
        /// The availability zone in which to create
        /// the server. Conflicts with `availability_zone_hints`. Changing this creates
        /// a new server.
        /// </summary>
        [Input("availabilityZone")]
        public Input<string>? AvailabilityZone { get; set; }

        /// <summary>
        /// The availability zone in which to
        /// create the server. This argument is preferred to `availability_zone`, when
        /// scheduling the server on a
        /// [particular](https://docs.openstack.org/nova/latest/admin/availability-zones.html)
        /// host or node. Conflicts with `availability_zone`. Changing this creates a
        /// new server.
        /// </summary>
        [Input("availabilityZoneHints")]
        public Input<string>? AvailabilityZoneHints { get; set; }

        [Input("blockDevices")]
        private InputList<Inputs.InstanceBlockDeviceGetArgs>? _blockDevices;

        /// <summary>
        /// Configuration of block devices. The block_device
        /// structure is documented below. Changing this creates a new server.
        /// You can specify multiple block devices which will create an instance with
        /// multiple disks. This configuration is very flexible, so please see the
        /// following [reference](https://docs.openstack.org/nova/latest/user/block-device-mapping.html)
        /// for more information.
        /// </summary>
        public InputList<Inputs.InstanceBlockDeviceGetArgs> BlockDevices
        {
            get => _blockDevices ?? (_blockDevices = new InputList<Inputs.InstanceBlockDeviceGetArgs>());
            set => _blockDevices = value;
        }

        /// <summary>
        /// Whether to use the config_drive feature to
        /// configure the instance. Changing this creates a new server.
        /// </summary>
        [Input("configDrive")]
        public Input<bool>? ConfigDrive { get; set; }

        /// <summary>
        /// The flavor ID of
        /// the desired flavor for the server. Changing this resizes the existing server.
        /// </summary>
        [Input("flavorId")]
        public Input<string>? FlavorId { get; set; }

        /// <summary>
        /// The name of the
        /// desired flavor for the server. Changing this resizes the existing server.
        /// </summary>
        [Input("flavorName")]
        public Input<string>? FlavorName { get; set; }

        /// <summary>
        /// Whether to force the OpenStack instance to be
        /// forcefully deleted. This is useful for environments that have reclaim / soft
        /// deletion enabled.
        /// </summary>
        [Input("forceDelete")]
        public Input<bool>? ForceDelete { get; set; }

        /// <summary>
        /// (Optional; Required if `image_name` is empty and not booting
        /// from a volume. Do not specify if booting from a volume.) The image ID of
        /// the desired image for the server. Changing this creates a new server.
        /// </summary>
        [Input("imageId")]
        public Input<string>? ImageId { get; set; }

        /// <summary>
        /// (Optional; Required if `image_id` is empty and not booting
        /// from a volume. Do not specify if booting from a volume.) The name of the
        /// desired image for the server. Changing this creates a new server.
        /// </summary>
        [Input("imageName")]
        public Input<string>? ImageName { get; set; }

        /// <summary>
        /// The name of a key pair to put on the server. The key
        /// pair must already be created and associated with the tenant's account.
        /// Changing this creates a new server.
        /// </summary>
        [Input("keyPair")]
        public Input<string>? KeyPair { get; set; }

        [Input("metadata")]
        private InputMap<object>? _metadata;

        /// <summary>
        /// Metadata key/value pairs to make available from
        /// within the instance. Changing this updates the existing server metadata.
        /// </summary>
        public InputMap<object> Metadata
        {
            get => _metadata ?? (_metadata = new InputMap<object>());
            set => _metadata = value;
        }

        /// <summary>
        /// The human-readable
        /// name of the network. Changing this creates a new server.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("networks")]
        private InputList<Inputs.InstanceNetworkGetArgs>? _networks;

        /// <summary>
        /// An array of one or more networks to attach to the
        /// instance. The network object structure is documented below. Changing this
        /// creates a new server.
        /// </summary>
        public InputList<Inputs.InstanceNetworkGetArgs> Networks
        {
            get => _networks ?? (_networks = new InputList<Inputs.InstanceNetworkGetArgs>());
            set => _networks = value;
        }

        [Input("personalities")]
        private InputList<Inputs.InstancePersonalityGetArgs>? _personalities;

        /// <summary>
        /// Customize the personality of an instance by
        /// defining one or more files and their contents. The personality structure
        /// is described below.
        /// </summary>
        public InputList<Inputs.InstancePersonalityGetArgs> Personalities
        {
            get => _personalities ?? (_personalities = new InputList<Inputs.InstancePersonalityGetArgs>());
            set => _personalities = value;
        }

        /// <summary>
        /// Provide the VM state. Only 'active' and 'shutoff'
        /// are supported values. *Note*: If the initial power_state is the shutoff
        /// the VM will be stopped immediately after build and the provisioners like
        /// remote-exec or files are not supported.
        /// </summary>
        [Input("powerState")]
        public Input<string>? PowerState { get; set; }

        /// <summary>
        /// The region in which to create the server instance. If
        /// omitted, the `region` argument of the provider is used. Changing this
        /// creates a new server.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("schedulerHints")]
        private InputList<Inputs.InstanceSchedulerHintGetArgs>? _schedulerHints;

        /// <summary>
        /// Provide the Nova scheduler with hints on how
        /// the instance should be launched. The available hints are described below.
        /// </summary>
        public InputList<Inputs.InstanceSchedulerHintGetArgs> SchedulerHints
        {
            get => _schedulerHints ?? (_schedulerHints = new InputList<Inputs.InstanceSchedulerHintGetArgs>());
            set => _schedulerHints = value;
        }

        [Input("securityGroups")]
        private InputList<string>? _securityGroups;

        /// <summary>
        /// An array of one or more security group names
        /// or ids to associate with the server. Changing this results in adding/removing
        /// security groups from the existing server. *Note*: When attaching the
        /// instance to networks using Ports, place the security groups on the Port
        /// and not the instance.
        /// </summary>
        public InputList<string> SecurityGroups
        {
            get => _securityGroups ?? (_securityGroups = new InputList<string>());
            set => _securityGroups = value;
        }

        /// <summary>
        /// Whether to try stop instance gracefully
        /// before destroying it, thus giving chance for guest OS daemons to stop correctly.
        /// If instance doesn't stop within timeout, it will be destroyed anyway.
        /// </summary>
        [Input("stopBeforeDestroy")]
        public Input<bool>? StopBeforeDestroy { get; set; }

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// A set of string tags for the instance. Changing this
        /// updates the existing instance tags.
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The user data to provide when launching the instance.
        /// Changing this creates a new server.
        /// </summary>
        [Input("userData")]
        public Input<string>? UserData { get; set; }

        /// <summary>
        /// Map of additional vendor-specific options.
        /// Supported options are described below.
        /// </summary>
        [Input("vendorOptions")]
        public Input<Inputs.InstanceVendorOptionsGetArgs>? VendorOptions { get; set; }

        public InstanceState()
        {
        }
    }
}
