#!/usr/bin/env ruby

WINDOW_TEXT_COLOR = "#333333"   
BUTTON_COLOR      = "#f7f7f7"   
LIGHT_COLOR       = "#ffffff"   
DARK_COLOR        = "#d6d6d6" 
MID_COLOR         = "#eaeaea" 
TEXT_COLOR        = "#4d4d4d" 
BRIGHT_TEXT_COLOR = "#000000" 
BASE_COLOR        = "#000000"
WINDOW_COLOR      = "#ffffff"

puts "Light mode script is running..."

def color_brush(hex_color)
  RBA::QBrush.new(RBA::QColor.new(hex_color))
end

palette = RBA::QPalette.new


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

RBA::QApplication.setPalette(palette)