import ipaddress


def calculate_subnet(network):
    try:
        net = ipaddress.ip_network(network, strict=False)

        print("\nNetwork Information")
        print("-------------------")
        print("Network Address :", net.network_address)
        print("Broadcast       :", net.broadcast_address)
        print("Subnet Mask     :", net.netmask)
        print("CIDR            :", net.prefixlen)
        print("Total Addresses :", net.num_addresses)

        if net.version == 4 and net.num_addresses > 2:
            print("Usable Hosts    :", net.num_addresses - 2)
        else:
            print("Usable Hosts    : Depends on network type")

    except ValueError:
        print("Invalid network address.")


while True:
    network = input("\nEnter network (example: 192.168.1.0/24): ")

    if network.lower() == "exit":
        print("Exiting...")
        break

    calculate_subnet(network)
