
@allure.story('获取用户标签统计')
def test_get_result_status_count_09():
    """获取用户标签统计"""
    time_stamp = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    query_params = {
        "access_token": mt.get_token(),