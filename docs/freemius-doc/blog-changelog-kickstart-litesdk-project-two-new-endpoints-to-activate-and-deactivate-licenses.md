[Changelog](https://freemius.com/changelog/) / Kickstart LiteSDK Project – Two new endpoints to activate and deactivate licenses

We are super stoked to announce that we have kickstarted the LiteSDK project. The LiteSDK is meant to be a lightweight alternative to our classic [WordPress SDK](https://github.com/Freemius/wordpress-sdk). It will have minimal features, for example, license activation, software updates, etc. We aim to make the project as modular as possible, to gradually add features that can optionally be included in a WordPress product.

To ease the communication layer of the LiteSDK, we have introduced two new endpoints in our API.

### License Activation endpoint

`/v1/plugins/:plugin_id/activate.json` (public)

Use this endpoint to activate a license on a new or existing site. It expects the following required parameters:

- `license_key` – The license key
- `uid` – A unique identifier of the site

**UID:** The generation of the UID must be done by the client. More on it later.

Optionally it also accepts the following parameters:

- `url` – The URL of the site
- `title` – The title of the site
- `version` – The version of the WordPress plugin/theme.
- `install_id` – The ID of an existing install/site (must belong to the same user and must have the same UID when it was created).

On a `POST` request, with the above parameters the endpoint can

- Create an Install and/or activate the license on the existing install.
- Create a user if the license does not have a user already (ghosted licenses that partners can create from the Developer Dashboard).
  
  - In such case, the endpoint will expect `first_name`, `last_name` and `user_email` parameters.
- If the install already had an activation of the plugin for a different license, it will be deactivated.

Upon success, it returns the `id`, `public_key` and `secret_key` of the `user` and the `install` entities.

### License deactivation endpoint

`/v1/plugins/:plugin_id/deactivate.json` (public)

Use this endpoint to deactivate the previously activated licenses on an installation. It expects the following required parameters:

- `uid` – The same UID used when activating the license
- `install_id` – The ID of the install from where you want to deactivate the license
- `license_key` – The key of the license you want to deactivate

On a `POST` request, the endpoint will deactivate the license from the `install` entity. It will return the properties of the `install` entity on success.

### Usage POC

We have created a POC (Proof-of-Concept) of a WordPress project demonstrating the new endpoints. This POC is still under heavy development and we are yet to write documentation. But if you want to take a look, you can visit our [GitHub project](https://github.com/Freemius/wp-sdk-lite).

The project has the following features at the moment:

- Provides abstraction for the API communication.
- Generation and storage of the `uid` parameter.
- Storing license activation status and providing methods to check for updates, sync license status with the server etc.

### [Call for Testers](https://freemius.com/cdn-cgi/l/email-protection#93e0e6e3e3fce1e7d3f5e1f6f6fefae6e0bdf0fcfe)

Over time, we aim to turn it into a proper LiteSDK that can be used in production. At this stage, please help us identify more use cases by trying out the POC in your projects. We are always listening to understand how we can make our products better. If you need help trying out the POC, please get in touch with our [support](https://freemius.com/cdn-cgi/l/email-protection#24575154544b56506442564141494d51570a474b49). You can also “watch” the project under GitHub to subscribe to updates.