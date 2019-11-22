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
        /// Use this data source to get the ID of an available OpenStack port.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/networking_port_v2.html.markdown.
        /// </summary>
        public static Task<GetPortResult> GetPort(GetPortArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetPortResult>("openstack:networking/getPort:getPort", args ?? ResourceArgs.Empty, options.WithVersion());
    }

    public sealed class GetPortArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The administrative state of the port.
        /// </summary>
        [Input("adminStateUp")]
        public Input<bool>? AdminStateUp { get; set; }

        /// <summary>
        /// Human-readable description of the port.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The ID of the device the port belongs to.
        /// </summary>
        [Input("deviceId")]
        public Input<string>? DeviceId { get; set; }

        /// <summary>
        /// The device owner of the port.
        /// </summary>
        [Input("deviceOwner")]
        public Input<string>? DeviceOwner { get; set; }

        /// <summary>
        /// The port DNS name to filter. Available, when Neutron
        /// DNS extension is enabled.
        /// </summary>
        [Input("dnsName")]
        public Input<string>? DnsName { get; set; }

        /// <summary>
        /// The port IP address filter.
        /// </summary>
        [Input("fixedIp")]
        public Input<string>? FixedIp { get; set; }

        /// <summary>
        /// The MAC address of the port.
        /// </summary>
        [Input("macAddress")]
        public Input<string>? MacAddress { get; set; }

        /// <summary>
        /// The name of the port.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the network the port belongs to.
        /// </summary>
        [Input("networkId")]
        public Input<string>? NetworkId { get; set; }

        /// <summary>
        /// The ID of the port.
        /// </summary>
        [Input("portId")]
        public Input<string>? PortId { get; set; }

        /// <summary>
        /// The owner of the port.
        /// </summary>
        [Input("projectId")]
        public Input<string>? ProjectId { get; set; }

        /// <summary>
        /// The region in which to obtain the V2 Neutron client.
        /// A Neutron client is needed to retrieve port ids. If omitted, the
        /// `region` argument of the provider is used.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("securityGroupIds")]
        private InputList<string>? _securityGroupIds;

        /// <summary>
        /// The list of port security group IDs to filter.
        /// </summary>
        public InputList<string> SecurityGroupIds
        {
            get => _securityGroupIds ?? (_securityGroupIds = new InputList<string>());
            set => _securityGroupIds = value;
        }

        /// <summary>
        /// The status of the port.
        /// </summary>
        [Input("status")]
        public Input<string>? Status { get; set; }

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// The list of port tags to filter.
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        [Input("tenantId")]
        public Input<string>? TenantId { get; set; }

        public GetPortArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetPortResult
    {
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly bool? AdminStateUp;
        /// <summary>
        /// The collection of Fixed IP addresses on the port in the
        /// order returned by the Network v2 API.
        /// </summary>
        public readonly ImmutableArray<string> AllFixedIps;
        /// <summary>
        /// The set of security group IDs applied on the port.
        /// </summary>
        public readonly ImmutableArray<string> AllSecurityGroupIds;
        /// <summary>
        /// The set of string tags applied on the port.
        /// </summary>
        public readonly ImmutableArray<string> AllTags;
        /// <summary>
        /// An IP/MAC Address pair of additional IP
        /// addresses that can be active on this port. The structure is described
        /// below.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetPortAllowedAddressPairsResult> AllowedAddressPairs;
        /// <summary>
        /// The port binding information. The structure is described below.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetPortBindingsResult> Bindings;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string? DeviceId;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string? DeviceOwner;
        /// <summary>
        /// The list of maps representing port DNS assignments.
        /// </summary>
        public readonly ImmutableArray<ImmutableDictionary<string, object>> DnsAssignments;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string? DnsName;
        /// <summary>
        /// An extra DHCP option configured on the port.
        /// The structure is described below.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetPortExtraDhcpOptionsResult> ExtraDhcpOptions;
        public readonly string? FixedIp;
        /// <summary>
        /// The additional MAC address.
        /// </summary>
        public readonly string? MacAddress;
        /// <summary>
        /// Name of the DHCP option.
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string? NetworkId;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string? PortId;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string? ProjectId;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string? Region;
        public readonly ImmutableArray<string> SecurityGroupIds;
        public readonly string? Status;
        public readonly ImmutableArray<string> Tags;
        public readonly string? TenantId;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetPortResult(
            bool? adminStateUp,
            ImmutableArray<string> allFixedIps,
            ImmutableArray<string> allSecurityGroupIds,
            ImmutableArray<string> allTags,
            ImmutableArray<Outputs.GetPortAllowedAddressPairsResult> allowedAddressPairs,
            ImmutableArray<Outputs.GetPortBindingsResult> bindings,
            string? description,
            string? deviceId,
            string? deviceOwner,
            ImmutableArray<ImmutableDictionary<string, object>> dnsAssignments,
            string? dnsName,
            ImmutableArray<Outputs.GetPortExtraDhcpOptionsResult> extraDhcpOptions,
            string? fixedIp,
            string? macAddress,
            string? name,
            string? networkId,
            string? portId,
            string? projectId,
            string? region,
            ImmutableArray<string> securityGroupIds,
            string? status,
            ImmutableArray<string> tags,
            string? tenantId,
            string id)
        {
            AdminStateUp = adminStateUp;
            AllFixedIps = allFixedIps;
            AllSecurityGroupIds = allSecurityGroupIds;
            AllTags = allTags;
            AllowedAddressPairs = allowedAddressPairs;
            Bindings = bindings;
            Description = description;
            DeviceId = deviceId;
            DeviceOwner = deviceOwner;
            DnsAssignments = dnsAssignments;
            DnsName = dnsName;
            ExtraDhcpOptions = extraDhcpOptions;
            FixedIp = fixedIp;
            MacAddress = macAddress;
            Name = name;
            NetworkId = networkId;
            PortId = portId;
            ProjectId = projectId;
            Region = region;
            SecurityGroupIds = securityGroupIds;
            Status = status;
            Tags = tags;
            TenantId = tenantId;
            Id = id;
        }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class GetPortAllowedAddressPairsResult
    {
        /// <summary>
        /// The additional IP address.
        /// </summary>
        public readonly string IpAddress;
        /// <summary>
        /// The MAC address of the port.
        /// </summary>
        public readonly string MacAddress;

        [OutputConstructor]
        private GetPortAllowedAddressPairsResult(
            string ipAddress,
            string macAddress)
        {
            IpAddress = ipAddress;
            MacAddress = macAddress;
        }
    }

    [OutputType]
    public sealed class GetPortBindingsResult
    {
        /// <summary>
        /// The ID of the host, which has the allocatee port.
        /// </summary>
        public readonly string HostId;
        /// <summary>
        /// A JSON string containing the binding profile information.
        /// </summary>
        public readonly string Profile;
        /// <summary>
        /// A map of JSON strings containing additional details for this
        /// specific binding.
        /// </summary>
        public readonly ImmutableDictionary<string, object> VifDetails;
        /// <summary>
        /// The VNIC type of the port binding.
        /// </summary>
        public readonly string VifType;
        /// <summary>
        /// VNIC type for the port.
        /// </summary>
        public readonly string VnicType;

        [OutputConstructor]
        private GetPortBindingsResult(
            string hostId,
            string profile,
            ImmutableDictionary<string, object> vifDetails,
            string vifType,
            string vnicType)
        {
            HostId = hostId;
            Profile = profile;
            VifDetails = vifDetails;
            VifType = vifType;
            VnicType = vnicType;
        }
    }

    [OutputType]
    public sealed class GetPortExtraDhcpOptionsResult
    {
        /// <summary>
        /// IP protocol version
        /// </summary>
        public readonly int IpVersion;
        /// <summary>
        /// The name of the port.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// Value of the DHCP option.
        /// </summary>
        public readonly string Value;

        [OutputConstructor]
        private GetPortExtraDhcpOptionsResult(
            int ipVersion,
            string name,
            string value)
        {
            IpVersion = ipVersion;
            Name = name;
            Value = value;
        }
    }
    }
}
