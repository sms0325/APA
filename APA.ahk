#SingleInstance, force
#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.

#Include APAManager.ahk
#Include APAReminder.ahk

TransparentColor = EEAA99
Gui +LastFound +AlwaysOnTop +ToolWindow
Gui, Color, %TransparentColor%
Gui, Font, S72, Arial Black
Gui, Add, Text,, Hello
WinSet, TransColor, %TransparentColor%
Gui -Caption
Gui, Show