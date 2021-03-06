#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-21 22:21:03
# @Author  : Flying Hu (1152598046@qq.com)
# @Link    : http://www.flyinghu.cn/
# @Version : $Id$


# 图片验证码redis有效期  单位 秒
IMAGE_CODE_REDIS_EXPIRES = 180

# 短信验证码redis有效期  单位 秒
SMS_CODE_REDIS_EXPIRES = 300

# 发送短信验证码间隔  单位 秒
SEND_SMS_CODE_INTERVEL = 60

# 限制ip登录错误次数
LOGIN_ERROR_MAX_TIMES = 5

# 登录错误限制时间 单位: 秒
LOGIN_ERROR_FORBID_TIME = 600

# 腾讯云访问资源url头
TENG_XUN_FILE_URL_HEAD = 'https://robot-1259307444.cos.ap-guangzhou.myqcloud.com/'