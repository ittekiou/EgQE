#!/usr/bin/env python3
"""
Simple SVG to PNG converter using PIL and svgpathtools
"""

import sys
import os
from PIL import Image, ImageDraw
import xml.etree.ElementTree as ET

def convert_svg_to_png_simple(svg_path, png_path=None, width=800, height=600):
    """
    Simple SVG to PNG conversion using PIL
    """
    try:
        # If no output path specified, create one
        if png_path is None:
            base_name = os.path.splitext(svg_path)[0]
            png_path = f"{base_name}.png"
        
        # Create a white background image
        img = Image.new('RGB', (width, height), 'white')
        
        # Parse SVG to get basic info
        tree = ET.parse(svg_path)
        root = tree.getroot()
        
        # Get SVG dimensions
        svg_width = int(root.get('width', width))
        svg_height = int(root.get('height', height))
        
        print(f"SVG dimensions: {svg_width}x{svg_height}")
        print(f"Converting to PNG: {width}x{height}")
        
        # For now, just create a placeholder image with text
        draw = ImageDraw.Draw(img)
        
        # Add title
        try:
            from PIL import ImageFont
            # Try to use a default font
            font = ImageFont.load_default()
        except:
            font = None
        
        # Draw some basic info
        draw.text((10, 10), f"Converted from: {os.path.basename(svg_path)}", fill='black', font=font)
        draw.text((10, 30), f"Original size: {svg_width}x{svg_height}", fill='black', font=font)
        draw.text((10, 50), f"Output size: {width}x{height}", fill='black', font=font)
        draw.text((10, 80), "Note: This is a placeholder image.", fill='red', font=font)
        draw.text((10, 100), "For full SVG rendering, use a browser or", fill='red', font=font)
        draw.text((10, 120), "specialized SVG viewer.", fill='red', font=font)
        
        # Save the image
        img.save(png_path, 'PNG')
        
        print(f"Created placeholder PNG: {png_path}")
        print("Note: This is a basic placeholder. For full SVG rendering,")
        print("consider using a web browser or specialized SVG tools.")
        
    except Exception as e:
        print(f"Error: {e}")
        print("Creating a simple placeholder image...")
        
        # Create a simple placeholder
        img = Image.new('RGB', (width, height), 'lightblue')
        draw = ImageDraw.Draw(img)
        draw.text((width//2-100, height//2), "SVG to PNG", fill='black')
        draw.text((width//2-150, height//2+30), "Placeholder Image", fill='black')
        
        if png_path is None:
            png_path = "diagram3_wave_equations_placeholder.png"
        
        img.save(png_path, 'PNG')
        print(f"Created placeholder: {png_path}")

if __name__ == "__main__":
    svg_file = "diagram3_wave_equations.svg"
    
    if not os.path.exists(svg_file):
        print(f"Error: {svg_file} not found")
        sys.exit(1)
    
    convert_svg_to_png_simple(svg_file) 