#!/usr/bin/env ruby

#V ColorPalette_dark

WINDOW_TEXT_COLOR = "#d3dae3"   # Light gray for window text (high readability)
BUTTON_COLOR      = "#2a2d32"   # Dark neutral gray for buttons
LIGHT_COLOR       = "#5c6166"   # Lighter shade for depth
DARK_COLOR        = "#3a3f44"   # Subtle contrast for shadows
MID_COLOR         = "#4b5157"   # Mid-tone neutral gray for balance
TEXT_COLOR        = "#c0c6cf"   # Warmer light gray for text clarity
BRIGHT_TEXT_COLOR = "#f4f4f9"   # Off-white for emphasized text
BASE_COLOR        = "#1c1e22"   # Dark base for the main background
WINDOW_COLOR      = "#1b2735"   # Deep navy for professional accent

puts "Dark mode script is running..."  # Log to terminal

# Helper method to create a color brush
def color_brush(hex_color)
  RBA::QBrush.new(RBA::QColor.new(hex_color))
end

palette = RBA::QPalette.new

# Active color group
palette.setColorGroup(
  RBA::QPalette::Active,
  color_brush(WINDOW_TEXT_COLOR),  # windowText
  color_brush(BUTTON_COLOR),       # button
  color_brush(LIGHT_COLOR),        # light
  color_brush(DARK_COLOR),         # dark
  color_brush(MID_COLOR),          # mid
  color_brush(TEXT_COLOR),         # text
  color_brush(BRIGHT_TEXT_COLOR),  # brightText
  color_brush(BASE_COLOR),         # base
  color_brush(WINDOW_COLOR),       # window
)

# Apply the palette
RBA::QApplication.setPalette(palette)
