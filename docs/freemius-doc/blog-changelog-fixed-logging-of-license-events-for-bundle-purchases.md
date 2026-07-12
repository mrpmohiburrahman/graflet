[Changelog](https://freemius.com/changelog/) / Fixed logging of license events for bundle purchases

We noticed an edge case where if a bundle was being manually renewed, the `license.extended` event of the child licenses was not being logged.

In this deployment, we have fixed the issue. So, in case you are listening to this through a [webhook](help-documentation-marketing-automation-events-webhooks.md), you will now get the said event for child licenses.