Reminder(title, snooze, window)
{
    TransparentColor = EEAA99
    Gui +LastFound +AlwaysOnTop +ToolWindow
    Gui, Color, %TransparentColor%
    Gui, Font, s40, Impact
    Gui, Add, Text, , %title%
    Gui, Add, Button, default, Yes
    Gui, Add, Button, x+20, Snooze
    WinSet, TransColor, %TransparentColor%
    Gui -Caption
    Gui, Show

    return
}