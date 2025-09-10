Ubuntu Image Fetcher

A mindful tool for connecting, respecting, and sharing — inspired by the Ubuntu philosophy

“I am because we are.” – Ubuntu proverb

 Project Overview

The Ubuntu Image Fetcher is a Python script that demonstrates how Ubuntu’s principles of community, respect, and sharing can be applied to technology.

It allows users to:

Download images from the web by providing URLs.

Save them into a shared folder (Fetched_Images).

Handle errors gracefully, respecting that not all connections succeed.

Prevent duplicates and check content type for safety.

This project was built to practice using Python’s requests library, file management, and error handling while honoring Ubuntu values.

Features

-Download images from one or multiple URLs

-Creates a Fetched_Images folder automatically

-Skips duplicates to avoid clutter

-Validates that the content is an image (via HTTP headers)

-Handles network errors gracefully

 Installation
-Clone this repository:
git clone https://github.com/Lizz064/Ubuntu_Requests.git
cd Ubuntu_Requests

Install required dependencies:
python -m pip install requests

Enter one or more image URLs (separated by commas). Example:
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter one or more image URLs (separated by commas): https://picsum.photos/200/300
✓ Successfully fetched: image_ab12cd34.jpg
✓ Image saved to Fetched_Images/image_ab12cd34.jpg


“A person is a person through other persons.” – Ubuntu
