// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Openstack.Blockstorage
{
    public static partial class Invokes
    {
        /// <summary>
        /// Use this data source to get information about an existing snapshot.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/blockstorage_snapshot_v3.html.markdown.
        /// </summary>
        public static Task<GetSnapshotV3Result> GetSnapshotV3(GetSnapshotV3Args? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetSnapshotV3Result>("openstack:blockstorage/getSnapshotV3:getSnapshotV3", args ?? ResourceArgs.Empty, options.WithVersion());
    }

    public sealed class GetSnapshotV3Args : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Pick the most recently created snapshot if there
        /// are multiple results.
        /// </summary>
        [Input("mostRecent")]
        public Input<bool>? MostRecent { get; set; }

        /// <summary>
        /// The name of the snapshot.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The region in which to obtain the V3 Block Storage
        /// client. If omitted, the `region` argument of the provider is used.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The status of the snapshot.
        /// </summary>
        [Input("status")]
        public Input<string>? Status { get; set; }

        /// <summary>
        /// The ID of the snapshot's volume.
        /// </summary>
        [Input("volumeId")]
        public Input<string>? VolumeId { get; set; }

        public GetSnapshotV3Args()
        {
        }
    }

    [OutputType]
    public sealed class GetSnapshotV3Result
    {
        /// <summary>
        /// The snapshot's description.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// The snapshot's metadata.
        /// </summary>
        public readonly ImmutableDictionary<string, object> Metadata;
        public readonly bool? MostRecent;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string Region;
        /// <summary>
        /// The size of the snapshot.
        /// </summary>
        public readonly int Size;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string Status;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string VolumeId;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetSnapshotV3Result(
            string description,
            ImmutableDictionary<string, object> metadata,
            bool? mostRecent,
            string name,
            string region,
            int size,
            string status,
            string volumeId,
            string id)
        {
            Description = description;
            Metadata = metadata;
            MostRecent = mostRecent;
            Name = name;
            Region = region;
            Size = size;
            Status = status;
            VolumeId = volumeId;
            Id = id;
        }
    }
}