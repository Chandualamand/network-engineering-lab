import socket
import time


def check_host(host):
    print("\nChecking:", host)

    try:
        start_time = time.time()

        ip_address = socket.gethostbyname(host)

        elapsed = (time.time() - start_time) * 1000

        print("IP Address :", ip_address)
        print("DNS Lookup : Successful")
        print("Response   : {:.2f} ms".format(elapsed))

    except socket.gaierror:
        print("DNS Lookup : Failed")
        print("The hostname could not be resolved.")


while True:
    host = input("\nEnter hostname or IP address (type 'exit' to quit): ")

    if host.lower() == "exit":
        print("Exiting...")
        break

    check_host(host)
