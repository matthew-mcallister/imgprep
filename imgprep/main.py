import sys
from PyQt6.QtGui import QImage, QPixmap

from PyQt6.QtWidgets import QApplication, QGridLayout, QHBoxLayout, QLabel, QLayout, QScrollArea, QWidget

from imgprep.project import Project
from imgprep.util import get_logger


logger = get_logger('imgprep')


class ImageGrid(QScrollArea):
    def __init__(self, project: Project) -> None:
        super().__init__()

        self.grid = QGridLayout()
        for i, img in enumerate(project.images):
            if i > 100:
                # TODO: Lazy load large directories
                break
            image = QImage(img.path)
            pixmap = QPixmap.fromImage(image)
            pixmap = pixmap.scaledToHeight(200)
            label = QLabel()
            label.setPixmap(pixmap)
            self.grid.addWidget(label, i // 4, i % 4)

        self.inner = QWidget()
        self.inner.setLayout(self.grid)
        self.setWidget(self.inner)


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        p = Project('.')

        self.image_grid = ImageGrid(p)
        self.layout_ = QHBoxLayout()
        self.layout_.addWidget(self.image_grid)
        self.setLayout(self.layout_)

        self.setWindowTitle('ImgPrep')


def main() -> None:
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
