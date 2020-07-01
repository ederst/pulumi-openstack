// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OpenStack.BlockStorage
{
    /// <summary>
    /// This resource is experimental and may be removed in the future! Feedback
    /// is requested if you find this resource useful or if you find any problems
    /// with it.
    /// 
    /// Creates a general purpose attachment connection to a Block
    /// Storage volume using the OpenStack Block Storage (Cinder) v3 API.
    /// Depending on your Block Storage service configuration, this
    /// resource can assist in attaching a volume to a non-OpenStack resource
    /// such as a bare-metal server or a remote virtual machine in a
    /// different cloud provider.
    /// 
    /// This does not actually attach a volume to an instance. Please use
    /// the `openstack.compute.VolumeAttach` resource for that.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using OpenStack = Pulumi.OpenStack;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var volume1 = new OpenStack.BlockStorage.Volume("volume1", new OpenStack.BlockStorage.VolumeArgs
    ///         {
    ///             Size = 1,
    ///         });
    ///         var va1 = new OpenStack.BlockStorage.VolumeAttach("va1", new OpenStack.BlockStorage.VolumeAttachArgs
    ///         {
    ///             Device = "auto",
    ///             HostName = "devstack",
    ///             Initiator = "iqn.1993-08.org.debian:01:e9861fb1859",
    ///             IpAddress = "192.168.255.10",
    ///             OsType = "linux2",
    ///             Platform = "x86_64",
    ///             VolumeId = volume1.Id,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class VolumeAttach : Pulumi.CustomResource
    {
        /// <summary>
        /// Specify whether to attach the volume as Read-Only
        /// (`ro`) or Read-Write (`rw`). Only values of `ro` and `rw` are accepted.
        /// If left unspecified, the Block Storage API will apply a default of `rw`.
        /// </summary>
        [Output("attachMode")]
        public Output<string?> AttachMode { get; private set; } = null!;

        /// <summary>
        /// This is a map of key/value pairs that contain the connection
        /// information. You will want to pass this information to a provisioner
        /// script to finalize the connection. See below for more information.
        /// </summary>
        [Output("data")]
        public Output<ImmutableDictionary<string, object>> Data { get; private set; } = null!;

        /// <summary>
        /// The device to tell the Block Storage service this
        /// volume will be attached as. This is purely for informational purposes.
        /// You can specify `auto` or a device such as `/dev/vdc`.
        /// </summary>
        [Output("device")]
        public Output<string?> Device { get; private set; } = null!;

        /// <summary>
        /// The storage driver that the volume is based on.
        /// </summary>
        [Output("driverVolumeType")]
        public Output<string> DriverVolumeType { get; private set; } = null!;

        /// <summary>
        /// The host to attach the volume to.
        /// </summary>
        [Output("hostName")]
        public Output<string> HostName { get; private set; } = null!;

        /// <summary>
        /// The iSCSI initiator string to make the connection.
        /// </summary>
        [Output("initiator")]
        public Output<string?> Initiator { get; private set; } = null!;

        /// <summary>
        /// The IP address of the `host_name` above.
        /// </summary>
        [Output("ipAddress")]
        public Output<string?> IpAddress { get; private set; } = null!;

        /// <summary>
        /// A mount point base name for shared storage.
        /// </summary>
        [Output("mountPointBase")]
        public Output<string> MountPointBase { get; private set; } = null!;

        /// <summary>
        /// Whether to connect to this volume via multipath.
        /// </summary>
        [Output("multipath")]
        public Output<bool?> Multipath { get; private set; } = null!;

        /// <summary>
        /// The iSCSI initiator OS type.
        /// </summary>
        [Output("osType")]
        public Output<string?> OsType { get; private set; } = null!;

        /// <summary>
        /// The iSCSI initiator platform.
        /// </summary>
        [Output("platform")]
        public Output<string?> Platform { get; private set; } = null!;

        /// <summary>
        /// The region in which to obtain the V3 Block Storage
        /// client. A Block Storage client is needed to create a volume attachment.
        /// If omitted, the `region` argument of the provider is used. Changing this
        /// creates a new volume attachment.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// The ID of the Volume to attach to an Instance.
        /// </summary>
        [Output("volumeId")]
        public Output<string> VolumeId { get; private set; } = null!;

        /// <summary>
        /// A wwnn name. Used for Fibre Channel connections.
        /// </summary>
        [Output("wwnn")]
        public Output<string?> Wwnn { get; private set; } = null!;

        /// <summary>
        /// An array of wwpn strings. Used for Fibre Channel
        /// connections.
        /// </summary>
        [Output("wwpns")]
        public Output<ImmutableArray<string>> Wwpns { get; private set; } = null!;


        /// <summary>
        /// Create a VolumeAttach resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public VolumeAttach(string name, VolumeAttachArgs args, CustomResourceOptions? options = null)
            : base("openstack:blockstorage/volumeAttach:VolumeAttach", name, args ?? new VolumeAttachArgs(), MakeResourceOptions(options, ""))
        {
        }

        private VolumeAttach(string name, Input<string> id, VolumeAttachState? state = null, CustomResourceOptions? options = null)
            : base("openstack:blockstorage/volumeAttach:VolumeAttach", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing VolumeAttach resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static VolumeAttach Get(string name, Input<string> id, VolumeAttachState? state = null, CustomResourceOptions? options = null)
        {
            return new VolumeAttach(name, id, state, options);
        }
    }

    public sealed class VolumeAttachArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specify whether to attach the volume as Read-Only
        /// (`ro`) or Read-Write (`rw`). Only values of `ro` and `rw` are accepted.
        /// If left unspecified, the Block Storage API will apply a default of `rw`.
        /// </summary>
        [Input("attachMode")]
        public Input<string>? AttachMode { get; set; }

        /// <summary>
        /// The device to tell the Block Storage service this
        /// volume will be attached as. This is purely for informational purposes.
        /// You can specify `auto` or a device such as `/dev/vdc`.
        /// </summary>
        [Input("device")]
        public Input<string>? Device { get; set; }

        /// <summary>
        /// The host to attach the volume to.
        /// </summary>
        [Input("hostName", required: true)]
        public Input<string> HostName { get; set; } = null!;

        /// <summary>
        /// The iSCSI initiator string to make the connection.
        /// </summary>
        [Input("initiator")]
        public Input<string>? Initiator { get; set; }

        /// <summary>
        /// The IP address of the `host_name` above.
        /// </summary>
        [Input("ipAddress")]
        public Input<string>? IpAddress { get; set; }

        /// <summary>
        /// Whether to connect to this volume via multipath.
        /// </summary>
        [Input("multipath")]
        public Input<bool>? Multipath { get; set; }

        /// <summary>
        /// The iSCSI initiator OS type.
        /// </summary>
        [Input("osType")]
        public Input<string>? OsType { get; set; }

        /// <summary>
        /// The iSCSI initiator platform.
        /// </summary>
        [Input("platform")]
        public Input<string>? Platform { get; set; }

        /// <summary>
        /// The region in which to obtain the V3 Block Storage
        /// client. A Block Storage client is needed to create a volume attachment.
        /// If omitted, the `region` argument of the provider is used. Changing this
        /// creates a new volume attachment.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The ID of the Volume to attach to an Instance.
        /// </summary>
        [Input("volumeId", required: true)]
        public Input<string> VolumeId { get; set; } = null!;

        /// <summary>
        /// A wwnn name. Used for Fibre Channel connections.
        /// </summary>
        [Input("wwnn")]
        public Input<string>? Wwnn { get; set; }

        [Input("wwpns")]
        private InputList<string>? _wwpns;

        /// <summary>
        /// An array of wwpn strings. Used for Fibre Channel
        /// connections.
        /// </summary>
        public InputList<string> Wwpns
        {
            get => _wwpns ?? (_wwpns = new InputList<string>());
            set => _wwpns = value;
        }

        public VolumeAttachArgs()
        {
        }
    }

    public sealed class VolumeAttachState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Specify whether to attach the volume as Read-Only
        /// (`ro`) or Read-Write (`rw`). Only values of `ro` and `rw` are accepted.
        /// If left unspecified, the Block Storage API will apply a default of `rw`.
        /// </summary>
        [Input("attachMode")]
        public Input<string>? AttachMode { get; set; }

        [Input("data")]
        private InputMap<object>? _data;

        /// <summary>
        /// This is a map of key/value pairs that contain the connection
        /// information. You will want to pass this information to a provisioner
        /// script to finalize the connection. See below for more information.
        /// </summary>
        public InputMap<object> Data
        {
            get => _data ?? (_data = new InputMap<object>());
            set => _data = value;
        }

        /// <summary>
        /// The device to tell the Block Storage service this
        /// volume will be attached as. This is purely for informational purposes.
        /// You can specify `auto` or a device such as `/dev/vdc`.
        /// </summary>
        [Input("device")]
        public Input<string>? Device { get; set; }

        /// <summary>
        /// The storage driver that the volume is based on.
        /// </summary>
        [Input("driverVolumeType")]
        public Input<string>? DriverVolumeType { get; set; }

        /// <summary>
        /// The host to attach the volume to.
        /// </summary>
        [Input("hostName")]
        public Input<string>? HostName { get; set; }

        /// <summary>
        /// The iSCSI initiator string to make the connection.
        /// </summary>
        [Input("initiator")]
        public Input<string>? Initiator { get; set; }

        /// <summary>
        /// The IP address of the `host_name` above.
        /// </summary>
        [Input("ipAddress")]
        public Input<string>? IpAddress { get; set; }

        /// <summary>
        /// A mount point base name for shared storage.
        /// </summary>
        [Input("mountPointBase")]
        public Input<string>? MountPointBase { get; set; }

        /// <summary>
        /// Whether to connect to this volume via multipath.
        /// </summary>
        [Input("multipath")]
        public Input<bool>? Multipath { get; set; }

        /// <summary>
        /// The iSCSI initiator OS type.
        /// </summary>
        [Input("osType")]
        public Input<string>? OsType { get; set; }

        /// <summary>
        /// The iSCSI initiator platform.
        /// </summary>
        [Input("platform")]
        public Input<string>? Platform { get; set; }

        /// <summary>
        /// The region in which to obtain the V3 Block Storage
        /// client. A Block Storage client is needed to create a volume attachment.
        /// If omitted, the `region` argument of the provider is used. Changing this
        /// creates a new volume attachment.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The ID of the Volume to attach to an Instance.
        /// </summary>
        [Input("volumeId")]
        public Input<string>? VolumeId { get; set; }

        /// <summary>
        /// A wwnn name. Used for Fibre Channel connections.
        /// </summary>
        [Input("wwnn")]
        public Input<string>? Wwnn { get; set; }

        [Input("wwpns")]
        private InputList<string>? _wwpns;

        /// <summary>
        /// An array of wwpn strings. Used for Fibre Channel
        /// connections.
        /// </summary>
        public InputList<string> Wwpns
        {
            get => _wwpns ?? (_wwpns = new InputList<string>());
            set => _wwpns = value;
        }

        public VolumeAttachState()
        {
        }
    }
}
