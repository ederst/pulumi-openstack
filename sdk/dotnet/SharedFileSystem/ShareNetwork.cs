// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OpenStack.SharedFileSystem
{
    /// <summary>
    /// Use this resource to configure a share network.
    /// 
    /// A share network stores network information that share servers can use when
    /// shares are created.
    /// 
    /// ## Example Usage
    /// ### Basic share network
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using OpenStack = Pulumi.OpenStack;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var network1 = new OpenStack.Networking.Network("network1", new OpenStack.Networking.NetworkArgs
    ///         {
    ///             AdminStateUp = true,
    ///         });
    ///         var subnet1 = new OpenStack.Networking.Subnet("subnet1", new OpenStack.Networking.SubnetArgs
    ///         {
    ///             Cidr = "192.168.199.0/24",
    ///             IpVersion = 4,
    ///             NetworkId = network1.Id,
    ///         });
    ///         var sharenetwork1 = new OpenStack.SharedFileSystem.ShareNetwork("sharenetwork1", new OpenStack.SharedFileSystem.ShareNetworkArgs
    ///         {
    ///             Description = "test share network",
    ///             NeutronNetId = network1.Id,
    ///             NeutronSubnetId = subnet1.Id,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// ### Share network with associated security services
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using OpenStack = Pulumi.OpenStack;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var network1 = new OpenStack.Networking.Network("network1", new OpenStack.Networking.NetworkArgs
    ///         {
    ///             AdminStateUp = true,
    ///         });
    ///         var subnet1 = new OpenStack.Networking.Subnet("subnet1", new OpenStack.Networking.SubnetArgs
    ///         {
    ///             Cidr = "192.168.199.0/24",
    ///             IpVersion = 4,
    ///             NetworkId = network1.Id,
    ///         });
    ///         var securityservice1 = new OpenStack.SharedFileSystem.SecurityService("securityservice1", new OpenStack.SharedFileSystem.SecurityServiceArgs
    ///         {
    ///             Description = "created by terraform",
    ///             DnsIp = "192.168.199.10",
    ///             Domain = "example.com",
    ///             Ou = "CN=Computers,DC=example,DC=com",
    ///             Password = "s8cret",
    ///             Server = "192.168.199.10",
    ///             Type = "active_directory",
    ///             User = "joinDomainUser",
    ///         });
    ///         var sharenetwork1 = new OpenStack.SharedFileSystem.ShareNetwork("sharenetwork1", new OpenStack.SharedFileSystem.ShareNetworkArgs
    ///         {
    ///             Description = "test share network with security services",
    ///             NeutronNetId = network1.Id,
    ///             NeutronSubnetId = subnet1.Id,
    ///             SecurityServiceIds = 
    ///             {
    ///                 securityservice1.Id,
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// This resource can be imported by specifying the ID of the share network
    /// 
    /// ```sh
    ///  $ pulumi import openstack:sharedfilesystem/shareNetwork:ShareNetwork sharenetwork_1 &lt;id&gt;
    /// ```
    /// </summary>
    public partial class ShareNetwork : Pulumi.CustomResource
    {
        /// <summary>
        /// The share network CIDR.
        /// </summary>
        [Output("cidr")]
        public Output<string> Cidr { get; private set; } = null!;

        /// <summary>
        /// The human-readable description for the share network.
        /// Changing this updates the description of the existing share network.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The IP version of the share network. Can either be 4 or 6.
        /// </summary>
        [Output("ipVersion")]
        public Output<int> IpVersion { get; private set; } = null!;

        /// <summary>
        /// The name for the share network. Changing this updates the name
        /// of the existing share network.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The share network type. Can either be VLAN, VXLAN, GRE, or flat.
        /// </summary>
        [Output("networkType")]
        public Output<string> NetworkType { get; private set; } = null!;

        /// <summary>
        /// The UUID of a neutron network when setting up or updating
        /// a share network. Changing this updates the existing share network if it's not used by
        /// shares.
        /// </summary>
        [Output("neutronNetId")]
        public Output<string> NeutronNetId { get; private set; } = null!;

        /// <summary>
        /// The UUID of the neutron subnet when setting up or
        /// updating a share network. Changing this updates the existing share network if it's
        /// not used by shares.
        /// </summary>
        [Output("neutronSubnetId")]
        public Output<string> NeutronSubnetId { get; private set; } = null!;

        /// <summary>
        /// The owner of the Share Network.
        /// </summary>
        [Output("projectId")]
        public Output<string> ProjectId { get; private set; } = null!;

        /// <summary>
        /// The region in which to obtain the V2 Shared File System client.
        /// A Shared File System client is needed to create a share network. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// share network.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// The list of security service IDs to associate with
        /// the share network. The security service must be specified by ID and not name.
        /// </summary>
        [Output("securityServiceIds")]
        public Output<ImmutableArray<string>> SecurityServiceIds { get; private set; } = null!;

        /// <summary>
        /// The share network segmentation ID.
        /// </summary>
        [Output("segmentationId")]
        public Output<int> SegmentationId { get; private set; } = null!;


        /// <summary>
        /// Create a ShareNetwork resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ShareNetwork(string name, ShareNetworkArgs args, CustomResourceOptions? options = null)
            : base("openstack:sharedfilesystem/shareNetwork:ShareNetwork", name, args ?? new ShareNetworkArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ShareNetwork(string name, Input<string> id, ShareNetworkState? state = null, CustomResourceOptions? options = null)
            : base("openstack:sharedfilesystem/shareNetwork:ShareNetwork", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ShareNetwork resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ShareNetwork Get(string name, Input<string> id, ShareNetworkState? state = null, CustomResourceOptions? options = null)
        {
            return new ShareNetwork(name, id, state, options);
        }
    }

    public sealed class ShareNetworkArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The human-readable description for the share network.
        /// Changing this updates the description of the existing share network.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name for the share network. Changing this updates the name
        /// of the existing share network.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The UUID of a neutron network when setting up or updating
        /// a share network. Changing this updates the existing share network if it's not used by
        /// shares.
        /// </summary>
        [Input("neutronNetId", required: true)]
        public Input<string> NeutronNetId { get; set; } = null!;

        /// <summary>
        /// The UUID of the neutron subnet when setting up or
        /// updating a share network. Changing this updates the existing share network if it's
        /// not used by shares.
        /// </summary>
        [Input("neutronSubnetId", required: true)]
        public Input<string> NeutronSubnetId { get; set; } = null!;

        /// <summary>
        /// The region in which to obtain the V2 Shared File System client.
        /// A Shared File System client is needed to create a share network. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// share network.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("securityServiceIds")]
        private InputList<string>? _securityServiceIds;

        /// <summary>
        /// The list of security service IDs to associate with
        /// the share network. The security service must be specified by ID and not name.
        /// </summary>
        public InputList<string> SecurityServiceIds
        {
            get => _securityServiceIds ?? (_securityServiceIds = new InputList<string>());
            set => _securityServiceIds = value;
        }

        public ShareNetworkArgs()
        {
        }
    }

    public sealed class ShareNetworkState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The share network CIDR.
        /// </summary>
        [Input("cidr")]
        public Input<string>? Cidr { get; set; }

        /// <summary>
        /// The human-readable description for the share network.
        /// Changing this updates the description of the existing share network.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The IP version of the share network. Can either be 4 or 6.
        /// </summary>
        [Input("ipVersion")]
        public Input<int>? IpVersion { get; set; }

        /// <summary>
        /// The name for the share network. Changing this updates the name
        /// of the existing share network.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The share network type. Can either be VLAN, VXLAN, GRE, or flat.
        /// </summary>
        [Input("networkType")]
        public Input<string>? NetworkType { get; set; }

        /// <summary>
        /// The UUID of a neutron network when setting up or updating
        /// a share network. Changing this updates the existing share network if it's not used by
        /// shares.
        /// </summary>
        [Input("neutronNetId")]
        public Input<string>? NeutronNetId { get; set; }

        /// <summary>
        /// The UUID of the neutron subnet when setting up or
        /// updating a share network. Changing this updates the existing share network if it's
        /// not used by shares.
        /// </summary>
        [Input("neutronSubnetId")]
        public Input<string>? NeutronSubnetId { get; set; }

        /// <summary>
        /// The owner of the Share Network.
        /// </summary>
        [Input("projectId")]
        public Input<string>? ProjectId { get; set; }

        /// <summary>
        /// The region in which to obtain the V2 Shared File System client.
        /// A Shared File System client is needed to create a share network. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// share network.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("securityServiceIds")]
        private InputList<string>? _securityServiceIds;

        /// <summary>
        /// The list of security service IDs to associate with
        /// the share network. The security service must be specified by ID and not name.
        /// </summary>
        public InputList<string> SecurityServiceIds
        {
            get => _securityServiceIds ?? (_securityServiceIds = new InputList<string>());
            set => _securityServiceIds = value;
        }

        /// <summary>
        /// The share network segmentation ID.
        /// </summary>
        [Input("segmentationId")]
        public Input<int>? SegmentationId { get; set; }

        public ShareNetworkState()
        {
        }
    }
}
