#!/usr/bin/env python3   

#*****Lib.Section*****

import os 
import sys
import json
import pyshark
import requests 
import time as t 
import threading
import subprocess
import dns.resolver
from pathlib import Path as pt
from urllib.parse import urljoin


banner = r"""  __       __            __         ______             __   ______    ______                    
/  |  _  /  |          /  |       /      \           /  | /      \  /      \                   
$$ | / \ $$ |  ______  $$ |____  /$$$$$$  | _______  $$/ /$$$$$$  |/$$$$$$  |______    ______  
$$ |/$  \$$ | /      \ $$      \ $$ \__$$/ /       \ /  |$$ |_ $$/ $$ |_ $$//      \  /      \ 
$$ /$$$  $$ |/$$$$$$  |$$$$$$$  |$$      \ $$$$$$$  |$$ |$$   |    $$   |  /$$$$$$  |/$$$$$$  |
$$ $$/$$ $$ |$$    $$ |$$ |  $$ | $$$$$$  |$$ |  $$ |$$ |$$$$/     $$$$/   $$    $$ |$$ |  $$/ 
$$$$/  $$$$ |$$$$$$$$/ $$ |__$$ |/  \__$$ |$$ |  $$ |$$ |$$ |      $$ |    $$$$$$$$/ $$ |      
$$$/    $$$ |$$       |$$    $$/ $$    $$/ $$ |  $$ |$$ |$$ |      $$ |    $$       |$$ |      
$$/      $$/  $$$$$$$/ $$$$$$$/   $$$$$$/  $$/   $$/ $$/ $$/       $$/      $$$$$$$/ $$/       
                                                                                            Credit : vaibhav0x44    """

#**********************


"""Function Block"""

def dns_lookup(domain):
    try:
        # DNS (AAAA) record lookup 
        answers = dns.resolver.query(domain, 'A')
        
        # Extract IP addresses
        ip_addresses = [answer.address for answer in answers]
        
        return ip_addresses
    except dns.resolver.NoAnswer:
        return "No A records found for the domain."
    except dns.resolver.NXDOMAIN:
        return "Domain does not exist."
    except dns.exception.Timeout:
        return "DNS lookup timed out."
    except Exception as n:
        return f"An error occurred: {n}"

def check_robots_txt(domain):
    try:
        # Adjoin URL + robots.txt
        url = f"http://{domain}/robots.txt"
        
        # Send GET request to fetch the robots.txt file
        response = requests.get(url)
        
        if response.status_code == 200:
            return response.text
        elif response.status_code == 404:
            return "robots.txt file not found."
        else:
            return f"Failed to retrieve robots.txt: HTTP {response.status_code}"
    
    except requests.RequestException as n:
        return f"Error fetching robots.txt: {n}"

def directory_enumeration(domain):
    common_word_path = pt("word.csv")
    common_dir = common_word_path.read_text().split(",")
    results = [] 
    
    for directory in common_dir:
        url = f"http://{domain}/{directory}"
        try: 
            response = requests.get(url)
            if response.status_code == 200:
                results.append(f"Found: {url}")
            elif response.status_code == 403:
                results.append(f"Forbidden: {url}")
            elif response.status_code == 401:
                results.append(f"Unauthorized: {url}")
        
        except requests.RequestException:
            pass
    
    return results
    
def result0 (ips, robots_txt_content , directory_results):

    results = [ ips , robots_txt_content , directory_results ]
    for r in results :
        return {"IP Address " :  ips,
                "Robots File " : robots_txt_content , 
                "Directory Endpoints ":  directory_results
                }


def livePacket_capture(interface = "eth0") : # For Bash Env's (caution : use sudo py file name) 
    cap = pyshark.LiveCapture(interface=interface)
    print(f"Listening on {interface}... Press Ctrl+C [KeyBoardInterrupt] to stop.\n")
    for packet in cap.sniff_continuously():
        try:
            print(f"{packet.ip.src} → {packet.ip.dst} ({packet.highest_layer})")
        except AttributeError:
            continue

""" Bash Env Check """

def listen () :
    return None 

def main() : 
    shell = os.environ.get("SHELL" , "")
    if "bash" in shell : 
        listen()

    else : 
        print("===Windows-nt===");newlines();newlines()

def newlines():
    print("\n")

def wait():
    t.sleep(3)


if __name__ == "__main__":
    main()

    print(banner);newlines()

    if "--capture-only" in sys.argv:
        livePacket_capture("eth0")
        sys.exit()

    elif os.name == "posix" : 
        subprocess.Popen(['xterm', '-e', 'python3', 'websniffer.py','--capture-only'])

        domain_name = input("Enter the domain name: ")
        #capture_thread = threading.Thread(target=livePacket_capture , args = ("eth0",) , daemon = True )
        #capture_thread.start()


        # Perform DNS lookup
        ips = dns_lookup(domain_name)   
        print(f"IP addresses for {domain_name}:")
        if isinstance(ips, list):
            for ip in ips:
                print(ip)
            else:
                print(ips)

                newlines();wait()
                print("Checking robots.txt file:")
                robots_txt_content = check_robots_txt(domain_name)
                print(robots_txt_content)

                newlines();wait()
                print("Performing directory enumeration:")
                directory_results = directory_enumeration(domain_name)

                for result in directory_results:
                    print(result)

                    newlines();wait()
                    print(f"Saving Recon Results: {domain_name}.json ⌯⌲")
                    recon_resultPath = pt(f"{domain_name}.json")
                    json_results = json.dumps(result0(ips , robots_txt_content , directory_results ) , indent=4)
                    recon_resultPath.write_text(json_results)

    elif os.name == "nt" :

        domain_name = input("Enter the domain name: ")
        # Perform DNS lookup
        ips = dns_lookup(domain_name)

        print(f"IP addresses for {domain_name}:")
        if isinstance(ips, list):
            for ip in ips:
                print(ip)
            else:
                print(ips)

                newlines();wait()
                print("Checking robots.txt file:")
                robots_txt_content = check_robots_txt(domain_name)
                print(robots_txt_content)

                newlines();wait()
                print("Performing directory enumeration:")
                directory_results = directory_enumeration(domain_name)
                for result in directory_results:
                    print(result)

                    newlines();wait()
                    print(f"Saving Recon Results: {domain_name}.json ⌯⌲")
                    recon_resultPath = pt(f"{domain_name}.json")
                    json_results = json.dumps(result0(ips , robots_txt_content , directory_results ) , indent=4)
                    recon_resultPath.write_text(json_results)

                else : 
                    print("Exiting.....")
                    quit()

                    #EOF 







