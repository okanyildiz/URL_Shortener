# URL_Shortener

This script offers a simple utility to automatically detect and shorten URLs within a text file using the tinyurl.com service. It's especially handy for markdown files or other textual content where you'd like to replace long, unwieldy URLs with shorter versions.

## 🌟 Features

- URL Detection: Utilizes regex to automatically identify all URLs present in the designated input.md file.
- Automatic Shortening: Every detected URL is shortened via the tinyurl.com API. 
- File Input/Output: Reads from input.md and writes the content with the shortened URLs to output.md.


## 🚀 How to Use

- 📥 Clone or download this repository.
- 📝 Fill the input.md file with your content, which includes the URLs you wish to shorten.
- ▶️ Run the script:

  ``` python your_script_name.py ```

- 📤 Check the output.md file for the content with the now shortened URLs.

## 🔧 Requirements

- Python 3.x
- requests library (to make the HTTP requests).
  To install the required library, use:

``` pip install requests ```
