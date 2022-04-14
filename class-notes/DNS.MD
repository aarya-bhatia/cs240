# Lecture 4/12: Domain Name System (DNS)

## IP Address (Layer 3)

- IPv4: 32 bit identifier for every internet device.
  - Ex 127.0.0.1 Localhost
- IPv6: 128 bit identifier for every internet device.
  - Hex digits separated with a colon or double colon
  - Ex a137::1
  - double colon fills everything in between with zeroes

## User-Supplied Address

- Strings separated by dots (Ex. cs.illinois.edu)
- Designed to be human readable

## DNS

- Hierchical system used to identify resources' address using a human-readable string.

We want to translate a Web Address into IP Address

- quickly
- caching
- decentralised

Web Address

- cs.illinois.edu

IP Address

- 192.17.18.21

FQDN

- Does **NOT** contain protocol information

Ex. http://cs.illinois.edu/

- http - protocol
- / - path

i.e. GET / HTTP

Fully qualified domain names

- Always read backwards
- Always starts with a dot when read backwards
- '.' Is the root name server

cs.illinois.edu.

- Last bit is MSB

1. TLD: Top level domain: The last (first) string in our domain\* ('.edu.')
   - About 1500 total TLDs
   - All edu websites under this TLD
   - Others are: .com, .org .gov, .ai, .net, .biz, .io, .wtf, .me, .site, .page
   - country domains like .in, .fr, .co.uk
2. SLD/2LD: Second Level domain: The next component in the URL always one string without dots
3. Subdomains: Every other domain under SLD is a sub-domain cs.illinois.edu (cs), waf.cs.illinois.edu (waf.cs)

Purpose of DNS system to provide us with DNS Record

- Time to Live TTL value: An age-based cache that denotes how long the record is fresh, in seconds.

### Record Types

1. A- IPv4 address of the web server
2. AAAA- IPv6 address
3. NS- Next level (child) DNS Servers
4. MX- IP address for emails
5. TXT- Free-form string

To view records

Command Line: `dig`
Web-based Tool

DNS Resolution

- Billinois of DNS requests per hour
- 13 Authoritative root DNS Servers "dot server" (.edu.)
  - Find the TLD '.edu.' data and get info about DNS Record
  - They provde the addresses to the TLD Name Server (NS) (Responsible for the ~1500 TLDs)

TLD Name Servers

- Provides address to SLD NSs
- . -> edu -> illinois.edu

SLD NS

- Provide records for the 2LD services and anay subdomain NS

Preferred DNS Server

- Local: DNS happens often, end users in the same geographical area usually have similar DNS Requests.
- Private: Some DNS servers are shared, some are private to one user.
- User-defined: public-available DNS Servers
