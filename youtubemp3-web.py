from flask import Flask, render_template, request, send_from_directory, redirect
import youtube_dl

app = Flask(__name__)

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'mp3s/%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]}
    
@app.route("/")
def index():
    if 'youtube' in request.args:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(request.args['youtube'])
            return redirect('/download/{}.mp3'.format(info['title']))
    return render_template('index.html')

@app.route("/download/<path:filename>")
def download(filename):
    return send_from_directory(directory='mp3s', filename=filename)


if __name__ == "__main__":
    app.run(debug=True)
