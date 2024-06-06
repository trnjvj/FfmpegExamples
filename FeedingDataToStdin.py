from pathlib import Path

from ffmpeg import FFmpeg, Progress


def main():
    ffmpeg = (
        FFmpeg()
        .option("y")
        .input("pipe:0")
        .output(
            "input.mp4",
            codec="copy",
        )
    )

    @ffmpeg.on("progress")
    def on_progress(progress: Progress):
        print(progress)

    ffmpeg.execute(Path("input.ts").read_bytes())


if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    import asyncio
from pathlib import Path

from ffmpeg import Progress
from ffmpeg.asyncio import FFmpeg


async def main():
    ffmpeg = (
        FFmpeg()
        .option("y")
        .input("pipe:0")
        .output(
            "input.mp4",
            codec="copy",
        )
    )

    @ffmpeg.on("progress")
    def on_progress(progress: Progress):
        print(progress)

    await ffmpeg.execute(Path("input.ts").read_bytes())


if __name__ == "__main__":
    asyncio.run(main())
    
    
    
    
    
    
    import subprocess

from ffmpeg import FFmpeg, Progress


def main():
    streamlink = subprocess.Popen(
        ["streamlink", "--stdout", "https://twitch.tv/zilioner", "best"],
        stdout=subprocess.PIPE,
        stderr=subprocess.DEVNULL,
    )

    ffmpeg = FFmpeg().option("y").input("pipe:0").output("output.mp4", c="copy")

    @ffmpeg.on("progress")
    def on_progress(progress: Progress):
        print(progress)

    ffmpeg.execute(streamlink.stdout)


if __name__ == "__main__":
    main()
    
    
    
    
    
    import asyncio

from ffmpeg import Progress
from ffmpeg.asyncio import FFmpeg


async def main():
    streamlink = await asyncio.create_subprocess_exec(
        "streamlink",
        "--stdout",
        "https://twitch.tv/zilioner",
        "best",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.DEVNULL,
    )

    ffmpeg = FFmpeg().option("y").input("pipe:0").output("output.mp4", c="copy")

    @ffmpeg.on("progress")
    def on_progress(progress: Progress):
        print(progress)

    await ffmpeg.execute(streamlink.stdout)


if __name__ == "__main__":
    asyncio.run(main())







