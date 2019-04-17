// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package containerinfra

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this data source to get the ID of an available OpenStack Magnum cluster
// template.
func LookupClusterTemplate(ctx *pulumi.Context, args *GetClusterTemplateArgs) (*GetClusterTemplateResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["name"] = args.Name
		inputs["region"] = args.Region
	}
	outputs, err := ctx.Invoke("openstack:containerinfra/getClusterTemplate:getClusterTemplate", inputs)
	if err != nil {
		return nil, err
	}
	return &GetClusterTemplateResult{
		ApiserverPort: outputs["apiserverPort"],
		ClusterDistro: outputs["clusterDistro"],
		Coe: outputs["coe"],
		CreatedAt: outputs["createdAt"],
		DnsNameserver: outputs["dnsNameserver"],
		DockerStorageDriver: outputs["dockerStorageDriver"],
		DockerVolumeSize: outputs["dockerVolumeSize"],
		ExternalNetworkId: outputs["externalNetworkId"],
		FixedNetwork: outputs["fixedNetwork"],
		FixedSubnet: outputs["fixedSubnet"],
		Flavor: outputs["flavor"],
		FloatingIpEnabled: outputs["floatingIpEnabled"],
		HttpProxy: outputs["httpProxy"],
		HttpsProxy: outputs["httpsProxy"],
		Image: outputs["image"],
		InsecureRegistry: outputs["insecureRegistry"],
		KeypairId: outputs["keypairId"],
		Labels: outputs["labels"],
		MasterFlavor: outputs["masterFlavor"],
		MasterLbEnabled: outputs["masterLbEnabled"],
		Name: outputs["name"],
		NetworkDriver: outputs["networkDriver"],
		NoProxy: outputs["noProxy"],
		ProjectId: outputs["projectId"],
		Public: outputs["public"],
		Region: outputs["region"],
		RegistryEnabled: outputs["registryEnabled"],
		ServerType: outputs["serverType"],
		TlsDisabled: outputs["tlsDisabled"],
		UpdatedAt: outputs["updatedAt"],
		UserId: outputs["userId"],
		VolumeDriver: outputs["volumeDriver"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getClusterTemplate.
type GetClusterTemplateArgs struct {
	// The name of the cluster template.
	Name interface{}
	// The region in which to obtain the V1 Container Infra
	// client.
	// If omitted, the `region` argument of the provider is used.
	Region interface{}
}

// A collection of values returned by getClusterTemplate.
type GetClusterTemplateResult struct {
	// The API server port for the Container Orchestration
	// Engine for this cluster template.
	ApiserverPort interface{}
	// The distro for the cluster (fedora-atomic, coreos, etc.).
	ClusterDistro interface{}
	// The Container Orchestration Engine for this cluster template.
	Coe interface{}
	// The time at which cluster template was created.
	CreatedAt interface{}
	// Address of the DNS nameserver that is used in nodes of the
	// cluster.
	DnsNameserver interface{}
	// Docker storage driver. Changing this updates the
	// Docker storage driver of the existing cluster template.
	DockerStorageDriver interface{}
	// The size (in GB) of the Docker volume.
	DockerVolumeSize interface{}
	// The ID of the external network that will be used for
	// the cluster.
	ExternalNetworkId interface{}
	// The fixed network that will be attached to the cluster.
	FixedNetwork interface{}
	// =The fixed subnet that will be attached to the cluster.
	FixedSubnet interface{}
	// The flavor for the nodes of the cluster.
	Flavor interface{}
	// Indicates whether created cluster should create IP
	// floating IP for every node or not.
	FloatingIpEnabled interface{}
	// The address of a proxy for receiving all HTTP requests and
	// relay them.
	HttpProxy interface{}
	// The address of a proxy for receiving all HTTPS requests and
	// relay them.
	HttpsProxy interface{}
	// The reference to an image that is used for nodes of the cluster.
	Image interface{}
	// The insecure registry URL for the cluster template.
	InsecureRegistry interface{}
	// The name of the Compute service SSH keypair.
	KeypairId interface{}
	// The list of key value pairs representing additional properties
	// of the cluster template.
	Labels interface{}
	// The flavor for the master nodes.
	MasterFlavor interface{}
	// Indicates whether created cluster should has a
	// loadbalancer for master nodes or not.
	MasterLbEnabled interface{}
	// See Argument Reference above.
	Name interface{}
	// The name of the driver for the container network.
	NetworkDriver interface{}
	// A comma-separated list of IP addresses that shouldn't be used in
	// the cluster.
	NoProxy interface{}
	// The project of the cluster template.
	ProjectId interface{}
	// Indicates whether cluster template should be public.
	Public interface{}
	// See Argument Reference above.
	Region interface{}
	// Indicates whether Docker registry is enabled in the
	// cluster.
	RegistryEnabled interface{}
	// The server type for the cluster template.
	ServerType interface{}
	// Indicates whether the TLS should be disabled in the cluster.
	TlsDisabled interface{}
	// The time at which cluster template was updated.
	UpdatedAt interface{}
	// The user of the cluster template.
	UserId interface{}
	// The name of the driver that is used for the volumes of the
	// cluster nodes.
	VolumeDriver interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
