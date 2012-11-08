include 'win32ax.inc' ; you can simply switch between win32ax, win32wx, win64ax and win64wx here

.code

  start:

	invoke	MessageBox,HWND_DESKTOP,"Hello, World!","oHai",MB_OK
	invoke	ExitProcess,0

.end start

