[Changelog](https://freemius.com/changelog/) / Freemius Checkout now supports localization

We’re super stoked to announce the immediate availability of localization in the Freemius Checkout App.

[![Localization or Translation in the Freemius Checkout App](https://freemius.com/blog/wp-content/uploads/2023/05/freemius-checkout-translated-italian.jpg)](https://freemius.com/blog/wp-content/uploads/2023/05/freemius-checkout-translated-italian.jpg)

Besides English, the Freemius Checkout App can now be used in any supported localization. Our system is capable of handling any language, even selecting the exact locale of a language (for example, French spoken in Spain vs French spoken in Mexico).

Since this is a brand-new feature, the language selector UI is opt-in only for now. Please read on to find out more.

### Loading the Freemius Checkout in your language

You can now pass a special URL Query Parameter `locale` to instruct the app to display a specific language when loading or linking the Freemius Checkout. For example, if the URL of the checkout is something like this:

```
https://checkout.freemius.com/mode/dialog/plugin/:plugin_id/plan/:plan_id/
```

You can now add the query parameter, which would result in this:

```
https://checkout.freemius.com/mode/dialog/plugin/:plugin_id/plan/:plan_id/?locale=es_ES
```

For the Freemius JavaScript SDK, you can simply pass a new parameter, either when configuring the handler or when opening the pop-up:

```
<script>
    var handler = FS.Checkout.configure({
        plugin_id:  "xxxx",
        plan_id:    "yyyy",
        public_key: "pk_xxxxxxxx",
        image:      "https://your-plugin-site.com/logo-100x100.png";,
        // Set the locale of the checkout pop-up
        locale:     "es_ES";
    });
    
    $("#purchase").on("click", function (e) {
        handler.open({
            name     : "My Awesome Plugin",
            licenses : $("#licenses").val(),
            // You can also override it here.
            locale   : "es_ES";
        });
        e.preventDefault();
    });
</script>
```

### Supported Values of the `locale`

For the time being, the `locale` supports the fully formatted language and country code. For example:

- `es_ES` – Spanish / Spain.
- `en_US` – English / US.

We have the following locales available for the time being.

- English – US (`en_US`)
- German – DE (`de_DE`)
- French – FR (`fr_FR`)
- Spanish – ES (`es_ES`)
- Italian – IT (`it_IT`)
- Dutch – NL (`nl_NL`)
- Bengali – IN (`bn_IN`)

All of the translations are AI-generated and are currently marked as `beta` (more on this later). If you wish to improve it or add more languages, please send us an email at [\[email protected\]](https://freemius.com/cdn-cgi/l/email-protection#3f4c4a4f4f504d4b7f594d5a5a52564a4c115c5052) and we can provide you with the source POT and PO files. Depending on requests, we might add more languages/locales in the future.

### Auto-selecting language for your users

We also support a feature to automatically select the best language for your user, based on browser information and geolocation. To start using this feature, you can enter one of the following values in the new `locale` URL parameter.

- `auto`: Will automatically select the best available language for the user. However, this won’t select languages that are marked as AI-translated or `beta` for the time being. If we identify a locale that we don’t support right now, we’ll keep showing the English language.
- `auto-beta`: Same as above, but will also select a language marked as `beta`. When a language marked as beta is selected, the UI will also show it (as in the screenshot above).

Example:

```
https://checkout.freemius.com/mode/dialog/plugin/:plugin_id/plan/:plan_id/?locale=auto-beta
```

### FAQs

#### I don’t see the language selector UI as shown in the image

Since this is a new feature, it is currently opt-in only. You have to specifically pass the `locale` parameter either in the URL or through the JS API.

#### I chose `auto`, yet the language (XX) is not visible in the Checkout App

It’s possible that we haven’t translated the language applicable to the geolocation. If a user requires a different language, we’ll revert to English and still show the language selector UI. Please check the list above to see what languages are available.