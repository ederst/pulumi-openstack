// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Openstack.Compute
{
    /// <summary>
    /// Manages a V2 Server Group resource within OpenStack.
    /// 
    /// ## Policies
    /// 
    /// * `affinity` - All instances/servers launched in this group will be hosted on
    ///     the same compute node.
    /// 
    /// * `anti-affinity` - All instances/servers launched in this group will be
    ///     hosted on different compute nodes.
    /// 
    /// * `soft-affinity` - All instances/servers launched in this group will be hosted
    ///     on the same compute node if possible, but if not possible they
    ///     still will be scheduled instead of failure. To use this policy your
    ///     OpenStack environment should support Compute service API 2.15 or above.
    /// 
    /// * `soft-anti-affinity` - All instances/servers launched in this group will be
    ///     hosted on different compute nodes if possible, but if not possible they
    ///     still will be scheduled instead of failure. To use this policy your
    ///     OpenStack environment should support Compute service API 2.15 or above.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_servergroup_v2.html.markdown.
    /// </summary>
    public partial class ServerGroup : Pulumi.CustomResource
    {
        /// <summary>
        /// The instances that are part of this server group.
        /// </summary>
        [Output("members")]
        public Output<ImmutableArray<string>> Members { get; private set; } = null!;

        /// <summary>
        /// A unique name for the server group. Changing this creates
        /// a new server group.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The set of policies for the server group. All policies
        /// are mutually exclusive. See the Policies section for more information.
        /// Changing this creates a new server group.
        /// </summary>
        [Output("policies")]
        public Output<ImmutableArray<string>> Policies { get; private set; } = null!;

        /// <summary>
        /// The region in which to obtain the V2 Compute client.
        /// If omitted, the `region` argument of the provider is used. Changing
        /// this creates a new server group.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// Map of additional options.
        /// </summary>
        [Output("valueSpecs")]
        public Output<ImmutableDictionary<string, object>?> ValueSpecs { get; private set; } = null!;


        /// <summary>
        /// Create a ServerGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ServerGroup(string name, ServerGroupArgs? args = null, CustomResourceOptions? options = null)
            : base("openstack:compute/serverGroup:ServerGroup", name, args, MakeResourceOptions(options, ""))
        {
        }

        private ServerGroup(string name, Input<string> id, ServerGroupState? state = null, CustomResourceOptions? options = null)
            : base("openstack:compute/serverGroup:ServerGroup", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ServerGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ServerGroup Get(string name, Input<string> id, ServerGroupState? state = null, CustomResourceOptions? options = null)
        {
            return new ServerGroup(name, id, state, options);
        }
    }

    public sealed class ServerGroupArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A unique name for the server group. Changing this creates
        /// a new server group.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("policies")]
        private InputList<string>? _policies;

        /// <summary>
        /// The set of policies for the server group. All policies
        /// are mutually exclusive. See the Policies section for more information.
        /// Changing this creates a new server group.
        /// </summary>
        public InputList<string> Policies
        {
            get => _policies ?? (_policies = new InputList<string>());
            set => _policies = value;
        }

        /// <summary>
        /// The region in which to obtain the V2 Compute client.
        /// If omitted, the `region` argument of the provider is used. Changing
        /// this creates a new server group.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

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

        public ServerGroupArgs()
        {
        }
    }

    public sealed class ServerGroupState : Pulumi.ResourceArgs
    {
        [Input("members")]
        private InputList<string>? _members;

        /// <summary>
        /// The instances that are part of this server group.
        /// </summary>
        public InputList<string> Members
        {
            get => _members ?? (_members = new InputList<string>());
            set => _members = value;
        }

        /// <summary>
        /// A unique name for the server group. Changing this creates
        /// a new server group.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("policies")]
        private InputList<string>? _policies;

        /// <summary>
        /// The set of policies for the server group. All policies
        /// are mutually exclusive. See the Policies section for more information.
        /// Changing this creates a new server group.
        /// </summary>
        public InputList<string> Policies
        {
            get => _policies ?? (_policies = new InputList<string>());
            set => _policies = value;
        }

        /// <summary>
        /// The region in which to obtain the V2 Compute client.
        /// If omitted, the `region` argument of the provider is used. Changing
        /// this creates a new server group.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

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

        public ServerGroupState()
        {
        }
    }
}
