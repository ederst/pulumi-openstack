// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.OpenStack.VPNaaS
{
    /// <summary>
    /// Manages a V2 Neutron VPN service resource within OpenStack.
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
    ///         var service1 = new OpenStack.VPNaaS.Service("service1", new OpenStack.VPNaaS.ServiceArgs
    ///         {
    ///             AdminStateUp = true,
    ///             RouterId = "14a75700-fc03-4602-9294-26ee44f366b3",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// Services can be imported using the `id`, e.g.
    /// 
    /// ```sh
    ///  $ pulumi import openstack:vpnaas/service:Service service_1 832cb7f3-59fe-40cf-8f64-8350ffc03272
    /// ```
    /// </summary>
    public partial class Service : Pulumi.CustomResource
    {
        /// <summary>
        /// The administrative state of the resource. Can either be up(true) or down(false).
        /// Changing this updates the administrative state of the existing service.
        /// </summary>
        [Output("adminStateUp")]
        public Output<bool?> AdminStateUp { get; private set; } = null!;

        /// <summary>
        /// The human-readable description for the service.
        /// Changing this updates the description of the existing service.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The read-only external (public) IPv4 address that is used for the VPN service.
        /// </summary>
        [Output("externalV4Ip")]
        public Output<string> ExternalV4Ip { get; private set; } = null!;

        /// <summary>
        /// The read-only external (public) IPv6 address that is used for the VPN service.
        /// </summary>
        [Output("externalV6Ip")]
        public Output<string> ExternalV6Ip { get; private set; } = null!;

        /// <summary>
        /// The name of the service. Changing this updates the name of
        /// the existing service.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The region in which to obtain the V2 Networking client.
        /// A Networking client is needed to create a VPN service. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// service.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// The ID of the router. Changing this creates a new service.
        /// </summary>
        [Output("routerId")]
        public Output<string> RouterId { get; private set; } = null!;

        /// <summary>
        /// Indicates whether IPsec VPN service is currently operational. Values are ACTIVE, DOWN, BUILD, ERROR, PENDING_CREATE, PENDING_UPDATE, or PENDING_DELETE.
        /// </summary>
        [Output("status")]
        public Output<string> Status { get; private set; } = null!;

        /// <summary>
        /// SubnetID is the ID of the subnet. Default is null.
        /// </summary>
        [Output("subnetId")]
        public Output<string?> SubnetId { get; private set; } = null!;

        /// <summary>
        /// The owner of the service. Required if admin wants to
        /// create a service for another project. Changing this creates a new service.
        /// </summary>
        [Output("tenantId")]
        public Output<string> TenantId { get; private set; } = null!;

        /// <summary>
        /// Map of additional options.
        /// </summary>
        [Output("valueSpecs")]
        public Output<ImmutableDictionary<string, object>?> ValueSpecs { get; private set; } = null!;


        /// <summary>
        /// Create a Service resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Service(string name, ServiceArgs args, CustomResourceOptions? options = null)
            : base("openstack:vpnaas/service:Service", name, args ?? new ServiceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Service(string name, Input<string> id, ServiceState? state = null, CustomResourceOptions? options = null)
            : base("openstack:vpnaas/service:Service", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Service resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Service Get(string name, Input<string> id, ServiceState? state = null, CustomResourceOptions? options = null)
        {
            return new Service(name, id, state, options);
        }
    }

    public sealed class ServiceArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The administrative state of the resource. Can either be up(true) or down(false).
        /// Changing this updates the administrative state of the existing service.
        /// </summary>
        [Input("adminStateUp")]
        public Input<bool>? AdminStateUp { get; set; }

        /// <summary>
        /// The human-readable description for the service.
        /// Changing this updates the description of the existing service.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the service. Changing this updates the name of
        /// the existing service.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The region in which to obtain the V2 Networking client.
        /// A Networking client is needed to create a VPN service. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// service.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The ID of the router. Changing this creates a new service.
        /// </summary>
        [Input("routerId", required: true)]
        public Input<string> RouterId { get; set; } = null!;

        /// <summary>
        /// SubnetID is the ID of the subnet. Default is null.
        /// </summary>
        [Input("subnetId")]
        public Input<string>? SubnetId { get; set; }

        /// <summary>
        /// The owner of the service. Required if admin wants to
        /// create a service for another project. Changing this creates a new service.
        /// </summary>
        [Input("tenantId")]
        public Input<string>? TenantId { get; set; }

        [Input("valueSpecs")]
        private InputMap<object>? _valueSpecs;

        /// <summary>
        /// Map of additional options.
        /// </summary>
        public InputMap<object> ValueSpecs
        {
            get => _valueSpecs ?? (_valueSpecs = new InputMap<object>());
            set => _valueSpecs = value;
        }

        public ServiceArgs()
        {
        }
    }

    public sealed class ServiceState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The administrative state of the resource. Can either be up(true) or down(false).
        /// Changing this updates the administrative state of the existing service.
        /// </summary>
        [Input("adminStateUp")]
        public Input<bool>? AdminStateUp { get; set; }

        /// <summary>
        /// The human-readable description for the service.
        /// Changing this updates the description of the existing service.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The read-only external (public) IPv4 address that is used for the VPN service.
        /// </summary>
        [Input("externalV4Ip")]
        public Input<string>? ExternalV4Ip { get; set; }

        /// <summary>
        /// The read-only external (public) IPv6 address that is used for the VPN service.
        /// </summary>
        [Input("externalV6Ip")]
        public Input<string>? ExternalV6Ip { get; set; }

        /// <summary>
        /// The name of the service. Changing this updates the name of
        /// the existing service.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The region in which to obtain the V2 Networking client.
        /// A Networking client is needed to create a VPN service. If omitted, the
        /// `region` argument of the provider is used. Changing this creates a new
        /// service.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        /// <summary>
        /// The ID of the router. Changing this creates a new service.
        /// </summary>
        [Input("routerId")]
        public Input<string>? RouterId { get; set; }

        /// <summary>
        /// Indicates whether IPsec VPN service is currently operational. Values are ACTIVE, DOWN, BUILD, ERROR, PENDING_CREATE, PENDING_UPDATE, or PENDING_DELETE.
        /// </summary>
        [Input("status")]
        public Input<string>? Status { get; set; }

        /// <summary>
        /// SubnetID is the ID of the subnet. Default is null.
        /// </summary>
        [Input("subnetId")]
        public Input<string>? SubnetId { get; set; }

        /// <summary>
        /// The owner of the service. Required if admin wants to
        /// create a service for another project. Changing this creates a new service.
        /// </summary>
        [Input("tenantId")]
        public Input<string>? TenantId { get; set; }

        [Input("valueSpecs")]
        private InputMap<object>? _valueSpecs;

        /// <summary>
        /// Map of additional options.
        /// </summary>
        public InputMap<object> ValueSpecs
        {
            get => _valueSpecs ?? (_valueSpecs = new InputMap<object>());
            set => _valueSpecs = value;
        }

        public ServiceState()
        {
        }
    }
}
