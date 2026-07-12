[Changelog](https://freemius.com/changelog/) / New feature: Added authentication support for custom webhook events

We understand that [custom webhook events](help-documentation-marketing-automation-events-webhooks.md) are the cornerstone for integrating Freemius with any SaaS product. To make it even easier to consume webhooks sent from Freemius, we have introduced support for direct authentication using an HTTP signature.

From now on every [webhook request](help-documentation-marketing-automation-events-webhooks.md) that Freemius sends, will carry a HTTP\_X\_SIGNATURE header, which you can use to validate the request. Previously we’ve been asking to use the event\_id and re-retrieve the event from Freemius API to consume it. But with this update, you can skip the extra step and after authentication, you can directly consume the webhook request.

### Example usage

The `HTTP_X_SIGNATURE` header will have the `sha256` of the request payload encrypted with the secret key of your product.

[![](https://freemius.com/blog/wp-content/uploads/2024/08/getting-secret-key-freemius-dev-dashboard-1024x222.png)](https://freemius.com/blog/wp-content/uploads/2024/08/getting-secret-key-freemius-dev-dashboard.png)

Go to the Settings page of the product from the Developer Dashboard to get the secret key. Once you have it, you have to calculate the `hmac` hash with the `sha256` algorithm of the RAW HTTP payload using the secret key as the encryption key.

```
<?php
    // Retrieve the request's body payload.
    $input     = @file_get_contents("php://input");
    $hash      = hash_hmac('sha256', $input, '<PRODUCT_SECRET_KEY>');
    $signature = $_SERVER['HTTP_X_SIGNATURE'] ?? '';

    if ( ! hash_equals($hash, $signature))
    {
        // Invalid signature, don't expose any data to attackers.
        http_response_code(200);
        exit;
    }

    $event_json = json_decode($input);
    // Handle the event JSON as needed
```

The above shows how the `hash_hmac` can be used to calculate the `sha256` of the request payload with your product’s secret key with PHP.

Please note that getting the raw body is important here, instead of decoding the JSON and then encoding again, to avoid issues with JSON stringification. Here’s another example of a nodejs server using express.

```
const crypto = require('crypto');
const express = require('express');
const bodyParser = require('body-parser');

const app = express();

app.post('/webhook', bodyParser.raw({ type: '*/*' }), (req, res) => {
    const input = req.body.toString('utf8');
    const secret = '<PRODUCT_SECRET_KEY>';
    const hash = crypto.createHmac('sha256', secret).update(input).digest('hex');
    const signature = req.headers['x-signature'] || '';

    if (hash !== signature) {
        // Invalid signature, don't expose any data to attackers.
        res.status(200).send();
        return;
    }

    const eventJson = JSON.parse(input);
    // Handle the event JSON as needed
});

app.listen(3000, () => {
    console.log('Server is listening on port 3000');
});
```

We hope you find this feature useful when integrating your product with Freemius. You can read [here](help-documentation-marketing-automation-events-webhooks.md#event_types) about all the events we have available. For any queries please feel free to head to our [support](https://freemius.com/cdn-cgi/l/email-protection#671412171708151327011502020a0e12144904080a).