from fl_networking_tools import ImageViewer
import socket
import pickle
import time

udp_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_server.bind(("0.0.0.0", 20001))
viewer = ImageViewer()


def get_pixel_data():
    lost_pixels = 0
    latest_pix_pos = (0, 0)
    error_buffer = []
    while True:
        data, client_address = udp_server.recvfrom(1024)
        message = pickle.loads(data)
        pos = message[0]
        rgba = message[1]
        if pos[0] > latest_pix_pos[0] or pos[1] > latest_pix_pos[1]:
            while pos[0] - latest_pix_pos[0] > 1:
                latest_pix_pos = (latest_pix_pos[0] + 1, latest_pix_pos[1])
                error_buffer.append(latest_pix_pos)
                lost_pixels += 1
                viewer.text = 'error count : {0}'.format(lost_pixels)
            latest_pix_pos = pos

        elif pos[0] < latest_pix_pos[0]:
            if pos in error_buffer:
                error_buffer.remove(pos)
                lost_pixels -= 1
                viewer.text = 'error count : {0}'.format(lost_pixels)

        viewer.put_pixel(pos, rgba)


viewer.start(get_pixel_data)



