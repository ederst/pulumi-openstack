// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OpenStack.Identity
{
    public static class GetRole
    {
        /// <summary>
        /// Use this data source to get the ID of an OpenStack role.
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
        ///         var admin = Output.Create(OpenStack.Identity.GetRole.InvokeAsync(new OpenStack.Identity.GetRoleArgs
        ///         {
        ///             Name = "admin",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetRoleResult> InvokeAsync(GetRoleArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetRoleResult>("openstack:identity/getRole:getRole", args ?? new GetRoleArgs(), options.WithVersion());
    }


    public sealed class GetRoleArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The domain the role belongs to.
        /// </summary>
        [Input("domainId")]
        public string? DomainId { get; set; }

        /// <summary>
        /// The name of the role.
        /// </summary>
        [Input("name", required: true)]
        public string Name { get; set; } = null!;

        /// <summary>
        /// The region in which to obtain the V3 Keystone client.
        /// If omitted, the `region` argument of the provider is used.
        /// </summary>
        [Input("region")]
        public string? Region { get; set; }

        public GetRoleArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetRoleResult
    {
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string DomainId;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// See Argument Reference above.
        /// </summary>
        public readonly string Region;

        [OutputConstructor]
        private GetRoleResult(
            string domainId,

            string id,

            string name,

            string region)
        {
            DomainId = domainId;
            Id = id;
            Name = name;
            Region = region;
        }
    }
}
