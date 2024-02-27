from datetime import datetime


def pytest_configure():
    # 配置加载完毕后，测试用例执行前执行

    print(f"{datetime.now()} pytest_configure")