import os
import requests

# Get absolute path to channel list
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CHANNEL_LIST = os.path.join(BASE_DIR, "../channel_list.txt")

def url_grabber(url):
    """Fetches the M3U8 link from a YouTube video."""
    try:
        response = requests.get(url, timeout=15).text
        m3u8_index = response.find('.m3u8') + 5
        if m3u8_index < 5:
            print(f"Error: M3U8 link not found for {url}")
            return None

        snippet = response[max(0, m3u8_index - 200):m3u8_index]
        start_index = snippet.find('https://')
        if start_index == -1:
            print(f"Error: M3U8 link malformed for {url}")
            return None

        link = snippet[start_index:]
        return link[:link.find('.m3u8') + 5]
    except requests.RequestException as e:
        print(f"Error fetching URL {url}: {e}")
        return None

def main():
    with open(CHANNEL_LIST, "r") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('~~'):
                continue

            if not line.startswith('https'):
                # Metadata line
                parts = line.split('|')
                if len(parts) != 4:
                    print(f"Error: Invalid channel metadata format -> {line}")
                    continue
                ch_name, group_title, tvg_logo, tvg_id = map(str.strip, parts)
                print(f'\n#EXTINF:-1 group-title="{group_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')
            else:
                # URL line
                m3u8_link = url_grabber(line)
                if m3u8_link:
                    print(m3u8_link)

if __name__ == "__main__":
    main()
