import logging
from pathlib import Path


logger = logging.getLogger('imgprep')


class SourceImage:
    path: str

    def __init__(self, path: Path | str) -> None:
        self.path = str(path)


class Project:
    images: list[SourceImage]

    def __init__(self, dir: Path | str | None) -> None:
        path = Path(dir or '.')
        paths = [
            *path.rglob('*.[pP][nN][gG]'),
            *path.rglob('*.[jJ][pP][gG]'),
            *path.rglob('*.[jJ][pP][eE][gG]'),
            # TODO: webp support?
        ]
        self.images = [
            SourceImage(path)
            for path in paths
        ]
        logger.debug(f'added files {self.images}')
