# --------------------------------
# p448 -- 패키지 만들기 (2)
# "from test_package import * "로
# 모듈을 읽어 들일 때 가져올 모듈
__all__ = ["test_module_a", "test_module_b"]
# 패키지를 읽어들일 때 처리를 작성할 수도 있음.
print("test_package를 읽어 들였습니다.")