# main.py

from parser import parse_dns_dump

def main():
    # Step 1: Get user input
    domain_name = input("Enter the domain name (e.g., example.com): ").strip()
    print("Paste your DNS text dump below. Press Ctrl+D (on Linux/Mac) or Ctrl+Z then Enter (on Windows) to finish:")

    # Read user’s pasted DNS dump until EOF
    dns_lines = []
    try:
        while True:
            line = input()
            dns_lines.append(line)
    except EOFError:
        pass

    # Save lines to a file named after the domain
    file_name = f"{domain_name.replace('.', '_')}_dump.txt"
    with open(file_name, 'w') as f:
        f.write("\n".join(dns_lines))

    # Step 2: Parse the saved DNS dump
    records = parse_dns_dump(file_name)

    # For now, just print the parsed records to confirm it works
    print("Parsed DNS Records:")
    for record in records:
        print(record)

if __name__ == "__main__":
    main()
