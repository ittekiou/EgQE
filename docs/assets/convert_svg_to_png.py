#!/usr/bin/env python3
"""
SVG to PNG converter using cairosvg
"""

import sys
import os
from cairosvg import svg2png

def convert_svg_to_png(svg_path, png_path=None, width=800, height=600):
    """
    Convert SVG file to PNG
    
    Args:
        svg_path (str): Path to input SVG file
        png_path (str): Path to output PNG file (optional)
        width (int): Output width in pixels
        height (int): Output height in pixels
    """
    try:
        # If no output path specified, create one
        if png_path is None:
            base_name = os.path.splitext(svg_path)[0]
            png_path = f"{base_name}.png"
        
        # Convert SVG to PNG
        svg2png(
            url=svg_path,
            write_to=png_path,
            output_width=width,
            output_height=height
        )
        
        print(f"Successfully converted {svg_path} to {png_path}")
        print(f"Output size: {width}x{height} pixels")
        
    except ImportError:
        print("Error: cairosvg not installed. Installing...")
        os.system("pip3 install cairosvg")
        print("Please run the script again after installation.")
        
    except Exception as e:
        print(f"Error converting file: {e}")

if __name__ == "__main__":
    # Default file paths
    svg_file = "diagram3_wave_equations.svg"
    
    # Check if file exists
    if not os.path.exists(svg_file):
        print(f"Error: {svg_file} not found")
        sys.exit(1)
    
    # Convert with default settings
    convert_svg_to_png(svg_file) 