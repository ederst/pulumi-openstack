// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OpenStack.LoadBalancer
{
    /// <summary>
    /// Manages a V1 load balancer vip resource within OpenStack.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/lb_vip_v1.html.markdown.
    /// </summary>
    public partial class Vip : Pulumi.CustomResource
    {
        /// <summary>
        /// The IP address of the vip. Changing this creates a new
        /// vip.
        /// </summary>
        [Output("address")]
        public Output<string> Address { get; private set; } = null!;

        /// <summary>
        /// The administrative state of the vip.
        /// Acceptable values are "true" and "false". Changing this value updates the
        /// state of the existing vip.
        /// </summary>
        [Output("adminStateUp")]
        public Output<bool> AdminStateUp { get; private set; } = null!;

        /// <summary>
        /// The maximum number of connections allowed for the
        /// vip. Default is -1, meaning no limit. Changing this updates the conn_limit
        /// of the existing vip.
        /// </summary>
        [Output("connLimit")]
        public Output<int> ConnLimit { get; private set; } = null!;

        /// <summary>
        /// Human-readable description for the vip. Changing
        /// this updates the description of the existing vip.
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// A *Networking* Floating IP that will be associated
        /// with the vip. The Floating IP must be provisioned already.
        /// </summary>
        [Output("floatingIp")]
        public Output<string?> FloatingIp { get; private set; } = null!;

        /// <summary>
        /// The name of the vip. Changing this updates the name of
        /// the existing vip.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Omit this field to prevent session persistence.
        /// The persistence object structure is documented below. Changing this updates
        /// the persistence of the existing vip.
        /// </summary>
        [Output("persistence")]
        public Output<ImmutableDictionary<string, object>?> Persistence { get; private set; } = null!;

        /// <summary>
        /// The ID of the pool with which the vip is associated.
        /// Changing this updates the pool_id of the existing vip.
        /// </summary>
        [Output("poolId")]
        public Output<string> PoolId { get; private set; } = null!;

        /// <summary>
        /// The port on which to listen for client traffic. Changing
        /// this creates a new vip.
        /// </summary>
        [Output("port")]
        public Output<int> Port { get; private set; } = null!;

        /// <summary>
        /// Port UUID for this VIP at associated floating IP (if any).
        /// </summary>
        [Output("portId")]
        public Output<string> PortId { get; private set; } = null!;

        /// <summary>
        /// The protocol - can be either 'TCP, 'HTTP', or
        /// HTTPS'. Changing this creates a new vip.
        /// </summary>
        [Output("protocol")]
        public Output<string> Protocol { get; private set; } = null!;

        /// <summary>
        /// The region in which to obtain the V2 Networking client.
        /// A Networking client is needed to create a VIP. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// VIP.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// The network on which to allocate the vip's address. A
        /// tenant can only create vips on networks authorized by policy (e.g. networks
        /// that belong to them or networks that are shared). Changing this creates a
        /// new vip.
        /// </summary>
        [Output("subnetId")]
        public Output<string> SubnetId { get; private set; } = null!;

        /// <summary>
        /// The owner of the vip. Required if admin wants to
        /// create a vip member for another tenant. Changing this creates a new vip.
        /// </summary>
        [Output("tenantId")]
        public Output<string> TenantId { get; private set; } = null!;


        /// <summary>
        /// Create a Vip resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Vip(string name, VipArgs args, CustomResourceOptions? options = null)
            : base("openstack:loadbalancer/vip:Vip", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private Vip(string name, Input<string> id, VipState? state = null, CustomResourceOptions? options = null)
            : base("openstack:loadbalancer/vip:Vip", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Vip resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Vip Get(string name, Input<string> id, VipState? state = null, CustomResourceOptions? options = null)
        {
            return new Vip(name, id, state, options);
        }
    }

    public sealed class VipArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The IP address of the vip. Changing this creates a new
        /// vip.
        /// </summary>
        [Input("address")]
        public Input<string>? Address { get; set; }

        /// <summary>
        /// The administrative state of the vip.
        /// Acceptable values are "true" and "false". Changing this value updates the
        /// state of the existing vip.
        /// </summary>
        [Input("adminStateUp")]
        public Input<bool>? AdminStateUp { get; set; }

        /// <summary>
        /// The maximum number of connections allowed for the
        /// vip. Default is -1, meaning no limit. Changing this updates the conn_limit
        /// of the existing vip.
        /// </summary>
        [Input("connLimit")]
        public Input<int>? ConnLimit { get; set; }

        /// <summary>
        /// Human-readable description for the vip. Changing
        /// this updates the description of the existing vip.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// A *Networking* Floating IP that will be associated
        /// with the vip. The Floating IP must be provisioned already.
        /// </summary>
        [Input("floatingIp")]
        public Input<string>? FloatingIp { get; set; }

        /// <summary>
        /// The name of the vip. Changing this updates the name of
        /// the existing vip.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("persistence")]
        private InputMap<object>? _persistence;

        /// <summary>
        /// Omit this field to prevent session persistence.
        /// The persistence object structure is documented below. Changing this updates
        /// the persistence of the existing vip.
        /// </summary>
        public InputMap<object> Persistence
        {
            get => _persistence ?? (_persistence = new InputMap<object>());
            set => _persistence = value;
        }

        /// <summary>
        /// The ID of the pool with which the vip is associated.
        /// Changing this updates the pool_id of the existing vip.
        /// </summary>
        [Input("poolId", required: true)]
        public Input<string> PoolId { get; set; } = null!;

        /// <summary>
        /// The port on which to listen for client traffic. Changing
        /// this creates a new vip.
        /// </summary>
        [Input("port", required: true)]
        public Input<int> Port { get; set; } = null!;

        /// <summary>
        /// The protocol - can be either 'TCP, 'HTTP', or
        /// HTTPS'. Changing this creates a new vip.
        /// </summary>
        [Input("protocol", required: true)]
        public Input<string> Protocol { get; set; } = null!;

        /// <summary>
        /// The region in which to obtain the V2 Networking client.
        /// A Networking client is needed to create a VIP. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// VIP.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The network on which to allocate the vip's address. A
        /// tenant can only create vips on networks authorized by policy (e.g. networks
        /// that belong to them or networks that are shared). Changing this creates a
        /// new vip.
        /// </summary>
        [Input("subnetId", required: true)]
        public Input<string> SubnetId { get; set; } = null!;

        /// <summary>
        /// The owner of the vip. Required if admin wants to
        /// create a vip member for another tenant. Changing this creates a new vip.
        /// </summary>
        [Input("tenantId")]
        public Input<string>? TenantId { get; set; }

        public VipArgs()
        {
        }
    }

    public sealed class VipState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The IP address of the vip. Changing this creates a new
        /// vip.
        /// </summary>
        [Input("address")]
        public Input<string>? Address { get; set; }

        /// <summary>
        /// The administrative state of the vip.
        /// Acceptable values are "true" and "false". Changing this value updates the
        /// state of the existing vip.
        /// </summary>
        [Input("adminStateUp")]
        public Input<bool>? AdminStateUp { get; set; }

        /// <summary>
        /// The maximum number of connections allowed for the
        /// vip. Default is -1, meaning no limit. Changing this updates the conn_limit
        /// of the existing vip.
        /// </summary>
        [Input("connLimit")]
        public Input<int>? ConnLimit { get; set; }

        /// <summary>
        /// Human-readable description for the vip. Changing
        /// this updates the description of the existing vip.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// A *Networking* Floating IP that will be associated
        /// with the vip. The Floating IP must be provisioned already.
        /// </summary>
        [Input("floatingIp")]
        public Input<string>? FloatingIp { get; set; }

        /// <summary>
        /// The name of the vip. Changing this updates the name of
        /// the existing vip.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("persistence")]
        private InputMap<object>? _persistence;

        /// <summary>
        /// Omit this field to prevent session persistence.
        /// The persistence object structure is documented below. Changing this updates
        /// the persistence of the existing vip.
        /// </summary>
        public InputMap<object> Persistence
        {
            get => _persistence ?? (_persistence = new InputMap<object>());
            set => _persistence = value;
        }

        /// <summary>
        /// The ID of the pool with which the vip is associated.
        /// Changing this updates the pool_id of the existing vip.
        /// </summary>
        [Input("poolId")]
        public Input<string>? PoolId { get; set; }

        /// <summary>
        /// The port on which to listen for client traffic. Changing
        /// this creates a new vip.
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        /// <summary>
        /// Port UUID for this VIP at associated floating IP (if any).
        /// </summary>
        [Input("portId")]
        public Input<string>? PortId { get; set; }

        /// <summary>
        /// The protocol - can be either 'TCP, 'HTTP', or
        /// HTTPS'. Changing this creates a new vip.
        /// </summary>
        [Input("protocol")]
        public Input<string>? Protocol { get; set; }

        /// <summary>
        /// The region in which to obtain the V2 Networking client.
        /// A Networking client is needed to create a VIP. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// VIP.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The network on which to allocate the vip's address. A
        /// tenant can only create vips on networks authorized by policy (e.g. networks
        /// that belong to them or networks that are shared). Changing this creates a
        /// new vip.
        /// </summary>
        [Input("subnetId")]
        public Input<string>? SubnetId { get; set; }

        /// <summary>
        /// The owner of the vip. Required if admin wants to
        /// create a vip member for another tenant. Changing this creates a new vip.
        /// </summary>
        [Input("tenantId")]
        public Input<string>? TenantId { get; set; }

        public VipState()
        {
        }
    }
}
