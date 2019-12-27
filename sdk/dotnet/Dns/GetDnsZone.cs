// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OpenStack.Dns
{
    public static partial class Invokes
    {
        /// <summary>
        /// Use this data source to get the ID of an available OpenStack DNS zone.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/dns_zone_v2.html.markdown.
        /// </summary>
        public static Task<GetDnsZoneResult> GetDnsZone(GetDnsZoneArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetDnsZoneResult>("openstack:dns/getDnsZone:getDnsZone", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetDnsZoneArgs : Pulumi.InvokeArgs
    {
        [Input("attributes")]
        private Dictionary<string, object>? _attributes;
        public Dictionary<string, object> Attributes
        {
            get => _attributes ?? (_attributes = new Dictionary<string, object>());
            set => _attributes = value;
        }

        [Input("createdAt")]
        public string? CreatedAt { get; set; }

        /// <summary>
        /// A description of the zone.
        /// </summary>
        [Input("description")]
        public string? Description { get; set; }

        /// <summary>
        /// The email contact for the zone record.
        /// </summary>
        [Input("email")]
        public string? Email { get; set; }

        [Input("masters")]
        private List<string>? _masters;
        public List<string> Masters
        {
            get => _masters ?? (_masters = new List<string>());
            set => _masters = value;
        }

        /// <summary>
        /// The name of the zone.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        [Input("poolId")]
        public string? PoolId { get; set; }

        [Input("projectId")]
        public string? ProjectId { get; set; }

        /// <summary>
        /// The region in which to obtain the V2 DNS client.
        /// A DNS client is needed to retrieve zone ids. If omitted, the
        /// `region` argument of the provider is used.
        /// </summary>
        [Input("region")]
        public string? Region { get; set; }

        [Input("serial")]
        public int? Serial { get; set; }

        /// <summary>
        /// The zone's status.
        /// </summary>
        [Input("status")]
        public string? Status { get; set; }

        [Input("transferredAt")]
        public string? TransferredAt { get; set; }

        /// <summary>
        /// The time to live (TTL) of the zone.
        /// </summary>
        [Input("ttl")]
        public int? Ttl { get; set; }

        /// <summary>
        /// The type of the zone. Can either be `PRIMARY` or `SECONDARY`.
        /// </summary>
        [Input("type")]
        public string? Type { get; set; }

        [Input("updatedAt")]
        public string? UpdatedAt { get; set; }

        [Input("version")]
        public int? Version { get; set; }

        public GetDnsZoneArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetDnsZoneResult
    {
        /// <summary>
        /// Attributes of the DNS Service scheduler.
        /// </summary>
        public readonly ImmutableDictionary<string, object> Attributes;
        /// <summary>
        /// The time the zone was created.
        /// </summary>
        public readonly string CreatedAt;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string? Email;
        /// <summary>
        /// An array of master DNS servers. When `type` is  `SECONDARY`.
        /// </summary>
        public readonly ImmutableArray<string> Masters;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// The ID of the pool hosting the zone.
        /// </summary>
        public readonly string PoolId;
        /// <summary>
        /// The project ID that owns the zone.
        /// </summary>
        public readonly string ProjectId;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string Region;
        /// <summary>
        /// The serial number of the zone.
        /// </summary>
        public readonly int Serial;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string? Status;
        /// <summary>
        /// The time the zone was transferred.
        /// </summary>
        public readonly string TransferredAt;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly int? Ttl;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string? Type;
        /// <summary>
        /// The time the zone was last updated.
        /// </summary>
        public readonly string UpdatedAt;
        /// <summary>
        /// The version of the zone.
        /// </summary>
        public readonly int Version;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetDnsZoneResult(
            ImmutableDictionary<string, object> attributes,
            string createdAt,
            string? description,
            string? email,
            ImmutableArray<string> masters,
            string? name,
            string poolId,
            string projectId,
            string region,
            int serial,
            string? status,
            string transferredAt,
            int? ttl,
            string? type,
            string updatedAt,
            int version,
            string id)
        {
            Attributes = attributes;
            CreatedAt = createdAt;
            Description = description;
            Email = email;
            Masters = masters;
            Name = name;
            PoolId = poolId;
            ProjectId = projectId;
            Region = region;
            Serial = serial;
            Status = status;
            TransferredAt = transferredAt;
            Ttl = ttl;
            Type = type;
            UpdatedAt = updatedAt;
            Version = version;
            Id = id;
        }
    }
}
