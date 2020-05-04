// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OpenStack.LoadBalancer.Inputs
{

    public sealed class MembersMemberArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The IP address of the members to receive traffic from
        /// the load balancer.
        /// </summary>
        [Input("address", required: true)]
        public Input<string> Address { get; set; } = null!;

        /// <summary>
        /// The administrative state of the member.
        /// A valid value is true (UP) or false (DOWN). Defaults to true.
        /// </summary>
        [Input("adminStateUp")]
        public Input<bool>? AdminStateUp { get; set; }

        /// <summary>
        /// The unique ID for the members.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// Human-readable name for the member.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The port on which to listen for client traffic.
        /// </summary>
        [Input("protocolPort", required: true)]
        public Input<int> ProtocolPort { get; set; } = null!;

        /// <summary>
        /// The subnet in which to access the member.
        /// </summary>
        [Input("subnetId")]
        public Input<string>? SubnetId { get; set; }

        /// <summary>
        /// A positive integer value that indicates the relative
        /// portion of traffic that this members should receive from the pool. For
        /// example, a member with a weight of 10 receives five times as much traffic
        /// as a member with a weight of 2. Defaults to 1.
        /// </summary>
        [Input("weight")]
        public Input<int>? Weight { get; set; }

        public MembersMemberArgs()
        {
        }
    }
}
