// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Openstack.Networking
{
    public static partial class Invokes
    {
        /// <summary>
        /// Use this data source to get the ID of an available OpenStack network.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/networking_network_v2.html.markdown.
        /// </summary>
        public static Task<GetNetworkResult> GetNetwork(GetNetworkArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetNetworkResult>("openstack:networking/getNetwork:getNetwork", args, options.WithVersion());
    }

    public sealed class GetNetworkArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Human-readable description of the network.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The external routing facility of the network.
        /// </summary>
        [Input("external")]
        public Input<bool>? External { get; set; }

        /// <summary>
        /// The CIDR of a subnet within the network.
        /// </summary>
        [Input("matchingSubnetCidr")]
        public Input<string>? MatchingSubnetCidr { get; set; }

        /// <summary>
        /// The network MTU to filter. Available, when Neutron `net-mtu`
        /// extension is enabled.
        /// </summary>
        [Input("mtu")]
        public Input<int>? Mtu { get; set; }

        /// <summary>
        /// The name of the network.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the network.
        /// </summary>
        [Input("networkId")]
        public Input<string>? NetworkId { get; set; }

        /// <summary>
        /// The region in which to obtain the V2 Neutron client.
        /// A Neutron client is needed to retrieve networks ids. If omitted, the
        /// `region` argument of the provider is used.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The status of the network.
        /// </summary>
        [Input("status")]
        public Input<string>? Status { get; set; }

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// The list of network tags to filter.
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The owner of the network.
        /// </summary>
        [Input("tenantId")]
        public Input<string>? TenantId { get; set; }

        /// <summary>
        /// The VLAN transparent attribute for the
        /// network.
        /// </summary>
        [Input("transparentVlan")]
        public Input<bool>? TransparentVlan { get; set; }

        public GetNetworkArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetNetworkResult
    {
        /// <summary>
        /// The administrative state of the network.
        /// </summary>
        public readonly string AdminStateUp;
        /// <summary>
        /// The set of string tags applied on the network.
        /// </summary>
        public readonly ImmutableArray<string> AllTags;
        /// <summary>
        /// The availability zone candidates for the network.
        /// </summary>
        public readonly ImmutableArray<string> AvailabilityZoneHints;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// The network DNS domain. Available, when Neutron DNS extension
        /// is enabled
        /// </summary>
        public readonly string DnsDomain;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly bool? External;
        public readonly string? MatchingSubnetCidr;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly int? Mtu;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string? Name;
        public readonly string? NetworkId;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string Region;
        /// <summary>
        /// Specifies whether the network resource can be accessed by any
        /// tenant or not.
        /// </summary>
        public readonly string Shared;
        public readonly string? Status;
        public readonly ImmutableArray<string> Tags;
        public readonly string? TenantId;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly bool? TransparentVlan;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetNetworkResult(
            string adminStateUp,
            ImmutableArray<string> allTags,
            ImmutableArray<string> availabilityZoneHints,
            string? description,
            string dnsDomain,
            bool? external,
            string? matchingSubnetCidr,
            int? mtu,
            string? name,
            string? networkId,
            string region,
            string shared,
            string? status,
            ImmutableArray<string> tags,
            string? tenantId,
            bool? transparentVlan,
            string id)
        {
            AdminStateUp = adminStateUp;
            AllTags = allTags;
            AvailabilityZoneHints = availabilityZoneHints;
            Description = description;
            DnsDomain = dnsDomain;
            External = external;
            MatchingSubnetCidr = matchingSubnetCidr;
            Mtu = mtu;
            Name = name;
            NetworkId = networkId;
            Region = region;
            Shared = shared;
            Status = status;
            Tags = tags;
            TenantId = tenantId;
            TransparentVlan = transparentVlan;
            Id = id;
        }
    }
}
