import aiohttp, asyncio


class Photo:
    def __init__(self, album_id, photo_id, title, url, thumbnail_url) -> None:
        self.album_id = album_id
        self.photo_id = photo_id
        self.title = title
        self.url = url
        self.thumbnail_url = thumbnail_url

    @classmethod
    def from_json(cls, obj) -> "Photo":
        return Photo(
            obj["albumId"],
            obj["id"],
            obj["title"],
            obj["url"],
            obj["thumbnailUrl"],
        )


def print_photo_titles(photos):
    for photo in photos:
        print(f"{photo.title}", end="\n")


async def photos_by_album(task_name, album, session) -> list[Photo]:
    print(f"{task_name}")
    url = f"https://jsonplaceholder.typicode.com/photos?albumId={album}"

    response = await session.get(url)
    photos_json = await response.json()

    return [Photo.from_json(pj) for pj in photos_json]


async def main():
    async with aiohttp.ClientSession() as session:
        # photos = await photos_by_album("My task 1", 3, session)
        # print_photo_titles(photos)
        photos_in_albums = await asyncio.gather(
            *(
                photos_by_album(f"My task {i + 1}", album, session)
                for i, album in enumerate(range(2, 30))
            )
        )
        total_photos_count = sum(
            [len(photos_in_album) for photos_in_album in photos_in_albums]
        )
        print(f"{total_photos_count=}")


if __name__ == "__main__":
    asyncio.run(main())
