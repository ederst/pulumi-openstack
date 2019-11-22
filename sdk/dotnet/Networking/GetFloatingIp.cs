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
        /// Use this data source to get the ID of an available OpenStack floating IP.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/networking_floatingip_v2.html.markdown.
        /// </summary>
        public static Task<GetFloatingIpResult> GetFloatingIp(GetFloatingIpArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetFloatingIpResult>("openstack:networking/getFloatingIp:getFloatingIp", args ?? ResourceArgs.Empty, options.WithVersion());
    }

    public sealed class GetFloatingIpArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The IP address of the floating IP.
        /// </summary>
        [Input("address")]
        public Input<string>? Address { get; set; }

        /// <summary>
        /// Human-readable description of the floating IP.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The specific IP address of the internal port which should be associated with the floating IP.
        /// </summary>
        [Input("fixedIp")]
        public Input<string>? FixedIp { get; set; }

        /// <summary>
        /// The name of the pool from which the floating IP belongs to.
        /// </summary>
        [Input("pool")]
        public Input<string>? Pool { get; set; }

        /// <summary>
        /// The ID of the port the floating IP is attached.
        /// </summary>
        [Input("portId")]
        public Input<string>? PortId { get; set; }

        /// <summary>
        /// The region in which to obtain the V2 Neutron client.
        /// A Neutron client is needed to retrieve floating IP ids. If omitted, the
        /// `region` argument of the provider is used.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// status of the floating IP (ACTIVE/DOWN).
        /// </summary>
        [Input("status")]
        public Input<string>? Status { get; set; }

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// The list of floating IP tags to filter.
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The owner of the floating IP.
        /// </summary>
        [Input("tenantId")]
        public Input<string>? TenantId { get; set; }

        public GetFloatingIpArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetFloatingIpResult
    {
        public readonly string? Address;
        /// <summary>
        /// A set of string tags applied on the floating IP.
        /// </summary>
        public readonly ImmutableArray<string> AllTags;
        public readonly string? Description;
        /// <summary>
        /// The floating IP DNS domain. Available, when Neutron DNS
        /// extension is enabled.
        /// </summary>
        public readonly string DnsDomain;
        /// <summary>
        /// The floating IP DNS name. Available, when Neutron DNS extension
        /// is enabled.
        /// </summary>
        public readonly string DnsName;
        public readonly string? FixedIp;
        public readonly string? Pool;
        public readonly string? PortId;
        public readonly string? Region;
        public readonly string? Status;
        public readonly ImmutableArray<string> Tags;
        public readonly string? TenantId;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetFloatingIpResult(
            string? address,
            ImmutableArray<string> allTags,
            string? description,
            string dnsDomain,
            string dnsName,
            string? fixedIp,
            string? pool,
            string? portId,
            string? region,
            string? status,
            ImmutableArray<string> tags,
            string? tenantId,
            string id)
        {
            Address = address;
            AllTags = allTags;
            Description = description;
            DnsDomain = dnsDomain;
            DnsName = dnsName;
            FixedIp = fixedIp;
            Pool = pool;
            PortId = portId;
            Region = region;
            Status = status;
            Tags = tags;
            TenantId = tenantId;
            Id = id;
        }
    }
}
