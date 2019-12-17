// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OpenStack.Networking
{
    /// <summary>
    /// Manages a V2 networking quota resource within OpenStack.
    /// 
    /// &gt; **Note:** This usually requires admin privileges.
    /// 
    /// &gt; **Note:** This resource has a no-op deletion so no actual actions will be done against the OpenStack API 
    ///     in case of delete call.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/networking_quota_v2.html.markdown.
    /// </summary>
    public partial class QuotaV2 : Pulumi.CustomResource
    {
        /// <summary>
        /// Quota value for floating IPs. Changing this updates the
        /// existing quota.
        /// </summary>
        [Output("floatingip")]
        public Output<int> Floatingip { get; private set; } = null!;

        /// <summary>
        /// Quota value for networks. Changing this updates the
        /// existing quota.
        /// </summary>
        [Output("network")]
        public Output<int> Network { get; private set; } = null!;

        /// <summary>
        /// Quota value for ports. Changing this updates the
        /// existing quota.
        /// </summary>
        [Output("port")]
        public Output<int> Port { get; private set; } = null!;

        /// <summary>
        /// ID of the project to manage quota. Changing this
        /// creates new quota.
        /// </summary>
        [Output("projectId")]
        public Output<string> ProjectId { get; private set; } = null!;

        /// <summary>
        /// Quota value for RBAC policies.
        /// Changing this updates the existing quota.
        /// </summary>
        [Output("rbacPolicy")]
        public Output<int> RbacPolicy { get; private set; } = null!;

        /// <summary>
        /// The region in which to create the quota. If
        /// omitted, the `region` argument of the provider is used. Changing this
        /// creates new quota.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// Quota value for routers. Changing this updates the
        /// existing quota.
        /// </summary>
        [Output("router")]
        public Output<int> Router { get; private set; } = null!;

        /// <summary>
        /// Quota value for security groups. Changing
        /// this updates the existing quota.
        /// </summary>
        [Output("securityGroup")]
        public Output<int> SecurityGroup { get; private set; } = null!;

        /// <summary>
        /// Quota value for security group rules.
        /// Changing this updates the existing quota.
        /// </summary>
        [Output("securityGroupRule")]
        public Output<int> SecurityGroupRule { get; private set; } = null!;

        /// <summary>
        /// Quota value for subnets. Changing
        /// this updates the existing quota.
        /// </summary>
        [Output("subnet")]
        public Output<int> Subnet { get; private set; } = null!;

        /// <summary>
        /// Quota value for subnetpools.
        /// Changing this updates the existing quota.
        /// </summary>
        [Output("subnetpool")]
        public Output<int> Subnetpool { get; private set; } = null!;


        /// <summary>
        /// Create a QuotaV2 resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public QuotaV2(string name, QuotaV2Args args, CustomResourceOptions? options = null)
            : base("openstack:networking/quotaV2:QuotaV2", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private QuotaV2(string name, Input<string> id, QuotaV2State? state = null, CustomResourceOptions? options = null)
            : base("openstack:networking/quotaV2:QuotaV2", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing QuotaV2 resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static QuotaV2 Get(string name, Input<string> id, QuotaV2State? state = null, CustomResourceOptions? options = null)
        {
            return new QuotaV2(name, id, state, options);
        }
    }

    public sealed class QuotaV2Args : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Quota value for floating IPs. Changing this updates the
        /// existing quota.
        /// </summary>
        [Input("floatingip")]
        public Input<int>? Floatingip { get; set; }

        /// <summary>
        /// Quota value for networks. Changing this updates the
        /// existing quota.
        /// </summary>
        [Input("network")]
        public Input<int>? Network { get; set; }

        /// <summary>
        /// Quota value for ports. Changing this updates the
        /// existing quota.
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        /// <summary>
        /// ID of the project to manage quota. Changing this
        /// creates new quota.
        /// </summary>
        [Input("projectId", required: true)]
        public Input<string> ProjectId { get; set; } = null!;

        /// <summary>
        /// Quota value for RBAC policies.
        /// Changing this updates the existing quota.
        /// </summary>
        [Input("rbacPolicy")]
        public Input<int>? RbacPolicy { get; set; }

        /// <summary>
        /// The region in which to create the quota. If
        /// omitted, the `region` argument of the provider is used. Changing this
        /// creates new quota.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// Quota value for routers. Changing this updates the
        /// existing quota.
        /// </summary>
        [Input("router")]
        public Input<int>? Router { get; set; }

        /// <summary>
        /// Quota value for security groups. Changing
        /// this updates the existing quota.
        /// </summary>
        [Input("securityGroup")]
        public Input<int>? SecurityGroup { get; set; }

        /// <summary>
        /// Quota value for security group rules.
        /// Changing this updates the existing quota.
        /// </summary>
        [Input("securityGroupRule")]
        public Input<int>? SecurityGroupRule { get; set; }

        /// <summary>
        /// Quota value for subnets. Changing
        /// this updates the existing quota.
        /// </summary>
        [Input("subnet")]
        public Input<int>? Subnet { get; set; }

        /// <summary>
        /// Quota value for subnetpools.
        /// Changing this updates the existing quota.
        /// </summary>
        [Input("subnetpool")]
        public Input<int>? Subnetpool { get; set; }

        public QuotaV2Args()
        {
        }
    }

    public sealed class QuotaV2State : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Quota value for floating IPs. Changing this updates the
        /// existing quota.
        /// </summary>
        [Input("floatingip")]
        public Input<int>? Floatingip { get; set; }

        /// <summary>
        /// Quota value for networks. Changing this updates the
        /// existing quota.
        /// </summary>
        [Input("network")]
        public Input<int>? Network { get; set; }

        /// <summary>
        /// Quota value for ports. Changing this updates the
        /// existing quota.
        /// </summary>
        [Input("port")]
        public Input<int>? Port { get; set; }

        /// <summary>
        /// ID of the project to manage quota. Changing this
        /// creates new quota.
        /// </summary>
        [Input("projectId")]
        public Input<string>? ProjectId { get; set; }

        /// <summary>
        /// Quota value for RBAC policies.
        /// Changing this updates the existing quota.
        /// </summary>
        [Input("rbacPolicy")]
        public Input<int>? RbacPolicy { get; set; }

        /// <summary>
        /// The region in which to create the quota. If
        /// omitted, the `region` argument of the provider is used. Changing this
        /// creates new quota.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// Quota value for routers. Changing this updates the
        /// existing quota.
        /// </summary>
        [Input("router")]
        public Input<int>? Router { get; set; }

        /// <summary>
        /// Quota value for security groups. Changing
        /// this updates the existing quota.
        /// </summary>
        [Input("securityGroup")]
        public Input<int>? SecurityGroup { get; set; }

        /// <summary>
        /// Quota value for security group rules.
        /// Changing this updates the existing quota.
        /// </summary>
        [Input("securityGroupRule")]
        public Input<int>? SecurityGroupRule { get; set; }

        /// <summary>
        /// Quota value for subnets. Changing
        /// this updates the existing quota.
        /// </summary>
        [Input("subnet")]
        public Input<int>? Subnet { get; set; }

        /// <summary>
        /// Quota value for subnetpools.
        /// Changing this updates the existing quota.
        /// </summary>
        [Input("subnetpool")]
        public Input<int>? Subnetpool { get; set; }

        public QuotaV2State()
        {
        }
    }
}
