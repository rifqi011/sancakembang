from flask import Flask, render_template
import ascii_magic as AsciiArt

app = Flask(__name__)

@app.route('/')
def index():
    # Mengonversi gambar ke ASCII dan menyimpannya dalam format string
    art = AsciiArt.from_image("totoro.png")
    ascii_str = art.to_terminal(columns=120)

    # Render template web.html dengan melewatkan string ASCII ke template
    return render_template('web.html', ascii_str=ascii_str)

if __name__ == '__main__':
    app.run(debug=True)
