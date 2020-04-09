module github.com/pulumi/pulumi-openstack/provider/v2

go 1.12

require (
	github.com/hashicorp/terraform-plugin-sdk v1.7.0
	github.com/pulumi/pulumi-terraform-bridge/v2 v2.0.0-20200402101519-95d9d3e2b896
	github.com/pulumi/pulumi/sdk/v2 v2.0.0-beta.2.0.20200402101052-1dbf088db686
	github.com/terraform-providers/terraform-provider-openstack v1.26.0
)

replace github.com/Azure/go-autorest => github.com/Azure/go-autorest v12.4.3+incompatible
