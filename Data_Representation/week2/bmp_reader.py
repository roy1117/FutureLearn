from fl_networking_tools import ImageViewer


class BMPReader:
    def __init__(self, image_path):
        self.data_list = []
        self.viewer = ImageViewer()
        self.image_path = image_path
        with open(image_path, 'rb') as file:
            self.bytes_data = file.read()
        # file type data
        self.file_type_data = self.bytes_data[0:14]

        self.file_type = self.file_type_data[0:2].hex()
        print('file type : {0}'.format(self.file_type))
        self.data_list.append((self.file_type, 2))
        if self.file_type != '424d':
            raise print('file type is not .bmp')
        
        self.file_size = int.from_bytes(self.file_type_data[2:6], 'little')
        print('file size : {0}'.format(self.file_size))
        self.data_list.append((self.file_size, 4))

        self.pixel_data_offset = int.from_bytes(self.file_type_data[10:14], 'little')
        print('pixel_data_offset : {0}'.format(self.pixel_data_offset))
        self.data_list.append((self.pixel_data_offset, 4))

        # image information data
        self.image_information_data = self.bytes_data[14:54]

        self.header_size = int.from_bytes(self.image_information_data[0:4], 'little')
        print('header_size : {0}'.format(self.header_size))
        if self.header_size != 40:
            raise print('the file is damaged(header size)')

        self.image_width = int.from_bytes(self.image_information_data[4:8], 'little')
        print('image_width : {0}'.format(self.image_width))
        self.data_list.append((self.image_width, 4))

        self.image_height = int.from_bytes(self.image_information_data[8:12], 'little')
        print('image_height : {0}'.format(self.image_height))
        self.data_list.append((self.image_height, 4))

        self.planes = int.from_bytes(self.image_information_data[12:14], 'little')
        print('planes : {0}'.format(self.planes))
        self.data_list.append((self.planes, 2))

        self.bits_per_pixel = int.from_bytes(self.image_information_data[14:16], 'little')
        self.byte_per_pixel = (self.bits_per_pixel / 8)
        print('bits_per_pixel : {0}'.format(self.bits_per_pixel))
        self.data_list.append((self.bits_per_pixel, 2))

        self.compression = int.from_bytes(self.image_information_data[16:20], 'little')
        print('compression : {0}'.format(self.compression))
        self.data_list.append((self.compression, 4))

        self.image_size = int.from_bytes(self.image_information_data[20:24], 'little')
        print('image_size : {0}'.format(self.image_size))
        self.data_list.append((self.image_size, 4))

        self.x_pixel_per_meter = int.from_bytes(self.image_information_data[24:28], 'little')
        print('x_pixel_per_meter : {0}'.format(self.x_pixel_per_meter))
        self.data_list.append((self.x_pixel_per_meter, 4))

        self.y_pixel_per_meter = int.from_bytes(self.image_information_data[28:32], 'little')
        print('y_pixel_per_meter : {0}'.format(self.y_pixel_per_meter))
        self.data_list.append((self.y_pixel_per_meter, 4))

        self.total_colors = int.from_bytes(self.image_information_data[32:36], 'little')
        if self.total_colors == 0:
            if self.bits_per_pixel <= 8:
                self.actual_total_colors = 2 ** self.bits_per_pixel
        print('total_colors : {0}'.format(self.total_colors))
        self.data_list.append((self.total_colors, 4))


        self.important_colors = int.from_bytes(self.image_information_data[36:40], 'little')
        print('important_colors : {0}'.format(self.important_colors))
        self.data_list.append((self.important_colors, 4))

        # Color Pallet
        if self.actual_total_colors != 0:
            self.raw_color_pallet = self.bytes_data[54:54+self.actual_total_colors*4]
            self.data_list.append((self.raw_color_pallet, self.actual_total_colors*4))
            # print('raw_color_pallet : {0}'.format(self.raw_color_pallet))
            self.color_pallet = []
            for i in range(0, self.actual_total_colors*4, 4):
                r, g, b, a = self.raw_color_pallet[i:i+4]
                self.color_pallet.append((r, g, b, a))
            print(self.color_pallet)
        else:
            self.color_pallet = None

        # Raw Pixel Data
        self.pixel_data = []
        self.raw_pixel_data = self.bytes_data[54+self.actual_total_colors*4:]
        self.padding_bytes = int(4 - (self.image_width * self.byte_per_pixel) % 4)
        self.padded_image_width = int(self.image_width + self.padding_bytes / self.byte_per_pixel)
        counter = 0
        for j in range(0, self.padded_image_width * self.image_height, self.padded_image_width):
            counter += 1
            temp_list = []
            for i in self.raw_pixel_data.hex()[j:j+self.padded_image_width]:
                temp_list.append(i)
            self.pixel_data.insert(counter, temp_list)
        print('pixel_data : {0}'.format(self.pixel_data))

        self.display_image_file()

    def display_image_file(self):
        magnitude = 8
        self.viewer.text = "Zoomed {} %".format(magnitude*100)
        for row in range(0, self.image_width):
            for col in range(0, self.image_height):
                index = int(self.pixel_data[col][row], 16)
                rgb = self.color_pallet[index]
                for sub_row in range(0, magnitude):
                    for sub_col in range(0, magnitude):
                        self.viewer.put_pixel((row*magnitude+sub_row, (self.image_height - col)*magnitude+sub_col), rgb)
        self.viewer.start()

    def test_editing(self):
        with open(self.image_path.split('.')[0] + '_edited.bmp', 'wb') as file:
            reconstruct_data = self.rotate(90)
            file.write(reconstruct_data)

    def rotate(self, degree):
        reconstruct_data = self.reconstruct_data()
        return reconstruct_data

    def reconstruct_data(self):
        pass
