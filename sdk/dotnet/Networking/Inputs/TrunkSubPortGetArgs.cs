// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OpenStack.Networking.Inputs
{

    public sealed class TrunkSubPortGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the port to be made a subport of the trunk.
        /// </summary>
        [Input("portId", required: true)]
        public Input<string> PortId { get; set; } = null!;

        /// <summary>
        /// The numeric id of the subport segment.
        /// </summary>
        [Input("segmentationId", required: true)]
        public Input<int> SegmentationId { get; set; } = null!;

        /// <summary>
        /// The segmentation technology to use, e.g., "vlan".
        /// </summary>
        [Input("segmentationType", required: true)]
        public Input<string> SegmentationType { get; set; } = null!;

        public TrunkSubPortGetArgs()
        {
        }
    }
}