Release Notes is our monthly update that highlights the recent product improvements we’ve made, so you can easily stay up to date on what’s new. Here’s what we launched in December.

The new WordPress SDK introduces new awesome features, as well as many important bug fixes. It is available for download here:  
[https://github.com/Freemius/wordpress-sdk/tree/1.2.1.5](https://github.com/Freemius/wordpress-sdk/tree/1.2.1.5)

## Better Upgrade Flow

With the new SDK, users no longer need to deactivate the free version before activating the premium one. This is a huge improvement to the after-upgrade user-experience which we are really proud of! (Kudos to [@fajardoleo](https://github.com/fajardoleo)).

We updated the after upgrade admin notice and also the emails will be tweaked for users that are running the new SDK during the upgrade.

Obviously, a seamless experience would be automatically installing the premium version, but unfortunately, it is still not allowed based on the current [WordPress.org guidelines](https://developer.wordpress.org/plugins/wordpress-org/detailed-plugin-guidelines/ "WordPress.org Plugin Guidelines").

## Better Control for Usage Tracking

Users that opted-in can now disable/re-enable usage-tracking by clicking on a new link in the plugins page that reads: “Opt-Out/In”. The Opt-Out click will trigger the following confirmation message:

![image](https://cloud.githubusercontent.com/assets/6830121/20551353/6a96cd76-b10d-11e6-829e-c6cb1725a244.png)

If the user opts-out, the action will be tracked with a new event labeled `install.disconnected` that you can see in the user’s profile page on the Freemius dashboard.

Users that initially skipped the initial opt-in will now be able to click the “Opt-In” link in the plugins page to get redirected to the opt-in screen.

The opt-out option will only be available for free users to maintain premium plugin version updates from the API. Also, if the user opted out and later upgraded, he/she will automatically be opted-in again for the same reason.

In addition, we added a special method that returns a magic URL that you can add to your settings and re-prompt the users that skipped, to opt-in again ([Issue #42](https://github.com/Freemius/wordpress-sdk/issues/42)). Here’s the simplest usage:

```
<?php if ( my_freemius()->is_anonymous() ) : ?>
<a href="<?php echo my_freemius()->get_reconnect_url() ?>">Re-Connect</a>
<?php endif ?>
```

## Trials for Everyone!

We made a huge update in our trial mechanism which was only working for opted-in users, so users who had skipped can now get trials as well. Here’s how this mechanism works now:

1. After 24 hours from the plugin installation (or update with Freemius for the first time), a promotional admin notice will appear with a trial CTA:![image](https://cloud.githubusercontent.com/assets/6830121/20644483/b150ba30-b403-11e6-81eb-e4e845cdc03f.png)
2. If you want the trial to work for the skipped users, since we can’t pull any data from the Freemius API, you’ll have to add new special params we’ve added to your `init_sdk` method. The easiest way would be to login to your Freemius Dashboard, and copy the updated code from the *SDK INTEGRATION* page.
3. In addition to the admin notice, the *Upgrade* sub-menu item will change it’s label to *Start Trial* and the color will match the blue color of the promotional admin notice:  
   ![image](https://cloud.githubusercontent.com/assets/6830121/20644472/6d2396fc-b403-11e6-8bdb-9fe3c530ea65.png)  
   Additionally, if you have a top-level menu item, it will automatically add a pretty counter to even attract more attention:  
   ![image](https://cloud.githubusercontent.com/assets/6830121/20656754/e6e2c8c8-b4fd-11e6-8391-634e9ca04b16.png)
4. When the user clicks on any of the buttons, the pricing page will load in trial mode and will identify if the site is eligible for a trial based on the WordPress home URL, allowing the same user to start a trial on multiple sites.
5. Clicking the trial start button will prompt the user with a confirmation dialog box, a contextual “opt-in” modal window that explains to the user why we need to capture data:  
   ![image](https://cloud.githubusercontent.com/assets/6830121/21033878/db3ca02a-bd81-11e6-8fde-41921aadb536.png)  
   If the user approves – he/she will be opted-in, and the trial will start right away.

### Testing The Trials

Instead of waiting for 24-hours to trigger the trial promotion, we’ve added a new button to the *Freemius Debug* page which you can click to start the promotional notice right away (if eligible):

![image](https://cloud.githubusercontent.com/assets/6830121/20644476/848ada58-b403-11e6-928e-4eda91d74197.png)

In addition, the multi-site license prices are now hidden when viewing the pricing page in trial mode.

After receiving numerous requests, we managed to prioritize this use-case and it’s now fully supported (both from within the dashboard and on [Freemius Checkout](wordpress-checkout.md)).

## Editable Billing Business Information

So far, users’ billing information was only editable in the Freemius Developer dashboard. We noticed it triggered support tickets, especially from European business customers, asking to update the billing information on their invoices. Therefore, we enriched the billing tab in the account page so now customers can update their billing information themselves to get rid of those support requests and make it “self-served”:

![image](https://cloud.githubusercontent.com/assets/6830121/20611879/43ef90a8-b280-11e6-9726-e42ce47511d9.png)

## Conversion Optimization

We changed the default color of the *Upgrade* button to light green. It will only affect non-paying users:  
![image](https://cloud.githubusercontent.com/assets/6830121/20644551/19152fbe-b406-11e6-9a56-c5613d975271.png)

We’ve experimented that with our plugin and noticed a better conversion rate, which makes sense, simply because more people notice it 🙂

You can easily modify the color to whatever you want by adding the following CSS:

```
.fs-submenu-item.pricing.upgrade-mode { color: yellow }
```

## WordPress.org Compliance

Due to recent updates in .org guidelines, we got the following new default opt-in message for new users approved with the .org review team:

> Never miss an important update — opt-in to our security and feature updates notifications, and non-sensitive diagnostic tracking with freemius.com

It took us a while to get to this messaging, and as you can see it highlights the benefits of opting in, instead of *asking the user for a favor.*

## Additional Updates

1. This version introduces new filters, enabling an override of all *sticky messages* (messages with a “dismiss” button). The filters structure is `sticky_message_{$messageID}` and `sticky_title_{$messageID}`. You can add those filters with `my_freemius->add_filter()`.
2. Added a downgrade button to premium add-ons on the *Account* page.
3. All ‘API Connectivity issues’ admin notices will now also be shown for users running a premium code version. These notices are an important feedback mechanism that outputs the reason for the connectivity issue and provides troubleshooting solutions (when possible). We still haven’t figured out what to do when domain lookup is failing. We were sure it was a cURL specific issue, but after doing some debugging on a customer with that problem we found that the WordPress native “streams” HTTP API also fails for the same reason. We understand it’s annoying and adds some burden to the support (we feel you!). This remains a work in progress…
4. **Bug Fix:** WordPress core changed their `wp_nonce_url()` which causes a redirect to an empty page after activating a license using the link from the plugins page.
5. This SDK introduces a new permission request that will be added by default to the opt-in screen:  
   ![image](https://cloud.githubusercontent.com/assets/6830121/20551512/106f9092-b10f-11e6-9cf0-840b7aa5f023.png)  
   First of all – it’s a great way to set expectations with users by letting them know that your product will periodically show admin notices. Second… I can’t tell you about it yet, but we are cooking a new revolutionary killer feature! (still in stealth mode).

## Call for Translators

Freemius is becoming widely popular and we want to put more efforts into covering more languages. The Freemius WordPress SDK already supports RTL and is fully translated into English and Italian (thanks to [@plasmax](https://profiles.wordpress.org/plasmax/), [@mte90](https://profiles.wordpress.org/Mte90/) and [@dudu](https://profiles.wordpress.org/dudo/)). And in the progress of being translated into Danish, Hebrew, Japanese, and German. Many of you speak different languages – we need your help to make this happen! Please apply to join the translation contributor team, via our Transifex languages repository:  
[https://www.transifex.com/freemius/wordpress-sdk/dashboard/](https://www.transifex.com/freemius/wordpress-sdk/dashboard/)