// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Openstack.Networking
{
    /// <summary>
    /// Manages a V2 neutron security group rule resource within OpenStack.
    /// Unlike Nova security groups, neutron separates the group from the rules
    /// and also allows an admin to target a specific tenant_id.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/networking_secgroup_rule_v2.html.markdown.
    /// </summary>
    public partial class SecGroupRule : Pulumi.CustomResource
    {
        /// <summary>
        /// A description of the rule. Changing this creates a new security group rule.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The direction of the rule, valid values are __ingress__
        /// or __egress__. Changing this creates a new security group rule.
        /// </summary>
        [Output("direction")]
        public Output<string> Direction { get; private set; } = null!;

        /// <summary>
        /// The layer 3 protocol type, valid values are __IPv4__
        /// or __IPv6__. Changing this creates a new security group rule.
        /// </summary>
        [Output("ethertype")]
        public Output<string> Ethertype { get; private set; } = null!;

        /// <summary>
        /// The higher part of the allowed port range, valid
        /// integer value needs to be between 1 and 65535. Changing this creates a new
        /// security group rule.
        /// </summary>
        [Output("portRangeMax")]
        public Output<int> PortRangeMax { get; private set; } = null!;

        /// <summary>
        /// The lower part of the allowed port range, valid
        /// integer value needs to be between 1 and 65535. Changing this creates a new
        /// security group rule.
        /// </summary>
        [Output("portRangeMin")]
        public Output<int> PortRangeMin { get; private set; } = null!;

        /// <summary>
        /// The layer 4 protocol type, valid values are following. Changing this creates a new security group rule. This is required if you want to specify a port range.
        /// * __tcp__
        /// * __udp__
        /// * __icmp__
        /// * __ah__
        /// * __dccp__
        /// * __egp__
        /// * __esp__
        /// * __gre__
        /// * __igmp__
        /// * __ipv6-encap__
        /// * __ipv6-frag__
        /// * __ipv6-icmp__
        /// * __ipv6-nonxt__
        /// * __ipv6-opts__
        /// * __ipv6-route__
        /// * __ospf__
        /// * __pgm__
        /// * __rsvp__
        /// * __sctp__
        /// * __udplite__
        /// * __vrrp__
        /// </summary>
        [Output("protocol")]
        public Output<string> Protocol { get; private set; } = null!;

        /// <summary>
        /// The region in which to obtain the V2 networking client.
        /// A networking client is needed to create a port. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// security group rule.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// The remote group id, the value needs to be an
        /// Openstack ID of a security group in the same tenant. Changing this creates
        /// a new security group rule.
        /// </summary>
        [Output("remoteGroupId")]
        public Output<string> RemoteGroupId { get; private set; } = null!;

        /// <summary>
        /// The remote CIDR, the value needs to be a valid
        /// CIDR (i.e. 192.168.0.0/16). Changing this creates a new security group rule.
        /// </summary>
        [Output("remoteIpPrefix")]
        public Output<string> RemoteIpPrefix { get; private set; } = null!;

        /// <summary>
        /// The security group id the rule should belong
        /// to, the value needs to be an Openstack ID of a security group in the same
        /// tenant. Changing this creates a new security group rule.
        /// </summary>
        [Output("securityGroupId")]
        public Output<string> SecurityGroupId { get; private set; } = null!;

        /// <summary>
        /// The owner of the security group. Required if admin
        /// wants to create a port for another tenant. Changing this creates a new
        /// security group rule.
        /// </summary>
        [Output("tenantId")]
        public Output<string> TenantId { get; private set; } = null!;


        /// <summary>
        /// Create a SecGroupRule resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SecGroupRule(string name, SecGroupRuleArgs args, CustomResourceOptions? options = null)
            : base("openstack:networking/secGroupRule:SecGroupRule", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private SecGroupRule(string name, Input<string> id, SecGroupRuleState? state = null, CustomResourceOptions? options = null)
            : base("openstack:networking/secGroupRule:SecGroupRule", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing SecGroupRule resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SecGroupRule Get(string name, Input<string> id, SecGroupRuleState? state = null, CustomResourceOptions? options = null)
        {
            return new SecGroupRule(name, id, state, options);
        }
    }

    public sealed class SecGroupRuleArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A description of the rule. Changing this creates a new security group rule.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The direction of the rule, valid values are __ingress__
        /// or __egress__. Changing this creates a new security group rule.
        /// </summary>
        [Input("direction", required: true)]
        public Input<string> Direction { get; set; } = null!;

        /// <summary>
        /// The layer 3 protocol type, valid values are __IPv4__
        /// or __IPv6__. Changing this creates a new security group rule.
        /// </summary>
        [Input("ethertype", required: true)]
        public Input<string> Ethertype { get; set; } = null!;

        /// <summary>
        /// The higher part of the allowed port range, valid
        /// integer value needs to be between 1 and 65535. Changing this creates a new
        /// security group rule.
        /// </summary>
        [Input("portRangeMax")]
        public Input<int>? PortRangeMax { get; set; }

        /// <summary>
        /// The lower part of the allowed port range, valid
        /// integer value needs to be between 1 and 65535. Changing this creates a new
        /// security group rule.
        /// </summary>
        [Input("portRangeMin")]
        public Input<int>? PortRangeMin { get; set; }

        /// <summary>
        /// The layer 4 protocol type, valid values are following. Changing this creates a new security group rule. This is required if you want to specify a port range.
        /// * __tcp__
        /// * __udp__
        /// * __icmp__
        /// * __ah__
        /// * __dccp__
        /// * __egp__
        /// * __esp__
        /// * __gre__
        /// * __igmp__
        /// * __ipv6-encap__
        /// * __ipv6-frag__
        /// * __ipv6-icmp__
        /// * __ipv6-nonxt__
        /// * __ipv6-opts__
        /// * __ipv6-route__
        /// * __ospf__
        /// * __pgm__
        /// * __rsvp__
        /// * __sctp__
        /// * __udplite__
        /// * __vrrp__
        /// </summary>
        [Input("protocol")]
        public Input<string>? Protocol { get; set; }

        /// <summary>
        /// The region in which to obtain the V2 networking client.
        /// A networking client is needed to create a port. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// security group rule.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The remote group id, the value needs to be an
        /// Openstack ID of a security group in the same tenant. Changing this creates
        /// a new security group rule.
        /// </summary>
        [Input("remoteGroupId")]
        public Input<string>? RemoteGroupId { get; set; }

        /// <summary>
        /// The remote CIDR, the value needs to be a valid
        /// CIDR (i.e. 192.168.0.0/16). Changing this creates a new security group rule.
        /// </summary>
        [Input("remoteIpPrefix")]
        public Input<string>? RemoteIpPrefix { get; set; }

        /// <summary>
        /// The security group id the rule should belong
        /// to, the value needs to be an Openstack ID of a security group in the same
        /// tenant. Changing this creates a new security group rule.
        /// </summary>
        [Input("securityGroupId", required: true)]
        public Input<string> SecurityGroupId { get; set; } = null!;

        /// <summary>
        /// The owner of the security group. Required if admin
        /// wants to create a port for another tenant. Changing this creates a new
        /// security group rule.
        /// </summary>
        [Input("tenantId")]
        public Input<string>? TenantId { get; set; }

        public SecGroupRuleArgs()
        {
        }
    }

    public sealed class SecGroupRuleState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A description of the rule. Changing this creates a new security group rule.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The direction of the rule, valid values are __ingress__
        /// or __egress__. Changing this creates a new security group rule.
        /// </summary>
        [Input("direction")]
        public Input<string>? Direction { get; set; }

        /// <summary>
        /// The layer 3 protocol type, valid values are __IPv4__
        /// or __IPv6__. Changing this creates a new security group rule.
        /// </summary>
        [Input("ethertype")]
        public Input<string>? Ethertype { get; set; }

        /// <summary>
        /// The higher part of the allowed port range, valid
        /// integer value needs to be between 1 and 65535. Changing this creates a new
        /// security group rule.
        /// </summary>
        [Input("portRangeMax")]
        public Input<int>? PortRangeMax { get; set; }

        /// <summary>
        /// The lower part of the allowed port range, valid
        /// integer value needs to be between 1 and 65535. Changing this creates a new
        /// security group rule.
        /// </summary>
        [Input("portRangeMin")]
        public Input<int>? PortRangeMin { get; set; }

        /// <summary>
        /// The layer 4 protocol type, valid values are following. Changing this creates a new security group rule. This is required if you want to specify a port range.
        /// * __tcp__
        /// * __udp__
        /// * __icmp__
        /// * __ah__
        /// * __dccp__
        /// * __egp__
        /// * __esp__
        /// * __gre__
        /// * __igmp__
        /// * __ipv6-encap__
        /// * __ipv6-frag__
        /// * __ipv6-icmp__
        /// * __ipv6-nonxt__
        /// * __ipv6-opts__
        /// * __ipv6-route__
        /// * __ospf__
        /// * __pgm__
        /// * __rsvp__
        /// * __sctp__
        /// * __udplite__
        /// * __vrrp__
        /// </summary>
        [Input("protocol")]
        public Input<string>? Protocol { get; set; }

        /// <summary>
        /// The region in which to obtain the V2 networking client.
        /// A networking client is needed to create a port. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// security group rule.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The remote group id, the value needs to be an
        /// Openstack ID of a security group in the same tenant. Changing this creates
        /// a new security group rule.
        /// </summary>
        [Input("remoteGroupId")]
        public Input<string>? RemoteGroupId { get; set; }

        /// <summary>
        /// The remote CIDR, the value needs to be a valid
        /// CIDR (i.e. 192.168.0.0/16). Changing this creates a new security group rule.
        /// </summary>
        [Input("remoteIpPrefix")]
        public Input<string>? RemoteIpPrefix { get; set; }

        /// <summary>
        /// The security group id the rule should belong
        /// to, the value needs to be an Openstack ID of a security group in the same
        /// tenant. Changing this creates a new security group rule.
        /// </summary>
        [Input("securityGroupId")]
        public Input<string>? SecurityGroupId { get; set; }

        /// <summary>
        /// The owner of the security group. Required if admin
        /// wants to create a port for another tenant. Changing this creates a new
        /// security group rule.
        /// </summary>
        [Input("tenantId")]
        public Input<string>? TenantId { get; set; }

        public SecGroupRuleState()
        {
        }
    }
}
