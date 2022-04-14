# CS240 Lecture 4/7: Caching in HTTP

## What is caching

- **Key Idea**: Keep data close
- Any implementation that holds data for reuse in future requests.

Examples

- CPU Cache
- Page Tables

## Why is cachinng important on a cloud-scale?

- Caching saves both CPU and Bandwidth, both of which are not free.
- 'Clouds' may be far away - Bad UX if things are slow.

## Caching Levels

1. **Local Cache**: Data stored on your device - does not require any network to fetch
2. **Intermediate Cache** (Shared Cache): Data stored on any intermediate server between the users and the origin.
   - Proxy cache
   - CDN cache
3. **Origin**: Source of the content

## 1. Age Based Caching

- Allow users to store data for a pre-defined amount of time without communicating with the origin.
- Allow shared caches to also store and fetch the data

### Example CS240 website

- Bootstrap CSS library
- Google Fonts library
- JQuery js library
- Popper js library

Bootstrap makes HTTP get request for the resources

HTTP Reponse Headers

- **age**: Time in seconds since the content was updated from the origin
- **cache-control['max-age']**: Amount of time in seconds the content is 'fresh' (usable). After that time, the content is 'stale' and must be discarded.

## What happens when we request a page using this resource again before the content expires?

### How much traffic saved?

If we have a cache-hit, 100% of the traffic is saved.

### How much time is saved?

If we have a cache-hit, data is already local, **lots** of time saved.

### Disadvatange of age-based caching?

If we change the content, there is no way to force a cache update.

## 2. Entity Tag [Etag] Caching

- Provide a system to validate if the stored cache data is fresh.

HTTP Request headers

- **etag**: Any identifier that uniquely identifies the content of the response.

What happens when we request the page again?

You **must** make a new request.

Include header 'If-None-Match' to specify a list of etags- Server will check if the content has been modified.

- Cache-Hit: HTTP 304 Not Modified
- Cache-Miss: HTTP 200 with content

### Savings

- Traffic
  - The content data is not sent.
  - Only HTTP headers are needed.
- Time
  - Still required to make a round-trip to the server.
  - Do not need to wait for the content on hit.

Every request requires a round-trip time.

There are different use cases for Etag and age-based caching.
If there are no frequent changes in content, age-based should be used. Otherwise, use etag-caching.

### ETag Modern Drawback

The use of cookies is limited due to privacy conerns.

Using etags as a mechanism to track which user visits site.

Hidden 1pixel image that can be used with etags as cookie replacement.
