


class Test():

    def __init__(self, *args):
        pass

    @classmethod
    def from_h5(cls, filepath) -> cls:
        pass

    @classmethod
    def from_image(cls, img_array) -> cls:
        pass


def main():

    img_array = np.array(...)
    ms1 = Test.from_image(img_array)
    ms2 = Test.from_h5(f"this\path")


if __name__ == "__main__":
    main()