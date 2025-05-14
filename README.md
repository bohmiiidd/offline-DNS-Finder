# Subdomain Bruteforcer with Size Filtering 🔍

A Python script to discover subdomains by filtering responses based on size (similar to `ffuf -fs`). Built for speed with asynchronous requests and designed for penetration testing.

## Features ✨
- **Fast asynchronous requests** (using `aiohttp`)
- **Size-based filtering** (hide responses with specified length)
- **Color-coded output** (green=valid, yellow=filtered, red=errors)
- **Verbose mode** (`-v` flag to see all attempts)
- **Easy command-line arguments**

## Installation 📦
```bash
pip install aiohttp termcolor
```

## Usage 🚀
```bash
python3 subdomain_bruteforce.py \
  --host TARGET_DOMAIN \
  --ip TARGET_IP \
  --wordlist PATH_TO_WORDLIST \
  --size FILTER_SIZE \
  [-v]
```

### Example:
```bash
python3 subdomain_bruteforce.py \
  --host planning.htb \
  --ip 10.129.209.1 \
  --wordlist /usr/share/wordlists/subdomains.txt \
  --size 178 \
  -v
```

## Arguments 🛠️
| Argument      | Description                          | Example                |
|---------------|--------------------------------------|------------------------|
| `--host`      | Target domain (required)             | `planning.htb`         |
| `--ip`        | Target server IP (required)          | `10.129.209.1`         |
| `--wordlist`  | Path to subdomain wordlist (required) | `/path/to/wordlist.txt`|
| `--size`      | Filter responses with this size (required) | `178`           |
| `-v/--verbose`| Show all requests (including filtered/errors) | (flag)      |

## Output Example 📝
```
[+] Starting bruteforce on planning.htb (IP: 10.129.209.1)
[+] Wordlist: subdomains.txt | Filtering size: 178

[+] Valid: admin.planning.htb (Size: 1205)
[-] Filtered: test.planning.htb (Size: 178)
[!] Error: api.planning.htb -> TimeoutError
```
![vokoscreenNG-2025-05-14_14-56-41 567](https://github.com/user-attachments/assets/7ecff5e7-a82d-40eb-a0c4-8084ee7e14e7)

## Tips 💡
- For better performance, split large wordlists into smaller chunks
- Use `-v` when debugging to see why subdomains are being filtered
- Combine with other tools like `ffuf` for verification
