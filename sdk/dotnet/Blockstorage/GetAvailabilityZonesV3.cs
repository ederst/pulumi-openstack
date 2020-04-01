// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OpenStack.BlockStorage
{
    public static partial class Invokes
    {
        /// <summary>
        /// Use this data source to get a list of Block Storage availability zones from OpenStack
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/blockstorage_availability_zones_v3.html.markdown.
        /// </summary>
        [Obsolete("Use GetAvailabilityZonesV3.InvokeAsync() instead")]
        public static Task<GetAvailabilityZonesV3Result> GetAvailabilityZonesV3(GetAvailabilityZonesV3Args? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetAvailabilityZonesV3Result>("openstack:blockstorage/getAvailabilityZonesV3:getAvailabilityZonesV3", args ?? InvokeArgs.Empty, options.WithVersion());
    }
    public static class GetAvailabilityZonesV3
    {
        /// <summary>
        /// Use this data source to get a list of Block Storage availability zones from OpenStack
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/d/blockstorage_availability_zones_v3.html.markdown.
        /// </summary>
        public static Task<GetAvailabilityZonesV3Result> InvokeAsync(GetAvailabilityZonesV3Args? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetAvailabilityZonesV3Result>("openstack:blockstorage/getAvailabilityZonesV3:getAvailabilityZonesV3", args ?? InvokeArgs.Empty, options.WithVersion());
    }

    public sealed class GetAvailabilityZonesV3Args : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The region in which to obtain the Block Storage client.
        /// If omitted, the `region` argument of the provider is used.
        /// </summary>
        [Input("region")]
        public string? Region { get; set; }

        /// <summary>
        /// The `state` of the availability zones to match. Can
        /// either be `available` or `unavailable`. Default is `available`.
        /// </summary>
        [Input("state")]
        public string? State { get; set; }

        public GetAvailabilityZonesV3Args()
        {
        }
    }

    [OutputType]
    public sealed class GetAvailabilityZonesV3Result
    {
        /// <summary>
        /// The names of the availability zones, ordered alphanumerically, that
        /// match the queried `state`.
        /// </summary>
        public readonly ImmutableArray<string> Names;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string Region;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string? State;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetAvailabilityZonesV3Result(
            ImmutableArray<string> names,
            string region,
            string? state,
            string id)
        {
            Names = names;
            Region = region;
            State = state;
            Id = id;
        }
    }
}
