# VLAN and Switching Lab

## Objective

The purpose of this lab is to understand how VLANs can be used to separate different types of devices on a network.

This is a learning lab and does not represent production network configuration.

## Example Network

Consider a client site with:

- IP cameras
- Office computers
- Network management devices

Instead of placing everything in one broadcast domain, I would logically separate the traffic using VLANs.

## VLAN Design

| VLAN | Purpose | Example Network |
|---|---|---|
| VLAN 10 | Cameras | 192.168.10.0/24 |
| VLAN 20 | Office Users | 192.168.20.0/24 |
| VLAN 30 | Network Management | 192.168.30.0/24 |

## Why Use VLANs?

VLANs provide logical separation between different types of devices.

For example:

Camera traffic should not automatically have unrestricted access to office user devices.

This also makes it easier to apply different security and routing policies.

## Access Ports

A camera connected directly to a switch would normally be placed into the appropriate camera VLAN.

Example:

Camera → Switch Access Port → VLAN 10

## Trunk Links

If VLAN traffic needs to travel between switches, a trunk link can carry multiple VLANs.

Example:

Switch A → Trunk → Switch B

The trunk can carry:

- VLAN 10
- VLAN 20
- VLAN 30

## Inter-VLAN Communication

Devices in different VLANs require a Layer 3 device such as a router or Layer 3 switch to communicate.

Example:

VLAN 10 → Router/L3 Switch → VLAN 20

Security policies can then control which traffic is allowed.

## Troubleshooting Approach

If a camera cannot communicate with the expected destination, I would check:

1. Physical link
2. Switch port status
3. Correct access VLAN
4. IP address
5. Subnet mask
6. Default gateway
7. Trunk configuration
8. Whether the required VLAN exists across the path
9. Routing between VLANs
10. Firewall/security rules

## Key Learning

A VLAN problem can look like an application or device problem.

For example, a camera may have power and a link light but still be unable to communicate because the switch port is assigned to the wrong VLAN.
