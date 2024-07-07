import numpy as np
import onnxruntime
#import onnx

# 体绘制的方法
# 数据要求三维npy数组
def fault_go_rendering(data):
    """
    :param data: npy数据（128*128*128）
    :return: 直接返回识别好的断层数据
    """
    # 加载输入数据
    input_data = data

    # 数据先进行转置，之后进行input格式调整
    input_data = np.transpose(input_data)
    input_data = input_data.reshape(1, *input_data.shape, 1)

    print("input_data: ", input_data.shape)

    # 加载 ONNX 模型
    onnx_model_path = './model/pred_3d.onnx'
    ort_session = onnxruntime.InferenceSession(onnx_model_path)

    # 获取模型的输入名称
    input_name = ort_session.get_inputs()[0].name
    print("模型的输入名称:", input_name)

    # 检查模型格式是否完整及正确
    # model = onnx.load(onnx_model_path)
    # onnx.checker.check_model(model)
    # print(onnx.helper.printable_graph(model.graph))

    # 执行推断
    output = ort_session.run(None, {'input_1': input_data})

    print("output[0].shape: ", output[0].shape)

    pred = output[0]
    pred = pred[0, :, :, :, 0]
    pred = np.transpose(pred)
    pred = np.clip(pred, 0.4, 1)


    return pred




# 原始数据可能不是128*128*128的，现在要进行数据的转化
def fault_data_format_conversion(data):
    '''
    :param data: 原始三维数组
    :return: 模型训练好的三维数组
    '''

    # 假设 data 是一个大的三维数组，其形状为 (M, N, P)
    # 其中 M、N、P 分别表示三维数组的大小
    M, N, P = data.shape
    x, y, z = M, N, P
    if (M % 128):
        x = (M // 128 + 1) * 128
    if (N % 128):
        y = (N // 128 + 1) * 128
    if (P % 128):
        z = (P // 128 + 1) * 128

    print(x, y, z)

    new_data = np.zeros((x, y, z))
    new_data[:M, :N, :P] = data


    #data = np.random.rand(M, N, P)

    # 定义小三维数组的大小
    size = 128

    # 将大的三维数组拆分成小的 128x128x128 的小三维数组
    small_arrays = []
    for i in range(0, M, size):
        for j in range(0, N, size):
            for k in range(0, P, size):
                small_array = np.zeros((size, size, size))
                small_array_shape = new_data[i:i + size, j:j + size, k:k + size].shape
                small_array[:small_array_shape[0], :small_array_shape[1], :small_array_shape[2]] = new_data[i:i + size,
                                                                                                   j:j + size,
                                                                                                   k:k + size]
                small_arrays.append(fault_go_rendering(small_array.astype(np.float32)))

    # 将小数组整合成原来的大小
    reconstructed_data = np.zeros((x, y, z))
    idx = 0
    for i in range(0, M, size):
        for j in range(0, N, size):
            for k in range(0, P, size):
                reconstructed_data[i:i + size, j:j + size, k:k + size] = small_arrays[idx][:size, :size, :size]
                idx += 1

    # 打印重构后的三维数组的形状，检查是否和原来一样
    res_data = reconstructed_data[:M, :N, :P]
    print("重构后的三维数组的形状:", res_data.shape)

    # 将y=N的位置上的x-z切片的数变成0
    res_data[:, N - 1, :] = 0.4
    res_data[M - 1, :, :] = 0.4

    return res_data

if __name__=="__main__":
    data = np.load("D:\segy数据\ma\/f3_no_standardizer_512_384_128.npy")
    print(data.shape)
    pred_data = fault_data_format_conversion(data)
    print(pred_data.shape)
    np.save("D:\segy数据\ma\/f3_no_standardizer_512_384_128_pred.npy", pred_data)
