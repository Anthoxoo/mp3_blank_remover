import sys

from pydub import AudioSegment
from pydub.silence import split_on_silence
from pydub.utils import mediainfo

USAGE_MESSAGE = "Error, usage: mp3_blank_remover input_file_path.mp3"


def main():
    args = sys.argv
    if len(args) != 2:
        print(USAGE_MESSAGE)
        sys.exit(1)

    try:
        default_song = AudioSegment.from_mp3(args[1])
        cutted_parts = split_on_silence(default_song, 2000)

        metadatas = mediainfo(args[1])
        tags = metadatas.get("TAG", {})

        title = tags.get("title", "Unknown title")
        artist = tags.get("artist", "Unknown artist")
        album = tags.get("album", "Unknown Album")
        composer = tags.get("composer", "Unknown composer")
        bitrate_bits = int(
            metadatas.get("bit_rate", 192000)
        )  # Default value is 192000 if the bitrate is not found.
        bitrate_kbps = bitrate_bits // 1000

        # Create a silence chunk that's 0.5 seconds (or 500 ms) long for padding.
        silence_chunk = AudioSegment.silent(duration=500)
        final_song = AudioSegment.empty()
        final_song += silence_chunk

        for chunk in cutted_parts:
            final_song += chunk

        final_song += silence_chunk

        final_song.export(
            f"{title}_without_blank.mp3",
            format="mp3",
            bitrate=f"{bitrate_kbps}k",
            tags={"artist": artist, "album": album, "composer": composer},
        )

    except FileNotFoundError:
        print(
            f"Error, the file : '{args[1]}' has not been find, please verify the path given."
        )

    except Exception as e:
        print(f"An unknown error appeared : {e}")


if __name__ == "__main__":
    main()
