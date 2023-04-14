#NoEnv
SendMode Input
SetWorkingDir %A_ScriptDir%
IconFile = images/activated.ico
Menu,Tray,Icon, Shell32.DLL ,174, 1
if IconFile <>
	IfExist, %IconFile%
Menu, Tray, Icon, %IconFile%
ChangeWindowIcon(IconFile, hWnd) {
	Return
}

Gui, -Caption -DpiScale
Gui,Font, s22, Arial
Gui, Add, Picture, x0 y0, images/titlebar.png
Gui, Add, Text, x0 y0 w1100 h48 +BackgroundTrans gUImove
Gui, Add, Picture, x1120 y5 gClose +BackgroundTrans, exit.png
Gui, Add, Picture, x0 y48, images/background.png
Gui, Add, Picture, x527 y40 +BackgroundTrans vc1 gClick, images/button_on.png
Gui, Add, Picture, x527 y40 +BackgroundTrans vc2 gClick hidden, images/button_off.png
ci := 1
Gui, Show, w1168 h448, IPA-Keyboard
Return

uiMove:
	PostMessage, 0xA1, 2,,, A
Return

Click:
	GuiControl Hide, c%ci%
	ci := 3 - ci
	GuiControl Show, c%ci%
	Suspend
	if(A_IsSuspended)
		Menu,Tray,Icon, images/suspended.ico
	else
		Menu,Tray,Icon, images/activated.ico
Return

Keyboard:
	i::
	{
		Send {U+0069}
	}
	Return
	+i::
	{
		Send {U+026A}
	}
	Return
	y::
	{
		Send {U+0079}
	}
	Return
	+y::
	{
		Send {U+028F}
	}
	Return
	e::
	{
		Send {U+0065}
	}
	Return
	+e::
	{
		Send {U+0259}
	}
	Return
	+^e::
	{
		Send {U+0250}
	}
	Return
	ø::
	{
		Send {U+00F8}
	}
	Return
	+ø::
	{
		Send {U+0153}
	}
	Return
	+^ø::
	{
		Send {U+0276}
	}
	Return
	æ::
	{
		Send {U+025B}
	}
	Return
	a::
	{
		Send {U+00E6}
	}
	Return
	+a::
	{
		Send {U+0061}
	}
	Return
	+^a::
	{
		Send {U+0251}
	}
	Return
	u::
	{
		Send {U+0075}
	}
	Return
	o::
	{
		Send {U+006F}
	}
	Return
	+o::
	{
		Send {U+028C}
	}
	Return
	å::
	{
		Send {U+0254}
	}
	Return
	+å::
	{
		Send {U+0252}
	}
	Return
	p::
	{
		Send {U+0070}
		Send {U+02B0}
	}
	Return
	t::
	{
		Send {U+0074}
		Send {U+02E2}
	}
	Return
	+t::
	{
		Send {U+0074}
		Send {U+1D9D}
	}
	Return
	k::
	{
		Send {U+006B}
		Send {U+02B0}
	}
	Return
	b::
	{
		Send {U+0062}
		Send {U+0325}
	}
	Return
	g::
	{
		Send {U+0261}
		Send {U+030A}
	}
	Return
	d::
	{
		Send {U+0064}
		Send {U+0325}
	}
	Return
	+d::
	{
		Send {U+00F0}
	}
	Return
	m::
	{
		Send {U+006D}
	}
	Return
	n::
	{
		Send {U+006E}
	}
	Return
	+n::
	{
		Send {U+014B}
	}
	Return
	f::
	{
		Send {U+0066}
	}
	Return
	v::
	{
		Send {U+0076}
	}
	Return
	s::
	{
		Send {U+0073}
	}
	Return
	+s::
	{
		Send {U+0255}
	}
	Return
	r::
	{
		Send {U+0281}
	}
	Return
	+r::
	{
		Send {U+0281}
		Send {U+0325}
	}
	Return
	l::
	{
		Send {U+006C}
	}
	Return
	+l::
	{
		Send {U+006C}
		Send {U+0325}
	}
	Return
	j::
	{
		Send {U+006A}
	}
	Return
	+j::
	{
		Send {U+006A}
		Send {U+030A}
	}
	Return
	h::
	{
		Send {U+0068}
	}
	Return
	w::
	{
		Send {U+0077}
	}
	Return
	:::
	{
		Send {U+02D0}
	}
	Return
	?::
	{
		Send {U+02C0}
	}
	Return
	<::
	{
		Send {U+032F}
	}
	Return
	[::
	{
		Send {[}
	}
	Return
	]::
	{
		Send {]}
	}
	Return
	|::
	{
		Send {U+007C}
	}
	Return
	'::
	{
		Send {U+02C8}
	}
	Return
	,::
	{
		Send {U+0329}
	}
	Return
	-::
	{
		Send {U+032F}
	}
	Return

Close:
	GuiEscape:
	Exitapp