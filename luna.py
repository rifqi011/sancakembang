import ascii_magic as AsciiArt

art = AsciiArt.from_image("totoro.png")
art.to_terminal(columns=120)