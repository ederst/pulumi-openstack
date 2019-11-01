// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Openstack.Networking
{
    /// <summary>
    /// Manages a V2 router interface resource within OpenStack.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/networking_router_interface_v2.html.markdown.
    /// </summary>
    public partial class RouterInterface : Pulumi.CustomResource
    {
        /// <summary>
        /// ID of the port this interface connects to. Changing
        /// this creates a new router interface.
        /// </summary>
        [Output("portId")]
        public Output<string> PortId { get; private set; } = null!;

        /// <summary>
        /// The region in which to obtain the V2 networking client.
        /// A networking client is needed to create a router. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// router interface.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// ID of the router this interface belongs to. Changing
        /// this creates a new router interface.
        /// </summary>
        [Output("routerId")]
        public Output<string> RouterId { get; private set; } = null!;

        /// <summary>
        /// ID of the subnet this interface connects to. Changing
        /// this creates a new router interface.
        /// </summary>
        [Output("subnetId")]
        public Output<string> SubnetId { get; private set; } = null!;


        /// <summary>
        /// Create a RouterInterface resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public RouterInterface(string name, RouterInterfaceArgs args, CustomResourceOptions? options = null)
            : base("openstack:networking/routerInterface:RouterInterface", name, args, MakeResourceOptions(options, ""))
        {
        }

        private RouterInterface(string name, Input<string> id, RouterInterfaceState? state = null, CustomResourceOptions? options = null)
            : base("openstack:networking/routerInterface:RouterInterface", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing RouterInterface resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static RouterInterface Get(string name, Input<string> id, RouterInterfaceState? state = null, CustomResourceOptions? options = null)
        {
            return new RouterInterface(name, id, state, options);
        }
    }

    public sealed class RouterInterfaceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// ID of the port this interface connects to. Changing
        /// this creates a new router interface.
        /// </summary>
        [Input("portId")]
        public Input<string>? PortId { get; set; }

        /// <summary>
        /// The region in which to obtain the V2 networking client.
        /// A networking client is needed to create a router. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// router interface.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// ID of the router this interface belongs to. Changing
        /// this creates a new router interface.
        /// </summary>
        [Input("routerId", required: true)]
        public Input<string> RouterId { get; set; } = null!;

        /// <summary>
        /// ID of the subnet this interface connects to. Changing
        /// this creates a new router interface.
        /// </summary>
        [Input("subnetId")]
        public Input<string>? SubnetId { get; set; }

        public RouterInterfaceArgs()
        {
        }
    }

    public sealed class RouterInterfaceState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// ID of the port this interface connects to. Changing
        /// this creates a new router interface.
        /// </summary>
        [Input("portId")]
        public Input<string>? PortId { get; set; }

        /// <summary>
        /// The region in which to obtain the V2 networking client.
        /// A networking client is needed to create a router. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// router interface.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// ID of the router this interface belongs to. Changing
        /// this creates a new router interface.
        /// </summary>
        [Input("routerId")]
        public Input<string>? RouterId { get; set; }

        /// <summary>
        /// ID of the subnet this interface connects to. Changing
        /// this creates a new router interface.
        /// </summary>
        [Input("subnetId")]
        public Input<string>? SubnetId { get; set; }

        public RouterInterfaceState()
        {
        }
    }
}
