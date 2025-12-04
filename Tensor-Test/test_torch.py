import torch

# 1. PyTorch를 사용하여 3x3 크기의 랜덤 텐서 2개 생성
tensor1 = torch.rand(3, 3)
tensor2 = torch.rand(3, 3)

print("Tensor 1:\n", tensor1)
print("Tensor 2:\n", tensor2)

# 2. 두 텐서의 행렬곱(Matrix Multiplication) 계산
result = torch.matmul(tensor1, tensor2)

print("Result:\n", result)

# 3. 결과 텐서의 크기(shape)과 데이터 타입 출력
print("Shape:", result.shape)
print("Data Type:", result.dtype)
