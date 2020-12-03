import os


class HugeFileReader():
    """
    Reads files in binary backwards 
    """
    def __init__(self, file_name: str, num_of_lines_to_read: int) -> None:
        self.file_name = file_name
        self.NUM_LINES_FROM_END = num_of_lines_to_read

    def read_last_num_of_lines(self) -> list:
        """
        Read file and the number of
        """
        list_of_lines = []
        with open(self.file_name, 'rb') as file_obj:
            file_obj.seek(0, os.SEEK_END)

            # byte array obj (needs to be mutable not bytes())
            buffer_obj = bytearray()

            # Get the current position of pointer i.e eof
            # tell() returns an integer which is initially zero ( beginning of file)
            # however since we have pointed the read_obj to the end of the file
            # it will be greatest possible value
            pointer_location = file_obj.tell()
            
            # we are going to work backwards now !!!
            while pointer_location >= 0:
                # moving back 1 and reading each byte
                file_obj.seek(pointer_location)
                pointer_location = pointer_location -1
                read_byte = file_obj.read(1)

                if read_byte == b"\n":
                    # decode the buffer_obj and add to our list
                    list_of_lines.append(buffer_obj.decode()[::-1])
                    if len(list_of_lines) == self.NUM_LINES_FROM_END:
                        return list(reversed(list_of_lines))

                    # clear out the buffer_obj and start over until we hit the 
                    buffer_obj = bytearray()
                else:
                    # we haven't hit the new line so let's add that byte to the buffer_obj
                    buffer_obj.extend(read_byte)

            # we hit the first line!!!
            if len(buffer_obj) > 0:
                list_of_lines.append(buffer_obj.decode()[::-1])
        return list(reversed(list_of_lines))



if __name__ == "__main__":
    # TODO: make these command line inputs
    NUM_LINES_FROM_END = 10 
    file_name = "data/bigfile_450_mb.log"

    hfr = HugeFileReader(file_name, NUM_LINES_FROM_END)
    lines = hfr.read_last_num_of_lines()
    for line in lines:
        print(line)

