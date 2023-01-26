import numpy as np


class Freivald:
    def __init__(self, k):
        self.k = k

    def verify_freivald(self, file_path):
        """
        :param file_path: txt file path -> str
        :return: verification result 'Yes' or 'No' -> str
        """
        m1 = self.get_matrix(file_path)['m1']
        m2 = self.get_matrix(file_path)['m2']
        m3 = self.get_matrix(file_path)['m3']
        result = []
        for i in range(self.k):
            if self.compute_freivald(m1, m2, m3, file_path):
                result.append(1)
            else:
                result.append(0)
        print('No') if 0 in result else print('Yes')

    def compute_freivald(self, m1, m2, m3, file_path):
        """
        :param m1: n by n matrix -> array
        :param m2: n by n matrix -> array
        :param m3: n by n matrix -> array
        :param file_path: txt file path -> str
        :return: computation result whether m1*m2 = m3 -> bool
        """
        n = self.get_matrix_dim(file_path)
        rv = self.get_random_vector(file_path)
        m2rv = self.multiply_matrix(m2, rv)
        m3rv = self.multiply_matrix(m3, rv)
        m1m2rv = self.multiply_matrix(m1, m2rv)
        result = m1m2rv - m3rv
        if np.array_equal(result, np.zeros((n, 1))):
            return True

    def get_matrix_dim(self, file_path):
        """
        :param file_path: txt file path -> str
        :return: matrix dimension n -> int
        """
        input_list = self.clean_contents(file_path)
        n = self.str_to_int(input_list[0])[0]
        return n

    def get_matrix(self, file_path):
        """
        :param file_path: txt file path -> str
        :return: n by n matrix (m1, m2, m3) -> dict
        """
        entries = self.clean_contents(file_path)
        matrix_dict = {
            'm1': self.shape_matrix(entries[1], file_path),
            'm2': self.shape_matrix(entries[2], file_path),
            'm3': self.shape_matrix(entries[3], file_path)
        }
        return matrix_dict

    def shape_matrix(self, entries, file_path):
        """
        :param entries: entries of matrix -> list
        :param file_path: txt file path -> str
        :return: n by n matrix -> array
        """
        n = self.get_matrix_dim(file_path)
        entries = self.str_to_int(entries)
        matrix = np.matrix(entries)
        shaped_matrix = matrix.reshape(n, n)
        return shaped_matrix

    def read_txt(self, file_path):
        """
        :param file_path: txt file path -> str
        :return: contents of txt file -> list
        """
        with open(f'{file_path}', 'r') as file:
            contents = file.readlines()
            return contents

    def clean_contents(self, file_path):
        """
        :param file_path: txt file path -> str
        :return:
        """
        result = []
        contents = self.read_txt(file_path)
        for content in contents:
            cleaned_content = self.split_text(self.clean_text(content))
            result.append(cleaned_content)
        return result

    def get_random_vector(self, file_path):
        """
        :param n: size of matrix
        :return: numpy array of n by 1 vector
        """
        n = self.get_matrix_dim(file_path)
        rv = np.random.randint(2, size=(n, 1))
        return rv

    def multiply_matrix(self, m1, m2):
        """
        :param m1, m2: n by n matrix
        :return: numpy array of multiplied matrix (= m1 * m2)
        """
        mul_matrix = np.matmul(m1, m2)
        return mul_matrix

    def str_to_int(self, str_list):
        """
        :param str_list: list of strings -> list
        :return: list of integers -> list
        """
        result = []
        for item in str_list:
            item = int(item)
            result.append(item)
        return result

    def clean_text(self, raw_text):
        """
        :param raw_text: text with '\n' -> str
        :return: text without '\n' -> str
        """
        plain_text = raw_text.replace('\n', '')
        return plain_text

    def split_text(self, raw_text):
        """
        :param raw_text: text with blanks -> str
        :return: text without blanks -> str
        """
        plain_text = raw_text.split(' ')
        return plain_text
