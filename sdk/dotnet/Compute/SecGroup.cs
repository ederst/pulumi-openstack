// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OpenStack.Compute
{
    /// <summary>
    /// Manages a V2 security group resource within OpenStack.
    /// 
    /// Please note that managing security groups through the OpenStack Compute API
    /// has been deprecated. Unless you are using an older OpenStack environment, it is
    /// recommended to use the `openstack.networking.SecGroup`
    /// and `openstack.networking.SecGroupRule`
    /// resources instead, which uses the OpenStack Networking API.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_secgroup_v2.html.markdown.
    /// </summary>
    public partial class SecGroup : Pulumi.CustomResource
    {
        /// <summary>
        /// A description for the security group. Changing this
        /// updates the `description` of an existing security group.
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// A unique name for the security group. Changing this
        /// updates the `name` of an existing security group.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The region in which to obtain the V2 Compute client.
        /// A Compute client is needed to create a security group. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// security group.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// A rule describing how the security group operates. The
        /// rule object structure is documented below. Changing this updates the
        /// security group rules. As shown in the example above, multiple rule blocks
        /// may be used.
        /// </summary>
        [Output("rules")]
        public Output<ImmutableArray<Outputs.SecGroupRules>> Rules { get; private set; } = null!;


        /// <summary>
        /// Create a SecGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SecGroup(string name, SecGroupArgs args, CustomResourceOptions? options = null)
            : base("openstack:compute/secGroup:SecGroup", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private SecGroup(string name, Input<string> id, SecGroupState? state = null, CustomResourceOptions? options = null)
            : base("openstack:compute/secGroup:SecGroup", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing SecGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SecGroup Get(string name, Input<string> id, SecGroupState? state = null, CustomResourceOptions? options = null)
        {
            return new SecGroup(name, id, state, options);
        }
    }

    public sealed class SecGroupArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A description for the security group. Changing this
        /// updates the `description` of an existing security group.
        /// </summary>
        [Input("description", required: true)]
        public Input<string> Description { get; set; } = null!;

        /// <summary>
        /// A unique name for the security group. Changing this
        /// updates the `name` of an existing security group.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The region in which to obtain the V2 Compute client.
        /// A Compute client is needed to create a security group. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// security group.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("rules")]
        private InputList<Inputs.SecGroupRulesArgs>? _rules;

        /// <summary>
        /// A rule describing how the security group operates. The
        /// rule object structure is documented below. Changing this updates the
        /// security group rules. As shown in the example above, multiple rule blocks
        /// may be used.
        /// </summary>
        public InputList<Inputs.SecGroupRulesArgs> Rules
        {
            get => _rules ?? (_rules = new InputList<Inputs.SecGroupRulesArgs>());
            set => _rules = value;
        }

        public SecGroupArgs()
        {
        }
    }

    public sealed class SecGroupState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A description for the security group. Changing this
        /// updates the `description` of an existing security group.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// A unique name for the security group. Changing this
        /// updates the `name` of an existing security group.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The region in which to obtain the V2 Compute client.
        /// A Compute client is needed to create a security group. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// security group.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("rules")]
        private InputList<Inputs.SecGroupRulesGetArgs>? _rules;

        /// <summary>
        /// A rule describing how the security group operates. The
        /// rule object structure is documented below. Changing this updates the
        /// security group rules. As shown in the example above, multiple rule blocks
        /// may be used.
        /// </summary>
        public InputList<Inputs.SecGroupRulesGetArgs> Rules
        {
            get => _rules ?? (_rules = new InputList<Inputs.SecGroupRulesGetArgs>());
            set => _rules = value;
        }

        public SecGroupState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class SecGroupRulesArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Required if `from_group_id` or `self` is empty. The IP range
        /// that will be the source of network traffic to the security group. Use 0.0.0.0/0
        /// to allow all IP addresses. Changing this creates a new security group rule. Cannot
        /// be combined with `from_group_id` or `self`.
        /// </summary>
        [Input("cidr")]
        public Input<string>? Cidr { get; set; }

        /// <summary>
        /// Required if `cidr` or `self` is empty. The ID of a
        /// group from which to forward traffic to the parent group. Changing this creates a
        /// new security group rule. Cannot be combined with `cidr` or `self`.
        /// </summary>
        [Input("fromGroupId")]
        public Input<string>? FromGroupId { get; set; }

        /// <summary>
        /// An integer representing the lower bound of the port
        /// range to open. Changing this creates a new security group rule.
        /// </summary>
        [Input("fromPort", required: true)]
        public Input<int> FromPort { get; set; } = null!;

        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// The protocol type that will be allowed. Changing
        /// this creates a new security group rule.
        /// </summary>
        [Input("ipProtocol", required: true)]
        public Input<string> IpProtocol { get; set; } = null!;

        /// <summary>
        /// Required if `cidr` and `from_group_id` is empty. If true,
        /// the security group itself will be added as a source to this ingress rule. Cannot
        /// be combined with `cidr` or `from_group_id`.
        /// </summary>
        [Input("self")]
        public Input<bool>? Self { get; set; }

        /// <summary>
        /// An integer representing the upper bound of the port
        /// range to open. Changing this creates a new security group rule.
        /// </summary>
        [Input("toPort", required: true)]
        public Input<int> ToPort { get; set; } = null!;

        public SecGroupRulesArgs()
        {
        }
    }

    public sealed class SecGroupRulesGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Required if `from_group_id` or `self` is empty. The IP range
        /// that will be the source of network traffic to the security group. Use 0.0.0.0/0
        /// to allow all IP addresses. Changing this creates a new security group rule. Cannot
        /// be combined with `from_group_id` or `self`.
        /// </summary>
        [Input("cidr")]
        public Input<string>? Cidr { get; set; }

        /// <summary>
        /// Required if `cidr` or `self` is empty. The ID of a
        /// group from which to forward traffic to the parent group. Changing this creates a
        /// new security group rule. Cannot be combined with `cidr` or `self`.
        /// </summary>
        [Input("fromGroupId")]
        public Input<string>? FromGroupId { get; set; }

        /// <summary>
        /// An integer representing the lower bound of the port
        /// range to open. Changing this creates a new security group rule.
        /// </summary>
        [Input("fromPort", required: true)]
        public Input<int> FromPort { get; set; } = null!;

        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// The protocol type that will be allowed. Changing
        /// this creates a new security group rule.
        /// </summary>
        [Input("ipProtocol", required: true)]
        public Input<string> IpProtocol { get; set; } = null!;

        /// <summary>
        /// Required if `cidr` and `from_group_id` is empty. If true,
        /// the security group itself will be added as a source to this ingress rule. Cannot
        /// be combined with `cidr` or `from_group_id`.
        /// </summary>
        [Input("self")]
        public Input<bool>? Self { get; set; }

        /// <summary>
        /// An integer representing the upper bound of the port
        /// range to open. Changing this creates a new security group rule.
        /// </summary>
        [Input("toPort", required: true)]
        public Input<int> ToPort { get; set; } = null!;

        public SecGroupRulesGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class SecGroupRules
    {
        /// <summary>
        /// Required if `from_group_id` or `self` is empty. The IP range
        /// that will be the source of network traffic to the security group. Use 0.0.0.0/0
        /// to allow all IP addresses. Changing this creates a new security group rule. Cannot
        /// be combined with `from_group_id` or `self`.
        /// </summary>
        public readonly string? Cidr;
        /// <summary>
        /// Required if `cidr` or `self` is empty. The ID of a
        /// group from which to forward traffic to the parent group. Changing this creates a
        /// new security group rule. Cannot be combined with `cidr` or `self`.
        /// </summary>
        public readonly string? FromGroupId;
        /// <summary>
        /// An integer representing the lower bound of the port
        /// range to open. Changing this creates a new security group rule.
        /// </summary>
        public readonly int FromPort;
        public readonly string Id;
        /// <summary>
        /// The protocol type that will be allowed. Changing
        /// this creates a new security group rule.
        /// </summary>
        public readonly string IpProtocol;
        /// <summary>
        /// Required if `cidr` and `from_group_id` is empty. If true,
        /// the security group itself will be added as a source to this ingress rule. Cannot
        /// be combined with `cidr` or `from_group_id`.
        /// </summary>
        public readonly bool? Self;
        /// <summary>
        /// An integer representing the upper bound of the port
        /// range to open. Changing this creates a new security group rule.
        /// </summary>
        public readonly int ToPort;

        [OutputConstructor]
        private SecGroupRules(
            string? cidr,
            string? fromGroupId,
            int fromPort,
            string id,
            string ipProtocol,
            bool? self,
            int toPort)
        {
            Cidr = cidr;
            FromGroupId = fromGroupId;
            FromPort = fromPort;
            Id = id;
            IpProtocol = ipProtocol;
            Self = self;
            ToPort = toPort;
        }
    }
    }
}
