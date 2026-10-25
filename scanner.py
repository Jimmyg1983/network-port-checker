"""Check a short list of TCP ports on this computer only."""

import socket

TARGET = "127.0.0.1"
PORTS = [21, 22, 53, 80, 443, 3389, 8080]


def main():
    print("Local Network Port Checker")
    print(f"Scanning {TARGET}")
    print("-" * 35)

    for port in PORTS:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((TARGET, port))
            if result == 0:
                print(f"Port {port}: OPEN")
            else:
                print(f"Port {port}: Not open or unreachable")

    print("-" * 35)
    print("Scan complete!")


if __name__ == "__main__":
    main()
