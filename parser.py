# parser.py

def parse_dns_dump(file_path):
    records = []
    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # skip empty lines
            
            # Split by whitespace to a maximum of three parts:
            # subdomain, record_type, and the remainder (value and optional data)
            parts = line.split(None, 2)
            if len(parts) < 2:
                continue  # Not enough info, skip line
            
            if len(parts) == 2:
                # We have subdomain and record_type only, no value
                subdomain, record_type = parts
                value = ""
                extra_data = ""
            elif len(parts) == 3:
                subdomain, record_type, remainder = parts
                # The remainder could be just one value or multiple values.
                # For simplicity, let's say the first token in remainder is 'value' and
                # the rest is 'extra_data'.
                remainder_parts = remainder.split(None, 1)
                value = remainder_parts[0]
                extra_data = remainder_parts[1] if len(remainder_parts) > 1 else ""

            record = {
                "subdomain": subdomain,
                "record_type": record_type.upper(),
                "value": value,
                "extra_data": extra_data
            }
            records.append(record)

    return records
