[Changelog](https://freemius.com/changelog/) / Preventing env var Interpolation Issues in Secret Keys

The [secret key](help-documentation-saas-sdk-js-sdk-installation.md#retrieving-keys-from-the-developer-dashboard) our system generates (for example, for products) can include various special characters, including the `$` sign. While this is usually fine for many systems, some frameworks, like Next.js, interpret `$` as a reference to another variable and attempt to [interpolate](https://nextjs.org/docs/app/guides/environment-variables#referencing-other-variables) it. To avoid this, makers needed to escape the secret key using `\$`.

For example, if the generated secret key was:

```
sk_1234$abcd
```

then, when used with the Next.js framework, it needed to be escaped as:

```
sk_1234\$abcd
```

While the workaround is straightforward, this behavior is not always obvious and has led to wasted time debugging why integrations were failing.

To avoid running into this situation, starting today, no newly generated secret keys will include the `$` sign. Existing secret keys are not affected in any way.

If needed, you can go to Product → Settings → API & Keys and click the “Regenerate” button to create a fresh key without the `$` sign.

[![Regenerate secret key from Freemius Developer Dashboard](https://freemius.com/blog/wp-content/uploads/2026/01/regenerate-secret-key-1024x533.png)](https://freemius.com/blog/wp-content/uploads/2026/01/regenerate-secret-key.png)