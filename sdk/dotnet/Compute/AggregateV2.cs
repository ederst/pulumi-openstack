// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OpenStack.Compute
{
    /// <summary>
    /// Manages a Host Aggregate within Openstack Nova.
    /// 
    /// ## Example Usage
    /// ### Full example
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using OpenStack = Pulumi.OpenStack;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var dellServers = new OpenStack.Compute.AggregateV2("dellServers", new OpenStack.Compute.AggregateV2Args
    ///         {
    ///             Hosts = 
    ///             {
    ///                 "myhost01.example.com",
    ///                 "myhost02.example.com",
    ///             },
    ///             Metadata = 
    ///             {
    ///                 { "cpus", "56" },
    ///             },
    ///             Zone = "nova",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// ### Minimum required example
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using OpenStack = Pulumi.OpenStack;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var test = new OpenStack.Compute.AggregateV2("test", new OpenStack.Compute.AggregateV2Args
    ///         {
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// You can import an existing Host Aggregate by their ID.
    /// 
    /// ```sh
    ///  $ pulumi import openstack:compute/aggregateV2:AggregateV2 myaggregate 24
    /// ```
    /// 
    ///  The ID can be obtained with an openstack command$ openstack aggregate list +----+------+-------------------+ | ID | Name | Availability Zone | +----+------+-------------------+ | 59 | test | None
    /// 
    /// | +----+------+-------------------+
    /// </summary>
    public partial class AggregateV2 : Pulumi.CustomResource
    {
        /// <summary>
        /// The list of hosts contained in the Host Aggregate. The hosts must be added
        /// to Openstack and visible in the web interface, or the provider will fail to add them to the host
        /// aggregate.
        /// </summary>
        [Output("hosts")]
        public Output<ImmutableArray<string>> Hosts { get; private set; } = null!;

        /// <summary>
        /// The metadata of the Host Aggregate. Can be useful to indicate scheduler hints.
        /// </summary>
        [Output("metadata")]
        public Output<ImmutableDictionary<string, string>?> Metadata { get; private set; } = null!;

        /// <summary>
        /// The name of the Host Aggregate
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The name of the Availability Zone to use. If ommited, it will take the default
        /// availability zone.
        /// </summary>
        [Output("zone")]
        public Output<string> Zone { get; private set; } = null!;


        /// <summary>
        /// Create a AggregateV2 resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AggregateV2(string name, AggregateV2Args args, CustomResourceOptions? options = null)
            : base("openstack:compute/aggregateV2:AggregateV2", name, args ?? new AggregateV2Args(), MakeResourceOptions(options, ""))
        {
        }

        private AggregateV2(string name, Input<string> id, AggregateV2State? state = null, CustomResourceOptions? options = null)
            : base("openstack:compute/aggregateV2:AggregateV2", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing AggregateV2 resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AggregateV2 Get(string name, Input<string> id, AggregateV2State? state = null, CustomResourceOptions? options = null)
        {
            return new AggregateV2(name, id, state, options);
        }
    }

    public sealed class AggregateV2Args : Pulumi.ResourceArgs
    {
        [Input("hosts")]
        private InputList<string>? _hosts;

        /// <summary>
        /// The list of hosts contained in the Host Aggregate. The hosts must be added
        /// to Openstack and visible in the web interface, or the provider will fail to add them to the host
        /// aggregate.
        /// </summary>
        public InputList<string> Hosts
        {
            get => _hosts ?? (_hosts = new InputList<string>());
            set => _hosts = value;
        }

        [Input("metadata")]
        private InputMap<string>? _metadata;

        /// <summary>
        /// The metadata of the Host Aggregate. Can be useful to indicate scheduler hints.
        /// </summary>
        public InputMap<string> Metadata
        {
            get => _metadata ?? (_metadata = new InputMap<string>());
            set => _metadata = value;
        }

        /// <summary>
        /// The name of the Host Aggregate
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the Availability Zone to use. If ommited, it will take the default
        /// availability zone.
        /// </summary>
        [Input("zone", required: true)]
        public Input<string> Zone { get; set; } = null!;

        public AggregateV2Args()
        {
        }
    }

    public sealed class AggregateV2State : Pulumi.ResourceArgs
    {
        [Input("hosts")]
        private InputList<string>? _hosts;

        /// <summary>
        /// The list of hosts contained in the Host Aggregate. The hosts must be added
        /// to Openstack and visible in the web interface, or the provider will fail to add them to the host
        /// aggregate.
        /// </summary>
        public InputList<string> Hosts
        {
            get => _hosts ?? (_hosts = new InputList<string>());
            set => _hosts = value;
        }

        [Input("metadata")]
        private InputMap<string>? _metadata;

        /// <summary>
        /// The metadata of the Host Aggregate. Can be useful to indicate scheduler hints.
        /// </summary>
        public InputMap<string> Metadata
        {
            get => _metadata ?? (_metadata = new InputMap<string>());
            set => _metadata = value;
        }

        /// <summary>
        /// The name of the Host Aggregate
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The name of the Availability Zone to use. If ommited, it will take the default
        /// availability zone.
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public AggregateV2State()
        {
        }
    }
}