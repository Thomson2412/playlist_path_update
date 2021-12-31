import os


def update_path(input_dir, output_dir, old_path, new_path):
    for root, dirs, files in os.walk(input_dir):
        for filename in files:
            if "m3u" in os.path.splitext(filename)[1]:
                file_path = os.path.abspath(os.path.join(root, filename))
                with open(file_path, "r", encoding="iso-8859-1") as playlist_file:
                    old_content = playlist_file.read().strip()
                    updated_content = old_content.replace(old_path, new_path)
                    output_path = os.path.join(output_dir, filename)
                    with open(output_path, "w") as output_file:
                        output_file.write(updated_content)


if __name__ == '__main__':
    update_path(
        "playlists",
        "updated",
        "/media/thomas/Lexar",
        "/Volumes/LEXAR"
    )
