// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OpenStack.Compute
{
    /// <summary>
    /// Associate a floating IP to an instance. This can be used instead of the
    /// `floating_ip` options in `openstack.compute.Instance`.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/compute_floatingip_associate_v2.html.markdown.
    /// </summary>
    public partial class FloatingIpAssociate : Pulumi.CustomResource
    {
        /// <summary>
        /// The specific IP address to direct traffic to.
        /// </summary>
        [Output("fixedIp")]
        public Output<string?> FixedIp { get; private set; } = null!;

        /// <summary>
        /// The floating IP to associate.
        /// </summary>
        [Output("floatingIp")]
        public Output<string> FloatingIp { get; private set; } = null!;

        /// <summary>
        /// The instance to associte the floating IP with.
        /// </summary>
        [Output("instanceId")]
        public Output<string> InstanceId { get; private set; } = null!;

        /// <summary>
        /// The region in which to obtain the V2 Compute client.
        /// Keypairs are associated with accounts, but a Compute client is needed to
        /// create one. If omitted, the `region` argument of the provider is used.
        /// Changing this creates a new floatingip_associate.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        [Output("waitUntilAssociated")]
        public Output<bool?> WaitUntilAssociated { get; private set; } = null!;


        /// <summary>
        /// Create a FloatingIpAssociate resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public FloatingIpAssociate(string name, FloatingIpAssociateArgs args, CustomResourceOptions? options = null)
            : base("openstack:compute/floatingIpAssociate:FloatingIpAssociate", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private FloatingIpAssociate(string name, Input<string> id, FloatingIpAssociateState? state = null, CustomResourceOptions? options = null)
            : base("openstack:compute/floatingIpAssociate:FloatingIpAssociate", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing FloatingIpAssociate resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static FloatingIpAssociate Get(string name, Input<string> id, FloatingIpAssociateState? state = null, CustomResourceOptions? options = null)
        {
            return new FloatingIpAssociate(name, id, state, options);
        }
    }

    public sealed class FloatingIpAssociateArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The specific IP address to direct traffic to.
        /// </summary>
        [Input("fixedIp")]
        public Input<string>? FixedIp { get; set; }

        /// <summary>
        /// The floating IP to associate.
        /// </summary>
        [Input("floatingIp", required: true)]
        public Input<string> FloatingIp { get; set; } = null!;

        /// <summary>
        /// The instance to associte the floating IP with.
        /// </summary>
        [Input("instanceId", required: true)]
        public Input<string> InstanceId { get; set; } = null!;

        /// <summary>
        /// The region in which to obtain the V2 Compute client.
        /// Keypairs are associated with accounts, but a Compute client is needed to
        /// create one. If omitted, the `region` argument of the provider is used.
        /// Changing this creates a new floatingip_associate.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("waitUntilAssociated")]
        public Input<bool>? WaitUntilAssociated { get; set; }

        public FloatingIpAssociateArgs()
        {
        }
    }

    public sealed class FloatingIpAssociateState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The specific IP address to direct traffic to.
        /// </summary>
        [Input("fixedIp")]
        public Input<string>? FixedIp { get; set; }

        /// <summary>
        /// The floating IP to associate.
        /// </summary>
        [Input("floatingIp")]
        public Input<string>? FloatingIp { get; set; }

        /// <summary>
        /// The instance to associte the floating IP with.
        /// </summary>
        [Input("instanceId")]
        public Input<string>? InstanceId { get; set; }

        /// <summary>
        /// The region in which to obtain the V2 Compute client.
        /// Keypairs are associated with accounts, but a Compute client is needed to
        /// create one. If omitted, the `region` argument of the provider is used.
        /// Changing this creates a new floatingip_associate.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("waitUntilAssociated")]
        public Input<bool>? WaitUntilAssociated { get; set; }

        public FloatingIpAssociateState()
        {
        }
    }
}
