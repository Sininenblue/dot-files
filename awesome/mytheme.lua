local gears = require("gears")
local theme_assets = require("beautiful.theme_assets")
local xresources = require("beautiful.xresources")
local dpi = xresources.apply_dpi

local gfs = require("gears.filesystem")
local themes_path = gfs.get_themes_dir()

local theme = {}

theme.font = "JetBrainsMono Nerd  9"

-- Palette
local flamingo = "#F2CDCD"
local mauve = "#DDB6F2"
local pink = "#F5C2E7"
local maroon = "#E8A2AF"
local red = "#F28FAD"
local peach = "#F8BD96"
local yellow = "#FAE3B0"
local green = "#ABE9B3"
local teal = "#B5E8E0"
local blue = "#96CDFB"
local sky = "#89DCEB"

local black_0 = "#161320"
local black_1 = "#1A1826"
local black_2 = "#1E1E2E"
local black_3 = "#302D41"
local black_4 = "#575268"
local gray_0 = "#6E6C7E"
local gray_1 = "#988BA2"
local gray_2 = "#C3BAC6"
local white = "#D9E0EE"
local lavender = "#C9CBFF"
local rosewater = "#F5E0DC"

theme.wallpaper = "/home/sininenblue/Pictures/toko.png"

theme.bg_normal     = black_0
theme.bg_focus      = black_3
theme.bg_urgent     = red
theme.bg_minimize   = gray_0
theme.bg_systray    = black_0

theme.fg_normal     = gray_2
theme.fg_focus      = white
theme.fg_urgent     = white
theme.fg_minimize   = white

theme.useless_gap   = dpi(2)
theme.border_width  = dpi(2)
theme.border_normal = black_1
theme.border_focus  = black_4
theme.border_marked = maroon


theme.taglist_shape = function(cr, width, height)
    gears.shape.rectangle(cr, width, height)
end

theme.taglist_bg_focus = sky
theme.taglist_fg_focus = black_0

theme.taglist_bg_occupied = black_3
theme.taglist_bg_empty = black_0


theme.tasklist_plain_task_name = true
theme.separator_color = black_3

-- local taglist_square_size = dpi(5)
-- theme.taglist_squares_sel = theme_assets.taglist_squares_sel(
--     taglist_square_size,
--     gray_2
-- )
-- theme.taglist_squares_unsel = theme_assets.taglist_squares_sel(
--     taglist_square_size,
--     gray_2
-- )

theme.menu_submenu_icon = themes_path.."default/submenu.png"
theme.menu_height = dpi(20)
theme.menu_width  = dpi(100)

theme.titlebar_close_button_normal = themes_path.."default/titlebar/close_normal.png"
theme.titlebar_close_button_focus  = themes_path.."default/titlebar/close_focus.png"

theme.titlebar_minimize_button_normal = themes_path.."default/titlebar/minimize_normal.png"
theme.titlebar_minimize_button_focus  = themes_path.."default/titlebar/minimize_focus.png"

theme.titlebar_ontop_button_normal_inactive = themes_path.."default/titlebar/ontop_normal_inactive.png"
theme.titlebar_ontop_button_focus_inactive  = themes_path.."default/titlebar/ontop_focus_inactive.png"
theme.titlebar_ontop_button_normal_active = themes_path.."default/titlebar/ontop_normal_active.png"
theme.titlebar_ontop_button_focus_active  = themes_path.."default/titlebar/ontop_focus_active.png"

theme.titlebar_sticky_button_normal_inactive = themes_path.."default/titlebar/sticky_normal_inactive.png"
theme.titlebar_sticky_button_focus_inactive  = themes_path.."default/titlebar/sticky_focus_inactive.png"
theme.titlebar_sticky_button_normal_active = themes_path.."default/titlebar/sticky_normal_active.png"
theme.titlebar_sticky_button_focus_active  = themes_path.."default/titlebar/sticky_focus_active.png"

theme.titlebar_floating_button_normal_inactive = themes_path.."default/titlebar/floating_normal_inactive.png"
theme.titlebar_floating_button_focus_inactive  = themes_path.."default/titlebar/floating_focus_inactive.png"
theme.titlebar_floating_button_normal_active = themes_path.."default/titlebar/floating_normal_active.png"
theme.titlebar_floating_button_focus_active  = themes_path.."default/titlebar/floating_focus_active.png"

theme.titlebar_maximized_button_normal_inactive = themes_path.."default/titlebar/maximized_normal_inactive.png"
theme.titlebar_maximized_button_focus_inactive  = themes_path.."default/titlebar/maximized_focus_inactive.png"
theme.titlebar_maximized_button_normal_active = themes_path.."default/titlebar/maximized_normal_active.png"
theme.titlebar_maximized_button_focus_active  = themes_path.."default/titlebar/maximized_focus_active.png"

-- You can use your own layout icons like this:
theme.layout_fairh = themes_path.."default/layouts/fairhw.png"
theme.layout_fairv = themes_path.."default/layouts/fairvw.png"
theme.layout_floating  = themes_path.."default/layouts/floatingw.png"
theme.layout_magnifier = themes_path.."default/layouts/magnifierw.png"
theme.layout_max = themes_path.."default/layouts/maxw.png"
theme.layout_fullscreen = themes_path.."default/layouts/fullscreenw.png"
theme.layout_tilebottom = themes_path.."default/layouts/tilebottomw.png"
theme.layout_tileleft   = themes_path.."default/layouts/tileleftw.png"
theme.layout_tile = themes_path.."default/layouts/tilew.png"
theme.layout_tiletop = themes_path.."default/layouts/tiletopw.png"
theme.layout_spiral  = themes_path.."default/layouts/spiralw.png"
theme.layout_dwindle = themes_path.."default/layouts/dwindlew.png"
theme.layout_cornernw = themes_path.."default/layouts/cornernww.png"
theme.layout_cornerne = themes_path.."default/layouts/cornernew.png"
theme.layout_cornersw = themes_path.."default/layouts/cornersww.png"
theme.layout_cornerse = themes_path.."default/layouts/cornersew.png"

theme.awesome_icon = theme_assets.awesome_icon(
    theme.menu_height, theme.bg_focus, theme.fg_focus
)

theme.icon_theme = "Papirus-Dark"

return theme