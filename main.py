class MainWindow:
    def __init__(self, master, username, sock):
        # Tkinter Code Here

    def insert_msg(self, data):  # d_type 1 - msg
        self.chat_textbox.insert(END, "\n%s %s" % (datetime.now().strftime('%H:%M:%S'), data))
        self.chat_textbox.see(END)

    def send_msg(self, data, d_type=SEND_ENUM.TYPE_MSG, arg=0):
        data = str(data)
        if len(data) >= 1 and d_type == SEND_ENUM.TYPE_MSG:
            try:
                self.chat_textbox.insert(END, "\n%s [Me] %s" % (datetime.now().strftime('%H:%M:%S'), data))

                # For example, here has to use send_msg method from SockHandler class
                # self.sock_handler.send_msg(data)

            except sock_handling.ConnectionError as error:
                self.chat_textbox.insert(END, "\nError: The message was not delivered", "RED")
            else:
                pass
            finally:
                self.msg_box_entry.delete(0, 'end')
                self.chat_textbox.see(END)
        elif d_type != SEND_ENUM.TYPE_MSG:
            try:
                # also here self.sock_handler.send_msg(data, d_type)
            except sock_handling.ConnectionError as error:
                pass
        else:
            pass

class SockHandler:
    def __init__(self, client_socket):
        # nothing relevant for the Q

    def send_msg(self, data, d_type=SEND_ENUM.TYPE_MSG, arg=0):
        packed_data = self.pack_data(d_type, arg, data)

        if len(data) >= 1 and d_type == SEND_ENUM.TYPE_MSG:
            try:
                self.client_socket.send(packed_data)
            except socket.error:
                raise ConnectionError("Connection Error")

            finally:
                pass

        elif d_type != SEND_ENUM.TYPE_MSG:
            try:
                self.client_socket.send(packed_data)
            except socket.error:
                raise ConnectionError("Connection Error")

    def receive_data(self):
        try:
            while True:
                recv_data = self.client_socket.recv(self.BUFFER)
                (d_type,), data = struct.unpack("!I", recv_data[:4]), recv_data[4:]
                if d_type == RECV_ENUM.TYPE_MSG:

                    # For example, here has to use insert_msg method from MainWindow class

                elif d_type == RECV_ENUM.TYPE_USER_LIST:
                    pass
                elif d_type == RECV_ENUM.TYPE_POKE:
                    pass
        except socket.error:
            self.client_socket.close()
            raise ConnectionError("Connection Error")