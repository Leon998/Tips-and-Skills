import os


def batch_rename(path, begin_num):
    fileList = os.listdir(path)  # 获得所有文件名列表，可以print(fileList)查看
    fileList.sort()
    print(len(fileList))
    name_len = len(str(len(fileList)))
    print('Total string length of the new names =', name_len)
    L = []
    for i in range(1000):
        zfill = name_len -len(str(i))
        L.append('0' * zfill)
        L[i] += str(i)
    print(L)  # L is the list of latent new names
    idx = begin_num
    for filename in fileList:
        newname = L[idx] + ".jpg"
        print(filename, "==>", newname)
        idx += 1
        # os.rename(path + filename, path + newname)


if __name__ == '__main__':

    path = 'images/'
    batch_rename(path, 0)

