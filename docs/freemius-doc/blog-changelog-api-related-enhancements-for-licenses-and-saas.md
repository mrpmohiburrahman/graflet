[Changelog](https://freemius.com/changelog/) / API-related enhancements for Licenses and SaaS

We are pushing more enhancements in our system to cater to SaaS. Recently we looked deeply at our API and how SaaS makers can consume our API. In the process, we delivered the following enhancements.

### Using `product` scope in API endpoint paths

We’ve been using and documenting our API endpoints as `plugin` scopes. The endpoint path usually looks like this:

- v1/`plugins/{plugin_id}`/users.json
- v1/stores/{store\_id}/`plugins/{plugin_id}`/carts.json

While it makes sense for WP products, for general software, term `product` is more appropriate.

Therefore all our product-scoped endpoints can now be accessed with `products` instead of `plugins`. For examples:

- v1/`products/{product_id}`/users.json
- v1/stores/{store\_id}/`products/{product_id}`/carts.json

For backward compatibility purposes, the plugins will keep on working. This is just a small change to make the terminology easier for SaaS makers.

### Correcting public license activation endpoint

We realized we mistakenly [published](blog-changelog-kickstart-litesdk-project-two-new-endpoints-to-activate-and-deactivate-licenses.md) the license activation and deactivation endpoints under

- v1/products/{product\_id}/activate.json
- /v1/products/{product\_id}/deactivate.json

We fixed it by instead publishing under

- v1/products/{product\_id}/licenses/activate.json
- v1/products/{product\_id}/licenses/deactivate.json

The old endpoints are now deprecated and will be removed in the near future. We will also update our LiteSDK.

### New public endpoint for license validation

To ease license validation for software makers, we have introduced a new endpoint.

`/v1/products/{product_id}/installs/{install_id}/license.json` (public)

It requires the following parameters:

- `uid` – The UID of the install which was used during the license activation.
- `license_key` – The license key that was used to activate the install.

On a `GET` request, the endpoint will give back an `license` entity with details like expiration date, whether it is canceled etc.

You can read the [previous changelog](blog-changelog-kickstart-litesdk-project-two-new-endpoints-to-activate-and-deactivate-licenses.md) to under more about the license activation system. A proper documentation will be published soon.

### Consistent parameter naming

We realized the endpoints responsible for creating licenses were using a request parameter named `is_blocking` although the license entity itself has the property `is_block_features`. This property determines whether all “premium” features of a product should be blocked when the license expires.

To make it consistent we have introduced a backward-compatible change in the API endpoints to accept `is_block_features`. The following endpoints are affected

- /v1/products/{product\_id}/installs/{install\_id}/plans/{plan\_id}/pricing/{pricing\_id}/licenses.json
- /v1/products/{product\_id}/plans/{plan\_id}/pricing/{pricing\_id}/licenses.json

The endpoints are particularly useful when creating licenses for [migrated products](help-documentation-migration.md) or from SaaS.