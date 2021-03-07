# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 12:32:22 2021

@author: Aadhavan
"""

--GuiLibrary
local GuiLibrary = loadstring(game:HttpGet("https://pastebin.com/raw/eWKgbdix",true))()
GuiLibrary.options.underlinecolor = "rainbow"
--Tabs
local Teleports = GuiLibrary:CreateWindow("Teleports")
local Misc = GuiLibrary:CreateWindow("Misc")
--Misc
Misc:Bind("Toggle Gui",
          {flag = "Toggle", kbonly = true, default = Enum.KeyCode.LeftControl},
          function()
    game.CoreGui.ScreenGui.Container.Visible = not game.CoreGui.ScreenGui.Container.Visible
end)

Misc:Bind("Spawn TP",
          {flag = "SpawnTeleport", kbonly = true},
          function()
    game:GetService('Players').LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.new(-0.0351245105, 264, 22.2895088)
end)

Misc:Bind("Shop TP",
          {flag = "ShopTeleport", kbonly = true},
          function()
    game:GetService('Players').LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.new(Vector3.new(87, 264, -1))
end)

Misc:Bind("VIP TP",
          {flag = "VipTeleport", kbonly = true},
          function()
    game:GetService('Players').LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.new(Vector3.new(0.023, 264, -69.449))
end)

Misc:Bind("Mega VIP TP",
          {flag = "MVipTeleport", kbonly = true},
          function()
    game:GetService('Players').LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.new(Vector3.new(-0.993, 263.9663, 68.752))
end)

local DestroyGUI = Misc:Button("Delete Gui", function()
    game.CoreGui.ScreenGui:Destroy()
end)
--Teleports
local SpawnTP = Teleports:Button("Spawn", function()
    game:GetService('Players').LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.new(-0.0351245105, 264, 22.2895088)
end)

local ShopTP = Teleports:Button("Shop", function()
    game:GetService('Players').LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.new(Vector3.new(87, 264, -1))
end)

local VIPTP = Teleports:Button("VIP", function()
    game:GetService('Players').LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.new(Vector3.new(0.023, 264, -69.449))
end)

local MegaVIPTP = Teleports:Button("Mega VIP", function()
    game:GetService('Players').LocalPlayer.Character.HumanoidRootPart.CFrame = CFrame.new(Vector3.new(-0.993, 263.9663, 68.752))
end)