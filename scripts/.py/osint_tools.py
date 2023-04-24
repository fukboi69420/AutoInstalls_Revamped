import subprocess

def run_nmap(ip_address):
    """
    This function runs the nmap tool and returns the results.

    Parameters:
    ip_address (str): The IP address to scan

    Returns:
    str: The results of the nmap scan
    """
    try:
        # Run the nmap command and capture the output
        output = subprocess.check_output(["nmap", "-sV", ip_address])

        # Decode the output from bytes to string and return it
        return output.decode("utf-8")
    except subprocess.CalledProcessError as e:
        # Log the error
        print(f"Error: {e}")
        return ""
