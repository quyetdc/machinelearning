from utility.data_helpers import FileDAO
import os


class DataCollector(object):
    def __init__(self, file_path):
        self.name = 'DataCollector'
        self.file_path = file_path

    def collect_data_by_id(self, _id, _array_id=0, delimiter='\t',
                           _batch_num=100, limit=1e6, not_found_next_limit=1e6,
                           not_found_limit=1e6):
        data = []
        found_count = 0
        batch_count = 0
        not_found_next_count = 0
        not_found_count = 0
        file_dao = FileDAO(self.file_path)
        offset = 0
        eof = False
        while (found_count < limit) and (not eof) and (not_found_next_count < not_found_next_limit)\
                and (not_found_count < not_found_limit):
            lines, eof = file_dao.get_range_lines(offset, _batch_num)
            for line in lines:
                line_arr = line.split(delimiter)
                # if _id in line:
                #     data.append(line)
                if line_arr[_array_id] == _id:
                    data.append(line_arr)
                    found_count += 1
                    not_found_count = 0  # note
                else:
                    not_found_count += 1
                    print(not_found_count)
                    if found_count > 0:
                        not_found_next_count += 1
            offset += _batch_num
            batch_count += 1
        return data


def main():
    print('start...')
    # file_path = '../data/customer_saving_salary'
    file_path = '/media/cao/DATA/Study/Tech/Machine learning/Tech master/Purchase prediction/yoochoose-dataFull/yoochoose-clicks.dat'

    print os.path.isfile(file_path)
    data_collector = DataCollector(file_path=file_path)
    data = data_collector.collect_data_by_id(_id='30', delimiter=',', limit=1e3,
                                             not_found_next_limit=1e3, not_found_limit=1e5)
    print(data)
    print(len(data))


if __name__ == '__main__':
    main()

