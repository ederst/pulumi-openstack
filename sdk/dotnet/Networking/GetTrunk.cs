// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OpenStack.Networking
{
    public static partial class Invokes
    {
        /// <summary>
        /// Use this data source to get the ID of an available OpenStack trunk.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/networking_trunk_v2.html.markdown.
        /// </summary>
        [Obsolete("Use GetTrunk.InvokeAsync() instead")]
        public static Task<GetTrunkResult> GetTrunk(GetTrunkArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetTrunkResult>("openstack:networking/getTrunk:getTrunk", args ?? InvokeArgs.Empty, options.WithVersion());
    }
    public static class GetTrunk
    {
        /// <summary>
        /// Use this data source to get the ID of an available OpenStack trunk.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/networking_trunk_v2.html.markdown.
        /// </summary>
        public static Task<GetTrunkResult> InvokeAsync(GetTrunkArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetTrunkResult>("openstack:networking/getTrunk:getTrunk", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetTrunkArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The administrative state of the trunk.
        /// </summary>
        [Input("adminStateUp")]
        public bool? AdminStateUp { get; set; }

        /// <summary>
        /// Human-readable description of the trunk.
        /// </summary>
        [Input("description")]
        public string? Description { get; set; }

        /// <summary>
        /// The name of the trunk.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// The ID of the trunk parent port.
        /// </summary>
        [Input("portId")]
        public string? PortId { get; set; }

        /// <summary>
        /// The owner of the trunk.
        /// </summary>
        [Input("projectId")]
        public string? ProjectId { get; set; }

        /// <summary>
        /// The region in which to obtain the V2 Neutron client.
        /// A Neutron client is needed to retrieve trunk ids. If omitted, the
        /// `region` argument of the provider is used.
        /// </summary>
        [Input("region")]
        public string? Region { get; set; }

        /// <summary>
        /// The status of the trunk.
        /// </summary>
        [Input("status")]
        public string? Status { get; set; }

        [Input("tags")]
        private List<string>? _tags;

        /// <summary>
        /// The list of trunk tags to filter.
        /// </summary>
        public List<string> Tags
        {
            get => _tags ?? (_tags = new List<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The ID of the trunk.
        /// </summary>
        [Input("trunkId")]
        public string? TrunkId { get; set; }

        public GetTrunkArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetTrunkResult
    {
        public readonly bool? AdminStateUp;
        /// <summary>
        /// The set of string tags applied on the trunk.
        /// </summary>
        public readonly ImmutableArray<string> AllTags;
        public readonly string? Description;
        public readonly string? Name;
        /// <summary>
        /// The ID of the trunk subport.
        /// </summary>
        public readonly string? PortId;
        public readonly string ProjectId;
        public readonly string Region;
        public readonly string? Status;
        /// <summary>
        /// The set of the trunk subports. The structure of each subport is
        /// described below.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetTrunkSubPortsResult> SubPorts;
        public readonly ImmutableArray<string> Tags;
        public readonly string? TrunkId;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetTrunkResult(
            bool? adminStateUp,
            ImmutableArray<string> allTags,
            string? description,
            string? name,
            string? portId,
            string projectId,
            string region,
            string? status,
            ImmutableArray<Outputs.GetTrunkSubPortsResult> subPorts,
            ImmutableArray<string> tags,
            string? trunkId,
            string id)
        {
            AdminStateUp = adminStateUp;
            AllTags = allTags;
            Description = description;
            Name = name;
            PortId = portId;
            ProjectId = projectId;
            Region = region;
            Status = status;
            SubPorts = subPorts;
            Tags = tags;
            TrunkId = trunkId;
            Id = id;
        }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class GetTrunkSubPortsResult
    {
        /// <summary>
        /// The ID of the trunk parent port.
        /// </summary>
        public readonly string PortId;
        /// <summary>
        /// The numeric id of the subport segment.
        /// </summary>
        public readonly int SegmentationId;
        /// <summary>
        /// The segmenation tecnology used, e.g., "vlan".
        /// </summary>
        public readonly string SegmentationType;

        [OutputConstructor]
        private GetTrunkSubPortsResult(
            string portId,
            int segmentationId,
            string segmentationType)
        {
            PortId = portId;
            SegmentationId = segmentationId;
            SegmentationType = segmentationType;
        }
    }
    }
}
