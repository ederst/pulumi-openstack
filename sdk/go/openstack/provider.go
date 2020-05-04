// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package openstack

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// The provider type for the openstack package. By default, resources use package-wide configuration
// settings, however an explicit `Provider` instance may be created and passed during resource
// construction to achieve fine-grained programmatic control over provider settings. See the
// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
type Provider struct {
	pulumi.ProviderResourceState
}

// NewProvider registers a new resource with the given unique name, arguments, and options.
func NewProvider(ctx *pulumi.Context,
	name string, args *ProviderArgs, opts ...pulumi.ResourceOption) (*Provider, error) {
	if args == nil {
		args = &ProviderArgs{}
	}
	if args.AllowReauth == nil {
		args.AllowReauth = pulumi.BoolPtr(getEnvOrDefault(false, parseEnvBool, "OS_ALLOW_REAUTH").(bool))
	}
	if args.ApplicationCredentialId == nil {
		args.ApplicationCredentialId = pulumi.StringPtr(getEnvOrDefault("", nil, "OS_APPLICATION_CREDENTIAL_ID").(string))
	}
	if args.ApplicationCredentialName == nil {
		args.ApplicationCredentialName = pulumi.StringPtr(getEnvOrDefault("", nil, "OS_APPLICATION_CREDENTIAL_NAME").(string))
	}
	if args.ApplicationCredentialSecret == nil {
		args.ApplicationCredentialSecret = pulumi.StringPtr(getEnvOrDefault("", nil, "OS_APPLICATION_CREDENTIAL_SECRET").(string))
	}
	if args.AuthUrl == nil {
		args.AuthUrl = pulumi.StringPtr(getEnvOrDefault("", nil, "OS_AUTH_URL").(string))
	}
	if args.CacertFile == nil {
		args.CacertFile = pulumi.StringPtr(getEnvOrDefault("", nil, "OS_CACERT").(string))
	}
	if args.Cert == nil {
		args.Cert = pulumi.StringPtr(getEnvOrDefault("", nil, "OS_CERT").(string))
	}
	if args.Cloud == nil {
		args.Cloud = pulumi.StringPtr(getEnvOrDefault("", nil, "OS_CLOUD").(string))
	}
	if args.DefaultDomain == nil {
		args.DefaultDomain = pulumi.StringPtr(getEnvOrDefault("default", nil, "OS_DEFAULT_DOMAIN").(string))
	}
	if args.DelayedAuth == nil {
		args.DelayedAuth = pulumi.BoolPtr(getEnvOrDefault(false, parseEnvBool, "OS_DELAYED_AUTH").(bool))
	}
	if args.DomainId == nil {
		args.DomainId = pulumi.StringPtr(getEnvOrDefault("", nil, "OS_DOMAIN_ID").(string))
	}
	if args.DomainName == nil {
		args.DomainName = pulumi.StringPtr(getEnvOrDefault("", nil, "OS_DOMAIN_NAME").(string))
	}
	if args.EndpointType == nil {
		args.EndpointType = pulumi.StringPtr(getEnvOrDefault("", nil, "OS_ENDPOINT_TYPE").(string))
	}
	if args.Insecure == nil {
		args.Insecure = pulumi.BoolPtr(getEnvOrDefault(false, parseEnvBool, "OS_INSECURE").(bool))
	}
	if args.Key == nil {
		args.Key = pulumi.StringPtr(getEnvOrDefault("", nil, "OS_KEY").(string))
	}
	if args.Password == nil {
		args.Password = pulumi.StringPtr(getEnvOrDefault("", nil, "OS_PASSWORD").(string))
	}
	if args.ProjectDomainId == nil {
		args.ProjectDomainId = pulumi.StringPtr(getEnvOrDefault("", nil, "OS_PROJECT_DOMAIN_ID").(string))
	}
	if args.ProjectDomainName == nil {
		args.ProjectDomainName = pulumi.StringPtr(getEnvOrDefault("", nil, "OS_PROJECT_DOMAIN_NAME").(string))
	}
	if args.Region == nil {
		args.Region = pulumi.StringPtr(getEnvOrDefault("", nil, "OS_REGION_NAME").(string))
	}
	if args.Swauth == nil {
		args.Swauth = pulumi.BoolPtr(getEnvOrDefault(false, parseEnvBool, "OS_SWAUTH").(bool))
	}
	if args.TenantId == nil {
		args.TenantId = pulumi.StringPtr(getEnvOrDefault("", nil, "OS_TENANT_ID", "OS_PROJECT_ID").(string))
	}
	if args.TenantName == nil {
		args.TenantName = pulumi.StringPtr(getEnvOrDefault("", nil, "OS_TENANT_NAME", "OS_PROJECT_NAME").(string))
	}
	if args.Token == nil {
		args.Token = pulumi.StringPtr(getEnvOrDefault("", nil, "OS_TOKEN", "OS_AUTH_TOKEN").(string))
	}
	if args.UseOctavia == nil {
		args.UseOctavia = pulumi.BoolPtr(getEnvOrDefault(false, parseEnvBool, "OS_USE_OCTAVIA").(bool))
	}
	if args.UserDomainId == nil {
		args.UserDomainId = pulumi.StringPtr(getEnvOrDefault("", nil, "OS_USER_DOMAIN_ID").(string))
	}
	if args.UserDomainName == nil {
		args.UserDomainName = pulumi.StringPtr(getEnvOrDefault("", nil, "OS_USER_DOMAIN_NAME").(string))
	}
	if args.UserId == nil {
		args.UserId = pulumi.StringPtr(getEnvOrDefault("", nil, "OS_USER_ID").(string))
	}
	if args.UserName == nil {
		args.UserName = pulumi.StringPtr(getEnvOrDefault("", nil, "OS_USERNAME").(string))
	}
	var resource Provider
	err := ctx.RegisterResource("pulumi:providers:openstack", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

type providerArgs struct {
	// If set to `false`, OpenStack authorization won't be perfomed automatically, if the initial auth token get expired.
	// Defaults to `true`
	AllowReauth *bool `pulumi:"allowReauth"`
	// Application Credential ID to login with.
	ApplicationCredentialId *string `pulumi:"applicationCredentialId"`
	// Application Credential name to login with.
	ApplicationCredentialName *string `pulumi:"applicationCredentialName"`
	// Application Credential secret to login with.
	ApplicationCredentialSecret *string `pulumi:"applicationCredentialSecret"`
	// The Identity authentication URL.
	AuthUrl *string `pulumi:"authUrl"`
	// A Custom CA certificate.
	CacertFile *string `pulumi:"cacertFile"`
	// A client certificate to authenticate with.
	Cert *string `pulumi:"cert"`
	// An entry in a `clouds.yaml` file to use.
	Cloud *string `pulumi:"cloud"`
	// The name of the Domain ID to scope to if no other domain is specified. Defaults to `default` (Identity v3).
	DefaultDomain *string `pulumi:"defaultDomain"`
	// If set to `false`, OpenStack authorization will be perfomed, every time the service provider client is called. Defaults
	// to `true`.
	DelayedAuth *bool `pulumi:"delayedAuth"`
	// If set to `true`, the HTTP `Cache-Control: no-cache` header will not be added by default to all API requests.
	DisableNoCacheHeader *bool `pulumi:"disableNoCacheHeader"`
	// The ID of the Domain to scope to (Identity v3).
	DomainId *string `pulumi:"domainId"`
	// The name of the Domain to scope to (Identity v3).
	DomainName *string `pulumi:"domainName"`
	// A map of services with an endpoint to override what was from the Keystone catalog
	EndpointOverrides map[string]interface{} `pulumi:"endpointOverrides"`
	EndpointType      *string                `pulumi:"endpointType"`
	// Trust self-signed certificates.
	Insecure *bool `pulumi:"insecure"`
	// A client private key to authenticate with.
	Key *string `pulumi:"key"`
	// How many times HTTP connection should be retried until giving up.
	MaxRetries *int `pulumi:"maxRetries"`
	// Password to login with.
	Password *string `pulumi:"password"`
	// The ID of the domain where the proejct resides (Identity v3).
	ProjectDomainId *string `pulumi:"projectDomainId"`
	// The name of the domain where the project resides (Identity v3).
	ProjectDomainName *string `pulumi:"projectDomainName"`
	// The OpenStack region to connect to.
	Region *string `pulumi:"region"`
	// Use Swift's authentication system instead of Keystone. Only used for interaction with Swift.
	Swauth *bool `pulumi:"swauth"`
	// The ID of the Tenant (Identity v2) or Project (Identity v3) to login with.
	TenantId *string `pulumi:"tenantId"`
	// The name of the Tenant (Identity v2) or Project (Identity v3) to login with.
	TenantName *string `pulumi:"tenantName"`
	// Authentication token to use as an alternative to username/password.
	Token *string `pulumi:"token"`
	// If set to `true`, API requests will go the Load Balancer service (Octavia) instead of the Networking service (Neutron).
	UseOctavia *bool `pulumi:"useOctavia"`
	// The ID of the domain where the user resides (Identity v3).
	UserDomainId *string `pulumi:"userDomainId"`
	// The name of the domain where the user resides (Identity v3).
	UserDomainName *string `pulumi:"userDomainName"`
	// Username to login with.
	UserId *string `pulumi:"userId"`
	// Username to login with.
	UserName *string `pulumi:"userName"`
}

// The set of arguments for constructing a Provider resource.
type ProviderArgs struct {
	// If set to `false`, OpenStack authorization won't be perfomed automatically, if the initial auth token get expired.
	// Defaults to `true`
	AllowReauth pulumi.BoolPtrInput
	// Application Credential ID to login with.
	ApplicationCredentialId pulumi.StringPtrInput
	// Application Credential name to login with.
	ApplicationCredentialName pulumi.StringPtrInput
	// Application Credential secret to login with.
	ApplicationCredentialSecret pulumi.StringPtrInput
	// The Identity authentication URL.
	AuthUrl pulumi.StringPtrInput
	// A Custom CA certificate.
	CacertFile pulumi.StringPtrInput
	// A client certificate to authenticate with.
	Cert pulumi.StringPtrInput
	// An entry in a `clouds.yaml` file to use.
	Cloud pulumi.StringPtrInput
	// The name of the Domain ID to scope to if no other domain is specified. Defaults to `default` (Identity v3).
	DefaultDomain pulumi.StringPtrInput
	// If set to `false`, OpenStack authorization will be perfomed, every time the service provider client is called. Defaults
	// to `true`.
	DelayedAuth pulumi.BoolPtrInput
	// If set to `true`, the HTTP `Cache-Control: no-cache` header will not be added by default to all API requests.
	DisableNoCacheHeader pulumi.BoolPtrInput
	// The ID of the Domain to scope to (Identity v3).
	DomainId pulumi.StringPtrInput
	// The name of the Domain to scope to (Identity v3).
	DomainName pulumi.StringPtrInput
	// A map of services with an endpoint to override what was from the Keystone catalog
	EndpointOverrides pulumi.MapInput
	EndpointType      pulumi.StringPtrInput
	// Trust self-signed certificates.
	Insecure pulumi.BoolPtrInput
	// A client private key to authenticate with.
	Key pulumi.StringPtrInput
	// How many times HTTP connection should be retried until giving up.
	MaxRetries pulumi.IntPtrInput
	// Password to login with.
	Password pulumi.StringPtrInput
	// The ID of the domain where the proejct resides (Identity v3).
	ProjectDomainId pulumi.StringPtrInput
	// The name of the domain where the project resides (Identity v3).
	ProjectDomainName pulumi.StringPtrInput
	// The OpenStack region to connect to.
	Region pulumi.StringPtrInput
	// Use Swift's authentication system instead of Keystone. Only used for interaction with Swift.
	Swauth pulumi.BoolPtrInput
	// The ID of the Tenant (Identity v2) or Project (Identity v3) to login with.
	TenantId pulumi.StringPtrInput
	// The name of the Tenant (Identity v2) or Project (Identity v3) to login with.
	TenantName pulumi.StringPtrInput
	// Authentication token to use as an alternative to username/password.
	Token pulumi.StringPtrInput
	// If set to `true`, API requests will go the Load Balancer service (Octavia) instead of the Networking service (Neutron).
	UseOctavia pulumi.BoolPtrInput
	// The ID of the domain where the user resides (Identity v3).
	UserDomainId pulumi.StringPtrInput
	// The name of the domain where the user resides (Identity v3).
	UserDomainName pulumi.StringPtrInput
	// Username to login with.
	UserId pulumi.StringPtrInput
	// Username to login with.
	UserName pulumi.StringPtrInput
}

func (ProviderArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*providerArgs)(nil)).Elem()
}
