// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OpenStack.Networking
{
    /// <summary>
    /// Manages a V2 Neutron subnet resource within OpenStack.
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
    ///         var network1 = new OpenStack.Networking.Network("network1", new OpenStack.Networking.NetworkArgs
    ///         {
    ///             AdminStateUp = true,
    ///         });
    ///         var subnet1 = new OpenStack.Networking.Subnet("subnet1", new OpenStack.Networking.SubnetArgs
    ///         {
    ///             Cidr = "192.168.199.0/24",
    ///             NetworkId = network1.Id,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// Subnets can be imported using the `id`, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import openstack:networking/subnet:Subnet subnet_1 da4faf16-5546-41e4-8330-4d0002b74048
    /// ```
    /// </summary>
    public partial class Subnet : Pulumi.CustomResource
    {
        /// <summary>
        /// The collection of ags assigned on the subnet, which have been
        /// explicitly and implicitly added.
        /// </summary>
        [Output("allTags")]
        public Output<ImmutableArray<string>> AllTags { get; private set; } = null!;

        /// <summary>
        /// A block declaring the start and end range of
        /// the IP addresses available for use with DHCP in this subnet. Multiple
        /// `allocation_pool` blocks can be declared, providing the subnet with more
        /// than one range of IP addresses to use with DHCP. However, each IP range
        /// must be from the same CIDR that the subnet is part of.
        /// The `allocation_pool` block is documented below.
        /// </summary>
        [Output("allocationPools")]
        public Output<ImmutableArray<Outputs.SubnetAllocationPool>> AllocationPools { get; private set; } = null!;

        /// <summary>
        /// A block declaring the start and end range of the IP addresses available for
        /// use with DHCP in this subnet.
        /// The `allocation_pools` block is documented below.
        /// </summary>
        [Output("allocationPoolsCollection")]
        public Output<ImmutableArray<Outputs.SubnetAllocationPoolsCollection>> AllocationPoolsCollection { get; private set; } = null!;

        /// <summary>
        /// CIDR representing IP range for this subnet, based on IP
        /// version. You can omit this option if you are creating a subnet from a
        /// subnet pool.
        /// </summary>
        [Output("cidr")]
        public Output<string> Cidr { get; private set; } = null!;

        /// <summary>
        /// Human-readable description of the subnet. Changing this
        /// updates the name of the existing subnet.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// An array of DNS name server names used by hosts
        /// in this subnet. Changing this updates the DNS name servers for the existing
        /// subnet.
        /// </summary>
        [Output("dnsNameservers")]
        public Output<ImmutableArray<string>> DnsNameservers { get; private set; } = null!;

        /// <summary>
        /// The administrative state of the network.
        /// Acceptable values are "true" and "false". Changing this value enables or
        /// disables the DHCP capabilities of the existing subnet. Defaults to true.
        /// </summary>
        [Output("enableDhcp")]
        public Output<bool?> EnableDhcp { get; private set; } = null!;

        /// <summary>
        /// Default gateway used by devices in this subnet.
        /// Leaving this blank and not setting `no_gateway` will cause a default
        /// gateway of `.1` to be used. Changing this updates the gateway IP of the
        /// existing subnet.
        /// </summary>
        [Output("gatewayIp")]
        public Output<string> GatewayIp { get; private set; } = null!;

        /// <summary>
        /// (**Deprecated** - use `openstack.networking.SubnetRoute`
        /// instead) An array of routes that should be used by devices
        /// with IPs from this subnet (not including local subnet route). The host_route
        /// object structure is documented below. Changing this updates the host routes
        /// for the existing subnet.
        /// </summary>
        [Output("hostRoutes")]
        public Output<ImmutableArray<Outputs.SubnetHostRoute>> HostRoutes { get; private set; } = null!;

        /// <summary>
        /// IP version, either 4 (default) or 6. Changing this creates a
        /// new subnet.
        /// </summary>
        [Output("ipVersion")]
        public Output<int?> IpVersion { get; private set; } = null!;

        /// <summary>
        /// The IPv6 address mode. Valid values are
        /// `dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
        /// </summary>
        [Output("ipv6AddressMode")]
        public Output<string> Ipv6AddressMode { get; private set; } = null!;

        /// <summary>
        /// The IPv6 Router Advertisement mode. Valid values
        /// are `dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
        /// </summary>
        [Output("ipv6RaMode")]
        public Output<string> Ipv6RaMode { get; private set; } = null!;

        /// <summary>
        /// The name of the subnet. Changing this updates the name of
        /// the existing subnet.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The UUID of the parent network. Changing this
        /// creates a new subnet.
        /// </summary>
        [Output("networkId")]
        public Output<string> NetworkId { get; private set; } = null!;

        /// <summary>
        /// Do not set a gateway IP on this subnet. Changing
        /// this removes or adds a default gateway IP of the existing subnet.
        /// </summary>
        [Output("noGateway")]
        public Output<bool?> NoGateway { get; private set; } = null!;

        /// <summary>
        /// The prefix length to use when creating a subnet
        /// from a subnet pool. The default subnet pool prefix length that was defined
        /// when creating the subnet pool will be used if not provided. Changing this
        /// creates a new subnet.
        /// </summary>
        [Output("prefixLength")]
        public Output<int?> PrefixLength { get; private set; } = null!;

        /// <summary>
        /// The region in which to obtain the V2 Networking client.
        /// A Networking client is needed to create a Neutron subnet. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// subnet.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// The ID of the subnetpool associated with the subnet.
        /// </summary>
        [Output("subnetpoolId")]
        public Output<string?> SubnetpoolId { get; private set; } = null!;

        /// <summary>
        /// A set of string tags for the subnet.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<string>> Tags { get; private set; } = null!;

        /// <summary>
        /// The owner of the subnet. Required if admin wants to
        /// create a subnet for another tenant. Changing this creates a new subnet.
        /// </summary>
        [Output("tenantId")]
        public Output<string> TenantId { get; private set; } = null!;

        /// <summary>
        /// Map of additional options.
        /// </summary>
        [Output("valueSpecs")]
        public Output<ImmutableDictionary<string, object>?> ValueSpecs { get; private set; } = null!;


        /// <summary>
        /// Create a Subnet resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Subnet(string name, SubnetArgs args, CustomResourceOptions? options = null)
            : base("openstack:networking/subnet:Subnet", name, args ?? new SubnetArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Subnet(string name, Input<string> id, SubnetState? state = null, CustomResourceOptions? options = null)
            : base("openstack:networking/subnet:Subnet", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Subnet resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Subnet Get(string name, Input<string> id, SubnetState? state = null, CustomResourceOptions? options = null)
        {
            return new Subnet(name, id, state, options);
        }
    }

    public sealed class SubnetArgs : Pulumi.ResourceArgs
    {
        [Input("allocationPools")]
        private InputList<Inputs.SubnetAllocationPoolArgs>? _allocationPools;

        /// <summary>
        /// A block declaring the start and end range of
        /// the IP addresses available for use with DHCP in this subnet. Multiple
        /// `allocation_pool` blocks can be declared, providing the subnet with more
        /// than one range of IP addresses to use with DHCP. However, each IP range
        /// must be from the same CIDR that the subnet is part of.
        /// The `allocation_pool` block is documented below.
        /// </summary>
        public InputList<Inputs.SubnetAllocationPoolArgs> AllocationPools
        {
            get => _allocationPools ?? (_allocationPools = new InputList<Inputs.SubnetAllocationPoolArgs>());
            set => _allocationPools = value;
        }

        [Input("allocationPoolsCollection")]
        private InputList<Inputs.SubnetAllocationPoolsCollectionArgs>? _allocationPoolsCollection;

        /// <summary>
        /// A block declaring the start and end range of the IP addresses available for
        /// use with DHCP in this subnet.
        /// The `allocation_pools` block is documented below.
        /// </summary>
        [Obsolete(@"use allocation_pool instead")]
        public InputList<Inputs.SubnetAllocationPoolsCollectionArgs> AllocationPoolsCollection
        {
            get => _allocationPoolsCollection ?? (_allocationPoolsCollection = new InputList<Inputs.SubnetAllocationPoolsCollectionArgs>());
            set => _allocationPoolsCollection = value;
        }

        /// <summary>
        /// CIDR representing IP range for this subnet, based on IP
        /// version. You can omit this option if you are creating a subnet from a
        /// subnet pool.
        /// </summary>
        [Input("cidr")]
        public Input<string>? Cidr { get; set; }

        /// <summary>
        /// Human-readable description of the subnet. Changing this
        /// updates the name of the existing subnet.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("dnsNameservers")]
        private InputList<string>? _dnsNameservers;

        /// <summary>
        /// An array of DNS name server names used by hosts
        /// in this subnet. Changing this updates the DNS name servers for the existing
        /// subnet.
        /// </summary>
        public InputList<string> DnsNameservers
        {
            get => _dnsNameservers ?? (_dnsNameservers = new InputList<string>());
            set => _dnsNameservers = value;
        }

        /// <summary>
        /// The administrative state of the network.
        /// Acceptable values are "true" and "false". Changing this value enables or
        /// disables the DHCP capabilities of the existing subnet. Defaults to true.
        /// </summary>
        [Input("enableDhcp")]
        public Input<bool>? EnableDhcp { get; set; }

        /// <summary>
        /// Default gateway used by devices in this subnet.
        /// Leaving this blank and not setting `no_gateway` will cause a default
        /// gateway of `.1` to be used. Changing this updates the gateway IP of the
        /// existing subnet.
        /// </summary>
        [Input("gatewayIp")]
        public Input<string>? GatewayIp { get; set; }

        [Input("hostRoutes")]
        private InputList<Inputs.SubnetHostRouteArgs>? _hostRoutes;

        /// <summary>
        /// (**Deprecated** - use `openstack.networking.SubnetRoute`
        /// instead) An array of routes that should be used by devices
        /// with IPs from this subnet (not including local subnet route). The host_route
        /// object structure is documented below. Changing this updates the host routes
        /// for the existing subnet.
        /// </summary>
        [Obsolete(@"Use openstack_networking_subnet_route_v2 instead")]
        public InputList<Inputs.SubnetHostRouteArgs> HostRoutes
        {
            get => _hostRoutes ?? (_hostRoutes = new InputList<Inputs.SubnetHostRouteArgs>());
            set => _hostRoutes = value;
        }

        /// <summary>
        /// IP version, either 4 (default) or 6. Changing this creates a
        /// new subnet.
        /// </summary>
        [Input("ipVersion")]
        public Input<int>? IpVersion { get; set; }

        /// <summary>
        /// The IPv6 address mode. Valid values are
        /// `dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
        /// </summary>
        [Input("ipv6AddressMode")]
        public Input<string>? Ipv6AddressMode { get; set; }

        /// <summary>
        /// The IPv6 Router Advertisement mode. Valid values
        /// are `dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
        /// </summary>
        [Input("ipv6RaMode")]
        public Input<string>? Ipv6RaMode { get; set; }

        /// <summary>
        /// The name of the subnet. Changing this updates the name of
        /// the existing subnet.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The UUID of the parent network. Changing this
        /// creates a new subnet.
        /// </summary>
        [Input("networkId", required: true)]
        public Input<string> NetworkId { get; set; } = null!;

        /// <summary>
        /// Do not set a gateway IP on this subnet. Changing
        /// this removes or adds a default gateway IP of the existing subnet.
        /// </summary>
        [Input("noGateway")]
        public Input<bool>? NoGateway { get; set; }

        /// <summary>
        /// The prefix length to use when creating a subnet
        /// from a subnet pool. The default subnet pool prefix length that was defined
        /// when creating the subnet pool will be used if not provided. Changing this
        /// creates a new subnet.
        /// </summary>
        [Input("prefixLength")]
        public Input<int>? PrefixLength { get; set; }

        /// <summary>
        /// The region in which to obtain the V2 Networking client.
        /// A Networking client is needed to create a Neutron subnet. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// subnet.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The ID of the subnetpool associated with the subnet.
        /// </summary>
        [Input("subnetpoolId")]
        public Input<string>? SubnetpoolId { get; set; }

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// A set of string tags for the subnet.
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The owner of the subnet. Required if admin wants to
        /// create a subnet for another tenant. Changing this creates a new subnet.
        /// </summary>
        [Input("tenantId")]
        public Input<string>? TenantId { get; set; }

        [Input("valueSpecs")]
        private InputMap<object>? _valueSpecs;

        /// <summary>
        /// Map of additional options.
        /// </summary>
        public InputMap<object> ValueSpecs
        {
            get => _valueSpecs ?? (_valueSpecs = new InputMap<object>());
            set => _valueSpecs = value;
        }

        public SubnetArgs()
        {
        }
    }

    public sealed class SubnetState : Pulumi.ResourceArgs
    {
        [Input("allTags")]
        private InputList<string>? _allTags;

        /// <summary>
        /// The collection of ags assigned on the subnet, which have been
        /// explicitly and implicitly added.
        /// </summary>
        public InputList<string> AllTags
        {
            get => _allTags ?? (_allTags = new InputList<string>());
            set => _allTags = value;
        }

        [Input("allocationPools")]
        private InputList<Inputs.SubnetAllocationPoolGetArgs>? _allocationPools;

        /// <summary>
        /// A block declaring the start and end range of
        /// the IP addresses available for use with DHCP in this subnet. Multiple
        /// `allocation_pool` blocks can be declared, providing the subnet with more
        /// than one range of IP addresses to use with DHCP. However, each IP range
        /// must be from the same CIDR that the subnet is part of.
        /// The `allocation_pool` block is documented below.
        /// </summary>
        public InputList<Inputs.SubnetAllocationPoolGetArgs> AllocationPools
        {
            get => _allocationPools ?? (_allocationPools = new InputList<Inputs.SubnetAllocationPoolGetArgs>());
            set => _allocationPools = value;
        }

        [Input("allocationPoolsCollection")]
        private InputList<Inputs.SubnetAllocationPoolsCollectionGetArgs>? _allocationPoolsCollection;

        /// <summary>
        /// A block declaring the start and end range of the IP addresses available for
        /// use with DHCP in this subnet.
        /// The `allocation_pools` block is documented below.
        /// </summary>
        [Obsolete(@"use allocation_pool instead")]
        public InputList<Inputs.SubnetAllocationPoolsCollectionGetArgs> AllocationPoolsCollection
        {
            get => _allocationPoolsCollection ?? (_allocationPoolsCollection = new InputList<Inputs.SubnetAllocationPoolsCollectionGetArgs>());
            set => _allocationPoolsCollection = value;
        }

        /// <summary>
        /// CIDR representing IP range for this subnet, based on IP
        /// version. You can omit this option if you are creating a subnet from a
        /// subnet pool.
        /// </summary>
        [Input("cidr")]
        public Input<string>? Cidr { get; set; }

        /// <summary>
        /// Human-readable description of the subnet. Changing this
        /// updates the name of the existing subnet.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("dnsNameservers")]
        private InputList<string>? _dnsNameservers;

        /// <summary>
        /// An array of DNS name server names used by hosts
        /// in this subnet. Changing this updates the DNS name servers for the existing
        /// subnet.
        /// </summary>
        public InputList<string> DnsNameservers
        {
            get => _dnsNameservers ?? (_dnsNameservers = new InputList<string>());
            set => _dnsNameservers = value;
        }

        /// <summary>
        /// The administrative state of the network.
        /// Acceptable values are "true" and "false". Changing this value enables or
        /// disables the DHCP capabilities of the existing subnet. Defaults to true.
        /// </summary>
        [Input("enableDhcp")]
        public Input<bool>? EnableDhcp { get; set; }

        /// <summary>
        /// Default gateway used by devices in this subnet.
        /// Leaving this blank and not setting `no_gateway` will cause a default
        /// gateway of `.1` to be used. Changing this updates the gateway IP of the
        /// existing subnet.
        /// </summary>
        [Input("gatewayIp")]
        public Input<string>? GatewayIp { get; set; }

        [Input("hostRoutes")]
        private InputList<Inputs.SubnetHostRouteGetArgs>? _hostRoutes;

        /// <summary>
        /// (**Deprecated** - use `openstack.networking.SubnetRoute`
        /// instead) An array of routes that should be used by devices
        /// with IPs from this subnet (not including local subnet route). The host_route
        /// object structure is documented below. Changing this updates the host routes
        /// for the existing subnet.
        /// </summary>
        [Obsolete(@"Use openstack_networking_subnet_route_v2 instead")]
        public InputList<Inputs.SubnetHostRouteGetArgs> HostRoutes
        {
            get => _hostRoutes ?? (_hostRoutes = new InputList<Inputs.SubnetHostRouteGetArgs>());
            set => _hostRoutes = value;
        }

        /// <summary>
        /// IP version, either 4 (default) or 6. Changing this creates a
        /// new subnet.
        /// </summary>
        [Input("ipVersion")]
        public Input<int>? IpVersion { get; set; }

        /// <summary>
        /// The IPv6 address mode. Valid values are
        /// `dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
        /// </summary>
        [Input("ipv6AddressMode")]
        public Input<string>? Ipv6AddressMode { get; set; }

        /// <summary>
        /// The IPv6 Router Advertisement mode. Valid values
        /// are `dhcpv6-stateful`, `dhcpv6-stateless`, or `slaac`.
        /// </summary>
        [Input("ipv6RaMode")]
        public Input<string>? Ipv6RaMode { get; set; }

        /// <summary>
        /// The name of the subnet. Changing this updates the name of
        /// the existing subnet.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The UUID of the parent network. Changing this
        /// creates a new subnet.
        /// </summary>
        [Input("networkId")]
        public Input<string>? NetworkId { get; set; }

        /// <summary>
        /// Do not set a gateway IP on this subnet. Changing
        /// this removes or adds a default gateway IP of the existing subnet.
        /// </summary>
        [Input("noGateway")]
        public Input<bool>? NoGateway { get; set; }

        /// <summary>
        /// The prefix length to use when creating a subnet
        /// from a subnet pool. The default subnet pool prefix length that was defined
        /// when creating the subnet pool will be used if not provided. Changing this
        /// creates a new subnet.
        /// </summary>
        [Input("prefixLength")]
        public Input<int>? PrefixLength { get; set; }

        /// <summary>
        /// The region in which to obtain the V2 Networking client.
        /// A Networking client is needed to create a Neutron subnet. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// subnet.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The ID of the subnetpool associated with the subnet.
        /// </summary>
        [Input("subnetpoolId")]
        public Input<string>? SubnetpoolId { get; set; }

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// A set of string tags for the subnet.
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The owner of the subnet. Required if admin wants to
        /// create a subnet for another tenant. Changing this creates a new subnet.
        /// </summary>
        [Input("tenantId")]
        public Input<string>? TenantId { get; set; }

        [Input("valueSpecs")]
        private InputMap<object>? _valueSpecs;

        /// <summary>
        /// Map of additional options.
        /// </summary>
        public InputMap<object> ValueSpecs
        {
            get => _valueSpecs ?? (_valueSpecs = new InputMap<object>());
            set => _valueSpecs = value;
        }

        public SubnetState()
        {
        }
    }
}
