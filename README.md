# image-matrix-viewer

## Overview

**image-matrix-viewer** is a Streamlit-based web application for visualizing the pixel matrix of uploaded images. It displays the image, its pixel values in a table, and allows users to inspect individual pixel values by specifying coordinates.

## Features

- Upload images (`.jpg`, `.jpeg`, `.png`)
- View the image and its pixel matrix side by side
- Inspect pixel values by entering coordinates

## Installation

1. Clone the repository.
2. Install dependencies:

    ```sh
    pip install -r requirements.txt
    ```

3. Run the application:

    ```sh
    streamlit run main.py
    ```

## Usage

1. Upload an image using the file uploader.
2. The image and its pixel matrix will be displayed.
3. Enter `x` and `y` coordinates to view the pixel value at that location.

## File Structure

- [`main.py`](main.py): Main application code.
- [`requirements.txt`](requirements.txt): Python dependencies.
- [`pyproject.toml`](pyproject.toml): Project metadata.
- [`README.md`](README.md): Project documentation.

## Dependencies

- streamlit
- opencv-python
- numpy
- pillow

## License

Add your license information here.