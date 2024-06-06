from ffmpeg import FFmpeg


def main():
    ffmpeg = (
        FFmpeg()
        .option("y")
        .input("input.mp4")
        .output(
            "output.mp4",
            {"codec:v": "libx264"},
            vf="scale=1280:-1",
            preset="veryslow",
            crf=24,
        )
    )

    ffmpeg.execute()


if __name__ == "__main__":
    main()








import asyncio

from ffmpeg.asyncio import FFmpeg


async def main():
    ffmpeg = (
        FFmpeg()
        .option("y")
        .input("input.mp4")
        .output(
            "output.mp4",
            {"codec:v": "libx264"},
            vf="scale=1280:-1",
            preset="veryslow",
            crf=24,
        )
    )

    await ffmpeg.execute()


if __name__ == "__main__":
    asyncio.run(main())
    
    
    
    
    
    
    
    
    
    
    
    
    
    from ffmpeg import FFmpeg, Progress


def main():
    ffmpeg = (
        FFmpeg()
        .option("y")
        .input("input.mov")
        .output(
            "output.mp4",
            codec="copy",
        )
    )

    @ffmpeg.on("progress")
    def on_progress(progress: Progress):
        print(progress)

    ffmpeg.execute()


if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    
    
    import asyncio

from ffmpeg import Progress
from ffmpeg.asyncio import FFmpeg


async def main():
    ffmpeg = (
        FFmpeg()
        .option("y")
        .input("input.mov")
        .output(
            "output.mp4",
            codec="copy",
        )
    )

    @ffmpeg.on("progress")
    def on_progress(progress: Progress):
        print(progress)

    await ffmpeg.execute()


if __name__ == "__main__":
    asyncio.run(main())
    
    
    
    
    
    
    
    from ffmpeg import FFmpeg, Progress


def main():
    ffmpeg = (
        FFmpeg()
        .option("y")
        .input("input.mov")
        .output(
            "output.mp4",
            {"codec:v": "libx264", "filter:v": "scale=1280:-1"},
            preset="veryslow",
            crf=24,
        )
    )

    @ffmpeg.on("progress")
    def on_progress(progress: Progress):
        print(progress)

    ffmpeg.execute()


if __name__ == "__main__":
    main()









import asyncio

from ffmpeg import Progress
from ffmpeg.asyncio import FFmpeg


async def main():
    ffmpeg = (
        FFmpeg()
        .option("y")
        .input("input.mov")
        .output(
            "output.mp4",
            {"codec:v": "libx264", "filter:v": "scale=1280:-1"},
            vf="scale=1280:-1",
            preset="veryslow",
            crf=24,
        )
    )

    @ffmpeg.on("progress")
    def on_progress(progress: Progress):
        print(progress)

    await ffmpeg.execute()


if __name__ == "__main__":
    asyncio.run(main())
    
    
    
    
    
    
    
        