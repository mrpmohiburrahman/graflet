[Changelog](https://freemius.com/changelog/) / Improved Webhook Failure Detection and Recovery

Our [webhook mechanism](help-documentation-saas-events-webhooks.md) includes an error detection system that notifies you when a webhook fails multiple times consecutively. We also have a safeguard in place where, if a webhook fails more than 100 times, it is automatically disabled to avoid unnecessary load and potential downtime on your server.

[![](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-webhook-1024x549.png)](https://freemius.com/blog/wp-content/uploads/2025/12/freemius-webhook.png)

However, it came to our attention that we were not properly clearing the failure counter once the webhook endpoint recovered. This meant that even after the server started responding correctly, the accumulated failures could still lead to an automatic disablement.

This week, we’re rolling out an update to make this logic smarter. The failure counter will now correctly reset itself once the webhook endpoint stops returning errors for a sustained period of time.