// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Openstack.Firewall
{
    /// <summary>
    /// Manages a v1 firewall policy resource within OpenStack.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/fw_policy_v1.html.markdown.
    /// </summary>
    public partial class Policy : Pulumi.CustomResource
    {
        /// <summary>
        /// Audit status of the firewall policy
        /// (must be "true" or "false" if provided - defaults to "false").
        /// This status is set to "false" whenever the firewall policy or any of its
        /// rules are changed. Changing this updates the `audited` status of an existing
        /// firewall policy.
        /// </summary>
        [Output("audited")]
        public Output<bool?> Audited { get; private set; } = null!;

        /// <summary>
        /// A description for the firewall policy. Changing
        /// this updates the `description` of an existing firewall policy.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// A name for the firewall policy. Changing this
        /// updates the `name` of an existing firewall policy.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The region in which to obtain the v1 networking client.
        /// A networking client is needed to create a firewall policy. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// firewall policy.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// An array of one or more firewall rules that comprise
        /// the policy. Changing this results in adding/removing rules from the
        /// existing firewall policy.
        /// </summary>
        [Output("rules")]
        public Output<ImmutableArray<string>> Rules { get; private set; } = null!;

        /// <summary>
        /// Sharing status of the firewall policy (must be "true"
        /// or "false" if provided). If this is "true" the policy is visible to, and
        /// can be used in, firewalls in other tenants. Changing this updates the
        /// `shared` status of an existing firewall policy. Only administrative users
        /// can specify if the policy should be shared.
        /// </summary>
        [Output("shared")]
        public Output<bool?> Shared { get; private set; } = null!;

        [Output("tenantId")]
        public Output<string> TenantId { get; private set; } = null!;

        /// <summary>
        /// Map of additional options.
        /// </summary>
        [Output("valueSpecs")]
        public Output<ImmutableDictionary<string, object>?> ValueSpecs { get; private set; } = null!;


        /// <summary>
        /// Create a Policy resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Policy(string name, PolicyArgs? args = null, CustomResourceOptions? options = null)
            : base("openstack:firewall/policy:Policy", name, args, MakeResourceOptions(options, ""))
        {
        }

        private Policy(string name, Input<string> id, PolicyState? state = null, CustomResourceOptions? options = null)
            : base("openstack:firewall/policy:Policy", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Policy resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Policy Get(string name, Input<string> id, PolicyState? state = null, CustomResourceOptions? options = null)
        {
            return new Policy(name, id, state, options);
        }
    }

    public sealed class PolicyArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Audit status of the firewall policy
        /// (must be "true" or "false" if provided - defaults to "false").
        /// This status is set to "false" whenever the firewall policy or any of its
        /// rules are changed. Changing this updates the `audited` status of an existing
        /// firewall policy.
        /// </summary>
        [Input("audited")]
        public Input<bool>? Audited { get; set; }

        /// <summary>
        /// A description for the firewall policy. Changing
        /// this updates the `description` of an existing firewall policy.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// A name for the firewall policy. Changing this
        /// updates the `name` of an existing firewall policy.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The region in which to obtain the v1 networking client.
        /// A networking client is needed to create a firewall policy. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// firewall policy.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("rules")]
        private InputList<string>? _rules;

        /// <summary>
        /// An array of one or more firewall rules that comprise
        /// the policy. Changing this results in adding/removing rules from the
        /// existing firewall policy.
        /// </summary>
        public InputList<string> Rules
        {
            get => _rules ?? (_rules = new InputList<string>());
            set => _rules = value;
        }

        /// <summary>
        /// Sharing status of the firewall policy (must be "true"
        /// or "false" if provided). If this is "true" the policy is visible to, and
        /// can be used in, firewalls in other tenants. Changing this updates the
        /// `shared` status of an existing firewall policy. Only administrative users
        /// can specify if the policy should be shared.
        /// </summary>
        [Input("shared")]
        public Input<bool>? Shared { get; set; }

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

        public PolicyArgs()
        {
        }
    }

    public sealed class PolicyState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Audit status of the firewall policy
        /// (must be "true" or "false" if provided - defaults to "false").
        /// This status is set to "false" whenever the firewall policy or any of its
        /// rules are changed. Changing this updates the `audited` status of an existing
        /// firewall policy.
        /// </summary>
        [Input("audited")]
        public Input<bool>? Audited { get; set; }

        /// <summary>
        /// A description for the firewall policy. Changing
        /// this updates the `description` of an existing firewall policy.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// A name for the firewall policy. Changing this
        /// updates the `name` of an existing firewall policy.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The region in which to obtain the v1 networking client.
        /// A networking client is needed to create a firewall policy. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// firewall policy.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("rules")]
        private InputList<string>? _rules;

        /// <summary>
        /// An array of one or more firewall rules that comprise
        /// the policy. Changing this results in adding/removing rules from the
        /// existing firewall policy.
        /// </summary>
        public InputList<string> Rules
        {
            get => _rules ?? (_rules = new InputList<string>());
            set => _rules = value;
        }

        /// <summary>
        /// Sharing status of the firewall policy (must be "true"
        /// or "false" if provided). If this is "true" the policy is visible to, and
        /// can be used in, firewalls in other tenants. Changing this updates the
        /// `shared` status of an existing firewall policy. Only administrative users
        /// can specify if the policy should be shared.
        /// </summary>
        [Input("shared")]
        public Input<bool>? Shared { get; set; }

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

        public PolicyState()
        {
        }
    }
}
