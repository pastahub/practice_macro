GetSeed()
{
	file := FileOpen("seed.txt", "w")
	file.write()
	file.close()
	run, pythonw.exe find_seed.py
	ComObjCreate("SAPI.SpVoice").Speak("Fetching seed")
	Seed=
	while !Seed
	{
		FileRead, Seed, seed.txt
		Sleep, 10
	}
	ComObjCreate("SAPI.SpVoice").Speak("Seed found")
	clipboard := Seed
	SetKeyDelay, 30
	Send, {Tab}{Enter}{Tab}{Tab}{Tab}{Enter}^a^v{Tab}{Tab}{Enter}{Enter}{Enter}{Tab}{Tab}{Tab}{Tab}{Enter}{Tab}{Tab}{Tab}^v{Shift down}{Tab}{Tab}{Shift up}{Enter}
}

M::
GetSeed()