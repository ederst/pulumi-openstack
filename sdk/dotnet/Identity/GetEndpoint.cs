// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Openstack.Identity
{
    public static partial class Invokes
    {
        /// <summary>
        /// Use this data source to get the ID of an OpenStack endpoint.
        /// 
        /// &gt; **Note:** This usually requires admin privileges.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/identity_endpoint_v3.html.markdown.
        /// </summary>
        public static Task<GetEndpointResult> GetEndpoint(GetEndpointArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetEndpointResult>("openstack:identity/getEndpoint:getEndpoint", args ?? ResourceArgs.Empty, options.WithVersion());
    }

    public sealed class GetEndpointArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The region the endpoint is assigned to. The
        /// `region` and `endpoint_region` can be different.
        /// </summary>
        [Input("endpointRegion")]
        public Input<string>? EndpointRegion { get; set; }

        /// <summary>
        /// The endpoint interface. Valid values are `public`,
        /// `internal`, and `admin`. Default value is `public`
        /// </summary>
        [Input("interface")]
        public Input<string>? Interface { get; set; }

        /// <summary>
        /// The name of the endpoint.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The region in which to obtain the V3 Keystone client.
        /// If omitted, the `region` argument of the provider is used.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The service id this endpoint belongs to.
        /// </summary>
        [Input("serviceId")]
        public Input<string>? ServiceId { get; set; }

        /// <summary>
        /// The service name of the endpoint.
        /// </summary>
        [Input("serviceName")]
        public Input<string>? ServiceName { get; set; }

        /// <summary>
        /// The service type of the endpoint.
        /// </summary>
        [Input("serviceType")]
        public Input<string>? ServiceType { get; set; }

        public GetEndpointArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetEndpointResult
    {
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string? EndpointRegion;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string? Interface;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string Region;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string? ServiceId;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string? ServiceName;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string? ServiceType;
        /// <summary>
        /// The endpoint URL.
        /// </summary>
        public readonly string Url;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetEndpointResult(
            string? endpointRegion,
            string? @interface,
            string? name,
            string region,
            string? serviceId,
            string? serviceName,
            string? serviceType,
            string url,
            string id)
        {
            EndpointRegion = endpointRegion;
            Interface = @interface;
            Name = name;
            Region = region;
            ServiceId = serviceId;
            ServiceName = serviceName;
            ServiceType = serviceType;
            Url = url;
            Id = id;
        }
    }
}
