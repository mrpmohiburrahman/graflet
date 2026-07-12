[Changelog](https://freemius.com/changelog/) / Updated AWS S3 connection mechanism to strict TLS 1.2

AWS [announced](https://aws.amazon.com/blogs/security/tls-1-2-required-for-aws-endpoints/) a while back that TLS 1.2 will become the minimum requirement for all their API endpoints. We use AWS S3 to store assets like your product icons, store icons, screenshots etc. To ensure the smooth continuation of service, we audited our implementations and tested with a strict TLS 1.2 connection to the S3 API endpoints.

### Updating asset URLs

We have been serving asset URLs in protocol-relative formats, for example:  
`//s3-us-west-2.amazonaws.com/...`

While this will continue to work in our own apps because we host our apps in a strict `https` environment, this can break image rendering if such links are used on a `http` page. To make the impact minimal, we will now be serving (both existing and new) all asset links with `https` URL format:

`https://s3-us-west-2.amazonaws.com/...`

So in case, you’ve been adding the protocol to the URL for your own use case, please remove them and expect a full `https` URLs from our API.