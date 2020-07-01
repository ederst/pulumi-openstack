// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OpenStack.Identity
{
    public static class GetEndpoint
    {
        /// <summary>
        /// Use this data source to get the ID of an OpenStack endpoint.
        /// 
        /// &gt; **Note:** This usually requires admin privileges.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using OpenStack = Pulumi.OpenStack;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var endpoint1 = Output.Create(OpenStack.Identity.GetEndpoint.InvokeAsync(new OpenStack.Identity.GetEndpointArgs
        ///         {
        ///             ServiceName = "demo",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetEndpointResult> InvokeAsync(GetEndpointArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetEndpointResult>("openstack:identity/getEndpoint:getEndpoint", args ?? new GetEndpointArgs(), options.WithVersion());
    }


    public sealed class GetEndpointArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The region the endpoint is assigned to. The
        /// `region` and `endpoint_region` can be different.
        /// </summary>
        [Input("endpointRegion")]
        public string? EndpointRegion { get; set; }

        /// <summary>
        /// The endpoint interface. Valid values are `public`,
        /// `internal`, and `admin`. Default value is `public`
        /// </summary>
        [Input("interface")]
        public string? Interface { get; set; }

        /// <summary>
        /// The name of the endpoint.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// The region in which to obtain the V3 Keystone client.
        /// If omitted, the `region` argument of the provider is used.
        /// </summary>
        [Input("region")]
        public string? Region { get; set; }

        /// <summary>
        /// The service id this endpoint belongs to.
        /// </summary>
        [Input("serviceId")]
        public string? ServiceId { get; set; }

        /// <summary>
        /// The service name of the endpoint.
        /// </summary>
        [Input("serviceName")]
        public string? ServiceName { get; set; }

        /// <summary>
        /// The service type of the endpoint.
        /// </summary>
        [Input("serviceType")]
        public string? ServiceType { get; set; }

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
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
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

        [OutputConstructor]
        private GetEndpointResult(
            string? endpointRegion,

            string id,

            string? @interface,

            string? name,

            string region,

            string? serviceId,

            string? serviceName,

            string? serviceType,

            string url)
        {
            EndpointRegion = endpointRegion;
            Id = id;
            Interface = @interface;
            Name = name;
            Region = region;
            ServiceId = serviceId;
            ServiceName = serviceName;
            ServiceType = serviceType;
            Url = url;
        }
    }
}
