// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OpenStack.SharedFileSystem
{
    public static partial class Invokes
    {
        /// <summary>
        /// Use this data source to get the ID of an available Shared File System share.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/sharedfilesystem_share_v2.html.markdown.
        /// </summary>
        [Obsolete("Use GetShare.InvokeAsync() instead")]
        public static Task<GetShareResult> GetShare(GetShareArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetShareResult>("openstack:sharedfilesystem/getShare:getShare", args ?? InvokeArgs.Empty, options.WithVersion());
    }
    public static class GetShare
    {
        /// <summary>
        /// Use this data source to get the ID of an available Shared File System share.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/sharedfilesystem_share_v2.html.markdown.
        /// </summary>
        public static Task<GetShareResult> InvokeAsync(GetShareArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetShareResult>("openstack:sharedfilesystem/getShare:getShare", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetShareArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The human-readable description for the share.
        /// </summary>
        [Input("description")]
        public string? Description { get; set; }

        /// <summary>
        /// The export location path of the share. Available
        /// since Manila API version 2.35.
        /// </summary>
        [Input("exportLocationPath")]
        public string? ExportLocationPath { get; set; }

        /// <summary>
        /// The level of visibility for the share.
        /// length.
        /// </summary>
        [Input("isPublic")]
        public bool? IsPublic { get; set; }

        [Input("metadata")]
        private Dictionary<string, object>? _metadata;

        /// <summary>
        /// One or more metadata key and value pairs as a dictionary of
        /// strings.
        /// </summary>
        public Dictionary<string, object> Metadata
        {
            get => _metadata ?? (_metadata = new Dictionary<string, object>());
            set => _metadata = value;
        }

        /// <summary>
        /// The name of the share.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// The region in which to obtain the V2 Shared File System client.
        /// </summary>
        [Input("region")]
        public string? Region { get; set; }

        /// <summary>
        /// The UUID of the share's share network.
        /// </summary>
        [Input("shareNetworkId")]
        public string? ShareNetworkId { get; set; }

        /// <summary>
        /// The UUID of the share's base snapshot.
        /// </summary>
        [Input("snapshotId")]
        public string? SnapshotId { get; set; }

        /// <summary>
        /// A share status filter. A valid value is `creating`,
        /// `error`, `available`, `deleting`, `error_deleting`, `manage_starting`,
        /// `manage_error`, `unmanage_starting`, `unmanage_error`, `unmanaged`,
        /// `extending`, `extending_error`, `shrinking`, `shrinking_error`, or
        /// `shrinking_possible_data_loss_error`.
        /// </summary>
        [Input("status")]
        public string? Status { get; set; }

        public GetShareArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetShareResult
    {
        /// <summary>
        /// The share availability zone.
        /// </summary>
        public readonly string AvailabilityZone;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string Description;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string? ExportLocationPath;
        /// <summary>
        /// A list of export locations. For example, when a share
        /// server has more than one network interface, it can have multiple export
        /// locations.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetShareExportLocationsResult> ExportLocations;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly bool IsPublic;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly ImmutableDictionary<string, object> Metadata;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string ProjectId;
        /// <summary>
        /// The region in which to obtain the V2 Shared File System client.
        /// </summary>
        public readonly string Region;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string ShareNetworkId;
        /// <summary>
        /// The share protocol.
        /// </summary>
        public readonly string ShareProto;
        /// <summary>
        /// The share size, in GBs.
        /// </summary>
        public readonly int Size;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string SnapshotId;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string Status;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetShareResult(
            string availabilityZone,
            string description,
            string? exportLocationPath,
            ImmutableArray<Outputs.GetShareExportLocationsResult> exportLocations,
            bool isPublic,
            ImmutableDictionary<string, object> metadata,
            string name,
            string projectId,
            string region,
            string shareNetworkId,
            string shareProto,
            int size,
            string snapshotId,
            string status,
            string id)
        {
            AvailabilityZone = availabilityZone;
            Description = description;
            ExportLocationPath = exportLocationPath;
            ExportLocations = exportLocations;
            IsPublic = isPublic;
            Metadata = metadata;
            Name = name;
            ProjectId = projectId;
            Region = region;
            ShareNetworkId = shareNetworkId;
            ShareProto = shareProto;
            Size = size;
            SnapshotId = snapshotId;
            Status = status;
            Id = id;
        }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class GetShareExportLocationsResult
    {
        public readonly string Path;
        public readonly string Preferred;

        [OutputConstructor]
        private GetShareExportLocationsResult(
            string path,
            string preferred)
        {
            Path = path;
            Preferred = preferred;
        }
    }
    }
}
