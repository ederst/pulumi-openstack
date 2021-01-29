// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package objectstorage

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi-openstack/sdk/v2/go/openstack"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "openstack:objectstorage/container:Container":
		r, err = NewContainer(ctx, name, nil, pulumi.URN_(urn))
	case "openstack:objectstorage/containerObject:ContainerObject":
		r, err = NewContainerObject(ctx, name, nil, pulumi.URN_(urn))
	case "openstack:objectstorage/tempUrl:TempUrl":
		r, err = NewTempUrl(ctx, name, nil, pulumi.URN_(urn))
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	return
}

func init() {
	version, err := openstack.PkgVersion()
	if err != nil {
		fmt.Println("failed to determine package version. defaulting to v1: %v", err)
	}
	pulumi.RegisterResourceModule(
		"openstack",
		"objectstorage/container",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"openstack",
		"objectstorage/containerObject",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"openstack",
		"objectstorage/tempUrl",
		&module{version},
	)
}