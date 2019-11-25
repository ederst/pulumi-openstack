// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Openstack.Images
{
    public static partial class Invokes
    {
        /// <summary>
        /// Use this data source to get the ID of an available OpenStack image.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/images_image_v2.html.markdown.
        /// </summary>
        public static Task<GetImageResult> GetImage(GetImageArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetImageResult>("openstack:images/getImage:getImage", args ?? ResourceArgs.Empty, options.WithVersion());
    }

    public sealed class GetImageArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The status of the image. Must be one of
        /// "accepted", "pending", "rejected", or "all".
        /// </summary>
        [Input("memberStatus")]
        public Input<string>? MemberStatus { get; set; }

        /// <summary>
        /// If more than one result is returned, use the most
        /// recent image.
        /// </summary>
        [Input("mostRecent")]
        public Input<bool>? MostRecent { get; set; }

        /// <summary>
        /// The name of the image.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The owner (UUID) of the image.
        /// </summary>
        [Input("owner")]
        public Input<string>? Owner { get; set; }

        [Input("properties")]
        private InputMap<object>? _properties;

        /// <summary>
        /// a map of key/value pairs to match an image with.
        /// All specified properties must be matched.
        /// </summary>
        public InputMap<object> Properties
        {
            get => _properties ?? (_properties = new InputMap<object>());
            set => _properties = value;
        }

        /// <summary>
        /// The region in which to obtain the V2 Glance client.
        /// A Glance client is needed to create an Image that can be used with
        /// a compute instance. If omitted, the `region` argument of the provider
        /// is used.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The maximum size (in bytes) of the image to return.
        /// </summary>
        [Input("sizeMax")]
        public Input<int>? SizeMax { get; set; }

        /// <summary>
        /// The minimum size (in bytes) of the image to return.
        /// </summary>
        [Input("sizeMin")]
        public Input<int>? SizeMin { get; set; }

        /// <summary>
        /// Order the results in either `asc` or `desc`.
        /// </summary>
        [Input("sortDirection")]
        public Input<string>? SortDirection { get; set; }

        /// <summary>
        /// Sort images based on a certain key. Defaults to `name`.
        /// </summary>
        [Input("sortKey")]
        public Input<string>? SortKey { get; set; }

        /// <summary>
        /// Search for images with a specific tag.
        /// </summary>
        [Input("tag")]
        public Input<string>? Tag { get; set; }

        /// <summary>
        /// The visibility of the image. Must be one of
        /// "public", "private", "community", or "shared". Defaults to "private".
        /// </summary>
        [Input("visibility")]
        public Input<string>? Visibility { get; set; }

        public GetImageArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetImageResult
    {
        /// <summary>
        /// The checksum of the data associated with the image.
        /// </summary>
        public readonly string Checksum;
        public readonly string ContainerFormat;
        /// <summary>
        /// The date the image was created.
        /// * `container_format`: The format of the image's container.
        /// * `disk_format`: The format of the image's disk.
        /// </summary>
        public readonly string CreatedAt;
        public readonly string DiskFormat;
        /// <summary>
        /// the trailing path after the glance endpoint that represent the
        /// location of the image or the path to retrieve it.
        /// </summary>
        public readonly string File;
        public readonly string? MemberStatus;
        /// <summary>
        /// The metadata associated with the image.
        /// Image metadata allow for meaningfully define the image properties
        /// and tags. See https://docs.openstack.org/glance/latest/user/metadefs-concepts.html.
        /// </summary>
        public readonly ImmutableDictionary<string, object> Metadata;
        /// <summary>
        /// The minimum amount of disk space required to use the image.
        /// </summary>
        public readonly int MinDiskGb;
        /// <summary>
        /// The minimum amount of ram required to use the image.
        /// </summary>
        public readonly int MinRamMb;
        public readonly bool? MostRecent;
        public readonly string? Name;
        public readonly string? Owner;
        /// <summary>
        /// Freeform information about the image.
        /// </summary>
        public readonly ImmutableDictionary<string, object>? Properties;
        /// <summary>
        /// Whether or not the image is protected.
        /// </summary>
        public readonly bool Protected;
        public readonly string Region;
        /// <summary>
        /// The path to the JSON-schema that represent
        /// the image or image
        /// </summary>
        public readonly string Schema;
        /// <summary>
        /// The size of the image (in bytes).
        /// </summary>
        public readonly int SizeBytes;
        public readonly int? SizeMax;
        public readonly int? SizeMin;
        public readonly string? SortDirection;
        public readonly string? SortKey;
        public readonly string? Tag;
        /// <summary>
        /// The tags list of the image.
        /// </summary>
        public readonly ImmutableArray<string> Tags;
        /// <summary>
        /// The date the image was last updated.
        /// </summary>
        public readonly string UpdatedAt;
        public readonly string? Visibility;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetImageResult(
            string checksum,
            string containerFormat,
            string createdAt,
            string diskFormat,
            string file,
            string? memberStatus,
            ImmutableDictionary<string, object> metadata,
            int minDiskGb,
            int minRamMb,
            bool? mostRecent,
            string? name,
            string? owner,
            ImmutableDictionary<string, object>? properties,
            bool @protected,
            string region,
            string schema,
            int sizeBytes,
            int? sizeMax,
            int? sizeMin,
            string? sortDirection,
            string? sortKey,
            string? tag,
            ImmutableArray<string> tags,
            string updatedAt,
            string? visibility,
            string id)
        {
            Checksum = checksum;
            ContainerFormat = containerFormat;
            CreatedAt = createdAt;
            DiskFormat = diskFormat;
            File = file;
            MemberStatus = memberStatus;
            Metadata = metadata;
            MinDiskGb = minDiskGb;
            MinRamMb = minRamMb;
            MostRecent = mostRecent;
            Name = name;
            Owner = owner;
            Properties = properties;
            Protected = @protected;
            Region = region;
            Schema = schema;
            SizeBytes = sizeBytes;
            SizeMax = sizeMax;
            SizeMin = sizeMin;
            SortDirection = sortDirection;
            SortKey = sortKey;
            Tag = tag;
            Tags = tags;
            UpdatedAt = updatedAt;
            Visibility = visibility;
            Id = id;
        }
    }
}