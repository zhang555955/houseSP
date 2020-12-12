#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @File  : jsontest.py
# @Author: 橘子
# @Date  : 2020/12/9
# @Desc  : execise

import json

if __name__ == "__main__":
    print("json串解析高级实例")
    json_demo = """
        {
            "error": "0",
            "code": "0",
            "msg": "成功了！",
            "sys_time": 1607407056,
            "hostname": "web0",
            "use_cache": "off",
            "result": {
                "is_bond": "",
                "bond": "",
                "show_uid": "1934880283",
                "user_id": "1934880283",
                "photo": "http://q.3km.biz/uploads/disk4/avatar/84/d75/84d7560e358dee5629d64af24c6cd60f.jpg",
                "realname": "百里挑一并姝嗤荷更",
                "digcount": "4406",
                "serviceCount": "0",
                "remarkCount": "0",
                "age": "35",
                "sex": "男",
                "point": "50573",
                "lat": "39.393074",
                "lng": "117.015892",
                "address": "天津市",
                "store_name": "",
                "detail": "",
                "authentication": "1",
                "photoList": [
                    {
                        "view_lock": "0",
                        "is_view": "0",
                        "photo_id": "40002505295",
                        "src": "http://q.3km.biz/uploads/disk4/user/album/bb/c53/bbc53979fb5d47d396f666e8e2de38d4.jpg",
                        "shareInfo": {
                            "title": "约单APP",
                            "text": "「约单」全国领先的时间与技能共享平台",
                            "logo": "https://q.3km.biz/static/biglogo.png",
                            "url": "http://q.3km.biz/uploads/disk4/user/album/bb/c53/bbc53979fb5d47d396f666e8e2de38d4.jpg",
                            "shareObject": "1",
                            "callbackUrl": "{\"type\":\"1\"}",
                            "sharePlatforms": [
                                {
                                    "id": "0",
                                    "name": "QQ"
                                },
                                {
                                    "id": "1",
                                    "name": "微信"
                                },
                                {
                                    "id": "2",
                                    "name": "朋友圈"
                                },
                                {
                                    "id": "3",
                                    "name": "微博"
                                }
                            ]
                        },
                        "has_face": "2",
                        "cate_id": ""
                    },
                    {
                        "view_lock": "0",
                        "is_view": "0",
                        "photo_id": "3878109934",
                        "src": "http://q.3km.biz/uploads/disk4/user/album/9e/e8f/9ee8f2f931e0c315dde9df8a678c55b1.jpg",
                        "shareInfo": {
                            "title": "约单APP",
                            "text": "「约单」全国领先的时间与技能共享平台",
                            "logo": "https://q.3km.biz/static/biglogo.png",
                            "url": "http://q.3km.biz/uploads/disk4/user/album/9e/e8f/9ee8f2f931e0c315dde9df8a678c55b1.jpg",
                            "shareObject": "1",
                            "callbackUrl": "{\"type\":\"1\"}",
                            "sharePlatforms": [
                                {
                                    "id": "0",
                                    "name": "QQ"
                                },
                                {
                                    "id": "1",
                                    "name": "微信"
                                },
                                {
                                    "id": "2",
                                    "name": "朋友圈"
                                },
                                {
                                    "id": "3",
                                    "name": "微博"
                                }
                            ]
                        },
                        "has_face": "1",
                        "cate_id": "169"
                    },
                    {
                        "view_lock": "0",
                        "is_view": "0",
                        "photo_id": "3878109935",
                        "src": "http://q.3km.biz/uploads/disk4/user/album/cd/0ff/cd0ff388c21c73921165f43eb960986e.jpg",
                        "shareInfo": {
                            "title": "约单APP",
                            "text": "「约单」全国领先的时间与技能共享平台",
                            "logo": "https://q.3km.biz/static/biglogo.png",
                            "url": "http://q.3km.biz/uploads/disk4/user/album/cd/0ff/cd0ff388c21c73921165f43eb960986e.jpg",
                            "shareObject": "1",
                            "callbackUrl": "{\"type\":\"1\"}",
                            "sharePlatforms": [
                                {
                                    "id": "0",
                                    "name": "QQ"
                                },
                                {
                                    "id": "1",
                                    "name": "微信"
                                },
                                {
                                    "id": "2",
                                    "name": "朋友圈"
                                },
                                {
                                    "id": "3",
                                    "name": "微博"
                                }
                            ]
                        },
                        "has_face": "1",
                        "cate_id": "169"
                    },
                    {
                        "view_lock": "0",
                        "is_view": "0",
                        "photo_id": "3878109936",
                        "src": "http://q.3km.biz/uploads/disk4/user/album/c1/cf2/c1cf2d7a2bc94cbcb47274b0a2daab66.jpg",
                        "shareInfo": {
                            "title": "约单APP",
                            "text": "「约单」全国领先的时间与技能共享平台",
                            "logo": "https://q.3km.biz/static/biglogo.png",
                            "url": "http://q.3km.biz/uploads/disk4/user/album/c1/cf2/c1cf2d7a2bc94cbcb47274b0a2daab66.jpg",
                            "shareObject": "1",
                            "callbackUrl": "{\"type\":\"1\"}",
                            "sharePlatforms": [
                                {
                                    "id": "0",
                                    "name": "QQ"
                                },
                                {
                                    "id": "1",
                                    "name": "微信"
                                },
                                {
                                    "id": "2",
                                    "name": "朋友圈"
                                },
                                {
                                    "id": "3",
                                    "name": "微博"
                                }
                            ]
                        },
                        "has_face": "1",
                        "cate_id": "169"
                    }
                ],
                "photoCount": "65",
                "collected": "1",
                "blacked": "0",
                "black": "0",
                "digged": "0",
                "distance": "1494.1km",
                "sina_uid": "",
                "buttonShowInfo": {
                    "callButton": "0",
                    "favButton": "1",
                    "remarkButton": "0",
                    "requirementButton": "0"
                },
                "serviceInfo": { },
                "serviceList": [ ],
                "other_cates": {
                    "title": "Ta还能提供这些服务",
                    "cates": [
                        "推拿",
                        "导游",
                        "舞蹈",
                        "网球",
                        "游泳",
                        "美发"
                    ]
                },
                "snsList": {
                    "weixin": {
                        "id": "oHe-40d9aDXUdyNLdOvGXe02A4DU",
                        "show": "1",
                        "nickname": "明明"
                    }
                },
                "share": {
                    "title": "约单 - 时间交易平台",
                    "url": "http://3km.biz/p3hG",
                    "text": "我在【约单】找到了这位“买家”，真心不错哦，大家也去体验吧!",
                    "logo": "http://q.3km.biz/uploads/disk4/avatar/84/d75/84d7560e358dee5629d64af24c6cd60f.jpg"
                },
                "visitor": {
                    "num": "1002839",
                    "user_list": [
                        {
                            "uid": "1934721037",
                            "username": "邹贷惜萱",
                            "src": "http://q.3km.biz/uploads/disk4/avatar/82/5a7/825a76687591fb97df47ead2194b8544.jpg"
                        },
                        {
                            "uid": "1937191964",
                            "username": "钟灵靳灿",
                            "src": "http://q.3km.biz/uploads/disk4/avatar/1b/b65/1bb6599ce024340a3bc8c52a19719a4e.png"
                        },
                        {
                            "uid": "1936569938",
                            "username": "过客回头",
                            "src": "http://q.3km.biz/uploads/disk4/avatar/e3/7ec/e37ec6973f0cab12c279489be35808ba.png"
                        },
                        {
                            "uid": "1937342022",
                            "username": "羊羊羊吖",
                            "src": "http://q.3km.biz/uploads/yuedanios/avatar/d7/c50/d7c50d5afefd31e8a83a9c805c605758.png"
                        },
                        {
                            "uid": "60906457",
                            "username": "竹官戌",
                            "src": "http://q.3km.biz/uploads/disk4/avatar/12/44c/1244cffebc30f91c906657e573565836.png"
                        },
                        {
                            "uid": "50367831898",
                            "username": "智能乔朝",
                            "src": "http://q.3km.biz/uploads/yuedan/avatar/b0/cac/b0cacb68beabe088e0c61c2e3b66ae01.jpg"
                        },
                        {
                            "uid": "40002148279",
                            "username": "项丛丛匀实",
                            "src": "http://q.3km.biz/uploads/liaodan/avatar/fa/817/fa817c0d9386a58cdcaddc69f4a4eae1.jpg"
                        },
                        {
                            "uid": "52946735",
                            "username": "白朱",
                            "src": "http://q.3km.biz/uploads/user/avatar/1e/ac1/1eac13cacec31e9ccb78e3be582664b5.jpg"
                        }
                    ]
                },
                "avatar_tip": "1",
                "service_auth": "0",
                "auth_service": "0",
                "invite_auth_state": "1",
                "report_num": "",
                "mobile_auth": "1",
                "user_auth": "1",
                "alipay_auth": "1",
                "sesame_auth": "0",
                "weixin_auth": "1",
                "weibo_auth": "0",
                "shop_auth": "0",
                "insurance": "0",
                "share_icon_src": "http://q.3km.biz/static/user/share.png",
                "doyen_state": "2",
                "doyen_grade": "0",
                "doyen_honor": "未申请达人",
                "doyen_title": "服务达人",
                "doyen_url": "http://wx.soho.iyuedan.com/api30/h5/doyen/index?type=0&uid=1934880283",
                "doyen_apply": "http://wx.soho.iyuedan.com/api30/h5/doyen/bedoyen?type=0",
                "header_image_url": "http://q.3km.biz/static/user/user_back@2x.png",
                "reward_diamond": "0",
                "greet": 0,
                "invite_recharge": 0,
                "give_bonus": 0,
                "close_greet_alter": 0,
                "close_recharge_alter": 0,
                "close_bonus_alter": 0,
                "garrison": {
                    "status": "1",
                    "g_uid": "1934671642",
                    "g_avatar": "http://q.3km.biz/uploads/disk4/avatar/36/b3b/36b3b70d0990933534323982c2da1bb5.jpg",
                    "g_vip": "0",
                    "g_frame": "赠送价值超过2805钻石的礼物，就能轻松挤走gYUz滑板，成为Ta的守护天使",
                    "g_button": "就是这么任性，我要取代Ta",
                    "n_frame": "单次赠送价值超过26钻石的礼物，就能成为Ta的守护天使",
                    "n_button": "我要成为Ta的守护天使",
                    "n_note": "待完善"
                },
                "wechat_sign": "15*****（已验证）",
                "swop_wechat": "1",
                "bond_sign": "1507元（已缴纳）",
                "ranking": {
                    "stone": "4034",
                    "avatar": [
                        "http://q.3km.biz/uploads/disk4/avatar/36/b3b/36b3b70d0990933534323982c2da1bb5.jpg",
                        "http://q.3km.biz/uploads/disk4/avatar/d9/ccd/d9ccd7f51254bdeaeb169769c3567234.jpg",
                        "http://q.3km.biz/uploads/disk4/avatar/82/5a7/825a76687591fb97df47ead2194b8544.jpg",
                        "http://q.3km.biz/uploads/avatar_public/pend.jpg",
                        "http://q.3km.biz/uploads/avatar_male/2.jpg",
                        "http://q.3km.biz/uploads/disk4/avatar/aa/7c3/aa7c3633254a1cebbad0c5589e7b945e.png"
                    ],
                    "gift_diamond": "4034"
                },
                "is_vip": "1",
                "total_credits": "0",
                "album": [
                    {
                        "view_lock": "0",
                        "is_view": "0",
                        "photo_id": "3878109934",
                        "src": "http://q.3km.biz/uploads/disk4/user/album/9e/e8f/9ee8f2f931e0c315dde9df8a678c55b1.jpg/yuedan",
                        "shareInfo": {
                            "title": "约单APP",
                            "text": "「约单」全国领先的时间与技能共享平台",
                            "logo": "https://q.3km.biz/static/biglogo.png",
                            "url": "http://q.3km.biz/uploads/disk4/user/album/9e/e8f/9ee8f2f931e0c315dde9df8a678c55b1.jpg",
                            "shareObject": "1",
                            "callbackUrl": "{\"type\":\"1\"}",
                            "sharePlatforms": [
                                {
                                    "id": "0",
                                    "name": "QQ"
                                },
                                {
                                    "id": "1",
                                    "name": "微信"
                                },
                                {
                                    "id": "2",
                                    "name": "朋友圈"
                                },
                                {
                                    "id": "3",
                                    "name": "微博"
                                }
                            ]
                        },
                        "has_face": "1",
                        "cate_id": "169"
                    },
                    {
                        "view_lock": "0",
                        "is_view": "0",
                        "photo_id": "3878109935",
                        "src": "http://q.3km.biz/uploads/disk4/user/album/cd/0ff/cd0ff388c21c73921165f43eb960986e.jpg/yuedan",
                        "shareInfo": {
                            "title": "约单APP",
                            "text": "「约单」全国领先的时间与技能共享平台",
                            "logo": "https://q.3km.biz/static/biglogo.png",
                            "url": "http://q.3km.biz/uploads/disk4/user/album/cd/0ff/cd0ff388c21c73921165f43eb960986e.jpg",
                            "shareObject": "1",
                            "callbackUrl": "{\"type\":\"1\"}",
                            "sharePlatforms": [
                                {
                                    "id": "0",
                                    "name": "QQ"
                                },
                                {
                                    "id": "1",
                                    "name": "微信"
                                },
                                {
                                    "id": "2",
                                    "name": "朋友圈"
                                },
                                {
                                    "id": "3",
                                    "name": "微博"
                                }
                            ]
                        },
                        "has_face": "1",
                        "cate_id": "169"
                    },
                    {
                        "view_lock": "0",
                        "is_view": "0",
                        "photo_id": "3878109936",
                        "src": "http://q.3km.biz/uploads/disk4/user/album/c1/cf2/c1cf2d7a2bc94cbcb47274b0a2daab66.jpg/yuedan",
                        "shareInfo": {
                            "title": "约单APP",
                            "text": "「约单」全国领先的时间与技能共享平台",
                            "logo": "https://q.3km.biz/static/biglogo.png",
                            "url": "http://q.3km.biz/uploads/disk4/user/album/c1/cf2/c1cf2d7a2bc94cbcb47274b0a2daab66.jpg",
                            "shareObject": "1",
                            "callbackUrl": "{\"type\":\"1\"}",
                            "sharePlatforms": [
                                {
                                    "id": "0",
                                    "name": "QQ"
                                },
                                {
                                    "id": "1",
                                    "name": "微信"
                                },
                                {
                                    "id": "2",
                                    "name": "朋友圈"
                                },
                                {
                                    "id": "3",
                                    "name": "微博"
                                }
                            ]
                        },
                        "has_face": "1",
                        "cate_id": "169"
                    },
                    {
                        "view_lock": "0",
                        "is_view": "0",
                        "photo_id": "3875380548",
                        "src": "http://q.3km.biz/uploads/disk4/user/album/e7/336/e73368d76ca7298b42c743e3b00cbf6f.jpg/yuedan",
                        "shareInfo": {
                            "title": "约单APP",
                            "text": "「约单」全国领先的时间与技能共享平台",
                            "logo": "https://q.3km.biz/static/biglogo.png",
                            "url": "http://q.3km.biz/uploads/disk4/user/album/e7/336/e73368d76ca7298b42c743e3b00cbf6f.jpg",
                            "shareObject": "1",
                            "callbackUrl": "{\"type\":\"1\"}",
                            "sharePlatforms": [
                                {
                                    "id": "0",
                                    "name": "QQ"
                                },
                                {
                                    "id": "1",
                                    "name": "微信"
                                },
                                {
                                    "id": "2",
                                    "name": "朋友圈"
                                },
                                {
                                    "id": "3",
                                    "name": "微博"
                                }
                            ]
                        },
                        "has_face": "1",
                        "cate_id": "169"
                    }
                ],
                "get_remark": {
                    "count": "23",
                    "row": [
                        {
                            "remark_id": "40007777444",
                            "user_id": "254",
                            "realname": "",
                            "age": "",
                            "sex": "",
                            "avatar": "",
                            "lat": "",
                            "lng": "",
                            "detail": "觉得自己眼光还是不错的,很好 遇见你,我真是太幸运了~非常的感激",
                            "cate_id": "17",
                            "cate_name": "羽毛球",
                            "state": "254",
                            "state_name": "系统",
                            "created": "2020-09-06",
                            "score": "4",
                            "face": "4",
                            "attitude": "5",
                            "anonymity": "1",
                            "diggs": "0",
                            "reply": "",
                            "media_list": [ ],
                            "share_info": {
                                "title": "约单APP",
                                "text": "「约单」全国领先的时间与技能共享平台",
                                "logo": "https://q.3km.biz/static/biglogo.png",
                                "url": "http://3km.biz/sjBRm",
                                "shareObject": "0",
                                "callbackUrl": "{\"type\":\"1\"}",
                                "sharePlatforms": [
                                    {
                                        "id": "0",
                                        "name": "QQ"
                                    },
                                    {
                                        "id": "1",
                                        "name": "微信"
                                    },
                                    {
                                        "id": "2",
                                        "name": "朋友圈"
                                    },
                                    {
                                        "id": "3",
                                        "name": "微博"
                                    }
                                ]
                            },
                            "share_bubble": "得奖励",
                            "beremarked_user": {
                                "user_id": "1934880283",
                                "realname": "百里挑一并姝嗤荷更",
                                "age": "35",
                                "sex": "男",
                                "avatar": "http://q.3km.biz/uploads/disk4/avatar/84/d75/84d7560e358dee5629d64af24c6cd60f.jpg",
                                "lat": "39.393074",
                                "lng": "117.015892"
                            },
                            "recharge_jump": "{\"type\":30,\"doyen_uid\":\"0\",\"doyen_type\":4}",
                            "need_cate_id": "0"
                        }
                    ]
                },
                "give_remark": {
                    "count": "35",
                    "row": [
                        {
                            "remark_id": "40006652196",
                            "user_id": "1934880283",
                            "realname": "百里挑一并姝嗤荷更",
                            "age": "35",
                            "sex": "男",
                            "avatar": "http://q.3km.biz/uploads/disk4/avatar/84/d75/84d7560e358dee5629d64af24c6cd60f.jpg",
                            "lat": "39.393074",
                            "lng": "117.015892",
                            "detail": "一个字好,两个字很好,三个字太好了 哈哈…… 你笑点好低啊,跟你相处太愉快了",
                            "cate_id": "169",
                            "cate_name": "交友",
                            "state": "254",
                            "state_name": "系统",
                            "created": "2020-08-02",
                            "score": "4",
                            "face": "4",
                            "attitude": "4",
                            "anonymity": "0",
                            "diggs": "0",
                            "reply": "",
                            "media_list": [ ],
                            "share_info": {
                                "title": "约单APP",
                                "text": "「约单」全国领先的时间与技能共享平台",
                                "logo": "https://q.3km.biz/static/biglogo.png",
                                "url": "http://3km.biz/sjBRm",
                                "shareObject": "0",
                                "callbackUrl": "{\"type\":\"1\"}",
                                "sharePlatforms": [
                                    {
                                        "id": "0",
                                        "name": "QQ"
                                    },
                                    {
                                        "id": "1",
                                        "name": "微信"
                                    },
                                    {
                                        "id": "2",
                                        "name": "朋友圈"
                                    },
                                    {
                                        "id": "3",
                                        "name": "微博"
                                    }
                                ]
                            },
                            "share_bubble": "得奖励",
                            "beremarked_user": {
                                "user_id": "55185062",
                                "realname": "清楚的冬梅",
                                "age": "35",
                                "sex": "女",
                                "avatar": "http://q.3km.biz/uploads/disk4/avatar/c1/fd7/c1fd7f5e2cebcd503a25ebb85b39f1bc.jpg",
                                "lat": "39.9271",
                                "lng": "116.634259"
                            },
                            "recharge_jump": "{\"type\":30,\"doyen_uid\":\"1934880283\",\"doyen_type\":4}",
                            "need_cate_id": "0"
                        }
                    ]
                },
                "is_forbidden_user": "0",
                "personal_share": {
                    "sys_time": "1607407055",
                    "msg": "邀请好友就赚钱
        您邀请好友注册送您最高100元
        您邀请的好友再邀请用户注册送您最高50元",
                    "status": "1",
                    "time_interval": "86400",
                    "ok": "去邀请",
                    "cancel": "知道了",
                    "ok_jump": "{\"type\":15,\"url\":\"http:\\/\\/wx.soho.iyuedan.com\\/api3.0\\/share\\/ShareInfo?type=1\",\"title\":\"分享赚钱\"}"
                },
                "button_des": "充值返利",
                "button_jump": "{\"type\":30,\"doyen_uid\":\"1934880283\",\"doyen_type\":4}",
                "share_state": "1",
                "recent": {
                    "tips": "会员特权查看Ta的足迹",
                    "title": "近期足迹",
                    "num": "1",
                    "detail": [
                        "北京市昌平区沙河"
                    ],
                    "box_note": "https://i.3km.biz/static/service/mark/track.png",
                    "url": "http://fe.soho.iyuedan.com/app/track/index.html?user_id=1934880283"
                },
                "is_face_auth": "0",
                "bomb_box": { }
            }
        }
"""
#将json串转换成字典
json_dict = json.loads(json_demo)

#遍历字典
for (k, v) in json_dict.items():
    print(k, ":", v)
    for data in v:
        for (data_k, data_v) in data.items():
            print("  ", data_k, ":", data_v)
        #遍历列表
