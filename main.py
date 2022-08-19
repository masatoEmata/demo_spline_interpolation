import numpy as np
from scipy.interpolate import splprep, splev
import matplotlib.pyplot as plt

# https://www.web-dev-qa-db-ja.com/ja/python/%E9%96%89%E6%9B%B2%E7%B7%9A%E3%82%92%E4%B8%80%E9%80%A3%E3%81%AE%E7%82%B9%E3%81%AB%E9%81%A9%E5%90%88%E3%81%95%E3%81%9B%E3%82%8B/1054592661/
# define pts from the question

def clean_char_data(data):
    # data = sorted(data)
    x_list = []
    y_list = []
    for point in data:
        x = point[0]
        while x in x_list:
            x = x * 1.0001
        x_list.append(x)
        y = 400 - point[1]
        if y in y_list:
            y = y * 1.0001
        y_list.append(y)
    return [list(p) for p in zip(x_list, y_list)]


def simple_line_plot(data, point_num=1000):
    data = clean_char_data(data)
    pts = np.array(data)
    tck, u = splprep(pts.T, u=None, s=0.0)
    print(f'knot vector .. length: {len(tck[0])} \n{tck[0]}\n')
    print(f'coef ..: length:{len(tck[1])} \n{tck[1]}\n')
    print(f'Nd ..: {tck[2]}\n')
    u_new = np.linspace(u.min(), u.max(), point_num)
    x_new, y_new = splev(u_new, tck, der=0)
    # plt.plot(pts[:, 0], pts[:, 1], 'ro')
    plt.plot(x_new, y_new)
    print('xの値の数', len(x_new), 'yの値の数', len(y_new), y_new)


if __name__ == '__main__':
    stroke1 = [[97, 214], [97, 214], [113, 214], [149, 215], [190, 215],
        [242, 211], [261, 208], [269, 206], [276, 204]]
    stroke2 = [[210, 153], [209, 153], [191, 170], [177, 195], [172, 223], [172, 243], [
        174, 269], [181, 305], [192, 351], [206, 398], [226, 427], [242, 437], [248, 439]]
    stroke3 = [[292, 185], [292, 185], [290, 188], [280, 206], [272, 220], [262, 234], [252, 248], [241, 267], [229, 283], [222, 292], [208, 306], [202, 314], [190, 332], [174, 353], [158, 370], [140, 386], [107, 403], [96, 407], [82, 403], [74, 375], [75, 348], [85, 327], [95, 313], [121, 287], [138, 274], [160, 265], [176, 261], [200, 261], [222, 261], [247, 264], [268, 270], [287, 279], [300, 293], [312, 310], [317, 336], [318, 362], [318, 390], [313, 418], [293, 438], [263, 459], [235, 468], [231, 469]]

    simple_line_plot(stroke1)
    simple_line_plot(stroke2)
    simple_line_plot(stroke3)
    plt.show()

