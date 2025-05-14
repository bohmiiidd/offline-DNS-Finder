#!/usr/bin/env python3
import aiohttp
import asyncio
import argparse
from termcolor import colored

async def check_subdomain(session, url, subdomain, filtered_size, verbose=False):
    headers = {"Host": f"{subdomain}.{args.host}"}
    try:
        async with session.get(url, headers=headers, timeout=10) as response:
            content = await response.text()
            content_length = len(content)
            
            if content_length != filtered_size:
                print(colored(
                    f"[+] Valid: {subdomain}.{args.host} (Size: {content_length})",
                    "green"
                ))
            elif verbose:
                print(colored(
                    f"[-] Filtered: {subdomain}.{args.host} (Size: {content_length})",
                    "yellow"
                ))
    except Exception as e:
        if verbose:
            print(colored(
                f"[!] Error: {subdomain}.{args.host} -> {str(e)}",
                "red"
            ))

async def main(args):
    async with aiohttp.ClientSession() as session:
        with open(args.wordlist, 'r') as f:
            subdomains = [line.strip() for line in f if line.strip()]
        
        tasks = [
            check_subdomain(session, args.url, subdomain, args.size, args.verbose)
            for subdomain in subdomains
        ]
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Subdomain Bruteforcer with Size Filtering")
    parser.add_argument("--host", required=True, help="Target domain (e.g., planning.htb)")
    parser.add_argument("--ip", required=True, help="Target IP (e.g., 10.129.209.1)")
    parser.add_argument("--wordlist", required=True, help="Path to subdomain wordlist")
    parser.add_argument("--size", type=int, required=True, help="Filter out responses with this size")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show all requests (including filtered/errors)")
    
    args = parser.parse_args()
    args.url = f"http://{args.ip}"

    print(colored(
        f"\n[+] Starting bruteforce on {args.host} (IP: {args.ip})",
        "blue", attrs=["bold"]
    ))
    print(colored(
        f"[+] Wordlist: {args.wordlist} | Filtering size: {args.size}\n",
        "blue"
    ))

    asyncio.run(main(args))
