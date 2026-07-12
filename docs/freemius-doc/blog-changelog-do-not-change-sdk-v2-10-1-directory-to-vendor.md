[Changelog](https://freemius.com/changelog/) / Do NOT change SDK v2.10.1 directory to vendor

We recently released WordPress SDK v2.10.1, which includes a recommendation to move the SDK from the root directory to the vendor directory. **However, we strongly advise against changing the SDK directory at this time**.

You can update the SDK to the latest version to enjoy the new features. However, if you also change its location, it will likely result in an error during the update process for your paid products. So, if you haven’t been using composer, please don’t migrate to it now or if you have the SDK in the root directory, do not move it to the vendor directory.

### Regarding the error

The error is harmless and will not cause functional issues, but it may create a poor user experience for your customers. To avoid this, we ask that you refrain from changing the SDK location.

We are aware of the issue and are working on a solution. We will get back to you with more details after the holidays.

**If you’ve already deployed a version where you’ve changed the SDK location**

We recommend the following steps:

- Unrelease the version from the Developer Dashboard.
- Wait for an update from our end.

**If you must release another version**:

- If most of your customers have already updated: Keep the new SDK location.
- If only a small percentage of your customers have updated: Revert to the old SDK location.

In both cases, the error message may appear for some of your users.

We sincerely apologize for the inconvenience and appreciate your patience and understanding as we work on a solution. To give you an estimate, we have already built a fix and are in the process of refining and testing it to ensure it covers all use cases.

If you have any questions, please contact our [support team](https://freemius.com/cdn-cgi/l/email-protection#c0b3b5b0b0afb2b480a6b2a5a5ada9b5b3eea3afad).