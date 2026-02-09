import requests

def send_embed():
    print("--- Discord Embed Sender ---")
    webhook_url = input("Enter Webhook URL: ")
    title = input("Enter Embed Title: ")
    print("Enter Embed Description (Press Enter twice to finish):")
    description_lines = []
    while True:
        line = input()
        if not line:
            break
        description_lines.append(line)
    description = "\n".join(description_lines)
    color_input = input("Enter Embed Color (Hex, e.g. #3498db): ")

    if not color_input:
        color_input = "#3498db"
    
    if color_input.startswith("#"):
        color_input = color_input[1:]
    
    try:
        color = int(color_input, 16)
    except ValueError:
        print("Invalid color format. Using default blue.")
        color = 3447003

    payload = {
        "embeds": [
            {
                "title": title,
                "description": description,
                "color": color
            }
        ]
    }

    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 204:
            print("\nSuccessfully sent embed!")
        else:
            print(f"\nFailed to send embed. Status Code: {response.status_code}")
            print(f"Response: {response.text}")
    except Exception as e:
        print(f"\nAn error occurred: {e}")

if __name__ == "__main__":
    send_embed()
    input("\nPress Enter to exit...")
