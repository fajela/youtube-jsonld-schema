import json
import re

def time_to_seconds(time_str):
    """Converts a time in the format 'HH:MM:SS', 'MM:SS', or 'PTxHxMxS' to seconds."""
    if time_str.startswith('PT'):
        time_str = time_str[2:] # remove PT prefix
        hours = 0
        minutes = 0
        seconds = 0
        # extract hours, minutes, seconds
        if 'H' in time_str:
            hours_str, time_str = time_str.split('H')
            hours = int(hours_str)
        if 'M' in time_str:
            minutes_str, time_str = time_str.split('M')
            minutes = int(minutes_str)
        if 'S' in time_str:
            seconds_str, time_str = time_str.split('S')
            seconds = int(seconds_str)
        return hours * 3600 + minutes * 60 + seconds
    else:
        parts = list(map(int, time_str.split(':')))
        if len(parts) == 3:
            return parts[0] * 3600 + parts[1] * 60 + parts[2]
        elif len(parts) == 2:
            return parts[0] * 60 + parts[1]
        else:
            raise ValueError("Invalid time format")

def main():
    # Get user input
    name = input("Enter the name of the video: ")
    duration = input("Enter the duration of the video hh:mm:ss or mm:ss or PTxHxMxS: ")
    upload_date = input("Enter the upload date of the video in format yyyy-mm-dd: ")
    thumbnail_url = input("Enter the thumbnail URL of the video: ")
    description = input("Enter the description of the video: ")
    content_url = input("Enter the content URL of the video: ")
    regions_allowed = input("Enter the regions allowed for the video (e.g. Worldwide, USA, etc.): ")

    # Process timestamps
    timestamps_input = input("Enter the timestamps for the video (copy and paste all at once from YT, make sure they are correct): ")
    timestamps = re.split('(\d+:\d+:\d+|\d+:\d+)', timestamps_input)
    timestamps = [t.strip() for t in timestamps if t.strip()]  # Remove empty strings

    # Add commas after every description except the last one
    for i in range(1, len(timestamps)-1, 2):
        timestamps[i] += ','

    timestamps_str = ' '.join(timestamps)

    # Parse timestamps and descriptions
    timestamps_and_descriptions = [ts.strip() for ts in timestamps_str.split(',')]
    timestamps = []
    for td in timestamps_and_descriptions:
        ts, desc = td.split(' ', 1)
        timestamps.append((time_to_seconds(ts), desc))

    # Build "hasPart" array
    has_part = []
    for i in range(len(timestamps) - 1):
        ts1, desc1 = timestamps[i]
        ts2, desc2 = timestamps[i+1]
        has_part.append({
            "@type": "Clip",
            "name": desc1,
            "startOffset": ts1,
            "endOffset": ts2 - 1,
            "url": content_url + "&t=" + str(ts1)
        })
    # Handle last timestamp separately
    ts, desc = timestamps[-1]
    has_part.append({
        "@type": "Clip",
        "name": desc,
        "startOffset": ts,
        "endOffset": time_to_seconds(duration),
        "url": content_url + "&t=" + str(ts)
    })

    # Build full JSON-LD structure
    json_ld = {
        "@context": "https://schema.org/",
        "@type": "VideoObject",
        "name": name,
        "duration": duration,
        "uploadDate": upload_date,
        "thumbnailUrl": thumbnail_url,
        "description": description,
        "contentUrl": content_url,
        "regionsAllowed": regions_allowed,
        "hasPart": has_part
    }

    # Print the result
    print(json.dumps(json_ld, indent=2))

if __name__ == "__main__":
    main()