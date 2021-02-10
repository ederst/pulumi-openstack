// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package containerinfra

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// ## Import
//
// Clusters can be imported using the `id`, e.g.
//
// ```sh
//  $ pulumi import openstack:containerinfra/cluster:Cluster cluster_1 ce0f9463-dd25-474b-9fe8-94de63e5e42b
// ```
type Cluster struct {
	pulumi.CustomResourceState

	ApiAddress        pulumi.StringOutput      `pulumi:"apiAddress"`
	ClusterTemplateId pulumi.StringOutput      `pulumi:"clusterTemplateId"`
	CoeVersion        pulumi.StringOutput      `pulumi:"coeVersion"`
	ContainerVersion  pulumi.StringOutput      `pulumi:"containerVersion"`
	CreateTimeout     pulumi.IntOutput         `pulumi:"createTimeout"`
	CreatedAt         pulumi.StringOutput      `pulumi:"createdAt"`
	DiscoveryUrl      pulumi.StringOutput      `pulumi:"discoveryUrl"`
	DockerVolumeSize  pulumi.IntOutput         `pulumi:"dockerVolumeSize"`
	FixedNetwork      pulumi.StringOutput      `pulumi:"fixedNetwork"`
	FixedSubnet       pulumi.StringOutput      `pulumi:"fixedSubnet"`
	Flavor            pulumi.StringOutput      `pulumi:"flavor"`
	FloatingIpEnabled pulumi.BoolOutput        `pulumi:"floatingIpEnabled"`
	Keypair           pulumi.StringOutput      `pulumi:"keypair"`
	Kubeconfig        ClusterKubeconfigOutput  `pulumi:"kubeconfig"`
	Labels            pulumi.MapOutput         `pulumi:"labels"`
	MasterAddresses   pulumi.StringArrayOutput `pulumi:"masterAddresses"`
	MasterCount       pulumi.IntOutput         `pulumi:"masterCount"`
	MasterFlavor      pulumi.StringOutput      `pulumi:"masterFlavor"`
	MergeLabels       pulumi.BoolPtrOutput     `pulumi:"mergeLabels"`
	Name              pulumi.StringOutput      `pulumi:"name"`
	NodeAddresses     pulumi.StringArrayOutput `pulumi:"nodeAddresses"`
	NodeCount         pulumi.IntOutput         `pulumi:"nodeCount"`
	ProjectId         pulumi.StringOutput      `pulumi:"projectId"`
	Region            pulumi.StringOutput      `pulumi:"region"`
	StackId           pulumi.StringOutput      `pulumi:"stackId"`
	UpdatedAt         pulumi.StringOutput      `pulumi:"updatedAt"`
	UserId            pulumi.StringOutput      `pulumi:"userId"`
}

