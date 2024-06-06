import io
import wave

from ffmpeg import FFmpeg, Progress


def main():
    ffmpeg = (
        FFmpeg()
        .option("y")
        .input("input.mp4")
        .output(
            "pipe:1",
            {"codec:a": "pcm_s16le"},
            vn=None,
            f="wav",
        )
    )

    @ffmpeg.on("progress")
    def on_progress(progress: Progress):
        print(progress)

    wave_bytes = ffmpeg.execute()
    with wave.open(io.BytesIO(wave_bytes), "rb") as wave_file:
        print("Sample width in bytes:", wave_file.getsampwidth())
        print("Sampling frequency:", wave_file.getframerate())
        print("Number of frames:", wave_file.getnframes())


if __name__ == "__main__":
    main()






import asyncio
import io
import wave

from ffmpeg import Progress
from ffmpeg.asyncio import FFmpeg


async def main():
    ffmpeg = (
        FFmpeg()
        .option("y")
        .input("input.mp4")
        .output(
            "pipe:1",
            {"codec:a": "pcm_s16le"},
            vn=None,
            f="wav",
        )
    )

    @ffmpeg.on("progress")
    def on_progress(progress: Progress):
        print(progress)

    wave_bytes = await ffmpeg.execute()
    with wave.open(io.BytesIO(wave_bytes), "rb") as wave_file:
        print("Sample width in bytes:", wave_file.getsampwidth())
        print("Sampling frequency:", wave_file.getframerate())
        print("Number of frames:", wave_file.getnframes())


if __name__ == "__main__":
    asyncio.run(main())
    
    
    
    
    
    
    
    
    