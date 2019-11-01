// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Openstack.Loadbalancer
{
    /// <summary>
    /// Manages a V2 member resource within OpenStack.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/lb_member_v2.html.markdown.
    /// </summary>
    public partial class Member : Pulumi.CustomResource
    {
        /// <summary>
        /// The IP address of the member to receive traffic from
        /// the load balancer. Changing this creates a new member.
        /// </summary>
        [Output("address")]
        public Output<string> Address { get; private set; } = null!;

        /// <summary>
        /// The administrative state of the member.
        /// A valid value is true (UP) or false (DOWN).
        /// </summary>
        [Output("adminStateUp")]
        public Output<bool?> AdminStateUp { get; private set; } = null!;

        /// <summary>
        /// Human-readable name for the member.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The id of the pool that this member will be
        /// assigned to.
        /// </summary>
        [Output("poolId")]
        public Output<string> PoolId { get; private set; } = null!;

        /// <summary>
        /// The port on which to listen for client traffic.
        /// Changing this creates a new member.
        /// </summary>
        [Output("protocolPort")]
        public Output<int> ProtocolPort { get; private set; } = null!;

        /// <summary>
        /// The region in which to obtain the V2 Networking client.
        /// A Networking client is needed to create an . If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// member.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// The subnet in which to access the member
        /// </summary>
        [Output("subnetId")]
        public Output<string?> SubnetId { get; private set; } = null!;

        /// <summary>
        /// Required for admins. The UUID of the tenant who owns
        /// the member.  Only administrative users can specify a tenant UUID
        /// other than their own. Changing this creates a new member.
        /// </summary>
        [Output("tenantId")]
        public Output<string> TenantId { get; private set; } = null!;

        /// <summary>
        /// A positive integer value that indicates the relative
        /// portion of traffic that this member should receive from the pool. For
        /// example, a member with a weight of 10 receives five times as much traffic
        /// as a member with a weight of 2.
        /// </summary>
        [Output("weight")]
        public Output<int> Weight { get; private set; } = null!;


        /// <summary>
        /// Create a Member resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Member(string name, MemberArgs args, CustomResourceOptions? options = null)
            : base("openstack:loadbalancer/member:Member", name, args, MakeResourceOptions(options, ""))
        {
        }

        private Member(string name, Input<string> id, MemberState? state = null, CustomResourceOptions? options = null)
            : base("openstack:loadbalancer/member:Member", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Member resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Member Get(string name, Input<string> id, MemberState? state = null, CustomResourceOptions? options = null)
        {
            return new Member(name, id, state, options);
        }
    }

    public sealed class MemberArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The IP address of the member to receive traffic from
        /// the load balancer. Changing this creates a new member.
        /// </summary>
        [Input("address", required: true)]
        public Input<string> Address { get; set; } = null!;

        /// <summary>
        /// The administrative state of the member.
        /// A valid value is true (UP) or false (DOWN).
        /// </summary>
        [Input("adminStateUp")]
        public Input<bool>? AdminStateUp { get; set; }

        /// <summary>
        /// Human-readable name for the member.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The id of the pool that this member will be
        /// assigned to.
        /// </summary>
        [Input("poolId", required: true)]
        public Input<string> PoolId { get; set; } = null!;

        /// <summary>
        /// The port on which to listen for client traffic.
        /// Changing this creates a new member.
        /// </summary>
        [Input("protocolPort", required: true)]
        public Input<int> ProtocolPort { get; set; } = null!;

        /// <summary>
        /// The region in which to obtain the V2 Networking client.
        /// A Networking client is needed to create an . If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// member.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The subnet in which to access the member
        /// </summary>
        [Input("subnetId")]
        public Input<string>? SubnetId { get; set; }

        /// <summary>
        /// Required for admins. The UUID of the tenant who owns
        /// the member.  Only administrative users can specify a tenant UUID
        /// other than their own. Changing this creates a new member.
        /// </summary>
        [Input("tenantId")]
        public Input<string>? TenantId { get; set; }

        /// <summary>
        /// A positive integer value that indicates the relative
        /// portion of traffic that this member should receive from the pool. For
        /// example, a member with a weight of 10 receives five times as much traffic
        /// as a member with a weight of 2.
        /// </summary>
        [Input("weight")]
        public Input<int>? Weight { get; set; }

        public MemberArgs()
        {
        }
    }

    public sealed class MemberState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The IP address of the member to receive traffic from
        /// the load balancer. Changing this creates a new member.
        /// </summary>
        [Input("address")]
        public Input<string>? Address { get; set; }

        /// <summary>
        /// The administrative state of the member.
        /// A valid value is true (UP) or false (DOWN).
        /// </summary>
        [Input("adminStateUp")]
        public Input<bool>? AdminStateUp { get; set; }

        /// <summary>
        /// Human-readable name for the member.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The id of the pool that this member will be
        /// assigned to.
        /// </summary>
        [Input("poolId")]
        public Input<string>? PoolId { get; set; }

        /// <summary>
        /// The port on which to listen for client traffic.
        /// Changing this creates a new member.
        /// </summary>
        [Input("protocolPort")]
        public Input<int>? ProtocolPort { get; set; }

        /// <summary>
        /// The region in which to obtain the V2 Networking client.
        /// A Networking client is needed to create an . If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// member.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The subnet in which to access the member
        /// </summary>
        [Input("subnetId")]
        public Input<string>? SubnetId { get; set; }

        /// <summary>
        /// Required for admins. The UUID of the tenant who owns
        /// the member.  Only administrative users can specify a tenant UUID
        /// other than their own. Changing this creates a new member.
        /// </summary>
        [Input("tenantId")]
        public Input<string>? TenantId { get; set; }

        /// <summary>
        /// A positive integer value that indicates the relative
        /// portion of traffic that this member should receive from the pool. For
        /// example, a member with a weight of 10 receives five times as much traffic
        /// as a member with a weight of 2.
        /// </summary>
        [Input("weight")]
        public Input<int>? Weight { get; set; }

        public MemberState()
        {
        }
    }
}