// NewCluster registers a new resource with the given unique name, arguments, and options.
func NewCluster(ctx *pulumi.Context,
	name string, args *ClusterArgs, opts ...pulumi.ResourceOption) (*Cluster, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ClusterTemplateId == nil {
		return nil, errors.New("invalid value for required argument 'ClusterTemplateId'")
	}
	var resource Cluster
	err := ctx.RegisterResource("openstack:containerinfra/cluster:Cluster", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCluster gets an existing Cluster resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCluster(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ClusterState, opts ...pulumi.ResourceOption) (*Cluster, error) {
	var resource Cluster
	err := ctx.ReadResource("openstack:containerinfra/cluster:Cluster", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Cluster resources.
type clusterState struct {
	ApiAddress        *string                `pulumi:"apiAddress"`
	ClusterTemplateId *string                `pulumi:"clusterTemplateId"`
	CoeVersion        *string                `pulumi:"coeVersion"`
	ContainerVersion  *string                `pulumi:"containerVersion"`
	CreateTimeout     *int                   `pulumi:"createTimeout"`
	CreatedAt         *string                `pulumi:"createdAt"`
	DiscoveryUrl      *string                `pulumi:"discoveryUrl"`
	DockerVolumeSize  *int                   `pulumi:"dockerVolumeSize"`
	FixedNetwork      *string                `pulumi:"fixedNetwork"`
	FixedSubnet       *string                `pulumi:"fixedSubnet"`
	Flavor            *string                `pulumi:"flavor"`
	FloatingIpEnabled *bool                  `pulumi:"floatingIpEnabled"`
	Keypair           *string                `pulumi:"keypair"`
	Kubeconfig        *ClusterKubeconfig     `pulumi:"kubeconfig"`
	Labels            map[string]interface{} `pulumi:"labels"`
	MasterAddresses   []string               `pulumi:"masterAddresses"`
	MasterCount       *int                   `pulumi:"masterCount"`
	MasterFlavor      *string                `pulumi:"masterFlavor"`
	MergeLabels       *bool                  `pulumi:"mergeLabels"`
	Name              *string                `pulumi:"name"`
	NodeAddresses     []string               `pulumi:"nodeAddresses"`
	NodeCount         *int                   `pulumi:"nodeCount"`
	ProjectId         *string                `pulumi:"projectId"`
	Region            *string                `pulumi:"region"`
	StackId           *string                `pulumi:"stackId"`
	UpdatedAt         *string                `pulumi:"updatedAt"`
	UserId            *string                `pulumi:"userId"`
}

type ClusterState struct {
	ApiAddress        pulumi.StringPtrInput
	ClusterTemplateId pulumi.StringPtrInput
	CoeVersion        pulumi.StringPtrInput
	ContainerVersion  pulumi.StringPtrInput
	CreateTimeout     pulumi.IntPtrInput
	CreatedAt         pulumi.StringPtrInput
	DiscoveryUrl      pulumi.StringPtrInput
	DockerVolumeSize  pulumi.IntPtrInput
	FixedNetwork      pulumi.StringPtrInput
	FixedSubnet       pulumi.StringPtrInput
	Flavor            pulumi.StringPtrInput
	FloatingIpEnabled pulumi.BoolPtrInput
	Keypair           pulumi.StringPtrInput
	Kubeconfig        ClusterKubeconfigPtrInput
	Labels            pulumi.MapInput
	MasterAddresses   pulumi.StringArrayInput
	MasterCount       pulumi.IntPtrInput
	MasterFlavor      pulumi.StringPtrInput
	MergeLabels       pulumi.BoolPtrInput
	Name              pulumi.StringPtrInput
	NodeAddresses     pulumi.StringArrayInput
	NodeCount         pulumi.IntPtrInput
	ProjectId         pulumi.StringPtrInput
	Region            pulumi.StringPtrInput
	StackId           pulumi.StringPtrInput
	UpdatedAt         pulumi.StringPtrInput
	UserId            pulumi.StringPtrInput
}

func (ClusterState) ElementType() reflect.Type {
	return reflect.TypeOf((*clusterState)(nil)).Elem()
}

type clusterArgs struct {
	ClusterTemplateId string                 `pulumi:"clusterTemplateId"`
	CreateTimeout     *int                   `pulumi:"createTimeout"`
	DiscoveryUrl      *string                `pulumi:"discoveryUrl"`
	DockerVolumeSize  *int                   `pulumi:"dockerVolumeSize"`
	FixedNetwork      *string                `pulumi:"fixedNetwork"`
	FixedSubnet       *string                `pulumi:"fixedSubnet"`
	Flavor            *string                `pulumi:"flavor"`
	FloatingIpEnabled *bool                  `pulumi:"floatingIpEnabled"`
	Keypair           *string                `pulumi:"keypair"`
	Labels            map[string]interface{} `pulumi:"labels"`
	MasterCount       *int                   `pulumi:"masterCount"`
	MasterFlavor      *string                `pulumi:"masterFlavor"`
	MergeLabels       *bool                  `pulumi:"mergeLabels"`
	Name              *string                `pulumi:"name"`
	NodeCount         *int                   `pulumi:"nodeCount"`
	Region            *string                `pulumi:"region"`
}

// The set of arguments for constructing a Cluster resource.
type ClusterArgs struct {
	ClusterTemplateId pulumi.StringInput
	CreateTimeout     pulumi.IntPtrInput
	DiscoveryUrl      pulumi.StringPtrInput
	DockerVolumeSize  pulumi.IntPtrInput
	FixedNetwork      pulumi.StringPtrInput
	FixedSubnet       pulumi.StringPtrInput
	Flavor            pulumi.StringPtrInput
	FloatingIpEnabled pulumi.BoolPtrInput
	Keypair           pulumi.StringPtrInput
	Labels            pulumi.MapInput
	MasterCount       pulumi.IntPtrInput
	MasterFlavor      pulumi.StringPtrInput
	MergeLabels       pulumi.BoolPtrInput
	Name              pulumi.StringPtrInput
	NodeCount         pulumi.IntPtrInput
	Region            pulumi.StringPtrInput
}

func (ClusterArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*clusterArgs)(nil)).Elem()
}

type ClusterInput interface {
	pulumi.Input

	ToClusterOutput() ClusterOutput
	ToClusterOutputWithContext(ctx context.Context) ClusterOutput
}

func (*Cluster) ElementType() reflect.Type {
	return reflect.TypeOf((*Cluster)(nil))
}

func (i *Cluster) ToClusterOutput() ClusterOutput {
	return i.ToClusterOutputWithContext(context.Background())
}

func (i *Cluster) ToClusterOutputWithContext(ctx context.Context) ClusterOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ClusterOutput)
}

type ClusterOutput struct {
	*pulumi.OutputState
}

func (ClusterOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Cluster)(nil))
}

func (o ClusterOutput) ToClusterOutput() ClusterOutput {
	return o
}

func (o ClusterOutput) ToClusterOutputWithContext(ctx context.Context) ClusterOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ClusterOutput{})
}
