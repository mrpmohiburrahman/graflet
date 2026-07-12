---
title: "Generate Magic Links to Automatically Log in Customers to the Portal"
url: "https://freemius.com/help/documentation/users-account-management/magic-login-link/"
source: "docs"
section: "Docs"
category: "Customer Portal"
scraped_at: "2026-04-09T19:58:44+06:00"
word_count: 849
---

Using the Freemius API, you can generate magic links (or session links) that allow your customers to automatically log in to the Customer Portal without having to enter their credentials again. This provides a seamless experience for your customers when they want to manage their subscriptions, billing, and more.

Here is the flow:

1. The user logs in to your website or application.
2. Your website or application displays a "**Manage Account**" button that points to the [Customer Portal](https://customers.freemius.com).
3. When the user clicks the "**Manage Account**" button, a new tab opens with the Customer Portal, and the user is automatically logged in to their Customer Portal without the need to log in again.

To implement this flow securely, you need to generate a magic link from the Freemius API.

## Generate a Magic Link from the API[​](#generate-a-magic-link-from-the-api "Direct link to Generate a Magic Link from the API")

You need to send an authenticated request to [this API endpoint](https://docs.freemius.com/api/products/generate-portal-login-link) using the product's [bearer token](https://docs.freemius.com/api/section/bearer-token-auth).

- You can provide the email address of your user using the `email` parameter.
- Alternatively, you can provide the Freemius user ID using the `id` parameter. This is useful if you have saved the user's ID from Freemius locally (check our [integration](help-documentation-saas.md) guide).

Here are some examples:

- JS SDK
- PHP

```js
// Using the email address
const { link } =
  await freemius.api.user.retrieveHostedCustomerPortalByEmail(
    '[email protected]'
  );

// Using the Freemius user ID
const { link } = await freemius.api.user.retrieveHostedCustomerPortal(9999);
```

More information can be found in the [JS SDK documentation](help-documentation-saas-sdk-js-sdk-api.md#generate-magic-link-for-sso-to-customer-portal).

```php
// Configure the Freemius API client
const PRODUCT_ID = "1234";
const BEARER_TOKEN = "<YOUR_AccessToken_HERE>";

// Configure the payload with either the email address or the Freemius user ID
$payload = (object)["email" => "[email protected]"]; // or (object)["user_id" => 9999]

$curl = curl_init();

curl_setopt_array($curl, [
  CURLOPT_HTTPHEADER => [
    "Authorization: Bearer " . BEARER_TOKEN,
    "Content-Type: application/json"
  ],
  CURLOPT_POSTFIELDS => json_encode($payload),
  CURLOPT_URL => "https://api.freemius.com/v1/products/" . PRODUCT_ID . "/portal/login.json",
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_CUSTOMREQUEST => "POST",
]);

$response = curl_exec($curl);

// Get the magic link from the response
$link = json_decode($response)->link;
```

## Securely Logging in to the Customer Portal[​](#securely-logging-in-to-the-customer-portal "Direct link to Securely Logging in to the Customer Portal")

We recommend making an asynchronous request to your backend to generate the magic link when your customer clicks the "Manage Account" button.

warning

The generated link is valid for only 5 minutes. Do not generate it in advance, as it may expire before the user attempts to use it.

Once you receive the magic link from your backend, you can open it in a new tab to log the user in to the Customer Portal.

Assuming you have an endpoint at `/api/generate-magic-link` that generates the magic link, here is an example of how to implement this flow:

```js
document
  // Assuming the ID of the button is "manage-account-button"
  .getElementById('manage-account-button')
  // We want to intercept the click event to generate the magic link before opening the Customer Portal
  .addEventListener('click', async (event) => {
    event.preventDefault();

    try {
      const response = await fetch('/api/generate-magic-link', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (!response.ok) {
        throw new Error('Failed to generate magic link');
      }

      const { link } = await response.json();
      window.open(link, '_blank');
    } catch (error) {
      console.error('Error generating magic link:', error);
      alert(
        'Sorry, we were unable to log you in to the Customer Portal. Please try again later.'
      );
    }
  });
```

## Logging In to Specific Sections of the Customer Portal[​](#logging-in-to-specific-sections-of-the-customer-portal "Direct link to Logging In to Specific Sections of the Customer Portal")

The generated magic link will log the user in to the main "Websites" or "Licenses" page of the Customer Portal (depending on the types of products your store has).

However, if you want to log the user in to a specific section of the Customer Portal, you can modify the generated magic link by adding a `next` query parameter. This parameter should contain the URL of the section where you want to direct the user.

The `next` parameter should be a relative URL that starts with `/store/{store_id}/`. For example, to log the user in to the "Subscriptions" section of the Customer Portal, you would add `/store/{store_id}/subscriptions` to the generated magic link.

You must URL-encode the `next` parameter value. Here are some functions to help you with that:

- JS
- PHP

```js
function generateMagicLinkWithNextParameter(magicLink, nextPath) {
  const url = new URL(magicLink);
  url.searchParams.set('next', nextPath);
  return url.toString();
}
```

```php
function generateMagicLinkWithNextParameter($magicLink, $nextPath)
{
    $url = parse_url($magicLink);
    $queryParams = [];

    if (isset($url["query"])) {
        parse_str($url["query"], $queryParams);
    }

    $queryParams["next"] = $nextPath;

    $url["query"] = http_build_query($queryParams);

    return (isset($url["scheme"]) ? $url["scheme"] . "://" : "") .
        ($url["host"] ?? "") .
        (isset($url["port"]) ? ":" . $url["port"] : "") .
        ($url["path"] ?? "") .
        "?" .
        $url["query"] .
        (isset($url["fragment"]) ? "#" . $url["fragment"] : "");
}
```

Here are some URL paths for the different sections of the Customer Portal:

- **Websites**:
  
  - **Specific Website**:
  - **Specific Product**:
- **Downloads**:
- **Licenses**:
  
  - **Specific License**:
- **Payment/Invoices**:
- **Subscriptions**:
  
  - **Specific Subscription**:
- **My Profile**:
- **FAQ**:
- **Support**:
- **Earn** (Affiliate):
  
  - **Performance**:
  - **Affiliate URLs**:
  - **Referrals**:
  - **Visit Log**:
  - **Payouts**: