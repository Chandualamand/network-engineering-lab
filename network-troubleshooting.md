# Network Troubleshooting Methodology

## Objective

This document describes my approach to troubleshooting network connectivity problems.

## Troubleshooting Process

I start with the simplest checks before moving to more complex causes.

### 1. Understand the Problem

First I identify:

- What is not working?
- Which users or devices are affected?
- When did the problem start?
- Is the problem constant or intermittent?
- Was there any recent change?

### 2. Check Physical Connectivity

I check:

- Cable connections
- Link status
- Interface status
- Power
- Switch port status

### 3. Check IP Configuration

I verify:

- IP address
- Subnet mask
- Default gateway
- DNS server

### 4. Test Connectivity

I use tools such as:

- ping
- traceroute
- ip / ipconfig
- nslookup
- curl

### 5. Check the Network Path

If the device has an IP address but cannot reach the destination, I check:

- Default gateway
- Routing
- VLAN
- Firewall rules
- NAT
- Packet loss
- Latency

### 6. Check DNS

If the application works using an IP address but not using a hostname, I investigate DNS resolution.

### 7. Check for Packet Loss

For intermittent problems I look for:

- Packet loss
- Retransmissions
- Interface errors
- High utilization
- Link instability

Where available, I would use packet capture to understand what is happening at packet level.

## My Troubleshooting Principle

I try to prove where the failure occurs instead of changing multiple things at the same time.

The goal is to narrow the problem down from:

Physical Layer → Switching → IP → Routing → DNS → Firewall/NAT → Application

and identify the actual point of failure.
