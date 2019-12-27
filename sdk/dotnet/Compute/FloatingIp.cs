// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OpenStack.Compute
{
    /// <summary>
    /// Manages a V2 floating IP resource within OpenStack Nova (compute)
    /// that can be used for compute instances.
    /// 
    /// Please note that managing floating IPs through the OpenStack Compute API has
    /// been deprecated. Unless you are using an older OpenStack environment, it is
    /// recommended to use the `openstack.networking.FloatingIp`
    /// resource instead, which uses the OpenStack Networking API.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_floatingip_v2.html.markdown.
    /// </summary>
    public partial class FloatingIp : Pulumi.CustomResource
    {
        /// <summary>
        /// The actual floating IP address itself.
        /// </summary>
        [Output("address")]
        public Output<string> Address { get; private set; } = null!;

        /// <summary>
        /// The fixed IP address corresponding to the floating IP.
        /// </summary>
        [Output("fixedIp")]
        public Output<string> FixedIp { get; private set; } = null!;

        /// <summary>
        /// UUID of the compute instance associated with the floating IP.
        /// </summary>
        [Output("instanceId")]
        public Output<string> InstanceId { get; private set; } = null!;

        /// <summary>
        /// The name of the pool from which to obtain the floating
        /// IP. Changing this creates a new floating IP.
        /// </summary>
        [Output("pool")]
        public Output<string> Pool { get; private set; } = null!;

        /// <summary>
        /// The region in which to obtain the V2 Compute client.
        /// A Compute client is needed to create a floating IP that can be used with
        /// a compute instance. If omitted, the `region` argument of the provider
        /// is used. Changing this creates a new floating IP (which may or may not
        /// have a different address).
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;


        /// <summary>
        /// Create a FloatingIp resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public FloatingIp(string name, FloatingIpArgs args, CustomResourceOptions? options = null)
            : base("openstack:compute/floatingIp:FloatingIp", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private FloatingIp(string name, Input<string> id, FloatingIpState? state = null, CustomResourceOptions? options = null)
            : base("openstack:compute/floatingIp:FloatingIp", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing FloatingIp resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static FloatingIp Get(string name, Input<string> id, FloatingIpState? state = null, CustomResourceOptions? options = null)
        {
            return new FloatingIp(name, id, state, options);
        }
    }

    public sealed class FloatingIpArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the pool from which to obtain the floating
        /// IP. Changing this creates a new floating IP.
        /// </summary>
        [Input("pool", required: true)]
        public Input<string> Pool { get; set; } = null!;

        /// <summary>
        /// The region in which to obtain the V2 Compute client.
        /// A Compute client is needed to create a floating IP that can be used with
        /// a compute instance. If omitted, the `region` argument of the provider
        /// is used. Changing this creates a new floating IP (which may or may not
        /// have a different address).
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        public FloatingIpArgs()
        {
        }
    }

    public sealed class FloatingIpState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The actual floating IP address itself.
        /// </summary>
        [Input("address")]
        public Input<string>? Address { get; set; }

        /// <summary>
        /// The fixed IP address corresponding to the floating IP.
        /// </summary>
        [Input("fixedIp")]
        public Input<string>? FixedIp { get; set; }

        /// <summary>
        /// UUID of the compute instance associated with the floating IP.
        /// </summary>
        [Input("instanceId")]
        public Input<string>? InstanceId { get; set; }

        /// <summary>
        /// The name of the pool from which to obtain the floating
        /// IP. Changing this creates a new floating IP.
        /// </summary>
        [Input("pool")]
        public Input<string>? Pool { get; set; }

        /// <summary>
        /// The region in which to obtain the V2 Compute client.
        /// A Compute client is needed to create a floating IP that can be used with
        /// a compute instance. If omitted, the `region` argument of the provider
        /// is used. Changing this creates a new floating IP (which may or may not
        /// have a different address).
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        public FloatingIpState()
        {
        }
    }
}
