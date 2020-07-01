// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OpenStack.BlockStorage
{
    /// <summary>
    /// Manages a V2 block storage quotaset resource within OpenStack.
    /// 
    /// &gt; **Note:** This usually requires admin privileges.
    /// 
    /// &gt; **Note:** This resource has a no-op deletion so no actual actions will be done against the OpenStack API
    ///     in case of delete call.
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
    ///         var project1 = new OpenStack.Identity.Project("project1", new OpenStack.Identity.ProjectArgs
    ///         {
    ///         });
    ///         var quotaset1 = new OpenStack.BlockStorage.QuoteSetV2("quotaset1", new OpenStack.BlockStorage.QuoteSetV2Args
    ///         {
    ///             ProjectId = project1.Id,
    ///             Volumes = 10,
    ///             Snapshots = 4,
    ///             Gigabytes = 100,
    ///             PerVolumeGigabytes = 10,
    ///             Backups = 4,
    ///             BackupGigabytes = 10,
    ///             Groups = 100,
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class QuoteSetV2 : Pulumi.CustomResource
    {
        /// <summary>
        /// Quota value for backup gigabytes. Changing
        /// this updates the existing quotaset.
        /// </summary>
        [Output("backupGigabytes")]
        public Output<int> BackupGigabytes { get; private set; } = null!;

        /// <summary>
        /// Quota value for backups. Changing this updates the
        /// existing quotaset.
        /// </summary>
        [Output("backups")]
        public Output<int> Backups { get; private set; } = null!;

        /// <summary>
        /// Quota value for gigabytes. Changing this updates the
        /// existing quotaset.
        /// </summary>
        [Output("gigabytes")]
        public Output<int> Gigabytes { get; private set; } = null!;

        /// <summary>
        /// Quota value for groups. Changing this updates the
        /// existing quotaset.
        /// </summary>
        [Output("groups")]
        public Output<int> Groups { get; private set; } = null!;

        /// <summary>
        /// Quota value for gigabytes per volume .
        /// Changing this updates the existing quotaset.
        /// </summary>
        [Output("perVolumeGigabytes")]
        public Output<int> PerVolumeGigabytes { get; private set; } = null!;

        /// <summary>
        /// ID of the project to manage quotas. Changing this
        /// creates a new quotaset.
        /// </summary>
        [Output("projectId")]
        public Output<string> ProjectId { get; private set; } = null!;

        /// <summary>
        /// The region in which to create the volume. If
        /// omitted, the `region` argument of the provider is used. Changing this
        /// creates a new quotaset.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// Quota value for snapshots. Changing this updates the
        /// existing quotaset.
        /// </summary>
        [Output("snapshots")]
        public Output<int> Snapshots { get; private set; } = null!;

        /// <summary>
        /// Quota value for volumes. Changing this updates the
        /// existing quotaset.
        /// </summary>
        [Output("volumes")]
        public Output<int> Volumes { get; private set; } = null!;


        /// <summary>
        /// Create a QuoteSetV2 resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public QuoteSetV2(string name, QuoteSetV2Args args, CustomResourceOptions? options = null)
            : base("openstack:blockstorage/quoteSetV2:QuoteSetV2", name, args ?? new QuoteSetV2Args(), MakeResourceOptions(options, ""))
        {
        }

        private QuoteSetV2(string name, Input<string> id, QuoteSetV2State? state = null, CustomResourceOptions? options = null)
            : base("openstack:blockstorage/quoteSetV2:QuoteSetV2", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing QuoteSetV2 resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static QuoteSetV2 Get(string name, Input<string> id, QuoteSetV2State? state = null, CustomResourceOptions? options = null)
        {
            return new QuoteSetV2(name, id, state, options);
        }
    }

    public sealed class QuoteSetV2Args : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Quota value for backup gigabytes. Changing
        /// this updates the existing quotaset.
        /// </summary>
        [Input("backupGigabytes")]
        public Input<int>? BackupGigabytes { get; set; }

        /// <summary>
        /// Quota value for backups. Changing this updates the
        /// existing quotaset.
        /// </summary>
        [Input("backups")]
        public Input<int>? Backups { get; set; }

        /// <summary>
        /// Quota value for gigabytes. Changing this updates the
        /// existing quotaset.
        /// </summary>
        [Input("gigabytes")]
        public Input<int>? Gigabytes { get; set; }

        /// <summary>
        /// Quota value for groups. Changing this updates the
        /// existing quotaset.
        /// </summary>
        [Input("groups")]
        public Input<int>? Groups { get; set; }

        /// <summary>
        /// Quota value for gigabytes per volume .
        /// Changing this updates the existing quotaset.
        /// </summary>
        [Input("perVolumeGigabytes")]
        public Input<int>? PerVolumeGigabytes { get; set; }

        /// <summary>
        /// ID of the project to manage quotas. Changing this
        /// creates a new quotaset.
        /// </summary>
        [Input("projectId", required: true)]
        public Input<string> ProjectId { get; set; } = null!;

        /// <summary>
        /// The region in which to create the volume. If
        /// omitted, the `region` argument of the provider is used. Changing this
        /// creates a new quotaset.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// Quota value for snapshots. Changing this updates the
        /// existing quotaset.
        /// </summary>
        [Input("snapshots")]
        public Input<int>? Snapshots { get; set; }

        /// <summary>
        /// Quota value for volumes. Changing this updates the
        /// existing quotaset.
        /// </summary>
        [Input("volumes")]
        public Input<int>? Volumes { get; set; }

        public QuoteSetV2Args()
        {
        }
    }

    public sealed class QuoteSetV2State : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Quota value for backup gigabytes. Changing
        /// this updates the existing quotaset.
        /// </summary>
        [Input("backupGigabytes")]
        public Input<int>? BackupGigabytes { get; set; }

        /// <summary>
        /// Quota value for backups. Changing this updates the
        /// existing quotaset.
        /// </summary>
        [Input("backups")]
        public Input<int>? Backups { get; set; }

        /// <summary>
        /// Quota value for gigabytes. Changing this updates the
        /// existing quotaset.
        /// </summary>
        [Input("gigabytes")]
        public Input<int>? Gigabytes { get; set; }

        /// <summary>
        /// Quota value for groups. Changing this updates the
        /// existing quotaset.
        /// </summary>
        [Input("groups")]
        public Input<int>? Groups { get; set; }

        /// <summary>
        /// Quota value for gigabytes per volume .
        /// Changing this updates the existing quotaset.
        /// </summary>
        [Input("perVolumeGigabytes")]
        public Input<int>? PerVolumeGigabytes { get; set; }

        /// <summary>
        /// ID of the project to manage quotas. Changing this
        /// creates a new quotaset.
        /// </summary>
        [Input("projectId")]
        public Input<string>? ProjectId { get; set; }

        /// <summary>
        /// The region in which to create the volume. If
        /// omitted, the `region` argument of the provider is used. Changing this
        /// creates a new quotaset.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// Quota value for snapshots. Changing this updates the
        /// existing quotaset.
        /// </summary>
        [Input("snapshots")]
        public Input<int>? Snapshots { get; set; }

        /// <summary>
        /// Quota value for volumes. Changing this updates the
        /// existing quotaset.
        /// </summary>
        [Input("volumes")]
        public Input<int>? Volumes { get; set; }

        public QuoteSetV2State()
        {
        }
    }
}
