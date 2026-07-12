[Changelog](https://freemius.com/changelog/) / New JavaScript SDK for Freemius Checkout – Calling for testers

We have released a new beta version of our [JS SDK](help-documentation-selling-with-freemius-freemius-checkout-buy-button.md) for our Checkout. This version aims to:

1. Remove jQuery from the dependencies.
2. Provide better Developer Experience (DX) through type documents.
3. Provide both CDN and npm packages for any type of consumer.

We’ve also open-sourced it under the MIT license to accept contributions from our makers. You can find the repository [here](https://github.com/Freemius/freemius-checkout-js) on GitHub along with the [usage guide](https://github.com/Freemius/freemius-checkout-js?tab=readme-ov-file#usage-guide).

While we aim to replace the Legacy JS SDK soon, we would like to call for testers to help with this new system. Please read below to get started quickly.

### Using the new JS SDK

Instead of `https://checkout.freemius.com/checkout.min.js`, please use the new CDN under `https://checkout.freemius.com/js/v1/`. Here’s a quick code example:

```
<select id="licenses">
    <option value="1" selected="selected">Single Site License</option>
    <option value="2">2-Site License</option>
    <option value="unlimited">Unlimited Sites License</option>
</select>
<button id="purchase">Buy Button</button>

<script
    type="text/javascript"
    src="https://checkout.freemius.com/js/v1/"
></script>

<script type="text/javascript">
    const handler = new FS.Checkout({
        plugin_id: '9885',
        plan_id: '16634',
        public_key: 'pk_ccca7be7fa43aec791448b43c6266',
        image: 'https://your-plugin-site.com/logo-100x100.png',
    });

    document.querySelector('#purchase').addEventListener('click', (e) => {
        handler.open({
            name: 'My Awesome Plugin',
            licenses: document.querySelector('#licenses').value,
            // You can consume the response for after purchase logic.
            purchaseCompleted: function (response) {
                // The logic here will be executed immediately after the purchase confirmation.
                // alert(response.user.email);
            },
            success: function (response) {
                // The logic here will be executed after the customer closes the checkout, after a successful purchase.
                // alert(response.user.email);
            },
        });

        e.preventDefault();
    });
</script>
```

The difference with the Legacy JS SDK is:

1. We don’t need jQuery anymore. So you can remove it if you’re not using it for anything else.
2. Instead of accessing the singleton handler from `FS.Checkout.configure`, we now create a new handler with `new FS.Checkout` and use the instance accordingly.

You are free to create any number of instances if you’re selling multiple products from the same page. Cart recovery will also work as soon as you’ve instantiated and will only target the product the instance is responsible for.

### Easy migration from the Legacy JS SDK

To make it easy to migrate without changing much of your code, we have also developed a compatibility layer.

In your code, where you do

```
<script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
<script src="https://checkout.freemius.com/checkout.min.js"></script>
```

1. Remove the jQuery script tag if you aren’t using jQuery.
2. Replace the checkout script with the new one.

```
<script src="https://checkout.freemius.com/js/v1/legacy/"></script>
```

Now all your existing code should work as-is.

```
const handler = FS.Checkout.configure({
    plugin_id: '1234',
    plan_id: '5678',
    public_key: 'pk_ccca7be7fa43aec791448b43c6266',
    image: 'https://your-plugin-site.com/logo-100x100.png',
});

document.querySelector('#purchase').addEventListener('click', (e) => {
    handler.open({
        name: 'My Awesome Plugin',
        licenses: document.querySelector('#licenses').value,
        // You can consume the response for after purchase logic.
        purchaseCompleted: function (response) {
            // The logic here will be executed immediately after the purchase confirmation.
            // alert(response.user.email);
        },
        success: function (response) {
            // The logic here will be executed after the customer closes the checkout, after a successful purchase.
            // alert(response.user.email);
        },
    });

    e.preventDefault();
});
```

In the future, we will replace the Legacy JS SDK with this compatibility layer to reduce the footprint.

Please note that if you’re getting started or willing to refactor your code a little bit, kindly consider using the regular pattern instead of the legacy singleton pattern.

### Performance improvements

While working on the new JS SDK, we also looked into improving performance. Here are the results:

1. The new JS SDK loads about **60% faster** than the Legacy JS SDK – Your pricing page will load faster by 1 second on average.
2. The Checkout app itself also loads **40% faster** – Once users click the buy button the checkout will appear faster than before.

We hope you’ll help us test the new JS SDK so that we can get it out in the wild as soon as possible. If you have any questions, please don’t hesitate to write to our [support](https://freemius.com/cdn-cgi/l/email-protection#d3a0a6a3a3bca1a793b5a1b6b6bebaa6a0fdb0bcbe).