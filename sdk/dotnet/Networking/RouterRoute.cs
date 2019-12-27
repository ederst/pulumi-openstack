// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OpenStack.Networking
{
    /// <summary>
    /// Creates a routing entry on a OpenStack V2 router.
    /// 
    /// ## Notes
    /// 
    /// The `next_hop` IP address must be directly reachable from the router at the ``openstack.networking.RouterRoute``
    /// resource creation time.  You can ensure that by explicitly specifying a dependency on the ``openstack.networking.RouterInterface``
    /// resource that connects the next hop to the router, as in the example above.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/networking_router_route_v2.html.markdown.
    /// </summary>
    public partial class RouterRoute : Pulumi.CustomResource
    {
        /// <summary>
        /// CIDR block to match on the packet’s destination IP. Changing
        /// this creates a new routing entry.
        /// </summary>
        [Output("destinationCidr")]
        public Output<string> DestinationCidr { get; private set; } = null!;

        /// <summary>
        /// IP address of the next hop gateway.  Changing
        /// this creates a new routing entry.
        /// </summary>
        [Output("nextHop")]
        public Output<string> NextHop { get; private set; } = null!;

        /// <summary>
        /// The region in which to obtain the V2 networking client.
        /// A networking client is needed to configure a routing entry on a router. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// routing entry.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// ID of the router this routing entry belongs to. Changing
        /// this creates a new routing entry.
        /// </summary>
        [Output("routerId")]
        public Output<string> RouterId { get; private set; } = null!;


        /// <summary>
        /// Create a RouterRoute resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public RouterRoute(string name, RouterRouteArgs args, CustomResourceOptions? options = null)
            : base("openstack:networking/routerRoute:RouterRoute", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private RouterRoute(string name, Input<string> id, RouterRouteState? state = null, CustomResourceOptions? options = null)
            : base("openstack:networking/routerRoute:RouterRoute", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing RouterRoute resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static RouterRoute Get(string name, Input<string> id, RouterRouteState? state = null, CustomResourceOptions? options = null)
        {
            return new RouterRoute(name, id, state, options);
        }
    }

    public sealed class RouterRouteArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// CIDR block to match on the packet’s destination IP. Changing
        /// this creates a new routing entry.
        /// </summary>
        [Input("destinationCidr", required: true)]
        public Input<string> DestinationCidr { get; set; } = null!;

        /// <summary>
        /// IP address of the next hop gateway.  Changing
        /// this creates a new routing entry.
        /// </summary>
        [Input("nextHop", required: true)]
        public Input<string> NextHop { get; set; } = null!;

        /// <summary>
        /// The region in which to obtain the V2 networking client.
        /// A networking client is needed to configure a routing entry on a router. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// routing entry.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// ID of the router this routing entry belongs to. Changing
        /// this creates a new routing entry.
        /// </summary>
        [Input("routerId", required: true)]
        public Input<string> RouterId { get; set; } = null!;

        public RouterRouteArgs()
        {
        }
    }

    public sealed class RouterRouteState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// CIDR block to match on the packet’s destination IP. Changing
        /// this creates a new routing entry.
        /// </summary>
        [Input("destinationCidr")]
        public Input<string>? DestinationCidr { get; set; }

        /// <summary>
        /// IP address of the next hop gateway.  Changing
        /// this creates a new routing entry.
        /// </summary>
        [Input("nextHop")]
        public Input<string>? NextHop { get; set; }

        /// <summary>
        /// The region in which to obtain the V2 networking client.
        /// A networking client is needed to configure a routing entry on a router. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// routing entry.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// ID of the router this routing entry belongs to. Changing
        /// this creates a new routing entry.
        /// </summary>
        [Input("routerId")]
        public Input<string>? RouterId { get; set; }

        public RouterRouteState()
        {
        }
    }
}
