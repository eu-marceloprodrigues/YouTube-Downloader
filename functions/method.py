from moviepy import AudioFileClip
from pytubefix import YouTube
import os
import win32api
import win32con

def download_music(url):
    try:
        yt = YouTube(url)
        print(f"🎶 Baixando áudio de: {yt.title}")

        # Baixa o áudio
        stream = yt.streams.filter(only_audio=True).first()
        arquivo_baixado = stream.download(output_path='downloads')

        # Define novo nome .mp3
        base, _ = os.path.splitext(arquivo_baixado)
        mp3_arquivo = base + ".mp3"

        # Converte para MP3
        AudioFileClip(arquivo_baixado).write_audiofile(mp3_arquivo)

        # Remove o arquivo original (m4a/mp4)
        os.remove(arquivo_baixado)

        win32api.MessageBox(0, f"✅ Convertido e salvo como: \n {mp3_arquivo}"," Sucesso", win32con.MB_OK | win32con.MB_ICONINFORMATION)

    except Exception as e:
        win32api.MessageBox(0, f"❌ Erro ao baixar/converter :\n {e}","Falha", win32con.MB_OK | win32con.MB_ICONWARNING)


def download_video(url):
    try:
        yt = YouTube(url)
        
        # Baixa video
        stream = yt.streams.get_highest_resolution()
        arquivo_baixado = stream.download(output_path = 'downloads/video')

        # Renomeia arquivo
        base, _ = os.path.splitext(arquivo_baixado)
        nome_video = base

        win32api.MessageBox(
            0,
            f"✅ Vídeo '{nome_video}' baixado com sucesso!\nSalvo em: {base}",
            "Sucesso",
            win32con.MB_OK | win32con.MB_ICONINFORMATION,
        )

    except Exception as erro:
        win32api.MessageBox(
            0,
            f"❌ Erro ao baixar/converter vídeo:\n{erro}",
            "Falha",
            win32con.MB_OK | win32con.MB_ICONWARNING,
        )
