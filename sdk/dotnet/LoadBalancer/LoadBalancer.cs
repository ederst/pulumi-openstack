// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OpenStack.LoadBalancer
{
    /// <summary>
    /// Manages a V2 loadbalancer resource within OpenStack.
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
    ///         var lb1 = new OpenStack.LoadBalancer.LoadBalancer("lb1", new OpenStack.LoadBalancer.LoadBalancerArgs
    ///         {
    ///             VipSubnetId = "d9415786-5f1a-428b-b35f-2f1523e146d2",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// Load Balancer can be imported using the Load Balancer ID, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import openstack:loadbalancer/loadBalancer:LoadBalancer loadbalancer_1 19bcfdc7-c521-4a7e-9459-6750bd16df76
    /// ```
    /// </summary>
    [OpenStackResourceType("openstack:loadbalancer/loadBalancer:LoadBalancer")]
    public partial class LoadBalancer : Pulumi.CustomResource
    {
        /// <summary>
        /// The administrative state of the Loadbalancer.
        /// A valid value is true (UP) or false (DOWN).
        /// </summary>
        [Output("adminStateUp")]
        public Output<bool?> AdminStateUp { get; private set; } = null!;

        /// <summary>
        /// Human-readable description for the Loadbalancer.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The UUID of a flavor. Changing this creates a new
        /// loadbalancer.
        /// </summary>
        [Output("flavorId")]
        public Output<string> FlavorId { get; private set; } = null!;

        /// <summary>
        /// The name of the provider. Changing this
        /// creates a new loadbalancer.
        /// </summary>
        [Output("loadbalancerProvider")]
        public Output<string> LoadbalancerProvider { get; private set; } = null!;

        /// <summary>
        /// Human-readable name for the Loadbalancer. Does not have
        /// to be unique.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The region in which to obtain the V2 Networking client.
        /// A Networking client is needed to create an LB member. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// LB member.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// A list of security group IDs to apply to the
        /// loadbalancer. The security groups must be specified by ID and not name (as
        /// opposed to how they are configured with the Compute Instance).
        /// </summary>
        [Output("securityGroupIds")]
        public Output<ImmutableArray<string>> SecurityGroupIds { get; private set; } = null!;

        /// <summary>
        /// Required for admins. The UUID of the tenant who owns
        /// the Loadbalancer.  Only administrative users can specify a tenant UUID
        /// other than their own.  Changing this creates a new loadbalancer.
        /// </summary>
        [Output("tenantId")]
        public Output<string> TenantId { get; private set; } = null!;

        /// <summary>
        /// The ip address of the load balancer.
        /// Changing this creates a new loadbalancer.
        /// </summary>
        [Output("vipAddress")]
        public Output<string> VipAddress { get; private set; } = null!;

        /// <summary>
        /// The network on which to allocate the
        /// Loadbalancer's address. A tenant can only create Loadbalancers on networks
        /// authorized by policy (e.g. networks that belong to them or networks that
        /// are shared).  Changing this creates a new loadbalancer.
        /// It is available only for Octavia.
        /// </summary>
        [Output("vipNetworkId")]
        public Output<string> VipNetworkId { get; private set; } = null!;

        /// <summary>
        /// The port UUID that the loadbalancer will use.
        /// Changing this creates a new loadbalancer. It is available only for Octavia.
        /// </summary>
        [Output("vipPortId")]
        public Output<string> VipPortId { get; private set; } = null!;

        /// <summary>
        /// The subnet on which to allocate the
        /// Loadbalancer's address. A tenant can only create Loadbalancers on networks
        /// authorized by policy (e.g. networks that belong to them or networks that
        /// are shared).  Changing this creates a new loadbalancer.
        /// It is required to Neutron LBaaS but optional for Octavia.
        /// </summary>
        [Output("vipSubnetId")]
        public Output<string> VipSubnetId { get; private set; } = null!;


        /// <summary>
        /// Create a LoadBalancer resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public LoadBalancer(string name, LoadBalancerArgs? args = null, CustomResourceOptions? options = null)
            : base("openstack:loadbalancer/loadBalancer:LoadBalancer", name, args ?? new LoadBalancerArgs(), MakeResourceOptions(options, ""))
        {
        }

        private LoadBalancer(string name, Input<string> id, LoadBalancerState? state = null, CustomResourceOptions? options = null)
            : base("openstack:loadbalancer/loadBalancer:LoadBalancer", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing LoadBalancer resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static LoadBalancer Get(string name, Input<string> id, LoadBalancerState? state = null, CustomResourceOptions? options = null)
        {
            return new LoadBalancer(name, id, state, options);
        }
    }

    public sealed class LoadBalancerArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The administrative state of the Loadbalancer.
        /// A valid value is true (UP) or false (DOWN).
        /// </summary>
        [Input("adminStateUp")]
        public Input<bool>? AdminStateUp { get; set; }

        /// <summary>
        /// Human-readable description for the Loadbalancer.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The UUID of a flavor. Changing this creates a new
        /// loadbalancer.
        /// </summary>
        [Input("flavorId")]
        public Input<string>? FlavorId { get; set; }

        /// <summary>
        /// The name of the provider. Changing this
        /// creates a new loadbalancer.
        /// </summary>
        [Input("loadbalancerProvider")]
        public Input<string>? LoadbalancerProvider { get; set; }

        /// <summary>
        /// Human-readable name for the Loadbalancer. Does not have
        /// to be unique.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The region in which to obtain the V2 Networking client.
        /// A Networking client is needed to create an LB member. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// LB member.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("securityGroupIds")]
        private InputList<string>? _securityGroupIds;

        /// <summary>
        /// A list of security group IDs to apply to the
        /// loadbalancer. The security groups must be specified by ID and not name (as
        /// opposed to how they are configured with the Compute Instance).
        /// </summary>
        public InputList<string> SecurityGroupIds
        {
            get => _securityGroupIds ?? (_securityGroupIds = new InputList<string>());
            set => _securityGroupIds = value;
        }

        /// <summary>
        /// Required for admins. The UUID of the tenant who owns
        /// the Loadbalancer.  Only administrative users can specify a tenant UUID
        /// other than their own.  Changing this creates a new loadbalancer.
        /// </summary>
        [Input("tenantId")]
        public Input<string>? TenantId { get; set; }

        /// <summary>
        /// The ip address of the load balancer.
        /// Changing this creates a new loadbalancer.
        /// </summary>
        [Input("vipAddress")]
        public Input<string>? VipAddress { get; set; }

        /// <summary>
        /// The network on which to allocate the
        /// Loadbalancer's address. A tenant can only create Loadbalancers on networks
        /// authorized by policy (e.g. networks that belong to them or networks that
        /// are shared).  Changing this creates a new loadbalancer.
        /// It is available only for Octavia.
        /// </summary>
        [Input("vipNetworkId")]
        public Input<string>? VipNetworkId { get; set; }

        /// <summary>
        /// The port UUID that the loadbalancer will use.
        /// Changing this creates a new loadbalancer. It is available only for Octavia.
        /// </summary>
        [Input("vipPortId")]
        public Input<string>? VipPortId { get; set; }

        /// <summary>
        /// The subnet on which to allocate the
        /// Loadbalancer's address. A tenant can only create Loadbalancers on networks
        /// authorized by policy (e.g. networks that belong to them or networks that
        /// are shared).  Changing this creates a new loadbalancer.
        /// It is required to Neutron LBaaS but optional for Octavia.
        /// </summary>
        [Input("vipSubnetId")]
        public Input<string>? VipSubnetId { get; set; }

        public LoadBalancerArgs()
        {
        }
    }

    public sealed class LoadBalancerState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The administrative state of the Loadbalancer.
        /// A valid value is true (UP) or false (DOWN).
        /// </summary>
        [Input("adminStateUp")]
        public Input<bool>? AdminStateUp { get; set; }

        /// <summary>
        /// Human-readable description for the Loadbalancer.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The UUID of a flavor. Changing this creates a new
        /// loadbalancer.
        /// </summary>
        [Input("flavorId")]
        public Input<string>? FlavorId { get; set; }

        /// <summary>
        /// The name of the provider. Changing this
        /// creates a new loadbalancer.
        /// </summary>
        [Input("loadbalancerProvider")]
        public Input<string>? LoadbalancerProvider { get; set; }

        /// <summary>
        /// Human-readable name for the Loadbalancer. Does not have
        /// to be unique.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The region in which to obtain the V2 Networking client.
        /// A Networking client is needed to create an LB member. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// LB member.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("securityGroupIds")]
        private InputList<string>? _securityGroupIds;

        /// <summary>
        /// A list of security group IDs to apply to the
        /// loadbalancer. The security groups must be specified by ID and not name (as
        /// opposed to how they are configured with the Compute Instance).
        /// </summary>
        public InputList<string> SecurityGroupIds
        {
            get => _securityGroupIds ?? (_securityGroupIds = new InputList<string>());
            set => _securityGroupIds = value;
        }

        /// <summary>
        /// Required for admins. The UUID of the tenant who owns
        /// the Loadbalancer.  Only administrative users can specify a tenant UUID
        /// other than their own.  Changing this creates a new loadbalancer.
        /// </summary>
        [Input("tenantId")]
        public Input<string>? TenantId { get; set; }

        /// <summary>
        /// The ip address of the load balancer.
        /// Changing this creates a new loadbalancer.
        /// </summary>
        [Input("vipAddress")]
        public Input<string>? VipAddress { get; set; }

        /// <summary>
        /// The network on which to allocate the
        /// Loadbalancer's address. A tenant can only create Loadbalancers on networks
        /// authorized by policy (e.g. networks that belong to them or networks that
        /// are shared).  Changing this creates a new loadbalancer.
        /// It is available only for Octavia.
        /// </summary>
        [Input("vipNetworkId")]
        public Input<string>? VipNetworkId { get; set; }

        /// <summary>
        /// The port UUID that the loadbalancer will use.
        /// Changing this creates a new loadbalancer. It is available only for Octavia.
        /// </summary>
        [Input("vipPortId")]
        public Input<string>? VipPortId { get; set; }

        /// <summary>
        /// The subnet on which to allocate the
        /// Loadbalancer's address. A tenant can only create Loadbalancers on networks
        /// authorized by policy (e.g. networks that belong to them or networks that
        /// are shared).  Changing this creates a new loadbalancer.
        /// It is required to Neutron LBaaS but optional for Octavia.
        /// </summary>
        [Input("vipSubnetId")]
        public Input<string>? VipSubnetId { get; set; }

        public LoadBalancerState()
        {
        }
    }
}
