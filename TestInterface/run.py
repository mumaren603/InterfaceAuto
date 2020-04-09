#Author: ls Liu
import unittest
from mainMethod.readConfig import readConf
from LogConf.loggerConf import loggerConf
from TestReport.report import raiseTestReport


logger = loggerConf().getLog()

# def all_case():
#     # 待执行用例的目录
#     test_dir = "F:\python s14\TestInterface\Testcase"
#     testcase = unittest.TestSuite()
#     discover = unittest.defaultTestLoader.discover(test_dir,
#                                                    pattern="test*.py",
#                                                    top_level_dir=None)
#     testcase.addTests(discover)  # 直接加载 discover    可以兼容python2和3
#     print(testcase)
#     return testcase
# if __name__ == "__main__":
#     # 返回实例
#     runner = unittest.TextTestRunner()
#     # run 所有用例
#     runner.run(all_case())

if __name__ == '__main__':
    # 设置待执行用例的目录
    testCasePath = readConf().getTestCasePath()
    logger.info("测试用例路径为：%s" %testCasePath)

    # 自动搜索指定目录下的case，构造测试集,执行顺序是命名顺序：先执行test_add，再执行test_sub
    discover = unittest.defaultTestLoader.discover(testCasePath, pattern='test*.py')

    # 实例化TextTestRunner类
    runner = unittest.TextTestRunner()

    # 使用run()方法运行测试套件（即运行测试套件中的所有用例）
    runner.run(discover)

    raiseTestReport()

