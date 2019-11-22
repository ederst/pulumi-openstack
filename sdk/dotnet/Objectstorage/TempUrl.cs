// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Openstack.Objectstorage
{
    /// <summary>
    /// Use this resource to generate an OpenStack Object Storage temporary URL.
    /// 
    /// The temporary URL will be valid for as long as TTL is set to (in seconds).
    /// Once the URL has expired, it will no longer be valid, but the resource
    /// will remain in place. If you wish to automatically regenerate a URL, set
    /// the `regenerate` argument to `true`. This will create a new resource with
    /// a new ID and URL.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/objectstorage_tempurl_v1.html.markdown.
    /// </summary>
    public partial class TempUrl : Pulumi.CustomResource
    {
        /// <summary>
        /// The container name the object belongs to.
        /// </summary>
        [Output("container")]
        public Output<string> Container { get; private set; } = null!;

        /// <summary>
        /// The method allowed when accessing this URL.
        /// Valid values are `GET`, and `POST`. Default is `GET`.
        /// </summary>
        [Output("method")]
        public Output<string?> Method { get; private set; } = null!;

        /// <summary>
        /// The object name the tempurl is for.
        /// </summary>
        [Output("object")]
        public Output<string> Object { get; private set; } = null!;

        /// <summary>
        /// Whether to automatically regenerate the URL when
        /// it has expired. If set to true, this will create a new resource with a new
        /// ID and new URL. Defaults to false.
        /// </summary>
        [Output("regenerate")]
        public Output<bool?> Regenerate { get; private set; } = null!;

        /// <summary>
        /// The region the tempurl is located in.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        [Output("split")]
        public Output<string?> Split { get; private set; } = null!;

        /// <summary>
        /// The TTL, in seconds, for the URL. For how long it should
        /// be valid.
        /// </summary>
        [Output("ttl")]
        public Output<int> Ttl { get; private set; } = null!;

        /// <summary>
        /// The URL
        /// </summary>
        [Output("url")]
        public Output<string> Url { get; private set; } = null!;


        /// <summary>
        /// Create a TempUrl resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public TempUrl(string name, TempUrlArgs args, CustomResourceOptions? options = null)
            : base("openstack:objectstorage/tempUrl:TempUrl", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private TempUrl(string name, Input<string> id, TempUrlState? state = null, CustomResourceOptions? options = null)
            : base("openstack:objectstorage/tempUrl:TempUrl", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing TempUrl resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static TempUrl Get(string name, Input<string> id, TempUrlState? state = null, CustomResourceOptions? options = null)
        {
            return new TempUrl(name, id, state, options);
        }
    }

    public sealed class TempUrlArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The container name the object belongs to.
        /// </summary>
        [Input("container", required: true)]
        public Input<string> Container { get; set; } = null!;

        /// <summary>
        /// The method allowed when accessing this URL.
        /// Valid values are `GET`, and `POST`. Default is `GET`.
        /// </summary>
        [Input("method")]
        public Input<string>? Method { get; set; }

        /// <summary>
        /// The object name the tempurl is for.
        /// </summary>
        [Input("object", required: true)]
        public Input<string> Object { get; set; } = null!;

        /// <summary>
        /// Whether to automatically regenerate the URL when
        /// it has expired. If set to true, this will create a new resource with a new
        /// ID and new URL. Defaults to false.
        /// </summary>
        [Input("regenerate")]
        public Input<bool>? Regenerate { get; set; }

        /// <summary>
        /// The region the tempurl is located in.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("split")]
        public Input<string>? Split { get; set; }

        /// <summary>
        /// The TTL, in seconds, for the URL. For how long it should
        /// be valid.
        /// </summary>
        [Input("ttl", required: true)]
        public Input<int> Ttl { get; set; } = null!;

        public TempUrlArgs()
        {
        }
    }

    public sealed class TempUrlState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The container name the object belongs to.
        /// </summary>
        [Input("container")]
        public Input<string>? Container { get; set; }

        /// <summary>
        /// The method allowed when accessing this URL.
        /// Valid values are `GET`, and `POST`. Default is `GET`.
        /// </summary>
        [Input("method")]
        public Input<string>? Method { get; set; }

        /// <summary>
        /// The object name the tempurl is for.
        /// </summary>
        [Input("object")]
        public Input<string>? Object { get; set; }

        /// <summary>
        /// Whether to automatically regenerate the URL when
        /// it has expired. If set to true, this will create a new resource with a new
        /// ID and new URL. Defaults to false.
        /// </summary>
        [Input("regenerate")]
        public Input<bool>? Regenerate { get; set; }

        /// <summary>
        /// The region the tempurl is located in.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("split")]
        public Input<string>? Split { get; set; }

        /// <summary>
        /// The TTL, in seconds, for the URL. For how long it should
        /// be valid.
        /// </summary>
        [Input("ttl")]
        public Input<int>? Ttl { get; set; }

        /// <summary>
        /// The URL
        /// </summary>
        [Input("url")]
        public Input<string>? Url { get; set; }

        public TempUrlState()
        {
        }
    }
}
