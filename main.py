import requests
import time

# Function to send the 'tap' request
def send_tap_request(amount, initdata):
    url = "https://app.blombard.com/api/v1/tap"
    
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'initdata': initdata,
        'origin': 'https://app.blombard.com',
        'priority': 'u=1, i',
        'referer': 'https://app.blombard.com/',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'token': '',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }
    
    data = {
        "amount": amount
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        print(f"TAP Response: {response.status_code} - {response.json()}")
    except Exception as e:
        print(f"An error occurred in 'tap' request: {e}")

# Function to send the 'claim rewards' request
def send_rewards_claim_request(initdata):
    url = "https://app.blombard.com/api/v1/rewards/claim"
    
    headers = {
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9',
        'content-type': 'application/json',
        'initdata': initdata,
        'origin': 'https://app.blombard.com',
        'priority': 'u=1, i',
        'referer': 'https://app.blombard.com/tasks',
        'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'token': '',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
    }
    
    data = {
        "achievement_id": "daily"
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        print(f"REWARDS CLAIM Response: {response.status_code} - {response.json()}")
    except Exception as e:
        print(f"An error occurred in 'rewards claim' request: {e}")

# Main script logic
def main():
    # Ask user for initdata value
    initdata = input("Enter the initdata value (query_id, user, auth_date, etc.): ")

    amount = 5000  # Fixed amount for tap requests
    rest_time = 5 * 60  # 5 minutes in seconds

    print("Starting automated script... Press CTRL+C to stop.")
    
    while True:
        # Task 1: Tap Request
        print("Sending TAP request...")
        send_tap_request(amount, initdata)
        
        # Task 2: Rewards Claim Request
        print("Sending REWARDS CLAIM request...")
        send_rewards_claim_request(initdata)
        
        # Wait for 5 minutes
        print(f"Tasks completed. Sleeping for {rest_time // 60} minutes...")
        time.sleep(rest_time)

# Run the script
if __name__ == "__main__":
    main()
