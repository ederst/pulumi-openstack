// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package database

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
	case "openstack:database/configuration:Configuration":
		r, err = NewConfiguration(ctx, name, nil, pulumi.URN_(urn))
	case "openstack:database/database:Database":
		r, err = NewDatabase(ctx, name, nil, pulumi.URN_(urn))
	case "openstack:database/instance:Instance":
		r, err = NewInstance(ctx, name, nil, pulumi.URN_(urn))
	case "openstack:database/user:User":
		r, err = NewUser(ctx, name, nil, pulumi.URN_(urn))
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
		"database/configuration",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"openstack",
		"database/database",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"openstack",
		"database/instance",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"openstack",
		"database/user",
		&module{version},
	)
}
