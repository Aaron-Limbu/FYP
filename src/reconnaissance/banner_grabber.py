import socket
import argparse


class BannerGrabber:
    def __init__(self, target, ports):
        self.target = target
        self.ports = ports

    def grab_banner(self, ip, port):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(5)
                s.connect((ip, port))
                s.sendall(b"HEAD / HTTP/1.1\r\n\r\n")
                banner = s.recv(1024).decode().strip()
                print(f"[+] Banner for {ip}:{port}:\n{banner}\n")
                return banner
        except (socket.timeout, socket.error) as e:
            print(f"[-] Unable to grab banner for {ip}:{port}: {e}")
            return None

    def run(self):
        try:
            ip = socket.gethostbyname(self.target)
            print(f"[+] Target resolved to IP: {ip}")
            print("[+] Starting banner grabbing...")

            for port in self.ports:
                print(f"[i] Scanning port {port}...")
                self.grab_banner(ip, port)

            print("[+] Banner grabbing completed.")
        except socket.gaierror as e:
            print(f"[-] Error resolving hostname {self.target}: {e}")
        except Exception as e:
            print(f"[-] Unexpected error: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Banner Grabbing Tool")
    parser.add_argument("-t", "--target", type=str, required=True, help="Target hostname or IP address")
    parser.add_argument(
        "-p", "--ports", type=str, required=False, default="80,443", help="Comma-separated list of ports to scan"
    )
    args = parser.parse_args()

    target = args.target
    ports = [int(port.strip()) for port in args.ports.split(",")]

    grabber = BannerGrabber(target, ports)
    grabber.run()