# DNS and DHCP Troubleshooting Lab

## Objective

This lab covers the basic role of DNS and DHCP in an IP network and how I would troubleshoot common problems.

---

## DHCP

DHCP automatically provides network configuration to clients.

A DHCP server can provide:

- IP address
- Subnet mask
- Default gateway
- DNS server

### Basic DHCP Process

The common DHCP process is:

1. DHCP Discover
2. DHCP Offer
3. DHCP Request
4. DHCP Acknowledgement

This is commonly remembered as DORA.

---

## DHCP Troubleshooting

If a client does not receive an IP address, I would check:

1. Physical connectivity
2. Switch port status
3. VLAN assignment
4. DHCP server availability
5. DHCP scope availability
6. DHCP relay configuration if the server is on another network
7. Whether the client is receiving an IP address

A client receiving an unexpected address can also indicate a DHCP configuration problem.

---

## DNS

DNS translates hostnames into IP addresses.

Example:

```text
example.com → IP address
