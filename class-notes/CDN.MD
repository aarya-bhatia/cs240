# [April 14]: Content Delivery Networks

How do we deploy our web app?

- Problems: slow, high traffic

Two types of content on any website.

- Static: Content that is delivered to all users identically
  - Examples
    - Images (assets)
    - Library files (js)
    - Stylesheets (css)
    - HTML non-user-specific
  - Static is easy to cache.
- Dynamic: All content that is computed at request time, usually specific to a user or a request.
  - Can only be privately cached. (Not CDN)

Since most content is static, we will look at caching strategies for static content.

## CDN Benifits

- **Compute**: If you use a rented cache, your server does not have to do anything on a cache-hit.
- **Speed**: CDN Servers are close to your users.
- **Server security**: All traffic can be configured/must be routed via CDNs. Your origin server is not on the internet openly.
- **Reliabililty**\*: If your origin goes down for a short time, the CDN caches are fresh and deliver content.
- **Bandwidth**: Shorter distance = lower cost

Using a CDN

- Step 1: Find a CDN Provider we want to use. Pricing depends on bandwidth and # requests.
- Step 2a: Tell your CDN Provider your origin.
- Step 2b: Update your NS Record to point to their NS.
