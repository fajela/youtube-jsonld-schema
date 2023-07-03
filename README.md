# YouTube Timestamps to JSON-LD

This Python script is designed to convert YouTube timestamps into the JSON-LD format, which is a JSON-based format to serialize Linked Data. The output JSON-LD can be used to improve the SEO of a webpage or a website by providing structured data to search engines.

## Features

- **Time Conversion**: The script can convert time in various formats including 'HH:MM:SS', 'MM:SS', or 'PTxHxMxS' to seconds.
- **Input Processing**: It processes user input to create video details, including name, duration, upload date, thumbnail URL, description, content URL, and regions allowed.
- **Timestamp Processing**: It can process timestamps and descriptions directly copied from YouTube video timestamps.
- **hasPart Array Creation**: The script creates a 'hasPart' array for video chapters, which includes details of each part, such as the start and end offset and the URL for that particular timestamp.
- **JSON-LD Structure Generation**: The script builds a complete JSON-LD structure for a video object.

## How to Use

1. Clone the repository to your local machine.
2. Run the script by typing `python3 script_name.py` in your terminal.
3. Enter the relevant information when prompted by the script.
4. The output will be a JSON-LD representation of your video content, which can be embedded into a webpage's HTML to provide rich, structured data that can be used by search engines and other applications.

## Contribute

If you want to contribute to this project and make it better, your help is very welcome. Create a pull request with your suggested changes, and they will be reviewed promptly.
