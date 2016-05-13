import os


class FileDAO(object):
    def __init__(self, file_path):
        self.name = 'FileDAO'
        self.file_path = file_path

    def get_line(self, line_number):
        f = open(self.file_path, 'r')
        data = iter(f)
        try:
            for i in range(line_number):
                data.next()
            line = data.next().strip()
        except StopIteration:
            line = None
        f.close()
        return line

    def get_line_as_array(self, line_number, delimiter='\t'):
        line = self.get_line(line_number)
        if line is not None:
            line_arr = line.strip().split(delimiter)
        else:
            line_arr = []
        return line_arr

    def get_range_lines_as_arrays(self, offset=-1, limit=0, delimiter='\t'):
        batch_data = []
        i_file = open(self.file_path, "r")
        data = iter(i_file)
        eof = False
        try:
            if offset > 0:
                for i in range(0, (offset + limit)):
                    if i > offset - 1:
                        batch_data.append(data.next().strip().split(delimiter))
                    else:
                        data.next()
            else:
                for i in range(0, limit):
                    batch_data.append(data.next().strip().split(delimiter))
        except StopIteration:
            eof = True
            pass
        i_file.close()
        return batch_data, eof

    def get_range_lines(self, offset=-1, limit=0):
        batch_data = []
        i_file = open(self.file_path, "r")
        data = iter(i_file)
        eof = False
        try:
            if offset > 0:
                for i in range(0, (offset + limit)):
                    if i > offset - 1:
                        batch_data.append(data.next().strip())
                        # line = data.next().strip()
                        # batch_data.append(line)
                    else:
                        data.next()
            else:
                for i in range(0, limit):
                    batch_data.append(data.next().strip())
        except StopIteration:
            eof = True
            pass
        i_file.close()
        return batch_data, eof


def main():
    print('start...')
    file_dao = FileDAO(file_path='../../data/customer_saving_salary')
    line_at3 = file_dao.get_line(3)
    line_at3_arr = file_dao.get_line_as_array(3)
    line_at_range3_5, _ = file_dao.get_range_lines(3, 2)
    line_at_range3_5_arr, _ = file_dao.get_range_lines_as_arrays(3, 2)
    print(line_at3)
    print(line_at3_arr)
    print(line_at_range3_5)
    print(line_at_range3_5_arr)


if __name__ == '__main__':
    main()

