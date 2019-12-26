// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OpenStack.Database
{
    /// <summary>
    /// Manages a V1 DB configuration resource within OpenStack.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/db_configuration_v1.html.markdown.
    /// </summary>
    public partial class Configuration : Pulumi.CustomResource
    {
        /// <summary>
        /// An array of configuration parameter name and value. Can be specified multiple times. The configuration object structure is documented below.
        /// </summary>
        [Output("configurations")]
        public Output<ImmutableArray<Outputs.ConfigurationConfigurations>> Configurations { get; private set; } = null!;

        /// <summary>
        /// An array of database engine type and version. The datastore
        /// object structure is documented below. Changing this creates resource.
        /// </summary>
        [Output("datastore")]
        public Output<Outputs.ConfigurationDatastore> Datastore { get; private set; } = null!;

        /// <summary>
        /// Description of the resource.
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// A unique name for the resource.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The region in which to create the db instance. Changing this
        /// creates a new instance.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;


        /// <summary>
        /// Create a Configuration resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Configuration(string name, ConfigurationArgs args, CustomResourceOptions? options = null)
            : base("openstack:database/configuration:Configuration", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private Configuration(string name, Input<string> id, ConfigurationState? state = null, CustomResourceOptions? options = null)
            : base("openstack:database/configuration:Configuration", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Configuration resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Configuration Get(string name, Input<string> id, ConfigurationState? state = null, CustomResourceOptions? options = null)
        {
            return new Configuration(name, id, state, options);
        }
    }

    public sealed class ConfigurationArgs : Pulumi.ResourceArgs
    {
        [Input("configurations")]
        private InputList<Inputs.ConfigurationConfigurationsArgs>? _configurations;

        /// <summary>
        /// An array of configuration parameter name and value. Can be specified multiple times. The configuration object structure is documented below.
        /// </summary>
        public InputList<Inputs.ConfigurationConfigurationsArgs> Configurations
        {
            get => _configurations ?? (_configurations = new InputList<Inputs.ConfigurationConfigurationsArgs>());
            set => _configurations = value;
        }

        /// <summary>
        /// An array of database engine type and version. The datastore
        /// object structure is documented below. Changing this creates resource.
        /// </summary>
        [Input("datastore", required: true)]
        public Input<Inputs.ConfigurationDatastoreArgs> Datastore { get; set; } = null!;

        /// <summary>
        /// Description of the resource.
        /// </summary>
        [Input("description", required: true)]
        public Input<string> Description { get; set; } = null!;

        /// <summary>
        /// A unique name for the resource.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The region in which to create the db instance. Changing this
        /// creates a new instance.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        public ConfigurationArgs()
        {
        }
    }

    public sealed class ConfigurationState : Pulumi.ResourceArgs
    {
        [Input("configurations")]
        private InputList<Inputs.ConfigurationConfigurationsGetArgs>? _configurations;

        /// <summary>
        /// An array of configuration parameter name and value. Can be specified multiple times. The configuration object structure is documented below.
        /// </summary>
        public InputList<Inputs.ConfigurationConfigurationsGetArgs> Configurations
        {
            get => _configurations ?? (_configurations = new InputList<Inputs.ConfigurationConfigurationsGetArgs>());
            set => _configurations = value;
        }

        /// <summary>
        /// An array of database engine type and version. The datastore
        /// object structure is documented below. Changing this creates resource.
        /// </summary>
        [Input("datastore")]
        public Input<Inputs.ConfigurationDatastoreGetArgs>? Datastore { get; set; }

        /// <summary>
        /// Description of the resource.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// A unique name for the resource.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The region in which to create the db instance. Changing this
        /// creates a new instance.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        public ConfigurationState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class ConfigurationConfigurationsArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A unique name for the resource.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public ConfigurationConfigurationsArgs()
        {
        }
    }

    public sealed class ConfigurationConfigurationsGetArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// A unique name for the resource.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("value", required: true)]
        public Input<string> Value { get; set; } = null!;

        public ConfigurationConfigurationsGetArgs()
        {
        }
    }

    public sealed class ConfigurationDatastoreArgs : Pulumi.ResourceArgs
    {
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        [Input("version", required: true)]
        public Input<string> Version { get; set; } = null!;

        public ConfigurationDatastoreArgs()
        {
        }
    }

    public sealed class ConfigurationDatastoreGetArgs : Pulumi.ResourceArgs
    {
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        [Input("version", required: true)]
        public Input<string> Version { get; set; } = null!;

        public ConfigurationDatastoreGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class ConfigurationConfigurations
    {
        /// <summary>
        /// A unique name for the resource.
        /// </summary>
        public readonly string Name;
        public readonly string Value;

        [OutputConstructor]
        private ConfigurationConfigurations(
            string name,
            string value)
        {
            Name = name;
            Value = value;
        }
    }

    [OutputType]
    public sealed class ConfigurationDatastore
    {
        public readonly string Type;
        public readonly string Version;

        [OutputConstructor]
        private ConfigurationDatastore(
            string type,
            string version)
        {
            Type = type;
            Version = version;
        }
    }
    }
}
