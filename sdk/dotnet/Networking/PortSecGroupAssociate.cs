// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Openstack.Networking
{
    /// <summary>
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/networking_port_secgroup_associate_v2.html.markdown.
    /// </summary>
    public partial class PortSecGroupAssociate : Pulumi.CustomResource
    {
        /// <summary>
        /// The collection of Security Group IDs on the port
        /// which have been explicitly and implicitly added.
        /// </summary>
        [Output("allSecurityGroupIds")]
        public Output<ImmutableArray<string>> AllSecurityGroupIds { get; private set; } = null!;

        /// <summary>
        /// Whether to replace or append the list of security
        /// groups, specified in the `security_group_ids`. Defaults to `false`.
        /// </summary>
        [Output("enforce")]
        public Output<bool?> Enforce { get; private set; } = null!;

        /// <summary>
        /// An UUID of the port to apply security groups to.
        /// </summary>
        [Output("portId")]
        public Output<string> PortId { get; private set; } = null!;

        /// <summary>
        /// The region in which to obtain the V2 networking client.
        /// A networking client is needed to manage a port. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// resource.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// A list of security group IDs to apply to
        /// the port. The security groups must be specified by ID and not name (as
        /// opposed to how they are configured with the Compute Instance).
        /// </summary>
        [Output("securityGroupIds")]
        public Output<ImmutableArray<string>> SecurityGroupIds { get; private set; } = null!;


        /// <summary>
        /// Create a PortSecGroupAssociate resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public PortSecGroupAssociate(string name, PortSecGroupAssociateArgs args, CustomResourceOptions? options = null)
            : base("openstack:networking/portSecGroupAssociate:PortSecGroupAssociate", name, args, MakeResourceOptions(options, ""))
        {
        }

        private PortSecGroupAssociate(string name, Input<string> id, PortSecGroupAssociateState? state = null, CustomResourceOptions? options = null)
            : base("openstack:networking/portSecGroupAssociate:PortSecGroupAssociate", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing PortSecGroupAssociate resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static PortSecGroupAssociate Get(string name, Input<string> id, PortSecGroupAssociateState? state = null, CustomResourceOptions? options = null)
        {
            return new PortSecGroupAssociate(name, id, state, options);
        }
    }

    public sealed class PortSecGroupAssociateArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Whether to replace or append the list of security
        /// groups, specified in the `security_group_ids`. Defaults to `false`.
        /// </summary>
        [Input("enforce")]
        public Input<bool>? Enforce { get; set; }

        /// <summary>
        /// An UUID of the port to apply security groups to.
        /// </summary>
        [Input("portId", required: true)]
        public Input<string> PortId { get; set; } = null!;

        /// <summary>
        /// The region in which to obtain the V2 networking client.
        /// A networking client is needed to manage a port. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// resource.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("securityGroupIds", required: true)]
        private InputList<string>? _securityGroupIds;

        /// <summary>
        /// A list of security group IDs to apply to
        /// the port. The security groups must be specified by ID and not name (as
        /// opposed to how they are configured with the Compute Instance).
        /// </summary>
        public InputList<string> SecurityGroupIds
        {
            get => _securityGroupIds ?? (_securityGroupIds = new InputList<string>());
            set => _securityGroupIds = value;
        }

        public PortSecGroupAssociateArgs()
        {
        }
    }

    public sealed class PortSecGroupAssociateState : Pulumi.ResourceArgs
    {
        [Input("allSecurityGroupIds")]
        private InputList<string>? _allSecurityGroupIds;

        /// <summary>
        /// The collection of Security Group IDs on the port
        /// which have been explicitly and implicitly added.
        /// </summary>
        public InputList<string> AllSecurityGroupIds
        {
            get => _allSecurityGroupIds ?? (_allSecurityGroupIds = new InputList<string>());
            set => _allSecurityGroupIds = value;
        }

        /// <summary>
        /// Whether to replace or append the list of security
        /// groups, specified in the `security_group_ids`. Defaults to `false`.
        /// </summary>
        [Input("enforce")]
        public Input<bool>? Enforce { get; set; }

        /// <summary>
        /// An UUID of the port to apply security groups to.
        /// </summary>
        [Input("portId")]
        public Input<string>? PortId { get; set; }

        /// <summary>
        /// The region in which to obtain the V2 networking client.
        /// A networking client is needed to manage a port. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// resource.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("securityGroupIds")]
        private InputList<string>? _securityGroupIds;

        /// <summary>
        /// A list of security group IDs to apply to
        /// the port. The security groups must be specified by ID and not name (as
        /// opposed to how they are configured with the Compute Instance).
        /// </summary>
        public InputList<string> SecurityGroupIds
        {
            get => _securityGroupIds ?? (_securityGroupIds = new InputList<string>());
            set => _securityGroupIds = value;
        }

        public PortSecGroupAssociateState()
        {
        }
    }
}
