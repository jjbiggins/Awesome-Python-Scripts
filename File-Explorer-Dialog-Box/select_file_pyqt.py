from PyQt5.QtWidgets import QFileDialog, QApplication
from PyQt5 import QtWidgets


def select_files(directory_location=None):
	qtapp = QApplication([directory_location])
	qtwgt = QtWidgets.QWidget()
	filenames, _ = QFileDialog.getOpenFileNames(qtwgt)
	return filenames


def main():
	filenames = select_files()
	print("You selected:\n", "\n".join(filenames))


if __name__ == "__main__":
	main()
