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
    /// Manages a V2 pool resource within OpenStack.
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
    ///         var pool1 = new OpenStack.LoadBalancer.Pool("pool1", new OpenStack.LoadBalancer.PoolArgs
    ///         {
    ///             LbMethod = "ROUND_ROBIN",
    ///             ListenerId = "d9415786-5f1a-428b-b35f-2f1523e146d2",
    ///             Persistence = new OpenStack.LoadBalancer.Inputs.PoolPersistenceArgs
    ///             {
    ///                 CookieName = "testCookie",
    ///                 Type = "APP_COOKIE",
    ///             },
    ///             Protocol = "HTTP",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class Pool : Pulumi.CustomResource
    {
        /// <summary>
        /// The administrative state of the pool.
        /// A valid value is true (UP) or false (DOWN).
        /// </summary>
        [Output("adminStateUp")]
        public Output<bool?> AdminStateUp { get; private set; } = null!;

        /// <summary>
        /// Human-readable description for the pool.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The load balancing algorithm to
        /// distribute traffic to the pool's members. Must be one of
        /// ROUND_ROBIN, LEAST_CONNECTIONS, SOURCE_IP, or SOURCE_IP_PORT (supported only
        /// in Octavia).
        /// </summary>
        [Output("lbMethod")]
        public Output<string> LbMethod { get; private set; } = null!;

        /// <summary>
        /// The Listener on which the members of the pool
        /// will be associated with. Changing this creates a new pool.
        /// Note:  One of LoadbalancerID or ListenerID must be provided.
        /// </summary>
        [Output("listenerId")]
        public Output<string?> ListenerId { get; private set; } = null!;

        /// <summary>
        /// The load balancer on which to provision this
        /// pool. Changing this creates a new pool.
        /// Note:  One of LoadbalancerID or ListenerID must be provided.
        /// </summary>
        [Output("loadbalancerId")]
        public Output<string?> LoadbalancerId { get; private set; } = null!;

        /// <summary>
        /// Human-readable name for the pool.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Omit this field to prevent session persistence.  Indicates
        /// whether connections in the same session will be processed by the same Pool
        /// member or not. Changing this creates a new pool.
        /// </summary>
        [Output("persistence")]
        public Output<Outputs.PoolPersistence> Persistence { get; private set; } = null!;

        /// <summary>
        /// The protocol - can either be TCP, HTTP, HTTPS, PROXY
        /// or UDP (supported only in Octavia). Changing this creates a new pool.
        /// </summary>
        [Output("protocol")]
        public Output<string> Protocol { get; private set; } = null!;

        /// <summary>
        /// The region in which to obtain the V2 Networking client.
        /// A Networking client is needed to create an . If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// pool.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// Required for admins. The UUID of the tenant who owns
        /// the pool.  Only administrative users can specify a tenant UUID
        /// other than their own. Changing this creates a new pool.
        /// </summary>
        [Output("tenantId")]
        public Output<string> TenantId { get; private set; } = null!;


        /// <summary>
        /// Create a Pool resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Pool(string name, PoolArgs args, CustomResourceOptions? options = null)
            : base("openstack:loadbalancer/pool:Pool", name, args ?? new PoolArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Pool(string name, Input<string> id, PoolState? state = null, CustomResourceOptions? options = null)
            : base("openstack:loadbalancer/pool:Pool", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Pool resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Pool Get(string name, Input<string> id, PoolState? state = null, CustomResourceOptions? options = null)
        {
            return new Pool(name, id, state, options);
        }
    }

    public sealed class PoolArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The administrative state of the pool.
        /// A valid value is true (UP) or false (DOWN).
        /// </summary>
        [Input("adminStateUp")]
        public Input<bool>? AdminStateUp { get; set; }

        /// <summary>
        /// Human-readable description for the pool.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The load balancing algorithm to
        /// distribute traffic to the pool's members. Must be one of
        /// ROUND_ROBIN, LEAST_CONNECTIONS, SOURCE_IP, or SOURCE_IP_PORT (supported only
        /// in Octavia).
        /// </summary>
        [Input("lbMethod", required: true)]
        public Input<string> LbMethod { get; set; } = null!;

        /// <summary>
        /// The Listener on which the members of the pool
        /// will be associated with. Changing this creates a new pool.
        /// Note:  One of LoadbalancerID or ListenerID must be provided.
        /// </summary>
        [Input("listenerId")]
        public Input<string>? ListenerId { get; set; }

        /// <summary>
        /// The load balancer on which to provision this
        /// pool. Changing this creates a new pool.
        /// Note:  One of LoadbalancerID or ListenerID must be provided.
        /// </summary>
        [Input("loadbalancerId")]
        public Input<string>? LoadbalancerId { get; set; }

        /// <summary>
        /// Human-readable name for the pool.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Omit this field to prevent session persistence.  Indicates
        /// whether connections in the same session will be processed by the same Pool
        /// member or not. Changing this creates a new pool.
        /// </summary>
        [Input("persistence")]
        public Input<Inputs.PoolPersistenceArgs>? Persistence { get; set; }

        /// <summary>
        /// The protocol - can either be TCP, HTTP, HTTPS, PROXY
        /// or UDP (supported only in Octavia). Changing this creates a new pool.
        /// </summary>
        [Input("protocol", required: true)]
        public Input<string> Protocol { get; set; } = null!;

        /// <summary>
        /// The region in which to obtain the V2 Networking client.
        /// A Networking client is needed to create an . If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// pool.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// Required for admins. The UUID of the tenant who owns
        /// the pool.  Only administrative users can specify a tenant UUID
        /// other than their own. Changing this creates a new pool.
        /// </summary>
        [Input("tenantId")]
        public Input<string>? TenantId { get; set; }

        public PoolArgs()
        {
        }
    }

    public sealed class PoolState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The administrative state of the pool.
        /// A valid value is true (UP) or false (DOWN).
        /// </summary>
        [Input("adminStateUp")]
        public Input<bool>? AdminStateUp { get; set; }

        /// <summary>
        /// Human-readable description for the pool.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The load balancing algorithm to
        /// distribute traffic to the pool's members. Must be one of
        /// ROUND_ROBIN, LEAST_CONNECTIONS, SOURCE_IP, or SOURCE_IP_PORT (supported only
        /// in Octavia).
        /// </summary>
        [Input("lbMethod")]
        public Input<string>? LbMethod { get; set; }

        /// <summary>
        /// The Listener on which the members of the pool
        /// will be associated with. Changing this creates a new pool.
        /// Note:  One of LoadbalancerID or ListenerID must be provided.
        /// </summary>
        [Input("listenerId")]
        public Input<string>? ListenerId { get; set; }

        /// <summary>
        /// The load balancer on which to provision this
        /// pool. Changing this creates a new pool.
        /// Note:  One of LoadbalancerID or ListenerID must be provided.
        /// </summary>
        [Input("loadbalancerId")]
        public Input<string>? LoadbalancerId { get; set; }

        /// <summary>
        /// Human-readable name for the pool.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Omit this field to prevent session persistence.  Indicates
        /// whether connections in the same session will be processed by the same Pool
        /// member or not. Changing this creates a new pool.
        /// </summary>
        [Input("persistence")]
        public Input<Inputs.PoolPersistenceGetArgs>? Persistence { get; set; }

        /// <summary>
        /// The protocol - can either be TCP, HTTP, HTTPS, PROXY
        /// or UDP (supported only in Octavia). Changing this creates a new pool.
        /// </summary>
        [Input("protocol")]
        public Input<string>? Protocol { get; set; }

        /// <summary>
        /// The region in which to obtain the V2 Networking client.
        /// A Networking client is needed to create an . If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// pool.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// Required for admins. The UUID of the tenant who owns
        /// the pool.  Only administrative users can specify a tenant UUID
        /// other than their own. Changing this creates a new pool.
        /// </summary>
        [Input("tenantId")]
        public Input<string>? TenantId { get; set; }

        public PoolState()
        {
        }
    }
}
