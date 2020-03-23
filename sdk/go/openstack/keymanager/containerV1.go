// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package keymanager

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a V1 Barbican container resource within OpenStack.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-openstack/blob/master/website/docs/r/keymanager_container_v1.html.markdown.
type ContainerV1 struct {
	pulumi.CustomResourceState

	// Allows to control an access to a container. Currently only
	// the `read` operation is supported. If not specified, the container is
	// accessible project wide. The `read` structure is described below.
	Acl ContainerV1AclOutput `pulumi:"acl"`
	// The list of the container consumers. The structure is described below.
	Consumers ContainerV1ConsumerArrayOutput `pulumi:"consumers"`
	// The container reference / where to find the container.
	ContainerRef pulumi.StringOutput `pulumi:"containerRef"`
	// The date the container was created.
	CreatedAt pulumi.StringOutput `pulumi:"createdAt"`
	// The creator of the container.
	CreatorId pulumi.StringOutput `pulumi:"creatorId"`
	// Human-readable name for the Container. Does not have
	// to be unique.
	Name pulumi.StringOutput `pulumi:"name"`
	// The region in which to obtain the V1 KeyManager client.
	// A KeyManager client is needed to create a container. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// V1 container.
	Region pulumi.StringOutput `pulumi:"region"`
	// A set of dictionaries containing references to secrets. The structure is described
	// below.
	SecretRefs ContainerV1SecretRefArrayOutput `pulumi:"secretRefs"`
	// The status of the container.
	Status pulumi.StringOutput `pulumi:"status"`
	// Used to indicate the type of container. Must be one of `generic`, `rsa` or `certificate`.
	Type pulumi.StringOutput `pulumi:"type"`
	// The date the container was last updated.
	UpdatedAt pulumi.StringOutput `pulumi:"updatedAt"`
}

// NewContainerV1 registers a new resource with the given unique name, arguments, and options.
func NewContainerV1(ctx *pulumi.Context,
	name string, args *ContainerV1Args, opts ...pulumi.ResourceOption) (*ContainerV1, error) {
	if args == nil || args.Type == nil {
		return nil, errors.New("missing required argument 'Type'")
	}
	if args == nil {
		args = &ContainerV1Args{}
	}
	var resource ContainerV1
	err := ctx.RegisterResource("openstack:keymanager/containerV1:ContainerV1", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetContainerV1 gets an existing ContainerV1 resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetContainerV1(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ContainerV1State, opts ...pulumi.ResourceOption) (*ContainerV1, error) {
	var resource ContainerV1
	err := ctx.ReadResource("openstack:keymanager/containerV1:ContainerV1", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ContainerV1 resources.
type containerV1State struct {
	// Allows to control an access to a container. Currently only
	// the `read` operation is supported. If not specified, the container is
	// accessible project wide. The `read` structure is described below.
	Acl *ContainerV1Acl `pulumi:"acl"`
	// The list of the container consumers. The structure is described below.
	Consumers []ContainerV1Consumer `pulumi:"consumers"`
	// The container reference / where to find the container.
	ContainerRef *string `pulumi:"containerRef"`
	// The date the container was created.
	CreatedAt *string `pulumi:"createdAt"`
	// The creator of the container.
	CreatorId *string `pulumi:"creatorId"`
	// Human-readable name for the Container. Does not have
	// to be unique.
	Name *string `pulumi:"name"`
	// The region in which to obtain the V1 KeyManager client.
	// A KeyManager client is needed to create a container. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// V1 container.
	Region *string `pulumi:"region"`
	// A set of dictionaries containing references to secrets. The structure is described
	// below.
	SecretRefs []ContainerV1SecretRef `pulumi:"secretRefs"`
	// The status of the container.
	Status *string `pulumi:"status"`
	// Used to indicate the type of container. Must be one of `generic`, `rsa` or `certificate`.
	Type *string `pulumi:"type"`
	// The date the container was last updated.
	UpdatedAt *string `pulumi:"updatedAt"`
}

type ContainerV1State struct {
	// Allows to control an access to a container. Currently only
	// the `read` operation is supported. If not specified, the container is
	// accessible project wide. The `read` structure is described below.
	Acl ContainerV1AclPtrInput
	// The list of the container consumers. The structure is described below.
	Consumers ContainerV1ConsumerArrayInput
	// The container reference / where to find the container.
	ContainerRef pulumi.StringPtrInput
	// The date the container was created.
	CreatedAt pulumi.StringPtrInput
	// The creator of the container.
	CreatorId pulumi.StringPtrInput
	// Human-readable name for the Container. Does not have
	// to be unique.
	Name pulumi.StringPtrInput
	// The region in which to obtain the V1 KeyManager client.
	// A KeyManager client is needed to create a container. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// V1 container.
	Region pulumi.StringPtrInput
	// A set of dictionaries containing references to secrets. The structure is described
	// below.
	SecretRefs ContainerV1SecretRefArrayInput
	// The status of the container.
	Status pulumi.StringPtrInput
	// Used to indicate the type of container. Must be one of `generic`, `rsa` or `certificate`.
	Type pulumi.StringPtrInput
	// The date the container was last updated.
	UpdatedAt pulumi.StringPtrInput
}

func (ContainerV1State) ElementType() reflect.Type {
	return reflect.TypeOf((*containerV1State)(nil)).Elem()
}

type containerV1Args struct {
	// Allows to control an access to a container. Currently only
	// the `read` operation is supported. If not specified, the container is
	// accessible project wide. The `read` structure is described below.
	Acl *ContainerV1Acl `pulumi:"acl"`
	// Human-readable name for the Container. Does not have
	// to be unique.
	Name *string `pulumi:"name"`
	// The region in which to obtain the V1 KeyManager client.
	// A KeyManager client is needed to create a container. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// V1 container.
	Region *string `pulumi:"region"`
	// A set of dictionaries containing references to secrets. The structure is described
	// below.
	SecretRefs []ContainerV1SecretRef `pulumi:"secretRefs"`
	// Used to indicate the type of container. Must be one of `generic`, `rsa` or `certificate`.
	Type string `pulumi:"type"`
}

// The set of arguments for constructing a ContainerV1 resource.
type ContainerV1Args struct {
	// Allows to control an access to a container. Currently only
	// the `read` operation is supported. If not specified, the container is
	// accessible project wide. The `read` structure is described below.
	Acl ContainerV1AclPtrInput
	// Human-readable name for the Container. Does not have
	// to be unique.
	Name pulumi.StringPtrInput
	// The region in which to obtain the V1 KeyManager client.
	// A KeyManager client is needed to create a container. If omitted, the
	// `region` argument of the provider is used. Changing this creates a new
	// V1 container.
	Region pulumi.StringPtrInput
	// A set of dictionaries containing references to secrets. The structure is described
	// below.
	SecretRefs ContainerV1SecretRefArrayInput
	// Used to indicate the type of container. Must be one of `generic`, `rsa` or `certificate`.
	Type pulumi.StringInput
}

func (ContainerV1Args) ElementType() reflect.Type {
	return reflect.TypeOf((*containerV1Args)(nil)).Elem()
}

